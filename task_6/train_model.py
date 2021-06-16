import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

data_path = './images/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# training data, labels
training_data, labels = [], []

# we need to create numpy array for the same as the cv2 only processes the numpy arrays
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    training_data.append(np.asarray(images, dtype=np.uint8))
    labels.append(i)

labels = np.asarray(labels, dtype=np.int32)

face_model = cv2.face_LBPHFaceRecognizer.create()
face_model.train(np.asarray(training_data), np.asarray(labels))
print("model trained successfully")

# Recognizer
face_classifier = cv2.CascadeClassifier('./haarCascade/haarcascade_frontalface_default.xml')

def face_detector(img):

    # convert iamge to gray scale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        # roi - region of interest
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

# open webcam
capture = cv2.VideoCapture(0)

while True:

    ret, frame = capture.read()
    
    image, face = face_detector(frame)
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        results = face_model.predict(face)
        # harry_model.predict(face)
        
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
            
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
        if confidence > 70:
            cv2.putText(image, "Hey Saurabh", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            cv2.waitKey(50)
            capture.release()
            cv2.destroyAllWindows()    
            os.chdir("terraformScript")
            os.system("terraform init")
            print("Terraform initiated")
            os.system("terraform apply -auto-approve")
            print("Setup Launched Successfully")
            break
         
        else:
            
            cv2.putText(image, "I dont know, how r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.putText(image, confidence, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        capture.release()
        cv2.destroyAllWindows()    
        break
 
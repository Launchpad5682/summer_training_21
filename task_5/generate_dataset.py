import cv2
import numpy as np

# https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters

# Load Haar face cascade
face_classifier = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

def face_extractor(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(image,1.3,5)

    if faces is ():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = image[y:y+h, x:x+w]

    return cropped_face

capture = cv2.VideoCapture(0)
count = 0

# collect 100 images using the webcam
while True:

    ret, frame = capture.read()

    if face_extractor(frame) is not None:
        count += 1 
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        file_name_path = './images/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        # org is the bottom-left corner of the image from where the text need to be started    
        cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Crop', face)

    else:
        print("Face not found")
        pass
        
    if cv2.waitKey(1) == 13 or count == 100:
        break


cv2.destroyAllWindows()
capture.release()
print("Samples collected")
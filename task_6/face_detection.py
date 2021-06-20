import cv2


def face_detector(img):
    # Recognizer
    face_classifier = cv2.CascadeClassifier(
        './haarCascade/haarcascade_frontalface_default.xml')
    # convert iamge to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        # roi - region of interest
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


def face_detection(model_path, trigger, mail_text=None, whatsapp_text=None):
    # open webcam
    face_model = cv2.face.LBPHFaceRecognizer_create()
    face_model.read(model_path)
    capture = cv2.VideoCapture(0)

    while True:

        ret, frame = capture.read()

        image, face = face_detector(frame)

        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value
            # this can referred https://stackoverflow.com/questions/39010477/confidence-in-opencv-facerecognizer-predict-method-output
            # it returns labels(number of users in camera view) and confidence, higher the number worse is the detection
            results = face_model.predict(face)

            if results[1] < 500:
                confidence = int(100 * (1 - (results[1])/400))
                display_string = str(confidence) + '% Confident it is User'

            cv2.putText(image, display_string, (100, 120),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

            if confidence > 90:
                cv2.putText(image, "Hey user", (250, 450),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Recognition', image)
                cv2.waitKey(1000)  # window was crashing too quickly
                capture.release()
                cv2.destroyAllWindows()
                # calling sending notification when it is face 1
                if mail_text is not None and whatsapp_text is not None:
                    trigger(mail_text=mail_text, whatsapp_text=whatsapp_text)

                # otherwise call the infrastructure setup
                else:
                    trigger()
                break

            else:

                cv2.putText(image, "I dont know, how r u", (250, 450),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(image, confidence, (250, 450),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Recognition', image)

        except:
            cv2.putText(image, "No Face Found", (220, 120),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image, "looking for face", (250, 450),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)
            pass

        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            capture.release()
            cv2.destroyAllWindows()
            break


# face_detection(model_path='./models/face_model_1.yml',trigger=trigger)

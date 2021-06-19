import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


def model_train(data_path, save_path):
    # data_path = './images/'
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
    print(type(face_model))
    print("model trained successfully")
    ## saved model for further use
    face_model.save(save_path)

# export the model (Future Work), This model can be saved to be used further - Done
# but training the model everytime for now


#model_train(data_path='./images/', save_path='./models/face_model_1.yml')

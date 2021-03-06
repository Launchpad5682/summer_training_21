
import os
import getpass
import destroy
import generate_dataset
import train_model
import face_detection
import eventTrigger
import sendNot

os.system("clear")
os.system("tput setaf 3")
print("\t\t\t Welcome to our Menu")
os.system("tput setaf 7")
print("\t\t\t -------------")

password = getpass.getpass("Enter your password to continue: ")

if password != "test":
    input("Password is incorrect")
    exit()

# else


def main():

    while True:
        os.system("clear")
        print("Select the options to perform")
        print("1. Add Face Data for Mail and WhatsApp Notification")
        print("2. Add Face Data for Launching Infrastructure")
        print("3. Verify Identity and Send Notification")
        print("4. Verify Identity and Launch Infrastructure")
        print("5. Destroy the Infrastructure")
        print("6. Exit")

        menu_option = int(input("Enter the option: "))

        if menu_option == 1:
            # Adding face data for Sending notification
            path = './images/face_1/'
            save_path = './models/face_model_1.yml'
            generate_dataset.generate_images(
                image_folder_path=path)
            train_model.model_train(data_path=path, save_path=save_path)

        elif menu_option == 2:
            # Adding face data for
            path = './images/face_2/'
            save_path = './models/face_model_2.yml'
            generate_dataset.generate_images(
                image_folder_path=path)
            train_model.model_train(data_path=path, save_path=save_path)

        elif menu_option == 3:
            # sending notification using face 1
            face_detection.face_detection(model_path='./models/face_model_1.yml', trigger=sendNot.trigger,
                                          mail_text='Hello Saurabh, Thanks for using face detection', whatsapp_text='Hello Saurabh, Thanks for using face detection')

        elif menu_option == 4:
            # triggering infrastructure launch using face 2
            face_detection.face_detection(
                model_path='./models/face_model_2.yml', trigger=eventTrigger.terraformLaunch)

        elif menu_option == 5:
            # destory infrastructure
            destroy.destroyInfra()

        elif menu_option == 6:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


if __name__ == '__main__':
    main()

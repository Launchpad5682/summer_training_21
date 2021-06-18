from mail import quickstart
from whatsapp import whatsapp
import os


def emailNot(message):
    # print(os.getcwd())
    os.chdir('mail')
    # print(os.getcwd())
    quickstart.main(message)
    os.chdir("..")


def whatsAppNot(message):
    whatsapp.sendWhatsApp(message)



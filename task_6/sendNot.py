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


def trigger(mail_text, whatsapp_text):
    emailNot(message=mail_text)
    whatsAppNot(message=whatsapp_text)

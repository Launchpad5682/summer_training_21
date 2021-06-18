from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN

# #
account_sid = 'YOUR_ACCOUNT_ID'
auth_token = 'YOUR_AUTH_TOKEN'


def sendWhatsApp(message):
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = 'whatsapp:+917023115389'

    client.messages.create(body=message,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)

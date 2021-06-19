# Sending Notification on WhatsApp and Mail and Launching architecture on AWS using Terraform and Face Recognition
<br>

## Brief Description
- On executing the `menu.py`, we get options to select and can easily be used.
- It has feature to add the face data and use that to recognize and send notifications and launch infrastructure using Terraform.
<hr>

## Dependencies 
- opencv (while using conda install using conda-forge channel)
- google-api-core
- google-api-python-client
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- numpy
- twilio
- Python 3.7.10
<hr>

### Conda Commands to install the dependencies
```
conda create cv_env
conda install -c conda-forge opencv=4.1.0
conda install -c conda-forge opencv=4.1.0
conda install opencv-contrib-python
conda install google-api-python-client 
conda install -c conda-forge  google-api-python-client google-auth-httplib2 google-auth-oauthlib
conda install -c conda-forge twilio
```
<hr>

## Setup
- We can easily setup the notification using Gmail API for mails and Twilio API for WhatsApp messages. `credentials.json `must be present in the mail module directory and `token.json` file must be empty or not present.
- Email can be authenticated very easily using the browser and then we can use it further in application.
- Twilio's WhatsApp API has very simple and easy setup, just create account, service and follow the references for the same while setting up the API.
- Then, just use the `menu program ` and enjoy the application.
- For face recognition part, haar cascade is used with OpenCV. 
## Demo

[![Demo Video](https://i9.ytimg.com/vi/SxBnX_hexzs/mq2.jpg?sqp=CPTeuIYG&rs=AOn4CLARZ3KWq2CkxR-fWGjGIVyEPgDMNg)](https://www.youtube.com/embed/SxBnX_hexzs)
## References: <br>
[Twilio API Blog](https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python)

[Gmail API Quickstart](https://developers.google.com/gmail/api/guides)
<hr>


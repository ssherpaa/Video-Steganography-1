import random
import smtplib, ssl
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "****"  # Enter your address
# receiver_email = "tchiring08@gmail.com"  # Enter receiver address
password = "*****"
subject = "Important! Password Reset!"
context = ssl.create_default_context()


def random_pass():
    letters = string.ascii_lowercase
    random_new_pass = ''.join(random.choice(letters) for i in range(8))
    return random_new_pass


def send_mail(receiver_email):
    new_pass = random_pass()
    message = f'''\
From: {sender_email}
Subject: Important! Password Reset!
    
Greeting from Video Steganography. You have requested for a password reset.

Your new Password is : {new_pass}

Please change this password after logging in.
    '''

    # message = """From: From Person <from@fromdomain.com>
    # To: To Person <to@todomain.com>
    # Subject: SMTP e-mail test
    #
    # This is a test e-mail message.
    # """

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    send_mail('****')

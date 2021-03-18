import smtplib
import os

# Email variables definition
# -----------------------------------------------------------------------------------------------
sender = 'svirahonda@gmail.com'
receiver = ['svirahonda@gmail.com'] #replace this by the owner's email address
smtp_provider = 'smtp.gmail.com'
smtp_port = 587
smtp_account = os.getenv("email_address") #replace this by your stmp account email address
smtp_password = os.getenv("gmail_password")
# -----------------------------------------------------------------------------------------------

def send_update(message):

    message = 'Subject: {}\n\n{}'.format('An automatic unit testing has ended recently.', message)

    try:
        server = smtplib.SMTP(smtp_provider,smtp_port)
        server.starttls()
        server.login(smtp_account,smtp_password)
        server.sendmail(sender, receiver, message)         
        print('Email sent successfully',flush=True)
        return
    except Exception as e:
        print('Something went wrong. Unable to send email.',flush=True)
        print('Exception: ',e)
        return

def exception(e_message):

    try:
        message = 'Subject: {}\n\n{}'.format('Something went wrong with the testing API.', e_message)
        server = smtplib.SMTP(smtp_provider,smtp_port)
        server.starttls()
        server.login(smtp_account,smtp_password)
        server.sendmail(sender, receiver, message)         
        print('Email sent successfully',flush=True)
        return
    except Exception as e:
        print('Something went wrong. Unable to send email.',flush=True)
        print('Exception: ',e)
        return

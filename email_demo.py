"""
    Sending email with HTML content and attachments

"""

import smtplib, os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('GM_EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('GM_EMAIL_PASS')
ATTACHMENT_PATH = 'email_demo'

msg = EmailMessage()
msg['Subject'] = 'Check out these comics and pdf and HTML content!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'yuliya.b.dev@gmail.com'
msg.set_content('This is a plain text email')

with open(os.path.join(ATTACHMENT_PATH, 'message.html')) as html_f:
    html_data = html_f.read()
    msg.add_alternative(html_data, subtype="html")

# attach images:
files = ['comic.png', 'comic1.png']
for file in files:
    with open(os.path.join(ATTACHMENT_PATH, file), 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# attach PDF:
files = ['pdf_file.pdf']
for file in files:
    with open(os.path.join(ATTACHMENT_PATH, file), 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('Message sent!')

# SEL a LOCAL DEBUG SERVER to test emails w/o sending them to the real address
# it will listen to the emails from local machine
# and show them in the terminal
#$ python3 -m smtpd -c DebuggingServer -n localhost:1025

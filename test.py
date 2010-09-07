# Setup smtp server
from smtplib import SMTP
smtp = SMTP('smtp.gmail.com:587')
smtp.starttls()
smtp.login('username', 'password')

# Prepare email
from pymailer import Email
email = Email()
email.server = smtp
email.recipients = ['taylorzr@gmail.com']
email.subject = 'pymailer test'				# optional
email.text = 'Sent using python pymailer module!'	# optional
email.attach(['README'])				# optional
email.send()

import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


class Email():
	def __init__(self, server=None, recipients=[], subject='', text='',  files=[], sender=''):
		self.server = server
		self.sender = sender
		self.recipients = recipients
		self.subject = subject
		self.text = text
		self.files = files
		
	def __assemble(self):
		# Message 
		self.message = MIMEMultipart()
		self.message['From'] = self.sender
		self.message['To'] = ', '.join(self.recipients)
		self.message['Subject'] = self.subject
		self.message.attach(MIMEText(self.text))
		# Attachments
		for file in self.files:
			part = MIMEBase('application', "octet-stream")
			part.set_payload( open(file, "rb").read() )
			Encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
			self.message.attach(part)
			
	def attach(self, files):
		for file in files:
			self.files.append(file)
			
	def send(self):
		assert(self.server)
		assert(self.recipients)
		self.__assemble()
		self.server.sendmail(self.sender, self.recipients, self.message.as_string())
		self.server.close()

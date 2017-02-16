from Logger import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from ConfigProvider import *


class Mail():
    def __init__(self):
        self.log = Logger().__get_log__()
        config = ConfigProvider.__config_properties__()
        self.smtp_host=config.get('mail','smtp_host')
        self.message = config.get('mail', 'message')
        self.subject = config.get('mail', 'subject')
        self.to_mail = config.get('mail', 'to')
        self.from_mail = config.get('mail', 'from')
        self.smtp_password_temp = config.get('mail', 'smtp_password')
        self.smtp_port = config.get('mail', 'smtp_port')

    def send_mail(self,output_file,output_dir):
            try:
                msg = MIMEMultipart()
                msg['From'] = self.from_mail
                msg['To'] = self.to_mail
                msg['Subject'] = self.subject
                body = self.message
                msg.attach(MIMEText(body, 'plain'))
                filename = output_file
                attachment = open(output_dir, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)
                smtp = smtplib.SMTP_SSL(self.smtp_host,self.smtp_port)
                smtp.ehlo()
                smtp.login(self.from_mail,self.smtp_password_temp)
                text = msg.as_string()
                smtp.sendmail(self.from_mail,self.to_mail,text)
                smtp.close()
                self.log.info("message sent successfully")
            except:
                self.log.info("message sending failed")








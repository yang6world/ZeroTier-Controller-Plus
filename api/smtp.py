import smtplib
from email.mime.text import MIMEText
from email.header import Header
from api.config.config import Config

config = Config()


class Email:
    def __init__(self):
        self.mail_host = config.SMTP_HOST  # 设置服务器
        self.mail_user = config.SMTP_USER  # 用户名
        self.mail_pass = config.SMTP_PASSWORD  # 口令
        self.sender = config.SMTP_SENDER

    def sing_in(self, receivers, subject, message):
        message = MIMEText(message, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = Header(receivers, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            s = smtplib.SMTP_SSL(self.mail_host, 587)
            s.starttls()
            s.ehlo()
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(self.sender, receivers, message.as_string())
            s.close()
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

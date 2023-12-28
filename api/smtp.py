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

    def send_registration_email(self, receivers, subject, user_name, registration):
        # 构建注册确认的邮件内容
        message_content = f"亲爱的 {user_name},\n\n感谢您注册我们的服务。请点击下面的链接来激活您的账户:\n{registration}"

        # 设置邮件格式
        message = MIMEText(message_content, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = Header(receivers, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        try:
            # 连接到SMTP服务器
            s = smtplib.SMTP_SSL(self.mail_host, 587)
            s.starttls()
            s.ehlo()
            s.login(self.mail_user, self.mail_pass)

            # 发送邮件
            s.sendmail(self.sender, receivers, message.as_string())
            s.close()
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class send_email:
    def send(self, file):
        msg = MIMEMultipart()
        # 发送者的账号
        msg_from = '1096075142@qq.com'
        # 发送者的授权码
        password = 'undhgelvdbzvgjae'
        # 接收者的账号
        msg_to = '2726493810@qq.com'
        # 邮件的主题
        subject = '选品系统自动化测试报告'
        #  邮件的内容
        content = '附件是最新的自动化测试报告'
        msg.attach(MIMEText(content, 'plain', "utf-8"))
        msg['Subject'] = subject
        msg['To'] = msg_to
        msg['From'] = msg_from
        att3 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att3['Content-Type'] = 'application/octet-stream'
        att3['Content-Disposition'] = 'attachment;filename="gttInterfaceTest.html"'
        msg.attach(att3)
        try:
            client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
            print("连接到邮箱服务器成功")
            client.login(msg_from, password)
            print("登录邮箱服务器成功")
            client.sendmail(msg_from, msg_to, msg.as_string())
            print("自动化测试报告邮件发送成功")
        except smtplib.SMTPException as e:
            print("发送邮件异常{}".format(e))

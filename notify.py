import threading

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
sender_qq = '123@qq.com'  # 发件人邮箱
pwd = ''
receiver = ['abc@qq.com']  # 收件人邮箱


def send(mail_title, mail_content):
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = SMTP_SSL(host_server)  # ssl登录

    # login(user,password):
    # user:登录邮箱的用户名。
    # password：登录邮箱的密码，像笔者用的是网易邮箱，网易邮箱一般是网页版，需要用到客户端密码，需要在网页版的网易邮箱中设置授权码，该授权码即为客户端密码。
    smtp.login(sender_qq, pwd)

    # sendmail(from_addr,to_addrs,msg,...):
    # from_addr:邮件发送者地址
    # to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
    # msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
    smtp.sendmail(sender_qq, receiver, msg.as_string())

    # quit():用于结束SMTP会话。
    smtp.quit()


def send_email(mail_title, mail_content):
    threading.Thread(target=send, args=(mail_title, mail_content)).start()

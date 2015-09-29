# -*- coding: utf-8 -*-
# from django.conf.global_settings import EMAIL_HOST_USER
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.core.mail import EmailMultiAlternatives, mail_admins
from Cable_Project.settings import EMAIL_HOST_USER
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import os.path


def set_email(request, username, email):
    if request.method == 'POST':
        subject, form_email, to = '中缆联盟', EMAIL_HOST_USER, email
        text_content = '中缆联盟激活邮件！'
        html_content = u'<b>激活链接：</b><a href="http://www.baidu.com">http:www.baidu.com</a>'
        msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        mail_admins(u'用户注册反馈', u'当前{}用户注册了该网站'.format(username), fail_silently=True)


class smtpMail(object):
    def __init__(self,
                 From        = "zllm58@sina.com", # zllm58@sina.com
                 from_smtp   = "smtp.sina.com", # smtp.sina.com.cn
                 from_user   = "zllm58", # zllm58
                 from_passrd = "zhonglanlianmeng", # zhonglanlianmeng
                 ):

        self.From = From
        self.from_smtp = from_smtp
        self.from_user = from_user
        self.from_passrd = from_passrd

    def send_mail(self, tomail=None, subject=None, content=None, file_name=None, user_uuid=None):
        msg = MIMEMultipart() # 邮件本身 发送附件
        msg['From'] = self.From
        msg['To'] = tomail
        msg['Subject'] = Header(subject, charset='UTF-8')#中文主题

        #添加邮件内容
        txt = MIMEText(content, _subtype='plain', _charset='UTF-8')
        #添加html的邮件内容
        txt = MIMEText("请点击以下链接或者将地址复制到浏览器完成注册。<br/><a href='http://10.57.122.45/account/register/{0}'>www.中联联盟.com/{1}</a><br/>中缆联盟期待您的加入！！！".format(user_uuid, user_uuid), _subtype='html',  _charset='UTF-8')
        msg.attach(txt)

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)

        ## 读入文件内容并格式化
        if file_name:
            data = open(file_name, 'rb')
            file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
            file_msg.set_payload(data.read())
            data.close()
            email.Encoders.encode_base64(file_msg)

            ## 设置附件头
            basename = os.path.basename(file_name)
            file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
            msg.attach(file_msg)

        #发送邮件
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)
        smtp.connect(self.from_smtp, 25)
        smtp.login(self.from_user, self.from_passrd)
        smtp.sendmail(self.From, tomail, msg.as_string())
        smtp.quit()
        print '%s邮件发送成功' % tomail


def send_email_main(to_mail=None, subject=None, content=None, file_name=None, user_uuid=None):
    sdmail = smtpMail()
    subject = '中缆联盟'
    content = '欢迎注册中缆联盟，请点击以下链接完成注册！'
    sdmail.send_mail(to_mail, subject, content, file_name, user_uuid)

# -*- coding:utf-8 -*-
# author: msun1996
import random, string

from django.core.mail import send_mail

from users.models import EmailverifyRecord
from mxonline.settings import EMAIL_FROM


def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])


def send_register_email(email, send_type='register'):
    email_record = EmailverifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '慕学网在线注册链接'
        email_body = '请点击注册链接激活帐号： http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    if send_type == 'forget':
        email_title = '慕学网找回密码链接'
        email_body = '请点击链接找回密码： http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
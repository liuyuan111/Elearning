from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings


# Create your models here.
#用户
class XXUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=20, default='')

#邮箱验证
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"邮箱验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型",choices=(("register",u"注册"), ("forget",u"找回密码"), ("update_email",u"修改邮箱")),max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间",default=datetime.now)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}{1}'.format(self.code,self.email)
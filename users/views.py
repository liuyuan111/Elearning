from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.urls import reverse
# Create your views here.
from random import Random
from django.core.mail import send_mail
from elearning.settings import EMAIL_FROM
from .models import *
from myapp.models import *
#生成随机字符串
def make_random_str(randomlength =8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) -1
    random = Random()
    for i in range(randomlength):
        str +=chars[random.randint(0,length)]
    return str
#发送邮件
def my_send_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = make_random_str(4)
    else:
        code = make_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.sendtype = send_type
    email_record.save()
    email_title=""
    email_body=""

    if send_type == "register":
        email_title = "XX课堂-注册激活链接"
        email_body = "请点击以下链接来激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "XX课堂-密码重置链接"
        email_body = "请点击以下链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "XX课堂，邮箱修改验证码"
        email_body = "你的邮箱修改验证码为：{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = XXUser.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'login.html', {'error_msg': '用户未激活！'})
        return render(request, "login.html")

class CommentView(View):

    def post(self, request, bid):

        comment = Comment()
        comment.user = request.user
        comment.blog = Blog.objects.get(id=bid)
        comment.content = request.POST.get('content')
        comment.pub_date = datetime.now()
        comment.save()

        return HttpResponseRedirect(reverse("blog-detail", kwargs={"bid":bid}))

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html',{'error_msg':'用户未激活！'})
        else:
            return render(request, 'login.html', {'error_msg':'用户名或者密码错误！'})

class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # repassword = request.POST.get('password')
        email = request.POST.get('email')
        my_send_email(email)
        # status_code = utils.my_send_email(email)

        user = XXUser()
        user.username = username
        user.email = email
        user.password = make_password(password)
        user.is_active = False

        user.save()
        return render(request, 'login.html')

def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

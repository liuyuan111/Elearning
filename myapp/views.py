from django.shortcuts import render
from .models import Banner, Category, Teacher, Course, Tags, StarStudent, Blog, Teacher, Org, Comment
from users.models import *
from datetime import datetime
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    banner_list = Banner.objects.all()
    starstudent_list = StarStudent.objects.all()
    org_list = Org.objects.all()
    category_list = Category.objects.all()[:6]

    blog_list = Blog.objects.all()[:3]

    teacher_list = Teacher.objects.all()

    # 数据统计
    teacher_count = Teacher.objects.count()
    course_count = Course.objects.count()
    user_count = XXUser.objects.count()
    category_count = Category.objects.count()

    course_list = Course.objects.order_by('pub_date').all()

    ctx = {
        'banner_list': banner_list,
        'category_list': category_list,
        'teacher_count': teacher_count,
        'course_count': course_count,
        'user_count': user_count,
        'category_count': category_count,
        'course_list': course_list,
        'starstudent_list': starstudent_list,
        'blog_list': blog_list,
        'teacher_list': teacher_list,
        'org_list': org_list
    }

    return render(request, 'index.html', ctx)

# DetailView


def course_detail(request, cid):
    course = Course.objects.get(pk=cid)
    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()

    ctx = {
        'course': course,
        'course_list': course_list,
        'category_list': category_list
    }
    return render(request, 'courses-detail.html', ctx)

def course(request):
    course_list = Course.objects.all()
    category_list = Category.objects.all()
    category_id = request.GET.get('category_id')
    if category_id:
        course_list = course_list.filter(category_id=category_id)
        category_id = int(category_id)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(course_list, per_page=4, request=request)

    course_list = p.page(page)

    ctx = {
        'post_list': course_list,
        'category_list': category_list,
        'category_id': category_id
    }
    return render(request, 'courses.html', ctx)


def blog_list(request):
    blog_list = Blog.objects.all()

    latest_blog_list = Blog.objects.order_by('pub_date').all()[:3]

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(blog_list, per_page=2, request=request)

    blog_list = p.page(page)

    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()

    tag_list = Tags.objects.all()

    ctx = {
        'post_list': blog_list,
        'latest_blog_list': latest_blog_list,
        'course_list': course_list,
        'category_list': category_list,
        'tag_list': tag_list
    }

    return render(request, 'news.html', ctx)



def blog_detail(request, bid):

    blog = Blog.objects.get(pk=bid)

    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()
    latest_blog_list = Blog.objects.order_by('pub_date').all()[:3]

    tag_list = Tags.objects.all()

    ctx = {
        'blog': blog,
        'latest_blog_list':latest_blog_list,
        'course_list': course_list,
        'category_list': category_list,
        'tag_list': tag_list
    }

    return render(request, 'news-detail.html', ctx)

from . import views
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-detail/<int:bid>', views.blog_detail, name='blog-detail'),
    path('course-detail/<int:cid>', views.course_detail, name='course-detail'),
]

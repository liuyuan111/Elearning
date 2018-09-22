from . import views
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    path('logout', views.my_logout, name='logout'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('comment/<int:bid>', views.CommentView.as_view(), name='comment'),
    # path('active/<char:active_code>', views.CommentView.as_view(), name='active'),
    url(r'^active/(?P<active_code>[0-9]+[A-Z]+[a-z]+)', views.ActiveView.as_view(), name='active')

]

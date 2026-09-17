from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]

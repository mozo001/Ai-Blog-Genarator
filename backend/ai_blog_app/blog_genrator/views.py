from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


def all_blogs(request):
    return render(request, 'all_blogs.html')


def blog_detail(request, slug=None):
    return render(request, 'blog_detail.html', {'slug': slug})

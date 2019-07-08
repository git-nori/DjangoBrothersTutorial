from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')  # クエリセットの取得
    return render(request, 'blogs/index.html', {'blogs': blogs})


def detail(request, blog_id):  # blogs/urls.pyに指定したblog_idを受け取る
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
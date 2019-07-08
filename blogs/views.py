from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')  # クエリセットの取得
    return render(request, 'blogs/index.html', {'blogs': blogs})
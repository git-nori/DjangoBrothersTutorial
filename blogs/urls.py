from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),  # http://127.0.0.1:8000/へのアクセスに対してviews.indexメソッドを呼ぶ
    path('detail/<int:blog_id>/', views.detail, name='detail'),  # blog_idはviews.pyにも渡される
]
from django.contrib import admin
from .models import Blog

# Register your models here.

# admin.site.register(Blog)  # BlogモデルをAdminページで利用できるよう設定

# Adminページに複数のフィールドを表示させるよう設定
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')  # 指定したフィールドが管理ページに表示されるよう設定
    list_display_links = ('id', 'title')  # 指定したフィールドはリンクがつくよう設定


admin.site.register(Blog, BlogAdmin)
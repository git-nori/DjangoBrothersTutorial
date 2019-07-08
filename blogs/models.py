from django.db import models

# Create your models here.
# Pythonコードでデータベースの構造を記述し、簡単に操作できるようにmodelsを設定
class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        """オブジェクトを扱う上で使用するフィールドを指定
            ブログオブジェクトの一覧ページ（http://127.0.0.1:8000/admin/blogs/blog/）にいくと、それぞれのブログのタイトルが表示される
        """
        return self.title
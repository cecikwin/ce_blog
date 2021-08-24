from django.db import models

# Create your models here.
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    author = models.CharField(max_length=100, verbose_name="作者")
    text = models.TextField(max_length=50000, verbose_name="正文")
    created_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)

    def __str__(self):
        return self.title
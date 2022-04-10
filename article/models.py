from django.db import models
from martor.models import MartorField
# Create your models here.
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name="分类")

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    category = models.ForeignKey(Categories, max_length=200, verbose_name="分类", on_delete=models.CASCADE)
    author = models.CharField(max_length=100, verbose_name="作者")
    outline = models.TextField(max_length=100, verbose_name="概要")
    image = models.ImageField(upload_to='images', verbose_name="封面图")
    text = MartorField()
    created_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    total_views = models.PositiveIntegerField(default=0)

from django.contrib import admin

# Register your models here.
from martor.widgets import AdminMartorWidget

from article import models

admin.site.register(models.Articles)

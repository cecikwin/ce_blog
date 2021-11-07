from django.conf.urls.static import static
from django.urls import path
from article.views import detail, index, author, contact, about, category
from ceBlog import settings

app_name = 'blog'

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:id>', detail, name="detail"),
    path('category/<int:id>', category, name="category"),
    path('author', author, name="author"),
    path('contact', contact, name="contact"),
    path('about', about, name="about")
]

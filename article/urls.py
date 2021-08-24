from django.urls import path
from article.views import article_detail, article_list

app_name = 'article'

urlpatterns = [
    path('list', article_list),
    path('detail/<int:id>', article_detail),
]
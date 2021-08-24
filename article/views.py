from django.http import HttpResponse
from django.shortcuts import render
from article.models import Articles


# Create your views here.

def article_list(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, "article/list.html", context)

def article_detail(request, id):
    article = Articles.objects.get(id=id)
    context = {'article': article}
    return render(request, "article/detail.html", context)

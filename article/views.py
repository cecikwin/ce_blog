import markdown
from django.http import HttpResponse
from django.shortcuts import render
from martor.utils import markdownify

from article.models import Articles
from article.models import Categories

categories = Categories.objects.all()
base_context = {'categories': categories}


# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    context.update(base_context)
    return render(request, "index.html", context)


def detail(request, id):
    article = Articles.objects.get(id=id)
    last_article = Articles.objects.filter(id__lt=id).order_by('id').last()
    next_article = Articles.objects.filter(id__gt=id).order_by('id').first()
    context = {'article': article, 'last_article': last_article, 'next_article': next_article}
    context.update(base_context)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    return render(request, "post-default.html", context)


def author(request):
    return render(request, "author.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def category(request, id):
    category = Categories.objects.get(id=id)
    articles = Articles.objects.filter(category_id=id)
    context = {'category': category, 'articles': articles}
    context.update(base_context)
    return render(request, "blog-grid.html", context)


# def inline_css(html, css=None):
#     if not css:
#         css = open('default.css', encoding='utf-8').read()
#     email_html_template = u"""
#             <!doctype html>
#             <html>
#                 <head>
#                     <meta charset="UTF-8">
#                     <style>
#                         {css}
#                     </style>
#                 </head>
#                 <body>
#                     {content}
#                 </body>
#             </html>"""
#     return email_html_template.format(css=css, content=html)

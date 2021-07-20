from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Article


def index(request):
    article_list = Article.objects.filter(is_published=True)
    paginator = Paginator(article_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Кухни на заказ|Блог',
        'articles': page_obj,
    }
    return render(request, 'blog/blog.html', context)


def article(request, article_slug):
    single_article = Article.objects.get(slug=article_slug)
    context = {
        'title': f'Кухни на заказ|{single_article.title}',
        'article': single_article
    }
    return render(request, 'blog/article.html', context)


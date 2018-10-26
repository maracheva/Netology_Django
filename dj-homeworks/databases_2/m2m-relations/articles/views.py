from django.views.generic import ListView

from articles.models import Article, Scope, ArticleScopeShip


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'  # сортируем по дате публикации




class ScopeListView(ListView):
    model = Scope
    ordering = 'topic'  # сортируем по разделам

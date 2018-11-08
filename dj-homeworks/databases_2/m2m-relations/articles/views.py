from django.views.generic import ListView

from articles.models import Article, Scope, ArticleScopeShip


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'  # сортируем по дате публикации

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_arcticles_list = []
        for article in context['object_list']:
            # выводим список разделов для каждой статьи
            list_scopes = [{'topic': scope.scope.topic, 'is_main': scope.is_main}
                           for scope in ArticleScopeShip.objects.filter(article=article)]
            # print(list_scopes)

             # сортируем список разделов по полю is_main далее по алфавиту
            article.scopes_new = sorted(list_scopes, key=lambda x: x['is_main'], reverse=True)
            new_arcticles_list.append(article)
            context['object_list'] = new_arcticles_list

        return context


class ScopeListView(ListView):
    model = Scope
    ordering = 'topic'  # сортируем по разделам




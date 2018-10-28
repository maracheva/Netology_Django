from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'


    def get_queryset(self):

        articles_2 = self.model.objects.only('author', 'genre').select_related('author', 'genre').defer('author__phone')
        # print('база 2', articles_2.query)

        return articles_2

        # выведем список всех полей
        # articles_0 = self.model.objects.all() # 1,10 ms (1 запрос )
        # print('база 0', articles_0.query)
        # база 0
        # SELECT "articles_article"."id",
        #       "articles_article"."author_id",
        #       "articles_article"."genre_id",
        #       "articles_article"."title",
        #       "articles_article"."text",
        #       "articles_article"."published_at",
        #       "articles_article"."image" FROM "articles_article"


        # articles_1 = self.model.objects.defer('published_at').select_related('author', 'genre').defer('author__phone')
        # print('база 1', articles_1.query)
        # база 1 исключим сразу published_at
        # SELECT "articles_article"."id",
        #       "articles_article"."author_id",
        #       "articles_article"."genre_id",
        #       "articles_article"."title",
        #       "articles_article"."text",
        #       "articles_article"."image",
        #       "articles_author"."id",
        #       "articles_author"."name",
        #       "articles_genre"."id",
        #       "articles_genre"."name"
        # FROM "articles_article"
        # INNER JOIN "articles_author" ON ("articles_article"."author_id" = "articles_author"."id")
        # INNER JOIN "articles_genre" ON ("articles_article"."genre_id" = "articles_genre"."id")


        # база 2 выберем только поля 'author', 'genre', из select_related - даные из связанных моделей по полям
        # SELECT "articles_article"."id",
        #       "articles_article"."author_id",
        #       "articles_article"."genre_id",
        #       "articles_author"."id",
        #       "articles_author"."name",
        #       "articles_author"."phone",
        #       "articles_genre"."id",
        #       "articles_genre"."name"
        # FROM "articles_article"
        # INNER JOIN "articles_author" ON ("articles_article"."author_id" = "articles_author"."id")
        # INNER JOIN "articles_genre" ON ("articles_article"."genre_id" = "articles_genre"."id")



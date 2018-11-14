from django.db import models

class Scope(models.Model):
    topic = models.CharField(max_length=25, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    # добавим связь M2M
    scopes = models.ManyToManyField(Scope, through='ArticleScopeShip')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title

    # выведем список тегов в list_display admin.py
    def show_tags(self):
        return ', '.join([tag.topic for tag in self.scopes.all()[:3]])

    show_tags.short_description = 'Тематики статьи'

    # @property
    # def sorted_tags(self):
    #     return self.scopes.order_by('scopeship__is_main')


class ArticleScopeShip(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='scopeship')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'

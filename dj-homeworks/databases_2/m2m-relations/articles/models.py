from django.db import models

class Scope(models.Model):
    topic = models.CharField(max_length=25, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['topic']  # сортируем в алфавитном порядке

    def str(self):
        return self.topic

    # задаем уникальность имени
    def __unicode__(self):  #
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
        ordering = ['title']  # сортируем в алфавитном порядке

    def __str__(self):
        return self.title


class ArticleScopeShip(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
        ordering = ['scope'] # сортируем в алфавитном порядке
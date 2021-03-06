from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент') #Не обязательно к заполнению
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #При создании текущая дата устанавлевается
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Обнавлено') #Устанавливается при каждом редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', related_name='get_news')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_ad']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


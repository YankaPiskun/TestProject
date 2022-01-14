from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент') #Не обязательно к заполнению
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #При создании текущая дата устанавлевается
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Обнавлено') #Устанавливается при каждом редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_ad']
# Create your models here.

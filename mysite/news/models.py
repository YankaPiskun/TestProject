from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) #Не обязательно к заполнению
    created_ad = models.DateTimeField(auto_now_add=True) #При создании текущая дата устанавлевается
    updated_ad = models.DateTimeField(auto_now=True) #Устанавливается при каждом редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
# Create your models here.

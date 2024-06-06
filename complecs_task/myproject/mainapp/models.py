from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    name = models.TextField(max_length=150, verbose_name='Название публикации')
    image = models.FileField(upload_to='publication_images', blank=True, null=True, verbose_name='Изображение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Публикации'
        verbose_name_plural = 'Публикация'


class Comment(models.Model):
    name = models.TextField(max_length=150)
    publications = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Комментарии к посту')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время комента')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарий'

class Profile(models.Model):
    icon = models.FileField(upload_to='icon', blank=True, null=True, verbose_name='Аватарка')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
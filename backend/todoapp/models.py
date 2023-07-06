from django.contrib.auth.models import User
from django.db import models

class projectModel(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название проекта')
    url_repo = models.URLField(verbose_name='Ссылка на репозиторий')
    users = models.ManyToManyField(User, verbose_name='Список пользователей')

    def __str__(self):
        return self.name

class todoModel(models.Model):
    project = models.ForeignKey(projectModel, verbose_name='Проект', on_delete=models.CASCADE)
    todo_text = models.TextField(verbose_name='Текст заметки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активность todo')


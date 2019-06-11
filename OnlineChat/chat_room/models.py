from django.db import models

from django.contrib.auth.models import User     # брать пользователя через джангу
# from djoser.urls.base import User                для аутентификация пользователя (2вариант)


class Room(models.Model):
    """
    Модель комнаты чата
    """
    creator = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Участники', related_name='invited_user')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    """
    Модель чата
    """
    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=1000)
    date = models.DateTimeField('Дата отправки', auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение чат'
        verbose_name_plural = 'сообщения чатов'

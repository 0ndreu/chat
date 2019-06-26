from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room, Chat

"""
получаем данные из бд в json и наоборот
"""

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализация пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'username')



class RoomSerializers(serializers.ModelSerializer):
    """
    Сериализация комнат чата
    """
    creator = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ('id', 'creator', 'invited', 'date')


class ChatSerializers(serializers.ModelSerializer):
    """сериализация чата"""
    user = UserSerializer()     # добавили, чтобы правильно отображался юзер, иначе выводится его id
    class Meta:
        model = Chat
        fields = ('user', 'date', 'text')


class ChatPostSerializers(serializers.ModelSerializer):
    """сериализация чата"""
    class Meta:
        model = Chat
        fields = ('room', 'text')

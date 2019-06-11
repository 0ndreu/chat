from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализация пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'username')



class RoomSerializers(serializers.ModelSerializer):
    """
    Сериализация комнат чата (получем данные из БД в json и наоборот)
    """
    creator = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')


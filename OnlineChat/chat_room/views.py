from django.db.models import Q                  # для добавления запросов ИЛИ
from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions          # проверять пользователя и давать доступы

from django.contrib.auth.models import User

from .models import Room, Chat
from .serializers import RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializer


class Rooms(APIView):            # как работают классы и как работает APIView
    """
    Комнаты чата
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))          # Для корректного отображения диалогов у пользователей
        serializer = RoomSerializers(rooms, many=True)      # many = true - для чего?
        return Response({'data': serializer.data})

    def post(self, request):
        Room.objects.create(creator=request.user)
        return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]  # права лоступа к диалогам

    def get(self, request):
        room = request.GET.get('room')     # получаем комнату
        chat = Chat.objects.filter(room=room)        # дата передает номер комнаты, и по ней фильтруем
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.DATA.get('room')      можно принимать так, а можно через сериализатор
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)      # передаем юзера, который запостил
            return Response(status=201)
        else:
            return Response(status=400)

class AddUserRoom(APIView):
    """Добавление пользователей в комнату чата"""
    def get(self, request):     # возвращает список пользователей
        users = User.objects.all()  # список всех польхователей
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):  # добавление пользователя в комнату
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)


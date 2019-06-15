from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions          # проверять пользователя и давать доступы

from .models import Room, Chat
from .serializers import RoomSerializers, ChatSerializers, ChatPostSerializers


class Rooms(APIView):            # как работают классы и как работает APIView
    """
    Комнаты чата
    """
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)      # many = true - для чего?
        return Response({'data': serializer.data})


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]  # права лоступа к диалогам

    def get(self, request):
        room = request.GET.get('room')     # получаем комнату. Когда будет post, вместо GET будем писать DATA
        chat = Chat.objects.filter(room=room)        # дата передает номер комнаты, и по ней фильтруем
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.DATA.get('room')      можно принимать так, а можно через сериализатор
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)      # передаем юзера, который запостил
            return Response({'status': 'Added'})
        else:
            return Response({'status': 'Error'})



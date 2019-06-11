from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions          # проверять пользователя и давать доступы

from .models import Room
from .serializers import RoomSerializers


class Rooms(APIView):            # как работают классы и как работает APIView
    """
    Комнаты чата
    """
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)      # many = true - для чего?
        return Response({'data': serializer.data})

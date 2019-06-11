from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    """
    Комнаты чата
    """
    list_display = ('creator', 'invited_users', 'date')

    def invited_users(self, obj):           # obj - данная комната
        return '\n'.join([user.username for user in obj.invited.all()])  # обращаемся через поле invited и передаем usermane

admin.site.register(Room, RoomAdmin)

from django.contrib import admin
from .models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """
    Комнаты чата
    """
    list_display = ('creator', 'invited_users', 'date')

    def invited_users(self, obj):           # obj - данная комната
        return '\n'.join([user.username for user in obj.invited.all()])  # обращаемся через поле invited и передаем usermane
    """
    из за того, что invited_users это ManyToMany, мы делаем такую штуку
    """

class ChatAdmin(admin.ModelAdmin):
    """
    диалоги
    """
    list_display = ('room', 'user', 'text', 'date')


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)

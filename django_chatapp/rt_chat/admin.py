from django.contrib import admin
from rt_chat.models import ChatGroup, GroupMessage

# Register your models here.
# admin.site.register(ChatGroup)
admin.site.register(GroupMessage)



class ChatGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('users_online',)  # Enables a UI for selecting users | For debugging purposes

admin.site.register(ChatGroup, ChatGroupAdmin)

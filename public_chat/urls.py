from django.urls import path
from public_chat.views import find_chat_room, give_title, create_chat_room


urlpatterns = [
    path('chat_servers/', find_chat_room, name='find-chat-room'),
    path('chat_server/', give_title, name='chat-server'),
    path('create_chat_room/', create_chat_room, name='create-chat-room'),


]





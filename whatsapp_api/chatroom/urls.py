from django.urls import path
from chatroom.controller.chatroom_controller import create_chatroom, list_chatrooms, get_chatroom

urlpatterns = [
    path('chatroom/create/', create_chatroom),
    path('list/', list_chatrooms),
    path('<str:name>/',  get_chatroom),
]
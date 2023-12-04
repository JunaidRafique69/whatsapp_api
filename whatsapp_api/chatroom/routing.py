from django.urls import re_path
from django.urls import re_path

from chatroom.consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chatroom_name>\w+)/$', ChatConsumer.as_asgi()),
]
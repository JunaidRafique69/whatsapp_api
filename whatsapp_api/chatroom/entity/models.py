import uuid
from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    max_members = models.IntegerField()
    chatroom_id = models.UUIDField(default=uuid.uuid4, editable=False)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
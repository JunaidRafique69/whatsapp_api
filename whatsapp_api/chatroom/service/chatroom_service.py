from chatroom.repository.chatroom_repository import ChatRoomRepository
import uuid
from django.contrib.auth.models import User
from chatroom.models import ChatRoom
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ChatRoomService:
    def __init__(self):
        self.chatroom_repository = ChatRoomRepository()

    def create_chatroom(self, name, max_members):
        # Create the chatroom with the provided parameters
        chatroom = self.chatroom_repository.create_chatroom(name, max_members)
        return chatroom

    def list_chatrooms(self):
        try:
            chatrooms = self.chatroom_repository.get_all_chatrooms()
            result = [{'name': chatroom.name} for chatroom in chatrooms]
            return result
        except ValueError as e:
            return [{'error': str(e)}]

    def get_chatroom_by_name(self, name):
        return self.chatroom_repository.get_chatroom_by_name(name)
    
    def enter_chatroom(self, user, chatroom_name):
        try:
            chatroom = self.chatroom_repository.get_chatroom_by_name(chatroom_name)
            if chatroom.members.count() < chatroom.max_members:
                chatroom.members.add(user)
                chatroom.save()
            else:
                raise ValueError("Chatroom is full.")
        except Exception as e:
            raise e
   
    def leave_chatroom(self, user, chatroom_name):
        try:
            chatroom = self.chatroom_repository.get_chatroom_by_name(chatroom_name)

            if user.is_authenticated:
                # User is authenticated
                user_id = user.id

                # Your leave chatroom logic here, using the user_id and chatroom_name
                # Remove the user from the chatroom members
                chatroom.members.remove(user)
                chatroom.save()

                return {'success': True, 'message': f"User left chatroom '{chatroom_name}' successfully."}
            else:
                return {'success': False, 'error': "Anonymous users cannot leave chatrooms by name."}
        except Exception as e:
            return {'success': False, 'error': str(e)}
        

    def send_message(self, user, chatroom_name, message):
    # Get the channel layer
        channel_layer = get_channel_layer()

        # Send the message to the chatroom's WebSocket group
        async_to_sync(channel_layer.group_send)(
            f"chat_{chatroom_name}",
            {
                "type": "chat.message",
                "message": message,
            },
        )
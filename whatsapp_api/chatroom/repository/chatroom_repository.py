from chatroom.models import ChatRoom

class ChatRoomRepository:
    @staticmethod
    def create_chatroom(name, max_members):
        chatroom = ChatRoom(name=name, max_members=max_members)
        chatroom.save()
        return chatroom

    @staticmethod
    def get_all_chatrooms():
        return ChatRoom.objects.all()

    @staticmethod
    def get_chatroom_by_name(name):
        return ChatRoom.objects.get(name=name)
    
    @staticmethod
    def leave_chatroom(self, user_id, chatroom_name):
            result = self.chatroom_repository.remove_user_from_chatroom(user_id, chatroom_name)
            if result['success']:
                return {'success': True}
            else:
                return {'success': False, 'error': result['error']}
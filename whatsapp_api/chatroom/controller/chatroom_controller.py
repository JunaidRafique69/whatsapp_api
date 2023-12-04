import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatroom.service.chatroom_service import ChatRoomService
from chatroom.models import ChatRoom

chatroom_service = ChatRoomService()

@csrf_exempt
def create_chatroom(request):
    if request.method == 'POST':
        # Parse JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        max_members_str = data.get('max_members')
        print(f"Received parameters - name: {name}, max_members: {max_members_str}")

        # Check if max_members parameter is provided
        if max_members_str is None:
            return JsonResponse({"error": "Max members parameter is required."}, status=400)

        # Validate max_members value (you may need additional validation)
        try:
            max_members = int(max_members_str)
            if max_members <= 0:
                raise ValueError("Max members should be a positive integer.")
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        try:
            # Create the chatroom
            chatroom = chatroom_service.create_chatroom(name, max_members)
            return JsonResponse({"message": f"Chatroom '{chatroom.name}' created successfully."})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."})

@csrf_exempt
def list_chatrooms(request):
    try:
        chatrooms = chatroom_service.list_chatrooms()
        return JsonResponse({"chatrooms": chatrooms})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def enter_chatroom(request, chatroom_name):
    if request.method == 'POST':
        try:
            user = request.user
            user_id = user.id if user and user.id else None

            chatroom_service.enter_chatroom(user_id, chatroom_name)
            return JsonResponse({"message": f"Entered chatroom '{chatroom_name}' successfully."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method."})


@csrf_exempt
def leave_chatroom(request, chatroom_name):
    if request.method == 'POST':
        try:
            user = request.user
            user_id = user.id if user and user.id else None

            chatroom_service.leave_chatroom(user_id, chatroom_name)
            return JsonResponse({"message": f"Left chatroom '{chatroom_name}' successfully."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method."})


def get_chatroom(request, name):
    try:
        chatroom = chatroom_service.get_chatroom_by_name(name)
        return JsonResponse({"chatroom": {"name": chatroom.name, "max_members": chatroom.max_members}})
    except ChatRoom.DoesNotExist:
        return JsonResponse({"error": "Chatroom not found."})


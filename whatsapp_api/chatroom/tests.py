# from django.test import TestCase

# from channels.testing import WebsocketCommunicator
# from whatsapp_api.routing import application

# async def test_chatroom_creation():
#     communicator = WebsocketCommunicator(application, "/ws/chatroom/create/")
#     connected, subprotocol = await communicator.connect()

#     assert connected

#     # Send a message
#     await communicator.send_json_to({
#         'name': 'Test Chatroom',
#         'max_members': 10,
#     })

#     # Receive the response
#     response = await communicator.receive_json_from()

#     assert response.get('message') == 'Chatroom "Test Chatroom" created with 10 max members.'

#     await communicator.disconnect()

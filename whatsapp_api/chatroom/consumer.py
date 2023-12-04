import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type')
        
        if message_type == 'text':
            message = text_data_json.get('message')
            await self.send(text_data=json.dumps({
                'message_type': 'text',
                'message': f'Text message received: {message}',
            }))
        elif message_type == 'attachment':
            # Handle attachment
            attachment_data = text_data_json.get('attachment')
            filename = attachment_data.get('filename')
            content = attachment_data.get('content')

            attachment_type = attachment_data.get('type', 'picture')  
            save_directory = os.path.join('root', attachment_type)

            os.makedirs(save_directory, exist_ok=True)

            file_path = os.path.join(save_directory, filename)
            with open(file_path, 'wb') as file:
                file.write(content)

            await self.send(text_data=json.dumps({
                'message_type': 'attachment',
                'message': f'Attachment saved: {file_path}',
            }))


    # async def chat_message(self, event):
    #     message = event['message']

    #     # Send the message to the WebSocket
    #     await SelfReg.send(text_data=json.dumps({
    #         'message': message
    #     }))
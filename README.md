# WhatsApp API Server

## Table of Contents

1. [Introduction](#introduction)
2. [Infrastructure](#infrastructure)
3. [Endpoints](#endpoints)
   - [1. Create Chatroom](#1-create-chatroom)
   - [2. List Chatroom](#2-list-chatroom)
   - [3. Leave Chatroom](#3-leave-chatroom)
   - [4. Enter Chatroom](#4-enter-chatroom)
   - [5. Send Message](#5-send-message)
   - [7. Send Attachment](#7-send-attachment)
4. [WebSocket Usage](#websocket-usage)
5. [Running Servers](#running-servers)
6. [Testing with WebSocketKing](#testing-with-websocketking)
7. [API Documentation](#api-documentation)

## Introduction

Welcome to the WhatsApp API server! This server provides a set of endpoints to create chatrooms, manage chatroom memberships, send messages, and more. The server leverages Django and Django Channels for the backend, ensuring a scalable and real-time chat experience.

## Infrastructure

- **Django**: A high-level Python web framework used for building robust web applications. In this case, it provides the foundation for the API endpoints and overall server structure.

- **Django Channels**: An extension for Django to handle WebSockets and other asynchronous protocols. It enables real-time communication between users in chatrooms.

- **Database Schema**: The server utilizes a relational database (RDB) schema for storing chatroom and message data. This ensures data consistency and easy retrieval.

- **WebSocket**: WebSockets are employed to facilitate real-time communication within chatrooms. This allows users to receive messages instantly without the need to constantly poll the server.

## Endpoints

## Create Chatroom

**Endpoint**: ` /chatroom/create`

**Method**: Post

```json
{
  "name": "whatsapp_chatroom2",
  "max_members": 10
}
```

### 2. List Chatroom

**Endpoint**: `/list-chatroom`

**Method**: GET

### 3. Leave Chatroom

**Endpoint**: `/leave-chatroom/{chatroom_name}`

**Method**: POST

### 4. Enter Chatroom

**Endpoint**: `/enter-chatroom/{chatroom_name}`

**Method**: POST

### 5. Send Message

**Endpoint**: `/send-message/{chatroom_name}`

**Method**: Web Socket

**Request Body**:

```json
{
  "type": "text",
  "message": "Hello, this is a text message!"
}
```

### 6. Send Attachment

**Endpoint** `/send-message/{chatroom_name}`

**Method**: Web Socket

```json
{
  "type": "attachment",
  "attachment": {
    "type": "video",
    "filename": "example_video.mp4",
    "content": "base64_encoded_content_here"
  }
}
```

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'n/a'

class FriendRequest:
    def __init__(self, data):
        request_id = data['request_id']
        recipient_id = data['recipient_id']
        sender_id = data['sender_id']
        created_at = data['created_at']
        updated_at = data['updated_at']
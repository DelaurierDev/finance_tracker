from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'finance_db'

class Friend:
    def __init__(self, data):
        relationship_id = data['relationship_id']
        user_id = data['user_id']
        friend_id = data['friend_id']
        created_at = data['created_at']
        updated_at = data['updated_at']
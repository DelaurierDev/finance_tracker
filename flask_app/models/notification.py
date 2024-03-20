from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'finance_db'

class Notification:
    def __init__(self, data):
        noti_id = data['noti_id']
        user_id = data['user_id']
        notification = data ['notification']
        created_at = data['created_at']
        updated_at = data['updated_at']
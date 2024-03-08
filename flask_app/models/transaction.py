from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'n/a'

class Transaction:
    def __init__(self, data):
        transaction_id = data['transaction_id']
        transaction_amount = data['transaction_amount']
        user_to = data['user_to']
        user_from = data['user_from']
        created_at = data['created_at']
        updated_at = data['updated_at']
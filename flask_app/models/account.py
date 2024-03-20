from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'finance_db'

class Account:
    def __init__(self, data):
        account_id = data['account_id']
        user_id = data['user_id']
        account_name = data['account_name']
        balance = data['balance']
        isChecking = data['isChecking']
        created_at = data['created_at']
        updated_at = data['updatedd_at']
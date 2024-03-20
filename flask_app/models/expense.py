from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'finance_db'

class Expense:
    def __init__(self, data):
        expense_id = data['expense_id']
        user_id = data['user_id']
        amount = data['amount']
        due_date = data['due_date']
        created_at = data['created_at']
        updated_at = data['updated_at']
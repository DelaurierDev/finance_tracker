from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
mydb = "n/a"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #Creating a class method to save users into the database when they create a user
    @classmethod
    def save_user(cls,data):
        query = 'INSERT INTO users (created_at, updated_at, password, username) VALUES (NOW(), NOW(),%(password)s,%(username)s);'
        return connectToMySQL(mydb).query_db(query,data)
    
    #A method used to get a user by user id
    @classmethod
    def get_by_id(cls, data):
        query = '''
        SELECT *
        FROM users
        WHERE id = %(id)s
        '''
        results = connectToMySQL(mydb).query_db(query,data)
        return results[0]
    
    #a method for validating login and user information    
    @staticmethod
    def validate_user(user):
        is_valid = True

        if len(user['username']) <3:
            flash("Usename must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be 8 characters or greater.")
            is_valid = False
        if user['password'] != user['confpassword']:
            flash("Passwords do not match!")
            is_valid = False
        return is_valid
    
    #A Method used to find the user by username so they can login from that as well.
    @classmethod
    def get_by_username(cls,data):
        query = '''
        SELECT *
        FROM users
        WHERE username = %(username)s'''

        result = connectToMySQL(mydb).query_db(query,data)

        if len(result) < 1:
            return False
        return cls(result[0])
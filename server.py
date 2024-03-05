from flask_app import app
from flask_app.controllers import users, transactions, notifications, friends, friend_requests,expenses,accounts


if __name__ == '__main__':
    app.run(debug=True)
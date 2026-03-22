# Location: App/models.py
# Database models
# Importing the database instance from the app factory
from App import mydb
# Task model definition / Table structure
class Task(mydb.Model):
    id = mydb.Column(mydb.Integer, primary_key=True)
    title = mydb.Column(mydb.String(100), nullable=False)
    status = mydb.Column(mydb.String(20), default="Pending")

    def __repr__(self):
        return f"<Task {self.id}: {self.title} [{self.status}]>"

# User model definition / Table structure
class User(mydb.Model):
    id = mydb.Column(mydb.Integer, primary_key=True)
    username = mydb.Column(mydb.String(100), nullable=False, unique=True)
    password = mydb.Column(mydb.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"
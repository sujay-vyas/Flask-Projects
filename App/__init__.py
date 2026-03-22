# App Factory
# Location: App/__init__.py
# Flask application initialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the Flask application and database instance
mydb = SQLAlchemy()

# Function to create and configure the Flask application
def create_app():
    todoapp = Flask(__name__, template_folder='templates', static_folder='static')
    todoapp.config['SECRET_KEY'] = 'RAYVIN'
    # Database configuration
    todoapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    todoapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Connecting the database instance to the Flask app
    #mydb.__init__(todoapp)
    mydb.init_app(todoapp)

    # Importing and registering blueprints
    from App.routes.Auth import auth_bp
    from App.routes.Task import task_bp   
    from App.routes.Register import register_bp
    todoapp.register_blueprint(auth_bp)
    todoapp.register_blueprint(task_bp)
    todoapp.register_blueprint(register_bp)

    return todoapp
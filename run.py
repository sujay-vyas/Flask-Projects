from App import create_app,mydb
from App.models import Task

app = create_app()
with app.app_context():
    mydb.create_all()
    # Optionally, you can add some initial data to the database

if __name__ == '__main__':
    app.run(debug=True)
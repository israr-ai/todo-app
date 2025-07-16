pip install virtualenv
virtualenv env
.\env\Scripts\activate.ps1
pip install flask
 pip install flask-sqlalchemy (for database)

 ## import the database in python
 ```
 >>python (enter) in virtual envirment 
 >>pip install flask flask_sqlalchemy
 >> in main.py
  Set DB path to SQLite file
>>BASE_DIR = os.path.abspath(os.path.dirname(__file__))
>>DB_PATH = os.path.join(BASE_DIR, 'todo.db')  # You can change the file name
 
 create_db.py
 ```
 from app import app, db

with app.app_context():
    db.create_all()
    print("✅ SQLite DB created: todo.db")
 ```

 >> Runto crate DB
 >python create_db.py
```
 ## sqlite viewer
 ```
 drag and drop the sql file in the sqlite viewer to show the all data .
 ```

 ## open the sqlalchemy doc 

 ## development HEROKU
 ```
 >>go to HERoku and create the account.
 >>install the hero cli
 >>in project install
 >>pip install guicorn
 >>pip freeze > requirements.txt
 >> create the Procfile
 ```
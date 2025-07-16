import os
from flask import Flask ,render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from main import app, db

app = Flask(__name__)
# Absolute path to external folder
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'external_data', 'mydata.db')


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.now)

    def __repr__(self) -> str:
        return f"{self.title} - { self.desc}"
    
   
@app.route("/", methods=['GET','POST'])
def hello_world():
    print("Request method :",request.method)
    if request.method == "POST":
        print("post")
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

   
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo=alltodo)

@app.route('/show')
def product():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<h1>this is products page</h1>"

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method == "POST":
       title = request.form.get('title')
       desc = request.form.get('desc')  
       todo = Todo.query.filter_by(sno=sno).first()
       todo.title = title
       todo.desc = desc
       db.session.add(todo)
       db.session.commit()
       return redirect('/')
    else:
     todo = Todo.query.filter_by(sno=sno).first()   
     return render_template('update.html' ,utodo=todo)

if __name__ == "__main__":
    app.run(debug=True )
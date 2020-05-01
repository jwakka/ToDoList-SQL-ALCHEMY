from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from form import ToDoList
import os





app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text =db.Column(db.String(200))
    complete = db.Column(db.Boolean)



@app.route('/')
def index():
    form =ToDoList()
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
  

    return render_template('index.html', incomplete=incomplete, complete=complete, form =form)

@app.route('/add', methods=[ 'POST'])
def add():
   
   
    todo = Todo(text=request.form['message'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
   
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.delete(todo)
   
    
    db.session.commit()
    
    return redirect(url_for('index'))







if __name__ == '__main__':
    app.run(debug=True)
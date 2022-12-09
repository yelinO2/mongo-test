from json import dumps
from flask import Flask,request
from models.note import Note
from database import Database


app = Flask(__name__)

Database.initialize()

note = Note(1, "MyFirstNote", "Hello World")

@app.route('/')
def Home():
    return "Welcome to Simple Note"

@app.route('/notes/')
def get_notes():
    result = note.from_mongo(1)
    return dumps(result)

@app.route('/notes/', methods = ['POST'])
def post_note():
    new_note = request.get_json()
    new_note_to_create = Note(new_note['note_id'], new_note['title'], new_note['content'])
    new_note_to_create.save_to_db()
    return new_note_to_create.json()

@app.route('/notes/<string:note_id>')
def search_note(note_id):
    note = Note.from_mongo(note_id)
    return note.json()
    

app.run(debug=True)
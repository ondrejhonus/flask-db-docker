
from flask import Flask, render_template, request, redirect, url_for 
from pymongo import MongoClient 
from bson import ObjectId 
  
app = Flask(__name__) 
  
client = MongoClient(host='test_mongodb',port=27017, username='root', password='pass',authSource="admin") 
db = client.mytododb 
notes_collection = db.notes 
  
@app.route('/') 
def index(): 
    notes = notes_collection.find() 
    return render_template('index.html', notes=notes) 
  
@app.route('/add_note', methods=['POST']) 
def add_note(): 
    note_name = request.form.get('note_name') 
    if note_name: 
        notes_collection.insert_one({'name': note_name}) 
    return redirect(url_for('index')) 
  
@app.route('/delete_note/<note_id>', methods=['GET']) 
def delete_note(note_id): 
    notes_collection.delete_one({'_id': ObjectId(note_id)}) 
    return redirect(url_for('index')) 
  
if __name__ == '__main__': 
    app.run(host='0.0.0.0',debug=True) 

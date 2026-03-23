from flask import Flask, request, render_template, redirect
import os
import json
from datetime import datetime

app = Flask(__name__)


# Configuration from environment variables
NOTES_FILE = os.environ.get("NOTES_FILE", "/data/notes.json")
APP_NAME = os.environ.get("APP_NAME", "My Notes App")


# Ensure the data directory exists
os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []


def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)


@app.route('/')
def home():
    notes = load_notes()
    return render_template('index.html', notes=notes, app_name=APP_NAME)


@app.route('/add', methods=['POST'])
def add_note():
    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': request.form.get('title', 'Untitled'),
        'content': request.form.get('content', ''),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes(notes)
    return redirect('/')


if __name__ == '__main__':
    # Create empty notes file if it doesn't exist
    if not os.path.exists(NOTES_FILE):
        save_notes([])
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
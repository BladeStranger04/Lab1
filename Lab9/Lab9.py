import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/')
@app.route('/main', methods=['GET'])
def main():
    return render_template('index.html', messages=[])

@app.route('/create', methods=['POST'])
def create():
    message = ''
    name = request.form['name']
    link = request.form['link']
    conn = get_db_connection()
    in_ = conn.execute('select name, link from db where name=?', (name,)).fetchall()
    if in_:
        message = f'User with nickname {name} found. Link changed.'
        conn.execute('UPDATE db SET link=? where name=?',
                     (name,link))
    else:
        message = f'User {name} with link {link} added.'
        conn.execute('INSERT INTO db (name, link) VALUES (?, ?)',
                     (name, link))
    conn.commit()
    conn.close()
    messages.append(message)
    return render_template('index.html', messages=messages)

if __name__ == "__main__":
    init_db()
    app.run()
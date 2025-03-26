from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = 'children.db'

# Create a route to select all children
@app.route('/children', methods=['GET'])
def get_children():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.execute('SELECT * FROM children')
    children = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return children

if __name__ == '__main__':
    app.run()

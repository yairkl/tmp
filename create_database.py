import sqlite3
import datetime
connection = sqlite3.connect('children.db')
cursor = connection.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS children (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthDate DATE NOT NULL
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO children (name, birthDate) VALUES (?, ?)
''', [
    ('Alice', datetime.date(2006, 5, 5)),
    ('Bob', datetime.date(2007, 6, 6)),
    ('Charlie', datetime.date(2008, 7, 7)),
    ('David', datetime.date(2009, 8, 8)),
    ('Eve', datetime.date(2010, 9, 9)),
    ('Frank', datetime.date(2011, 10, 10)),
    ('Grace', datetime.date(2012, 11, 11)),
    ('Heidi', datetime.date(2013, 12, 12)),
    ('Ivan', datetime.date(2014, 1, 1)),
    ('Judy', datetime.date(2015, 2, 2))
])

connection.commit()
connection.close()

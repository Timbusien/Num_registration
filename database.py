import sqlite3

db = sqlite3.connect('data')

NUM = db.cursor()

NUM.execute('CREATE TABLE IF NOT EXISTS user'
            '(name TEXT, number TEXT);')

def user_reg(name, number):
    db = sqlite3.connect('data')
    NUM = db.cursor()

    NUM.execute('INSERT INTO user '
                '(name, number) VALUES'
                '(?,?);', (name, number))

    db.commit()


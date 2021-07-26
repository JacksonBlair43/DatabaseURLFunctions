import sqlite3

connection = sqlite3.connect('testDB.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages
              (ID TEXT, message TEXT)''')

connection.commit()
connection.close()

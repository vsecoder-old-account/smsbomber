import sqlite3

#Коннект к базе
db = sqlite3.connect('database.db')
sql = db.cursor()

sql.execute("ALTER TABLE User ADD COLUMN bio TEXT")
db.commit()
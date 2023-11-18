import sqlite3

conection = sqlite3.connect('data.db')
sql = conection.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number TEXT, telegram_id INTEGER)""")


def register_user(name, number, telegram_id):
    conection = sqlite3.connect('data.db')
    sql = conection.cursor()

    sql.execute("""INSERT INTO users (name, number, telegram_id)""")
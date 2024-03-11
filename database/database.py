import sqlite3

class DataBase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = sqlite3.connect(self.path_to_db)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY,
            full_name VARCHAR(50),
            phone_number VARCHAR(13)
        )'''
        self.execute(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = """INSERT INTO users(telegram_id) VALUES (?) ON CONFLICT DO NOTHING"""
        self.execute(sql, parameters=(telegram_id,), commit=True)

    def chek_user(self, telegram_id):
        sql = '''SELECT full_name, phone_number FROM users WHERE telegram_id = ?'''
        return self.execute(sql, parameters=(telegram_id), fetchone=True)


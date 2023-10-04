import sqlite3

class SignUp:
    def __init__(self, db_name='bot_database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_user(self, telegram_id):
        self.cursor.execute('''
            INSERT INTO users (telegram_id)
            VALUES (?)
        ''', (telegram_id,))
        self.conn.commit()

    def get_user(self, telegram_id):
        self.cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
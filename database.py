import sqlite3

conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER,
    race TEXT,
    class TEXT
)
''')
conn.commit()
conn.close()
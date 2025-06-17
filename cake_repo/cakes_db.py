import sqlite3

class CakesDatabase:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()
        
    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS 
        meals (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        calories INTEGER,
        price REAL)
         """)
        self.conn.commit()
    
    def add_meal(self, name, calories, price):
        self.cur.execute(
            "INSERT INTO meals (name, calories, price) VALUES (?, ?, ?)",
            (name, calories, price)
        )
        self.conn.commit()
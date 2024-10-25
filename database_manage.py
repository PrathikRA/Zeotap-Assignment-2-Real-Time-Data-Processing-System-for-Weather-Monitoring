import sqlite3

class DBManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        """
        Create table to store daily weather data.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_summary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                date TEXT,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT
            )
        """)
        self.conn.commit()

    def insert_summary(self, city, date, avg_temp, max_temp, min_temp, dominant_condition):
        """
        Insert daily weather into the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (city, date, avg_temp, max_temp, min_temp, dominant_condition))
        self.conn.commit()

    def get_summaries(self):
        """
        Retrieve all weather data.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM weather_summary")
        return cursor.fetchall()

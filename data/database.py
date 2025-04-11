### data/database.py

python
import sqlite3
import os

DB_PATH = "kisandost_data.db"

def init_db():
    """
    Initializes the SQLite database and tables if they don't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS farming_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            soil_moisture REAL,
            temperature REAL,
            humidity REAL,
            crop_suggestion TEXT,
            irrigation_advice TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_data(timestamp, soil_moisture, temperature, humidity, crop_suggestion, irrigation_advice):
    """
    Inserts a new farming data record.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO farming_data (timestamp, soil_moisture, temperature, humidity, crop_suggestion, irrigation_advice)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, soil_moisture, temperature, humidity, crop_suggestion, irrigation_advice))

    conn.commit()
    conn.close()


def fetch_all_data():
    """
    Fetches all records from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM farming_data')
    rows = cursor.fetchall()

    conn.close()
    return rows



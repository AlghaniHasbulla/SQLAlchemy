import sqlite3
from pathlib import Path

DB_NAME = "data.db"  

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    return conn
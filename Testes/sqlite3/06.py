import sqlite3
from os import getenv, path

conn = sqlite3.connect(path.join(getenv("APPDATA"), "database.db"))
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS smogon (
    nome TEXT
)
""")


# TextParser_to_MySQL.py
import os
import requests
import json
from datetime import datetime, timezone
import mysql.connector

def read_text_file():
    file_path = "/mnt/localfiles/Letters.txt"
    print(f"Trying to read file at: {file_path}")  
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def logToDatabase():
    file_path = "/mnt/data/Letters.txt"

    db_config = {
        'host': '192.168.1.5',
        'user': 'root',      # Replace with your MySQL username
        'password': 'Kora4386!',  # Replace with your MySQL password
        'database': 'tylerpacdev'       # This matches the schema in your Workbench
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_contents (
                id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT
            );
        ''')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            cursor.execute("INSERT INTO file_contents (content) VALUES (%s);", (line.strip(),))

        conn.commit()
        print(f"Inserted {cursor.rowcount} rows into the database.")

    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    read_text_file()
    logToDatabase()
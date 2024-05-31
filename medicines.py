import sqlite3
from database import create_connection

def add_medicine(name, generic, company, price, quantity, expiry_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Medicines (name, generic, company, price, quantity, expiry_date) VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, generic, company, price, quantity, expiry_date))
    conn.commit()
    conn.close()

def get_all_medicines():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medicines")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_medicine(medicine_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Medicines WHERE id = ?', (medicine_id,))
    conn.commit()
    conn.close()

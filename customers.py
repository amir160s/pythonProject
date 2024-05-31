import sqlite3
from database import create_connection

def add_customer(name, contact):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Customers (name, contact) VALUES (?, ?)
    ''', (name, contact))
    conn.commit()
    conn.close()

def get_all_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_customer(customer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()

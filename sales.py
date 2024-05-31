import sqlite3
from database import create_connection

def add_sale(medicine_id, customer_id, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Sales (medicine_id, customer_id, quantity, date) VALUES (?, ?, ?, datetime('now'))
    ''', (medicine_id, customer_id, quantity))
    conn.commit()
    conn.close()

def get_all_sales():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sales")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_sale(sale_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Sales WHERE id = ?', (sale_id,))
    conn.commit()
    conn.close()

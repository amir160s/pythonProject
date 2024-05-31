import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('pharmacy.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def setup_database():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()

        # Drop the Medicines table if it exists (optional, only for initial setup/testing)
        cursor.execute('DROP TABLE IF EXISTS Medicines')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medicines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            generic TEXT NOT NULL,
            company TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            expiry_date TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
            id INTEGER PRIMARY KEY,
            medicine_id INTEGER,
            customer_id INTEGER,
            quantity INTEGER NOT NULL,
            date TEXT NOT NULL,
            salename TEXT NOT NULL,
            FOREIGN KEY(medicine_id) REFERENCES Medicines(id),
            FOREIGN KEY(customer_id) REFERENCES Customers(id)
        )
        ''')

        conn.commit()
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

# Call the setup_database function to ensure the database is ready
setup_database()

from database import create_connection

def login():
    conn = create_connection()
    cursor = conn.cursor()

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password exist in the database
    cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        # Call the main application function here
    else:
        print("Invalid username or password")

    conn.close()

from database import create_connection

def create_user():
    conn = create_connection()
    cursor = conn.cursor()

    # Prompt user to create a new username and password
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    # Insert the new user into the database
    cursor.execute("INSERT INTO Users (username=amir, password=1234) VALUES (?, ?)", (new_username, new_password))
    conn.commit()

    print("User created successfully!")

    conn.close()

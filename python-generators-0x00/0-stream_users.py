#!/usr/bin/env python3
import mysql.connector

def stream_users():
    """Generator that yields user rows one by one from the user_data table."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wiseman",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row  # Yield one row at a time

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return  # Exit gracefully if there's a connection or query error

#!/usr/bin/env python3
import mysql.connector

# Generator that streams user ages one by one
def stream_user_ages():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wiseman",
            database="ALX_prodev"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT age FROM user_data")

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row[0]

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return

# Function to compute average age using the generator
def compute_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        print(f"Average age of users: {total_age / count:.2f}")
    else:
        print("No user data found.")

# Run it
if __name__ == "__main__":
    compute_average_age()

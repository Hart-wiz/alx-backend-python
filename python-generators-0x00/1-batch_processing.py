#!/usr/bin/env python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of user rows from the database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wiseman",
            database="ALX_prodev"
        )

        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM user_data")
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch  # Yield a whole batch at a time

        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):  # 1st loop
        filtered_users = (user for user in batch if user.get('age', 0) > 25)  # generator expression
        for user in filtered_users:  # 2nd loop
            yield user

#!/usr/bin/env python3
import mysql.connector

def paginate_users(page_size, offset):
    """Fetch a page of users from the database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wiseman",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []

def lazy_paginate(page_size):
    """Generator that lazily yields users one page at a time."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        for user in page:
            yield user
        offset += page_size

#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows
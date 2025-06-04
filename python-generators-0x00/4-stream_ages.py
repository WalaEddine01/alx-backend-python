#!/usr/bin/python3
"""
"""
from mysql import connector
from mysql.connector import Error
import seed
lazy_paginator = __import__("2-lazy_paginate").lazy_paginate


def stream_user_ages():
    """
    """
    connection = seed.connect_to_prodev()
    for page in lazy_paginator(100):
        yield from page
    connection.close()


def avg_calculator():
    """
    """
    ages = stream_user_ages()
    avg = 0
    num_of_users = 0
    for age in ages:
        avg = avg + age["age"]
        num_of_users += 1

    avg = avg / num_of_users if num_of_users > 0 else 0
    print(f"Average age of users: {avg}")


if __name__ == "__main__":
    avg_calculator()

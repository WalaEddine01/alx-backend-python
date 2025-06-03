#!/usr/bin/python3

from uuid import uuid4
import uuid
import re

with open("user_data.csv", 'r') as file:
    next(file)
    prepared_data = [
        (str(uuid.uuid4()), name.strip(), email.strip(), int(age.strip().strip('"')))
        for line in file
        for name, email, age in [line.strip().split(',')]
    ]
    print(prepared_data)
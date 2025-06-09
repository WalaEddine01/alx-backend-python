#!/usr/bin/python3

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
)

logging.info("This is a test log entry.")

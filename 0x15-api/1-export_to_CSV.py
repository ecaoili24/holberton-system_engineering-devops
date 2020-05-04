#!/usr/bin/python3
"""
The following extends the Python script in task 0
to export data in CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    R = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                     .format(argv[1])).json()
    R_two = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'
        .format(argv[1])).json()

    userID = argv[1]
    name = R.get('username')
    with open('{:}.csv'.format(argv[1]), mode='w') as user_id_file:
        user_writer = csv.writer(user_id_file, quoting=csv.QUOTE_ALL)
        for task in R_two:
            user_writer.writerow([userID, name, task.get('completed'),
                                  task.get('title')])

#!/usr/bin/python3
"""
The following extends the Python script in task 0
to export data in CSV format
"""


import csv
import json
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
    tasks = {}
    list_task = []
    for item in R_two:
        task = {}
        task['task'] = item.get('title')
        task['completed'] = item.get('completed')
        task['username'] = name
        list_task.append(task)

    tasks[userID] = list_task

    with open("{:}.json".format(userID), 'w') as f:
        json.dump(tasks, f)

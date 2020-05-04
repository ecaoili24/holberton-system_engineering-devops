#!/usr/bin/python3
"""
The following module takes an employee ID and
returns information about his/her
TO DO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
        R = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                         .format(argv[1])).json()
        R_two = requests.get(
                'https://jsonplaceholder.typicode.com/todos/?userId={:}'
                .format(argv[1])).json()

        EMPLOYEE_NAME = R.get('name')
        TASK_TITLE = []
        NUMBER_OF_DONE_TASKS = 0

        for task in R_two:
                if task.get('completed') is True:
                        TASK_TITLE.append(task.get('title'))
                        NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(R_two)
        print("Employee {} is done with tasks({}/{}):".
              format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                     TOTAL_NUMBER_OF_TASKS))

        for t in TASK_TITLE:
                print("\t {}".format(t))

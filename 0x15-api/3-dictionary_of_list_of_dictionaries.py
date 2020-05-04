#!/usr/bin/python3
"""
Extentsion of Python script to
export data in the JSON format
"""
import json
import requests


if __name__ == "__main__":
    dict_tasks = {}
    R = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    R_two = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dict_tasks = {item.get("id"):
                  [{"task": j.get("title"),
                    "completed": j.get("completed"),
                    "username": item.get("username")}
                   for j in R_two
                   if j.get("userId") == item.get("id")]
                  for item in R}

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict_tasks, f)

#!/usr/bin/python3
""" to fetche and display TODO list progress for a given employee"""

import requests
from sys import argv

if __name__ == '__main__':
    # Get the user ID from the command line argument
    user_id = argv[1]

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the user information
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Get the user's TODO list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Filter the completed tasks
    completed_tasks = [task for task in todos if task.get('completed') is True]

    # Print the user's progress
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
        len(completed_tasks), len(todos)))

    # Print the titles of completed tasks
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))

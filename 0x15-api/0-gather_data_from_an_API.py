#!/usr/bin/python3

"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Fetch employee data
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch todo list
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_list = response.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = len([task for task in todo_list if task['completed']])
    progress = f"{employee_name} is done with tasks ({completed_tasks}/{total_tasks}):"

    # Display progress
    print(progress)
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)


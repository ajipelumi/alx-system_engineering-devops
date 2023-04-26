#!/usr/bin/python3
"""
Exports data in the JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()
    filename = '{}.json'.format(employee_id)
    todo_dict = {employee_id: []}

    # Format data
    for todo in todo_response:
        if todo.get("userId") == employee_id:
            todo_dict[employee_id].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_response.get("username")})

    # Export data into file
    with open(filename, 'w') as f:
        # Dump data into file
        json.dump(todo_dict, f)

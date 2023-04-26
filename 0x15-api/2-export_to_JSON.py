#!/usr/bin/python3
"""
Exports data in the JSON format.
"""
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
    todo_str = '{{ "{}": ['.format(employee_id)

    # Format data
    for idx, todo in enumerate(todo_response):
        if todo.get("userId") == employee_id:
            todo_str += '{{"task": "{}", "completed": {}, "username": "{}"}}, '\
                .format(todo.get("title"),
                        todo.get("completed"),
                        user_response.get("username"))

    todo_str = todo_str[:-2]  # Remove the trailing comma and space
    todo_str += "]}"

    # Export data into file
    with open(filename, 'w') as f:
        # Write string into file
        f.write(todo_str)

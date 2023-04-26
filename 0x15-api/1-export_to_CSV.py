#!/usr/bin/python3
"""
Exports data in the CSV format.
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
    filename = '{}.csv'.format(employee_id)
    todo_str = ""

    # Format data
    for todo in todo_response:
        if todo.get("userId") == employee_id:
            todo_str += '"{}","{}","{}","{}"\n'.format(
                    employee_id,
                    user_response.get('username'),
                    todo.get('completed'),
                    todo.get('title'))

    # Export data into file
    with open(filename, 'w') as f:
        # Write string into file
        f.write(todo_str)

#!/usr/bin/python3
""" This script returns information about an employee TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos'
    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()
    total = 0
    completed = 0
    completed_list = []

    for todo in todo_response:
        if todo.get("userId") == employee_id:
            total += 1
            if todo.get("completed"):
                completed += 1
                completed_list.append(todo)

    print('Employee {} is done with tasks({}/{})'.format(
                  user_response.get('name'),
                  completed,
                  total))

    for item in completed_list:
        print('\t{}'.format(item.get("title")))

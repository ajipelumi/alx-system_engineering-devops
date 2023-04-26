#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about the
employee TODO list progress.
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
    total = 0
    completed = 0
    completed_list = []

    # Get completed and total tasks
    for todo in todo_response:
        if todo.get("userId") == employee_id:
            total += 1
            if todo.get("completed"):
                completed += 1
                completed_list.append(todo)

    # Print Employee name as well as completed and total tasks
    print('Employee {} is done with tasks({}/{}):'.format(
                  user_response.get('name'),
                  completed,
                  total))

    # Print list of completed tasks
    for item in completed_list:
        print('\t {}'.format(item.get("title")))

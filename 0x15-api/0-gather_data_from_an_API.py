#!/usr/bin/python3
"""
This script returns information about an employee TODO list progress.
First line: Employee <EMPLOYEE_NAME> is done with tasks
    (<NUMBER_OF_DONE_TASKS>/<TOTAL_NUMBER_OF_TASKS>):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
        completed and non-completed tasks
Second and N next lines display the title of completed tasks: <TASK_TITLE>
    (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import sys
import requests


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

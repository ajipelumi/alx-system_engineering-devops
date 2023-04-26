#!/usr/bin/python3
"""
Exports data in the JSON format.
"""
import json
import requests


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    user_response = requests.get(user_url).json()
    filename = 'todo_all_employees.json'
    todo_dict = {}

    for user in user_response:
        employee_id = user.get("id")
        todo_dict[employee_id] = []
        todo_url = 'https://jsonplaceholder.typicode.com/todos'
        todo_response = requests.get(todo_url).json()

        for todo in todo_response:
            if todo.get("userId") == employee_id:
                todo_dict[employee_id].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")})

    # Export data into file
    with open(filename, 'w') as f:
        # Dump data into file
        json.dump(todo_dict, f)

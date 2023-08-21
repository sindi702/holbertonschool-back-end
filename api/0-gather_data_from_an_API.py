#!/usr/bin/python3
"""Getting completed tasks for a specific user using APIs"""
import json
import requests
import sys

def get_user_completed_tasks(user_id):
    """Fetch user information and their completed tasks from APIs"""
    try:
        user_api = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
        user_data = user_api.json()

        todos_api = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            params={'userId': user_id}
        )
        todos = todos_api.json()

        completed = [todo for todo in todos if todo['completed']]

        return user_data, completed

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_data, completed_tasks = get_user_completed_tasks(user_id)

    if user_data is None or completed_tasks is None:
        sys.exit(1)

    print(f"Employee {user_data['name']} is done with tasks "
          f"({len(completed_tasks)}/{len(completed_tasks) + len(user_data['todos'])}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    main()

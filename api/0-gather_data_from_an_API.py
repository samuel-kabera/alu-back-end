#!/usr/bin/python3
"""
Script that uses a REST API to get TODO list progress for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Define the URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Get user data
    user_response = requests.get(user_url)
    todo_response = requests.get(todos_url)

    # Check if content type is JSON before calling .json()
    if "application/json" in user_response.headers.get("Content-Type", ""):
        user_data = user_response.json()
    else:
        print("User data is not in JSON format.")
        sys.exit(1)

    if "application/json" in todo_response.headers.get("Content-Type", ""):
        todos_data = todo_response.json()
    else:
        print("TODO data is not in JSON format.")
        sys.exit(1)

    # Extract employee name
    employee_name = user_data.get("name")

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Display progress
    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_tasks}/{total_tasks}):"
    )

    # Print completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

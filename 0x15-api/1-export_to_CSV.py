#!/usr/bin/python3
"""
    This script extracts user data and to-do task data from two web APIs :
    https://jsonplaceholder.typicode.com/users/
    https://jsonplaceholder.typicode.com/todos/,
    processes the data, and prints information about completed tasks
    for a specific user.
"""
import requests # This is easier to use than urllib
import sys # For command line args
import csv
if __name__ == "__main__":
    user_id = sys.argv[1]
# print(type(user_id))
    count = 0 # Total number of tasks
    done = 0 # Completed tasks

    def get_to_do_list(user_id):
        """
        Fetches user data from Users API and to-do tasks data from To-Do Tasks API,
        combines them into a dictionary, and returns it as JSON.

        Args:
        user_id (str): The ID of the user for whom to retrieve data.

        Returns:
        Information about his/her TODO list progress.
        """

    try:
        #  1. Fetch User Data from Users API
        users_api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(users_api_url)
        user_data = user_response.json() # have it readable JSON format.
        username = user_data["name"]
        # 2. Extract todo Data from Todo API
        todo_api_url = f"https://jsonplaceholder.typicode.com/todos/"
        todo_response = requests.get(todo_api_url)
        todo_data = todo_response.json()
        # Create a new list of completed tasks for specific user.
        # Note: tasks_user1 is a list of dictionaries
        tasks_user1 = [task for task in todo_data
                       if task.get('userId') == int(user_id)
                       and task.get('completed') is True]
        # Formatted text
        files = f"{user_id}.csv"
        print(files)
        with open(files, 'w', newline='') as csvfile:
        # no fieldnames
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL) 
            for task in tasks_user1:
                print(task)
                thewriter.writerow({'USER_ID': task['userId'], 'USERNAME': username, 'TASK_COMPLETED_STATUS': task['title'], 'TASK_TITLE': task['completed']})
    except Exception as e:
        #  Handle errors gracefully, e.g. log the error and return an error message
        print(f"Error: {e}")
    # call the above method
    get_to_do_list(user_id)

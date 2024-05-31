#!/usr/bin/python3
"""
    This script extracts user data and to-do task data from two web APIs :
    https://jsonplaceholder.typicode.com/users/
    https://jsonplaceholder.typicode.com/todos/,
    processes the data, and prints information about completed tasks
    for a specific user.
"""
import requests
import sys
# task_user_completed = task_user_completed
# task_user = task_user
if __name__ == "__main__":
    user_id = sys.argv[1]
# print(type(user_id))
    count = 0
    done = 0

    def get_to_do_list(user_id):
        """
        Fetches user data from Users API and to-do tax data from To-Do Tax API,
        combines them into a dictionary, and returns it as JSON.

        Args:
        user_id (str): The ID of the user for whom to retrieve data.

        Returns:
        str: JSON string containing username and to-do tax completion status.
        """

    try:
        #  1. Fetch User Data from Users API
        users_api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(users_api_url)
        user_data = user_response.json()
        username = user_data["name"]
# print(username)
#         print("============================")
        todo_api_url = f"https://jsonplaceholder.typicode.com/todos/"
        todo_response = requests.get(todo_api_url)
        todo_data = todo_response.json()
#         print("done")
        task_user = sum(1 for task in todo_data
                        if task.get('userId') == int(user_id))
# print(task_user)
        task_user_completed = sum(1 for task in todo_data
                                  if task.get('userId') == int(user_id)
                                  and task.get('completed') is True)
#         print(task_user_completed)
        tasks_user1 = [task for task in todo_data
                       if task.get('userId') == int(user_id)
                       and task.get('completed') is True]
#         print(len(tasks_user1))
#         print("*****************")
        text = f"Employee {username} is done with" + \
               f"tasks({task_user_completed}/" + \
               f"{task_user}):"

        print(text)
        for task in tasks_user1:
            print(f"\t {task['title']}")
    except Exception as e:
        #  Handle errors gracefully, e.g.,
        #  log the error and return an error message
        print(f"Error: {e}")
# return json.dumps({"error": str(e)})

    get_to_do_list(user_id)

#!/usr/bin/python3
"""
    This script extracts user data and to-do task data from two web APIs :
    https://jsonplaceholder.typicode.com/users/
    https://jsonplaceholder.typicode.com/todos/,
    and export it as JSON format.
    for a specific user.
"""
import json
from collections import OrderedDict
import requests  # This is easier to use than urllib
import sys  # For command line args
if __name__ == "__main__":

    def get_to_do_list():
        """
        Fetches user data from Users API
        and to-do tasks data from To-Do Tasks API,
        combines them into a dictionary, and returns it as JSON.

        Args:
        user_id (str): The ID of the user for whom to retrieve data.

        Returns:
        A JSON file with all tasks assigned to user,(using username)
        """

    try:
        #  1. Fetch User Data from Users API
        users_api_url = f"https://jsonplaceholder.typicode.com/users/"
        user_response = requests.get(users_api_url)
        user_data = user_response.json()  # have it readable JSON format.
        # This creates a dictionary :
        # which has the key = userId, and value = username
        usernames = {user["id"]: user["username"] for user in user_data}

        # 2. Extract todo Data from Todo API
        todo_api_url = f"https://jsonplaceholder.typicode.com/todos/"
        todo_response = requests.get(todo_api_url)
        todo_data = todo_response.json()
        # Note: tasks_user is a list of dictionaries of all tasks.
        tasks_user = [task for task in todo_data]
        # This creates a dictionary:
        # with user id, as key and an empty list for each entry.
        # To be used on line
        grouped_tasks = {user["id"]: [] for user in user_data}
        # Reorder the keys of the dictionary
        ordered_keys = ["username", "title", "completed"]
        # Print the reordered dictionary
        # Open a JSON file, new or existing.
        files = f"todo_all_employees.json"
        with open(files, 'w', newline='') as jsonfile:
            # Removing "id" key, adding "username" key
            key_to_remove = "id"
            new_key = "username"
            for d in tasks_user:
                # makes user = userId of tasks. [distinct id]
                user = d["userId"]
                # checks if id is a key in usernames
                if user in usernames:
                    # This creates username variable, according to user id.
                    username1 = usernames[user]
                    # Remove the key from the dictionary
                    d.pop(key_to_remove, None)  # None is the default value
                    #                           if the key does not exist
                    # Add the new key-value pair to the dictionary
                    d[new_key] = username1
                    # Makes a list of tuples, with key,value pair in each tuple
                    # Changes the "title" key to "task", and re-order keys
                    reordered_items = [("task" if key == "title" else key,
                                        d[key]) for key in ordered_keys]
                    # Clear old dictionary
                    d.clear()
                # Update the dictionary with the reordered items
                    d.update(reordered_items)
                    # Appends the dictionary
                    # to the corresponding user id value,which is a list.
                    grouped_tasks[user].append(d)
            json_string = json.dump(grouped_tasks, jsonfile)
    except Exception as e:
        #  Handle errors gracefully,
        #  e.g. log the error and return an error message
        print(f"Error: {e}")
    # call the above method
    get_to_do_list()

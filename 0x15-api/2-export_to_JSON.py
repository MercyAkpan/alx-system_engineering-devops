#!/usr/bin/python3
"""
    This script extracts user data and to-do task data from two web APIs :
    https://jsonplaceholder.typicode.com/users/
    https://jsonplaceholder.typicode.com/todos/,
    and sends it, into csv format, same format used in EXCEL spreadsheet.
    for a specific user.
"""
import json
from collections import OrderedDict
import requests  # This is easier to use than urllib
import sys  # For command line args
if __name__ == "__main__":
    user_id = sys.argv[1]

    def get_to_do_list(user_id):
        """
        Fetches user data from Users API
        and to-do tasks data from To-Do Tasks API,
        combines them into a dictionary, and returns it as JSON.

        Args:
        user_id (str): The ID of the user for whom to retrieve data.

        Returns:
        A csv file with all tasks assigned to user,(using username)
        """

    try:
        #  1. Fetch User Data from Users API
        users_api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(users_api_url)
        user_data = user_response.json()  # have it readable JSON format.
        username = user_data["username"]
        # 2. Extract todo Data from Todo API
        todo_api_url = f"https://jsonplaceholder.typicode.com/todos/"
        todo_response = requests.get(todo_api_url)
        todo_data = todo_response.json()
        # Note: tasks_user is a list of dictionaries
        tasks_user = [task for task in todo_data
                       if task.get('userId') == int(user_id)]
#        print(tasks_user[0])
#        print()
        # and task.get('completed') is True] (if I want only completed tasks)
        # File to save it in.
        files = f"{user_id}.json"
        ordered_keys = ["title", "completed", "username"]
        # Print the reordered dictionary
        with open(files, 'w', newline='') as jsonfile:
                # fieldnames (columns for each field, but it won't be printed out as a header)
                    # allocating each fieldname to respective field.(unpacking the dictionary)
            key_to_remove = "id"
            new_key = "username"
            new_value = username
            for d in tasks_user:
#                print(d)
#                print("==============")
            # Remove the key from the dictionary
                d.pop(key_to_remove, None)  # None is the default value if the key does not exist
            # Add the new key-value pair to the dictionary
                d[new_key] = new_value
                reordered_items = [("task" if key == "title" else key, d[key]) for key in ordered_keys]
#                reordered_items = [(key, d[key]) for key in ordered_keys if key == 'title', ]
                d.clear()
            # Update the dictionary with the reordered items
                d.update(reordered_items)
#                print(d) # How am i able to access the last 'd', out of scope.
#                print("****************")
            newdict = {user_id : tasks_user}
#            print(newdict)
            json_string = json.dump(newdict, jsonfile)
    except Exception as e:
        #  Handle errors gracefully,
        #  e.g. log the error and return an error message
        print(f"Error: {e}")
    # call the above method
    get_to_do_list(user_id)

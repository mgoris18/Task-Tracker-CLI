import json
import os

from collections import OrderedDict

def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
        return []
    
    with open('tasks.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def get_next_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1 
#request task from user

task = input("Add Task: ")
tasks = []
tasks.append(task)

while True:
    a = input("Add Tasks? [Y/N]")
    if a == "y":
        print(input("Add Task: "))
        tasks.append
    elif a == "n":
        print(tasks)


#res = [{val: key for key, val in enumerate(
    #OrderedDict.fromkeys(tasks))}
    #[ele] for ele in tasks]

#json_object = json.dumps(tasks)

#with open("tasks.json", "w") as outfile:
    #outfile.write(json_object)

#print("Task added succesfully. ID:" + str(res))
#while True:
   # a = input("Add More Tasks? [Y/N]")
    #if a == "y":
        #print()


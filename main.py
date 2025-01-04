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
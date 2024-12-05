import json

from collections import OrderedDict

#request task from user

task = input("Add Task: ")
tasks = []
tasks.append(task)

while True:
    a = input("Add Tasks? [Y/N]")
    if a == "y":
        print(task)
        tasks.append


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


from pprint import pprint

import prettytable

def getAllTask(db, username):
    tasks = db["task"]
    return tasks.find({"username":username})

def printTasks(db, username):
    tasks = db["task"]
    rows = tasks.find({"username":username})
    table = ""
    if rows.count() > 0:
        table = prettytable.PrettyTable(["taskID", "username", "title", "datetime","description"])
        for row in rows:
            table.add_row([row['taskID'], row['username'], row['title'], row['datetime'], row['description']])

    print(table)
    return

def printAllTasks(db):
    tasks = db["task"]
    rows = tasks.find()
    table = ""
    if rows.count() > 0:
        table = prettytable.PrettyTable(["username", "title", "datetime", "description"])
        for row in rows:
            table.add_row([row['username'], row['title'], row['datetime'], row['description']])

    print(table)
    return

def deleteTask(db, taskToDelete):
    tasks = db["task"]
    tasks.delete_one({"username":taskToDelete[0], "title":taskToDelete[1]})
    return True

def createTask(db, task):
    tasks = db["task"]
    tasks.insert_one({"taskID":task[0], "username":task[1], "title":task[2], "datetime":task[3], "description":task[4]})
    return

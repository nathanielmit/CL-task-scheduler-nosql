import prettytable

def getUserReminders(db, username):
    reminders = db["reminder"]
    return reminders.find({"username":username})

def printReminders(db, username):
    reminders = db["reminder"]
    rows = getUserReminders(db, username)
    table = ""
    if rows.count() > 0:
        table = prettytable.PrettyTable(["_id", "taskID", "username", "name", "datetime"])
        for row in rows:
            table.add_row([row['_id'], row['taskID'], row['username'], row['name'], row['datetime']])

    print(table)
    return

def printAllReminders(db):
    reminders = db["reminder"]
    rows = reminders.find()
    table = ""
    if rows.count() > 0:
        table = prettytable.PrettyTable(["_id", "taskID", "username", "name", "datetime"])
        for row in rows:
            table.add_row([row['_id'], row['taskID'], row['username'], row['name'], row['datetime']])

    print(table)
    return

def getTodaysReminders(db, username):
    reminders = db["reminder"]
    rows = reminders.find({"username":username})
    # yourdatetime.date() == datetime.today().date()
    #rows = db.fetchall()
    if rows.count() > 0:
        print("Your reminders for today:")
    for row in rows:
        print(row[2] + " at " + row[3])
    return

def createReminder(db, reminder):
    reminders = db["reminder"]
    reminders.insert_one({"reminderID":reminder[0], "name":reminder[1], "datetime":reminder[2]})
    return

def deleteReminder(db, reminderToDelete):
    reminders = db["reminder"]
    reminders.delete_one({"username":reminderToDelete[0], "name":reminderToDelete[1]})
    return

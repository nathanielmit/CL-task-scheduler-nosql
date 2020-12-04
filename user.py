from reminder import *
import prettytable

def printAllUsers(db):
    users = db["user"]
    rows = users.find()
    print("values in return value of users.find()")
    for i in rows:
        print(i)
    table = ""
    if len(rows) > 0:
        table = prettytable.PrettyTable(["username", "name", "password"])
        for row in rows:
            table.add_row(row)

    print(table)
    return

def getUserName(db, username):
    users = db["user"]
    return users.find_one({"username":username})['name']

def loginUser(db, user):
    users = db["user"]
    rows = users.find_one({"username":user[0], "password":user[1]})
    print("rows\n", rows)
    if len(rows) > 0:
        return True
    else:
        return False

def registerUser(db, user):
    users = db["user"]
    return users.insert_one({"username":user[0], "name":user[1], "password":user[2]})

def login(db):
    authenticated = False
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Read username and password from database
    # Try to authenticate, if successful set authenticated to True
    user = (username, password)
    logged_in = loginUser(db, user)

    if logged_in:
        authenticated = True
        print("You successfully logged in!")
        name = getUserName(db, username)
        print("Thanks for logging in, " + name + "!")
        getTodaysReminders(db, username)
    else:
        print("Login failed!")
    return authenticated, username

def register(db):
    authenticated = False
    username = input("Enter username: ")
    name = input("Enter name: ")
    password = input("Enter password: ")
    new_user = (username, name, password)
    ret = registerUser(db, new_user)
    print("return value of register insert: ", ret.inserted_id)
    authenticated = True
    print("You've successfully registered!")
    return authenticated, username

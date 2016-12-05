__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

from tinydb import TinyDB, Query
from colorama import init, Fore, Back, Style

piddb = TinyDB('piddb.json')
items = Query()
init()

def menu():
    print("Please select from the following options:")
    for option in options():
        print(option['command'], "-", option['option'])

def showDB():
    print("\n\n")
    for item in piddb.all():
        print("------")
        for key in item.keys():
            print(key + ": ", item[key])
    print("-----\n\n")
    return

def addServerModel():
    print("\n\nLook up needed vaules by here: \nhttp://ucshcltool.cloudapps.cisco.com/public/rest/ \n"
          "http://ucshcltool.cloudapps.cisco.com/public/rest/\n")
    server_model = input("Server Model: ")
    id = input("ID: ")
    objtype = 'servermodel'
    server_type = "B"
    pid = input("pid: ")

    server = {'SERVER_MODEL': server_model,
              'ID': id,
              'objtype': objtype,
              'server_type': server_type,
              'pid': pid
              }
    piddb.insert(server)
    print(Fore.GREEN + "\nSuccessfully inserted Server {} into DB".format(server))
    print(Style.RESET_ALL)

    return

def addAdapter():
    print("\n\nLook up needed vaules by here: \nhttp://ucshcltool.cloudapps.cisco.com/public/rest/ \n"
          "http://ucshcltool.cloudapps.cisco.com/public/rest/\n")


    adapter = input("Adapter Model: ")
    objtype = 'adapter'
    pid = input("pid: ")

    server = {'adapter': adapter,
              'objtype': objtype,
              'pid': pid
              }
    piddb.insert(server)
    print(Fore.GREEN + "\nSuccessfully inserted Adapter {} into DB".format(server))
    print(Style.RESET_ALL)

    return

def delObject():
    print("\nPrinting all Objects\n")
    showDB()
    #query_key_ = input("Enter in Key to match to delete record(s): ")
    query_value = input("Enter PID to match: ")
    query = piddb.search(items.pid == query_value)

    print("You matched the following")
    for item in query:
        print("------")
        for key in item.keys():
            print(key + ": ", item[key])
    print("-----\n\n")

    confirm = input("Would you like to delete record(s) (y/n): ")

    if confirm == 'n':
        print(Fore.GREEN + "Item not deleted")
        print(Style.RESET_ALL)
    elif confirm == 'y':
        print(Fore.RED + "Deleted PID(s) {}".format(query_value))
        print(Style.RESET_ALL)
        piddb.remove(items.pid == query_value)
        print("Items Deleted")

    return


def options():
    options = [
        {'option':'Show Database', 'command':'1'},
        {'option':'Add Server Type', 'command':'2'},
        {'option':'Add Adapter', 'command':'3'},
        {'option':'Delete Record', 'command':'99'},
        {'option':'Quit', 'command':'quit'}
    ]
    return options

while True:
    menu()
    user_choice = input("Choose and option: ")
    if user_choice == '1':
        showDB()
    elif user_choice =='2':
        addServerModel()
    elif user_choice == '3':
        addAdapter()
    elif user_choice =='99':
        delObject()
    elif user_choice =='quit':
        quit()
    else:
        print("Not a valid choice. Try again")
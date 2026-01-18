import email
import sys

import Classes as cls
base = cls.base

isEdited = False
#-Functions section{

#-Testing_Function
def testing(email) -> bool:
    for key, value in base.items():
        if value['email'] == email:
            return False
        else:
            return True
    return None


#-Testing_Function

#-Remove-Function
def remove_users():
    isEdited = True
    for key, value in base.items():
        if value['email'] == email:
            del base[key]
#-Remove-Function




def check():
    if isEdited:
        print(""" You made a change and didn't save it. Are you sure you want to exit?
1. Yes
2. No""")
        command = input(">>> ")
        if command == '1' or command == 'Yes':
            print(" You exit successfully.")
            sys.exit()
        elif command == '2' or command == 'No':
            menu()
        else:
            print("Please enter a valid option.")
            check()


def menu():
    print("""
1. Create user
2. Remove user
3. Edit user
4. Save all
0. Exit""")
    command = input(">>> ")
    if command == '1':
        pass
    elif command == '2':
        remove_users()
        menu()
    elif command == '3':
        pass
    elif command == '4':
        pass
    elif command == '0':
        check()
    else:
        print("Invalid option. Try again.")
        menu()



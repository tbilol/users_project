import sys
import Classes as cls
import json
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
#-Testing_Function

#-Remove-Function

def remove_users():
    email = input("Enter your email address: ")
    for key, value in base.items():
        if testing(email):
            del base[key]
            isEdited = True
            print(f"{value['name']} has been removed successfully.")
        else:
            print(" Email not found")

#-Remove-Function

#-ShowUsers_Function
def show_users(email):
    def show_user():
        users = ''
        for key, value in base.items():
            users += f"""                                            +------------------------------------------------------------|
                                                |{key}:                                            |           
                                                |    +-------------------------------------------------------|
                                                |    |user_name     | {value['name']}             
                                                |    |user_email    | {value['email']}           
                                                |    |user_password | {value['password']}   
                                                |    +-------------------------------------------------------|
                                                |                                                            |
                                                +------------------------------------------------------------|\n"""
        return users
#-ShowUsers_Function

#-Save_Function
def save():
    with open('./front/data.json', 'w') as outfile:
        outfile.write(json.dumps([base], indent=4))
#-Save_Function

#-check function
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

#-menu function
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




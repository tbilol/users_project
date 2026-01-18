import sys
import Classes as cls
import json
base = cls.base
isEdited = False

def testing(email):
    val = ""
    isHas = False
    for key, value in base.items():
        if value['email'] == email:
            val = key
            isHas = True
            break
    return (isHas, val)

def create_user():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    answer = testing(email)[0]
    if answer:
        print(" This email address already exists.")
    else:
        global isEdited
        isEdited = True
        password = input("Enter your password: ")
        new_user = cls.User(name=name, email=email, password=password)
        new_user.add_db()
        print("Your created seccess.")

def remove_users():
    email = input("Enter your email address: ").strip()
    answer, key = testing(email)
    if answer:
        global isEdited
        isEdited = True
        del base[key]
        print(f" User has been removed successfully.")
    else:
        print(" Email not found")

def edit_users():
    email = input("Enter your email address: ").strip()
    answer, key = testing(email)
    if answer:
        global isEdited
        isEdited = True
        new_name = input("Enter your new - name: ").strip()
        new_email = input("Enter your new - email address: ").strip()
        new_password = input("Enter your new - password: ").strip()
        base[key] = {'name': new_name,
                     'email': new_email,
                     'password': new_password}
        print(" User has been edited successfully.")
    else:
        print(" Email not found")

def show_users():
    users = ''
    for key, value in base.items():
        users += f"""                                                +------------------------------------------------------------|
                                                |{key}:                                            |           
                                                |    +-------------------------------------------------------|
                                                |    |user_name     | {value['name']}             
                                                |    |user_email    | {value['email']}           
                                                |    |user_password | {value['password']}   
                                                |    +-------------------------------------------------------|
                                                |                                                            |
                                                +------------------------------------------------------------|\n"""
    return users

def save():
    global isEdited
    isEdited = False
    with open('./front/data.json', 'w') as outfile:
        outfile.write(json.dumps([base], indent=4))
        print("Data saved successfully.")

def check():
    if isEdited == True:
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
4. Show users
5. Save all
0. Exit""")
    command = input(">>> ")
    if command == '1':
        create_user()
        menu()
    elif command == '2':
        remove_users()
        menu()
    elif command == '3':
        pass
    elif command == '4':
        print(show_users())
        menu()
    elif command ==  '5':
        save()
        menu()
    elif command == '0':
        check()
    else:
        print("Invalid option. Try again.")
        menu()

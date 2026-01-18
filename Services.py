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
def remove_users(email):
    email = input("Enter your email address: ")
    for key, value in base.items():
        if testing(email):
            del base[key]
            isEdited = False
            return f"{value['name']} has been removed successfully."


#-Remove-Function


#-ShowUsers_Function
def show_users():
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
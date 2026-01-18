import Classes as cls
base = cls.base

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
def remove_users(email):
    for key, value in base.items():
        if value['email'] == email:
            del base[key]
#-Remove-Function


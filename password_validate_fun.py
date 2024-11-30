#functions of password validate
import re
def password_validate(password):
    passwd_regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$])(.{6,12})$"
    if(re.search(passwd_regex,password)):
        return password+" is valid"
    else:
        return password+" is not valid"

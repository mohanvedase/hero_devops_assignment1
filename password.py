#Create a Python script to check the password strength. 

'''
password should contain atleast 1 uppercase
password should contain atleast 1 lowercase
password should contain atleast 1 numeric number
password should contain atleast 1 special character
'''
#re specifies a set of strings that matches a particular expression

import re       

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check uppercase letters
    if not re.search(r'[A-Z]', password):    #re.search() searches for that particular pattern within the string.
        return "Password should contain at least one uppercase letter."

    # Check lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."

    # Check digits
    if not re.search(r'\d', password): #(1,2,....0)
        return "Password should contain at least one digit."

    # Check special characters
    if not re.search(r'[\W_]', password):#(!@#$%^&*_)
        return "Password should contain at least one special character."

    return "Password is strong."

    # Test the function
password = input("Enter a password: ")
result = check_password_strength(password)
print(result) 
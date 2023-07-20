### "hero_devops_assignment1"

##Create a Python script to check the password strength. 
In this code we check the strength of password by using different conditions.
#Conditions
password should contain atleast 1 uppercase
password should contain atleast 1 lowercase
password should contain atleast 1 numeric number
password should contain atleast 1 special character

For this code we import *re module*
This module allows you quickly to check a given string matches the pattern.
In re module there are two functions re.searach() , re.match(). 
These are very efficient and fast searching in string.
In this we re.search(), it search the expression and return the first occurrence.
#for example 
*if not re.search(r'[A-Z]', password):*
    + not operator is used to negate the result of the re.search() function.
    + If condition give True -not- operator give false and goes on to final condition.
    + If all conditions are false then  it returns the Return statement. 
    + r'[A-Z]' matches any single character in password that is an uppercase letter.
    + The raw string r'[A-Z]' is used in the code to prevent the backslash character from being interpreted as  escape character.

It is similar to all conditions . If password satisfies all the conditions the result will be "password is strong". 



##Write a Python program to monitor the health of the CPU.
In this program we check the health of the computer by checking the threshold limit of CPU 

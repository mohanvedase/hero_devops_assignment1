### "hero_devops_assignment1"
##Create a Python script to check the password strength. 
In this code we check the strength of password by using different conditions.
#Condition:- password should contain atleast 1 (uppercase,lowercase,numeric number,special character)
For this code we import *re module* .In this we re.search(), it search the expression and return the first occurrence.
for example :- *if not re.search(r'[A-Z]', password):*
    + not operator is used to negate the result of the re.search() function.
    + The raw string r'[A-Z]' is used in the code to prevent the backslash character from being interpreted as  escape character.
It is similar to all conditions . If password satisfies all the conditions the result will be "password is strong". 
## Write a Python program to monitor the health of the CPU.
In this program we check the health of the computer by checking the threshold limit of CPU . First we need to install psutils by using the command *pip install psutil*
psutil is a Python library that provides access to system-related information, such as CPU usage, memory usage, disk usage, and network usage. Psutil has a wide range of functions that you can use to get information about your system.
This code will print the CPU usage of the current process as a percentage.
We also import *time* to check the CPU usage for every time interval.
If an exception occurs, the try block will be skipped, and the except block will be executed.
*cpu_usage > threshold* We gave threshold value limit as 80 , as per code if limit raises above 80.It throws the alert message 
*print(f"Alert: CPU usage is {cpu_usage}%!")*
F-strings are created by prefixing a string with the letter "f" or "F".The string itself can be formatted in much the same way that you would with str.format(). 
*time.sleep(1)* code Wait for a second before checking again.for every one second alert msg appeared in a infinite loop, to stop this we use exception command.
## Write a program for performing regular backups of important files 
In this code , we want to copy a directory as a backup into desired location directory.
if the desired directory has a file name with same name then add Timestamp to name of the file in the directory.for this we ned to import differnt libraries like (*os , datetime , shutil*).
os library is used to access the go to desired locations in the system.datetime library is used to add timestamp to the backcopy. 
shutil library is used to copy the file.
*source = os.path.join(source_folder, file_name)*os.path.join() function is a convenient way to -combine- path components (source_folder, filename).
*shutil.copy(source, destination)*
destination = os.path.join(destination_folder, file_name)
this code is used to copy the file in source directory to desired destination directory
*new_destination = os.path.join(destination_folder, timestamp + " - " + file_name)*
if the destination directory has a same name file then add the timestamp to the file. 
*if __name__ == "__main__":*this statement in Python is used to execute code only when the file is being run as a script, and not when the file is being imported as a module.
#Wap that uses the getpass modlule to prompt the user for a password without echoing.What they type to console.
import getpass
password = getpass.getpass(prompt='Enter your password: ')
if password == "oxford":
    print("Welcome to the world of python programming")
else:
    print("Incorrect password. Access denied.")
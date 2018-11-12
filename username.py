#Python Code to print the username of the currently logged in user 
import os

username=os.environ.get('USERNAME')
print("username=" + str(username))
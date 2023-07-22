import keyboard
import glob
import os
from DictTypes import FileTypes
import tkinter as t

#username declaration
username: str

#checks if username.txt is not empty
def usernameCheck():  
    
    #opens "username" file
    usernamefile = open('username.txt', 'r+')
    
    #username check
    if usernamefile.read(1) == '':
        username = input('[SYSTEM]: Please input your username: ')
        usernamefile.write(' ' + username)
    else: username = usernamefile.read()
    
    #allows assignment
    return username

#usermane assignment
username = usernameCheck()

#sorts files
def fileSort(Extension, FolderName):
    
    #extention detection
    Files = glob.glob(f"c:/Users/{username}/Downloads/*.{Extension}")
    
    #sorting loop
    for i in Files:
        NewName = i.split('\\')[-1]
        NewPath = (f"c:/Users/{username}/Downloads/{FolderName}/{NewName}")
        os.replace(i, NewPath)

#checks if neccesary folder exist
def folderCheck():
    for FolderName in FileTypes.values():
        if not os.path.exists(f"c:/Users/{username}/Downloads/{FolderName}"):
            os.makedirs(f"c:/Users/{username}/Downloads/{FolderName}")
        else: continue
 
#calls fileSort for every extention type 
def sortCall():
    
    #calls fileSort until completion
    if len(username) > 0:
        for Extension, FolderName in FileTypes.items():
            fileSort(Extension, FolderName)
    
#Calls other functions    
def Main():
    
    #error handling
    try:
        folderCheck()
        sortCall()
    except PermissionError:
        print("A Permission Error has occurred! Try changing your username in the username.txt file.")
    
#makes sure that you are runnig this directly
if __name__ == '__main__':
    while True:
        Main()
    
    

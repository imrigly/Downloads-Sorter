import glob
import os
from SorterGUI import FileTypes

#username assignment
username: str = os.getlogin()

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
def silentMain():
    
    #error handling
    try:
        folderCheck()
        sortCall()
    except PermissionError:
        print("A Permission Error has occurred! Try changing your username in the username.txt file.")
    
#makes sure that you are runnig this directly
if __name__ == '__main__':
    while True:
        silentMain()

    
    

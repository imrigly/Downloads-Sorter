import glob
import os
import pickle

with open('DictTypes.pkl', 'rb') as f:
    FileTypes = pickle.load(f)

#username assingment
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
        print(f"[ACTION]: Moved {NewName} to {FolderName}")
    print(f"[SORT]: {Extension} sort completed!")

#checks if neccesary folder exist
def folderCheck():
    for FolderName in FileTypes.values():
        if not os.path.exists(f"c:/Users/{username}/Downloads/{FolderName}"):
            os.makedirs(f"c:/Users/{username}/Downloads/{FolderName}")
            print(f"[FOLDERS]: {FolderName} folder created successfully!")
        else: continue
 
#calls fileSort for every extention type 
def sortCall():
    
    #calls fileSort until completion
    if len(username) > 0:
        for Extension, FolderName in FileTypes.items():
            fileSort(Extension, FolderName)
        print("[COMPLETE]: All done!")
    
#Calls other functions    
def Main():
    
    #error handling
    try:
        folderCheck()
        sortCall()
    except PermissionError:
        print("A Permission Error has occurred!")
    
#makes sure that you are runnig this directly
if __name__ == '__main__':
    Main()
    
    

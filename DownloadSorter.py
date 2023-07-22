import keyboard
import glob
import shutil
from DictTypes import FileTypes

#opens "username" file
usernamefile = open('username.txt', 'r+')
 
def sortfiles(Extension, FolderName):
    
    #extention detection
    Files = glob.glob(f"c:/Users/{username}/Downloads/*.{Extension}")
    
    #sorting loop
    for i in Files:
        NewName = i.split('\\')[-1]
        NewPath = (f"c:/Users/{username}/Downloads/{FolderName}/{NewName}")
        shutil.move(i, NewPath)
        print(f"Moved {NewName} to {FolderName}")
    print(f"{Extension} sort completed!")

    
#good practice
if __name__ == '__main__':
    
    #username check
    if usernamefile.read(1) == '':
        username = input('Please input your username: ')
        usernamefile.write(' ' + username)
    else: username = usernamefile.read()

    #filesort
    if len(username) > 0:
        for Extension, FolderName in FileTypes.items():
            sortfiles(Extension, FolderName)
        print("All done!")

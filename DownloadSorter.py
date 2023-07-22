import keyboard
import glob
import shutil

usernamefile = open('username.txt', 'r+')
 
def sortfiles(Extension, FolderName):
    Files = glob.glob('c:/Users/imrig/Downloads/*.exe')
    for i in Files:
        NewName = i.split('\\')[-1]
        NewPath = ("c:/Users/imrig/Downloads/" + username + "/" + NewName)
        print(NewName)
        print(i)
        print(NewPath)
        shutil.move(i, NewPath)
    
if __name__ == '__main__':
    if usernamefile.read(1) == '':
        username = input('Please input your username: ')
        usernamefile.write(username)
    else: username = usernamefile.read()
    

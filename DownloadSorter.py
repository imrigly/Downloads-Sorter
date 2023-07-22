import keyboard
import glob
import shutil

FileTypes: dict =  {
    "exe":"Executables",
    "msi":"Executables",
    "torrent":"Torrents",
    "png":"Images",
    "svg":"Images",
    "jpg":"Images",
    "jpeg":"Images",
    "gif":"Images",
    "zip":"Compressed Files",
    "7z":"Compressed Files",
    "rar":"Compressed Files",
    "wav":"Audio",
    "mp3":"Audio",
    "flac":"Audio",
    "m4a":"Audio",
    "mkv":"Videos",
    "avi":"Videos",
    "mp4":"Videos",
    "webm":"Videos",
    "stl":"3D"
}

#opens "username" file
usernamefile = open('username.txt', 'r+')
 
def sortfiles(Extension, FolderName):
    
    #extention detection
    Files = glob.glob('c:/Users/' + username + '/Downloads/*.' + Extension)
    
    #sorting loop
    for i in Files:
        NewName = i.split('\\')[-1]
        NewPath = ("c:/Users/" + username + "/Downloads/" + FolderName + "/" + NewName)
        shutil.move(i, NewPath)
    
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
        

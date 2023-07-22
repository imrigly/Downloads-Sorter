from CmdSorter import Main
from CmdSorterSilent import silentMain
import tkinter as tk
from random import randint
from DictTypes import FileTypes

title: str

def pickTitle():
    roll = randint(1, 10)
    if roll == 10:
        title = "ImRigly's Downloads Sorter: Also try Terraria!"
    elif roll == 9:
        title = "ImRigly's Downloads Sorter: Also try Cruelty Squad!"
    else: title = "ImRigly's Downloads Sorter"
    return title

gui = tk.Tk()

if __name__ == "__main__":
    
    
    gui.title(pickTitle())
    
    gui.geometry('640x480')
    
    icon = tk.PhotoImage(file="res/sortericon.png")
    gui.iconphoto(True, icon)

    gui.config(background="#6281a2")
    
    maintext = tk.Label(gui, text="Welcome to my sorter's GUI!", font=('', 20, 'bold'), fg='#232323', bg='#6281a2').pack()

    sortbutton = tk.Button(gui, text="SORT", font=('', 30, 'bold'), fg='#232323', bg='#c12c3f', activebackground='#f04e65', bd=0, command=Main).pack()
    
    typetext = tk.Label(gui, text='Enter a new Filetype:', bg='#6281a2').pack()
    
    typeinput = tk.Entry(gui)
    typeinput.pack()
    
    foldertext = tk.Label(gui, text='Enter a Foldername for this type:', bg='#6281a2').pack()
    
    folderinput = tk.Entry(gui)
    folderinput.pack()
    

    
    def SendToDict():
        type = typeinput.get()
        folder = folderinput.get()
        FileTypes[type]=folder
        print(FileTypes)
        return FileTypes

    sendtodict = tk.Button(gui, text='Send (DOES NOT WORK!!!)', fg='#232323', bg='#c12c3f', activebackground='#f04e65', bd=0, command=SendToDict).pack()
    gui.mainloop()





    










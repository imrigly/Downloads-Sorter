from CmdSorter import Main
#from CmdSorterSilent import silentMain
import tkinter as tk
from random import randint
import pickle

with open('DictTypes.pkl', 'rb') as f:
    FileTypes = pickle.load(f)

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
dictwindow = tk.Tk()

if __name__ == "__main__":
    
    
    gui.title(pickTitle())
    dictwindow.title('DictTypes dictionary')
    
    gui.geometry('640x480')
    dictwindow.geometry('640x480')
    
    icon = tk.PhotoImage(file="res/sortericon.png")

    gui.iconphoto(True, icon)

    gui.config(background="#6281a2")
    
    dicttext = tk.Label(dictwindow, text=f'DictTypes: {FileTypes}', wraplength=300, justify='center').pack()
    
    maintext = tk.Label(gui, text="Welcome to my sorter's GUI! \n (garbage user interface)", font=('', 20, 'bold'), fg='#232323', bg='#6281a2').pack()

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
        with open('DictTypes.pkl', 'wb') as f:
            pickle.dump(FileTypes, f)
        return FileTypes

    sendtodict = tk.Button(gui, text='Send (RESTART AFTER SENDING!!!)', fg='#232323', bg='#c12c3f', activebackground='#f04e65', bd=0, command=SendToDict).pack()
    
    deltype = tk.Label(gui, text='Enter a Filetype to remove from the DictTypes dictionary :', bg='#6281a2').pack()
    
    delinput = tk.Entry(gui)
    delinput.pack()
    
    def DeleteType():
        deletetype = delinput.get()
        del FileTypes[deletetype]
        with open('DictTypes.pkl', 'wb') as f:
            pickle.dump(FileTypes, f)
    
    deletebutton = tk.Button(gui, text='Remove', fg='#232323', bg='#c12c3f', activebackground='#f04e65', bd=0, command=DeleteType).pack()
    
    gui.mainloop()





    










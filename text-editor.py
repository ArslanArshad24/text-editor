from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("900x600")
root.config(padx=20,pady=30)
root.title('Text Editor By Arslan')

def open_file():
    file = filedialog.askopenfile(mode='r',filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        file_text.insert(INSERT,content)
def clear():
    file_text.delete(1.0,END)

def save_file():
    save_file =filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if save_file is None:
        return
    text = file_text.get(1.0,END)
    save_file.write(text)
    save_file.close()

open_button = Button(root,text='Open File',command = open_file,bg='yellow')
open_button.grid(row=0,column=0,padx=10)

clear_button = Button(root,text='Clear',command = clear , bg='orange')
clear_button.grid(row=0,column=2,padx=10)

save_button = Button(root,text='Save File',command = save_file, bg = 'green' ,fg ='white')
save_button.grid(row=0,column=3,padx=10)

file_text = Text(root,height=30,width=100,wrap=WORD)
file_text.place(x=10,y=50)

root.mainloop()
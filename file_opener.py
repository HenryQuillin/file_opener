from tkinter import * 
from tkinter import filedialog
import tkinter.scrolledtext as st 

root = Tk()
root.title('A Random Gui')
root.geometry('200x200')
root.configure(background='grey38')

def close_file():
    print('Closing File')


def open_file():
    print('open file')
    open_file_name = filedialog.askopenfilename(title='Please select a file to open...', filetypes=(("txt files", "w.txt"), ('all files', 'w.w')))
    print('Opening file at'+open_file_name)

def submenu():
    menu = Menu(root)
    submenu = Menu(menu)
    root.config(menu=menu)
    menu.add_cascade(label="File", menu=submenu)
    submenu.add_command(label="Open", command=open_file)
    submenu.add_command(label='Close', command=close_file)
#    submenu.add_seperator()

def show_text_box():
    print('show_text_box')
    text_box = st.ScrolledText(root, bg='white', font='TkFixedFont')
    text_box.insert(INSERT,'inserting')
    text_box.place(x=100,y=100,width=100,height=100)


def read_file():
    print('read_file')


def write_file():
    print('write_file')


# simple buttons for UI 
Button(root, text='Show text box', command=show_text_box, bg='grey',highlightbackground='black',foreground='dark blue').grid(row=0,column=0)
Button(root, text='Get Text', command=read_file, bg='grey',highlightbackground='black',foreground='dark blue').grid(row=0,column=1)
Button(root, text='Write Text', command=write_file, bg='grey',highlightbackground='black',foreground='dark blue').grid(row=0,column=2)


submenu()
root.mainloop()
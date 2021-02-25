from tkinter import * 
from tkinter import filedialog
import tkinter.scrolledtext as st 

root = Tk()
root.title('A Random Gui')
root.geometry('300x200')
root.configure(background='grey38')
text_box = ''

def close_file():
    print('Closing File')
    close_file_name = filedialog.asksaveasfilename(title='Please select a file to close...', filetypes=(("txt files", "*txt"), ('all files', '*.*')))
    print('Saving to' + close_file_name)
    write_file(close_file_name)



def open_file():
    print('open file')
    open_file_name = filedialog.askopenfilename(title='Please select a file to open...', filetypes=(("txt files", "*txt"), ('all files', '*.*')))
    print('Opening file at'+open_file_name)
    read_file(open_file_name)

def submenu():
    menu = Menu(root)
    submenu = Menu(menu)
    root.config(menu=menu)
    menu.add_cascade(label="File", menu=submenu)
    submenu.add_command(label="Open", command=open_file)
    submenu.add_command(label='Close', command=close_file)
#   

def show_text_box(text):
    global text_box 
    print('show_text_box')
    text_box = st.ScrolledText(root, bg='white', font='TkFixedFont')
    text_box.insert(INSERT, text)
    text_box.place(x=100,y=100,width=100,height=100)

def read_file(file_path):
    print('read_file')
    file = open(file_path)
    text = ''
    for line in file:
        text = text + line 
    show_text_box(text)


def write_file(close_file_path):
    get_text_box = text_box.get('1.0', 'end-1c')
    print('write_file')
    print(close_file_path)
    new_file = open(close_file_path, 'w')
    new_file.writelines(get_text_box)




submenu()
root.mainloop()
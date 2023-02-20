import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import atexit

root = tk.Tk()
root.title("Note.py")
root.withdraw()
root.state("zoomed")
root.configure(bg="#121212")

text_scroll = Scrollbar(root)
text_scroll.pack(side="right", fill="y")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

text = Text(root, font=("Calibri", 18),width=screen_width, height=screen_height, selectbackground="blue", selectforeground="white", undo=True, yscrollcommand=text_scroll.set, bg="#121212", fg="white", insertbackground="white")
text.pack(side="left")


def create_file():
    directory = tk.filedialog.askdirectory()
    full_directory = f"{directory}/New Text Document.txt"
    file_new = open(full_directory, mode="w")
    file_new.write("")
def open_file():
    global file
    file = askopenfilename(parent=root, filetypes =[('Text Files', '*.txt'), ('Python Files', '*.py'), ('HTML Files', '*.html'), ('C++ Files', '*.cpp') ,("All Files", "*.*")])
    if file is not None:
        text_file = open(file, "r")
        content = text_file.read()
        print(content)
    root.title(f"{file} - Note.py")
    text.delete("1.0", "end")
    text.insert(INSERT, content)
    text.pack()
def save_file():
        text_file = open(file, "w")
        text_get = text.get("1.0", END)
        text_file.write(text_get)
        text_file.close()
        showinfo("Operation Success", "File Saved.")

def save_as():
    directory = tk.filedialog.asksaveasfilename()
    with open(directory, "w") as file_save_as:
        text_get = text.get("1.0", "end")
        file_save_as.write(text_get)
        file_save_as.close()
        showinfo("Operation Succes", "File Saved.")

def ask_save():
    save = tk.messagebox.askyesno("Save?", "Do you want to save?")
    if save == True:
        save_file()
        root.destroy()
    elif save == False:
        root.destroy()

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(
    label="New File",
    command=create_file
)
file_menu.add_command(
    label="Open File",
    command=open_file,
)
file_menu.add_command(
    label="Save File",
    command=save_file
)
file_menu.add_command(
    label="Save File As",
    command=save_as
)
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=ask_save,
)
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

def AboutMenu():
    AboutWindow = Toplevel(root)
    AboutWindow.title("Help")
    AboutWindow.geometry("400x400")
    AboutWindow.resizable(0,0)
    Label(AboutWindow, text="By clicking here, you probably are asking yourself:", font=5, wraplength=350).pack()
    Label(AboutWindow, text="How do I use this piece of software?", font=2.5).pack()
    Label(AboutWindow, text="").pack()
    Label(AboutWindow, text="You have to", font=1.5).pack()
    Label(AboutWindow, text="T Y P E", font=50).pack()


help_menu = Menu(menubar, tearoff=False)
help_menu.add_command(
    label="Help",
    command=AboutMenu
)
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

open_file()

atexit.register(ask_save)

root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
root.title("MALAMI VENTURES")
content = ttk.Frame(root)
button = ttk.Button(root, text='Hello World', )
button.grid()
label = ttk.Label(root, text='Full name:')
label.grid()
root.mainloop()
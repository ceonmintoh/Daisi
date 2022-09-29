from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry("600x500")
root.title("MALAMI VENTURES")
content = ttk.Frame(root)
button = ttk.Button(root, text='Hello World', )
button.grid()
label = ttk.Label(root, text='Full name:')
little = ttk.Label(root, text="Little")
bigger = ttk.Label(root, text='Much bigger label')
little.grid(column=3,row=2)
bigger.grid(column=3,row=2)
root.after(2000, lambda: little.lift())
label.grid()

p = ttk.Panedwindow(root, orient=VERTICAL)
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)
p.add(f1)
p.add(f2)
p.grid()

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
root.mainloop()
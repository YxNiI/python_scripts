from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(heigth=13, width=13)
frame = ttk.Frame(root, padding=10)

frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1)

# Use ".configure()"-method and print(), to list configuration-options of a tkinter-object.
# Use "dir()"-function, to get the methods of a tkinter-object.

print(root.configure())

root.mainloop()

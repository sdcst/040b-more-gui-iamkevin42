#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

"""
The 3rd method of placing widgets is to treat the window as a map with x and y
coordinates, and then place the widget based on the location from the top left
corner of the window.  Distances are measured in pixels

"""
window = tk.Tk()
window.title("Hi!")
window.geometry("200x400")



dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!", borderwidth=4, relief=SUNKEN)

button1 = tk.Button(window,text="A button\nis clickable")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#ee0000")
combo = ttk.Combobox(window,values=["1","2","3"])


# we can use the tkiner.place() command to fix the position of a widget.
# further options available can be found at https://www.tutorialspoint.com/python/tk_place.htm
label1.place(x=50,y=60)
label2.place(x=0,y=0)
button1.place(x=100,y=50)


#Note, widgets can overlap. In that case, the order is determined by when
#widget object was CREATED,not when it was placed.
#Objects created earlier are underneath objects that are created later.

window.mainloop()
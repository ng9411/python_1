
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox
window = Tk()

lb1 = Label(window, text="First_Name:",
            fg='black', font=("Helvetica", 10))
lb1.place(x=10, y=50)

txtfld = Entry(window, text="*", bd=5)
txtfld.place(x=100, y=50)


lb2 = Label(window, text="Last_Name:",
            fg='black', font=("Helvetica", 10))
lb2.place(x=10, y=80)

txtfld = Entry(window, text="*", bd=5)
txtfld.place(x=100, y=80)

lb3 = Label(window, text="Gender:",
            fg='black', font=("Helvetica", 10))
lb3.place(x=10, y=110)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=110)
r2.place(x=180, y=110)


lb4 = Label(window, text="Language:",
            fg='black', font=("Helvetica", 10))
lb4.place(x=10, y=150)


v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
C1 = Checkbutton(window, text="Telungu", variable=v1)
C2 = Checkbutton(window, text="English", variable=v2)
C3 = Checkbutton(window, text="Hindi", variable=v3)
C1.place(x=110, y=160)
C2.place(x=200, y=160)
C3.place(x=290, y=160)

lb5 = Label(window, text="Email:",
            fg='black', font=("Helvetica", 10))
lb5.place(x=10, y=200)

txtfld = Entry(window, text="*", bd=5)
txtfld.place(x=100, y=200)

lb6 = Label(window, text="Address:",
            fg='black', font=("Helvetica", 10))
lb6.place(x=10, y=270)
txtfld = Entry(window,
               text="*", bd=6)
txtfld.place(x=100, y=270)

lb7 = Label(window, text="State:",
            fg='black', font=("Helvetica", 10))
lb7.place(x=10, y=350)
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=100, y=350)

lb8 = Label(window, text="Zip:",
            fg='black', font=("Helvetica", 10))
lb8.place(x=10, y=450)
txtfld = Entry(window, text="*", bd=6)
txtfld.place(x=100, y=450)


lb9 = Label(window, text="Credit Card Type:",
            fg='black', font=("Helvetica", 10))
lb9.place(x=10, y=500)
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=200, y=500)


def __init__(self):
    self._window = tkinter.Tk()
    self._window.title("Converter")
    self._window["bg"] = "#20A3FF"  # background colour
    self._window.geometry("820x240")  # setting window size


window.title('Hello Python')
window.geometry("1305x652")
window.mainloop()

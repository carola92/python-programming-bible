#!/usr/bin/python3

import tkinter
from tkinter import *

window = Tk()

mButton = Menubutton(window, text = "Click Me!")
mButton.grid()
mButton.menu = Menu(mButton)
mButton["menu"] = mButton.menu

mButton.menu.add_checkbutton(label = "Item 1")
mButton.menu.add_checkbutton(label = "Item 2")
mButton.menu.add_checkbutton(label = "Item 3")
mButton.menu.add_checkbutton(label = "Item 4")
mButton.menu.add_checkbutton(label = "Item 5")
mButton.menu.add_checkbutton(label = "Item 6")
mButton.menu.add_checkbutton(label = "Item 7")

mButton.pack()

window.mainloop()

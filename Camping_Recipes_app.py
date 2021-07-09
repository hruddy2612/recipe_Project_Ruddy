#!/usr/bin/env python
# coding: utf-8


from tkinter import *

import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import tkinter.font as tkFont




#main window size and title
main_window = Tk()
main_window.geometry('800x500')
main_window.title('Camping Recipe App')

#fontsize
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(size = 10)

#main_window is the parent window
fram = Frame(main_window)

#adding label to search box
Label(fram,text='Search Recipe: ', font = fontStyle).pack(side=LEFT)


#adding of single line text box for search box
edit = Entry(fram)
 
#positioning of search text box
edit.pack(side=LEFT)

#adding of search button
butt = Button(fram, text='Search') 
butt.pack(side=RIGHT)
fram.pack(side=LEFT)
#keeps the app running
main_window.mainloop()



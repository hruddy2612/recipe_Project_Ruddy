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


#get current working directory
working_directory = os.getcwd()

#import the pandas dataframe
df = pd.read_csv(working_directory + '//recipe2.csv')

#get the list of names in the csv_file
#print the column titles as a list
col_list = df.columns

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
Label(fram,text='Search Recipes: ', font = fontStyle).pack(side=LEFT)


#adding of single line text box for search box
edit = Entry(fram)
 
#Put 'Search Recipe' inside search box
#edit.insert(0, "Find a Recipe:") 

#positioning of search text box
edit.pack(side=LEFT)


#for directions
fram3 = Frame(main_window)
fram3.place(relx = 0.4, rely = 0.6)
lbl2 = Label(fram3, font = fontStyle2)

#for ingredients
fram4 = Frame(main_window)
fram4.place(relx = 0.4, rely = 0.2)
lbl3 = Label(fram4, font = fontStyle2)

#adding of search button
butt = Button(fram, text='Search') 
butt.pack(side=RIGHT)
fram.pack(side=LEFT)
#keeps the app running
main_window.mainloop()



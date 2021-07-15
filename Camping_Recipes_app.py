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

#hello

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

#make s a string
entered_recipe = StringVar()

#adding of single line text box for search box
edit = Entry(fram, textvariable = entered_recipe)
 
#Put 'Search Recipe' inside search box
'''edit.insert(0, "Find a Recipe:") '''


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



def print_similar_recipes():
    
    #new label
    fram2 = Frame(main_window)
    fram2.place(relx = 0, rely = 0.6)
    lbl = Listbox(fram2, width = 40, height = 10)
    
    #get recipe name entered
    recipe = entered_recipe.get()
    
    #store similar recipes to what user inputs
    recipes = []    
    
    #split the user input
    inp = recipe.lower().split()
    
    #make the recipe name lowercase
    recipe_list = df['Recipe title'].tolist()
    
    recipe_list_adjusted = [''.join(s.split()).lower() for s in recipe_list]
    
    #find if the any words in the user input matches the recipe list
    for i in inp:
        
        for r, recipe in enumerate(recipe_list_adjusted):
            
            if i in recipe:
                
                recipes.append(recipe_list[r])
    
    #get unique recipes
    un_recipes = np.unique(recipes)
    
    #print out the recipes
    if len(un_recipes) > 0:
        
        for i,r in enumerate(un_recipes):
            #create a frame
            #lbl = Label(fram2, text = str(r), font = fontStyle)
            lbl.insert(i+1, str(r))
            lbl.pack()   
                       
        
    else:
        #create a frame
        show = "Recipe Not Found. Type a different recipe"
        lbl.insert(1, str(show))
        lbl.pack()
    



  #print stuff if selected
    def show_selected():
        
        #get the selected name
        selected = lbl.get(ANCHOR)
        try:
            #get the dataframe index
            idx = df[df['Recipe title'] == selected].index[0]

            #directions
            directions = df['Directions'][idx]
            col1 = 'DIRECTIONS:\n'            
            lbl2.config(text = col1 + directions, wraplength = 500)
            lbl2.pack()
            
            #ingredients
            ing = df['Ingredients'][idx]
            col2 = 'INGREDIENTS:\n'
            lbl3.config(text = col2 + ing, wraplength = 500)
            lbl3.pack()
            
            #image for recipe
            #fram4 = Frame(root)
            #fram4.pack(side = TOP)
            #img = PhotoImage(file = working_directory + '//' + 'smore.png')

            #Label(root, image=img).pack()
        
        except:
            
            lbl2.config(text = "Recipe Not Found. Type a different recipe")
            lbl2.pack()
            
            lbl3.config(text = '')
            lbl3.pack()

    
    Button(fram2, text = 'Show recipe', command = show_selected).pack(side = BOTTOM)  

#adding of search button
butt = Button(fram, text='Search', command = print_similar_recipes) 
butt.pack(side=RIGHT)
fram.pack(side=LEFT)

#keeps the app running
main_window.mainloop()



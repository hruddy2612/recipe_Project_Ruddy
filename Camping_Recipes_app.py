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

from PIL import ImageTk, Image

#get current working directory
working_directory = os.getcwd()

#import the pandas dataframe
df = pd.read_csv(working_directory + '//recipe2.csv')


#Functions#


def print_similar_recipes():
    
    #frame2, search results list box position on page
    frame2 = Frame(main_window) 
    frame2.place(x = 625, y = 35)

    #recipe search result list box size
    search_results= Listbox(frame2, width = 50, height = 10)
    
    #get recipe name entered
    recipe = entered_recipe.get()
    
    #store similar recipes to what user inputs
    recipes = []    
    
    #get user input and split words of input
    inp = recipe.lower().split()
    
    #get recipe from CSV, make the recipe name lowercase
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
            
            search_results.insert(i+1, str(r))
            search_results.pack()   
                       
        
    else:
        
        show = "Recipe Not Found. Type a different recipe"
        search_results.insert(1, str(show))
        search_results.pack()
    


  #print stuff if selected
    def show_selected():
        
        #get the selected name
        selected = search_results.get(ANCHOR)
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
            
        
        
        except:
            
            lbl2.config(text = "Recipe Not Found. Type a different recipe")
            lbl2.pack()
            
            lbl3.config(text = '')
            lbl3.pack()

    
    Button(frame2, text = 'Show recipe', command = show_selected).pack(side = BOTTOM)  


#create window
main_window = Tk()

#title of main window
main_window.title('Camping Recipe App')

#window state as zoomed 
main_window.state('zoomed')
#main_window.geometry('800x500')


#Frame 1, Search label textbox and button
frame1 = Frame(main_window)

#adding label to search box
Label(frame1,text='Search Recipes: ', font = (None, 10)).pack(side = LEFT)

#get the entry 
entered_recipe = StringVar()

#text box in frame1 next to search recipe (where recipe name is typed)
enter_recipe = Entry(frame1, textvariable = entered_recipe)

#position text box
enter_recipe.pack (side = LEFT)

#search button button
search_button = Button(frame1, text ='Search', command = print_similar_recipes) 
search_button.pack(side=RIGHT)
frame1.pack(side=LEFT)

#for the title and picture
frame3 = Frame(main_window)
frame3.place(x = 200, y = 350)

#for ingredients, directions, cook time information
frame4 = Frame(main_window)
frame4.place(x = 800, y = 250)





#fontsize
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(size = 10)
 
#Put 'Search Recipe' inside search box
'''edit.insert(0, "Find a Recipe:") '''








#keeps the app running
main_window.mainloop()



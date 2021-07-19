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
    

    
    #get user input and split words of input
    inp = recipe.lower().split()
    
    #get recipe from CSV, make the recipe name lowercase
    recipe_list = df['Recipe title'].tolist()
    #recipe_list_adjusted = [''.join(s.split()).lower() for s in recipe_list] # we'll do the inside the function
    
 

    def get_similar(inp, recipe_list):
        #store similar recipes to what user inputs
        recipes = []   

        # find if the any words in the user input matches the recipe list
        for i in inp:
            for recipe in recipe_list:
                recipe_lower = recipe.lower()
                if i in recipe.lower():
                    recipes.append(recipe)
        return recipes
    
    recipes = get_similar(inp, recipe_list)

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

#main window size and title
main_window = Tk()
main_window.geometry('800x500')

#title of main window
main_window.title('Camping Recipe App')

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

#fontsize
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(size = 10)


 
#Put 'Search Recipe' inside search box
'''edit.insert(0, "Find a Recipe:") '''



# CH use Text widget and insert image from file

# define new frame and put text area and scroll bar in it
textframe=Frame(main_window)
textframe.pack()  # this is bad placement, just for a test ....  

# create and pack the text area
text=Text(textframe, height=20, width=50,wrap=WORD)
text.pack(side=LEFT, fill=BOTH)

# yview callback gets called when the scroll bar or its arrows are moved
text_scroll=Scrollbar(textframe, command=text.yview)
text_scroll.pack(side=RIGHT,fill=Y)

# this connects changes in the scroll bar to changing the text area
# i.e. the text area will show a smaller window into the full text
text.configure(yscrollcommand=text_scroll.set)

text.insert(END, "-----------------------------------------\nHere is some text with an image\n")

from PIL import Image, ImageTk
img_PIL = Image.open("chili.jpg") # read in image into PIL

# resize to fit into a box
box_size = (300, 300)
img_PIL.thumbnail(box_size)

img = ImageTk.PhotoImage(img_PIL) # convert into Tk specific image object
text.image_create(END, image=img) # insert image (inside box)
text.insert(END, "\naaaaaaaaaaa\nbbbbbbbbbbbbbbb\nccccccccccccc\n") # test scroll bar

#for directions
fram3 = Frame(main_window)
fram3.place(relx = 0.4, rely = 0.6)
lbl2 = Label(fram3, font = fontStyle2)

#for ingredients
fram4 = Frame(main_window)
fram4.place(relx = 0.4, rely = 0.2)
lbl3 = Label(fram4, font = fontStyle2)


#keeps the app running
main_window.mainloop()



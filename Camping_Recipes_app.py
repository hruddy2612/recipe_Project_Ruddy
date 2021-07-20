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

        #clear the everything
        label_title_name.config(text = '')
        label_title_name.pack()
        label_content.config(text = '')
        label_content.pack()

        try:
            #get the dataframe index
            idx = df[df['Recipe title'] == selected].index[0]
            
            #print name of recipe            
            label_name.config(text = str(selected), font = (None, 20))
            label_name.pack(side = TOP)

            #picture
            pic = df['Picture Name'][idx]
            
            im = Image.open(working_directory + '//' + str(pic))
            
            im = im.resize((300, 200))
            
            main_window.im = ImageTk.PhotoImage(im)
            
            label_pic.configure(image = main_window.im)
            label_pic.pack(pady = 20, side = TOP)
            
            def show_ingredients():

                #selected = list_box.get(ANCHOR)    

                #get the dataframe index
                idx = df[df['Recipe title'] == selected].index[0]

                #ingredients
                ing = df['Ingredients'][idx]
                label_title_name.config(text = 'INGREDIENTS', font = (None, 15))
                label_title_name.pack(side = TOP)
                label_content.config(text = ing, wraplength = 500, anchor = 'w', font = (None, 10))
                label_content.pack(side = TOP, pady = 20, fill = 'both')


            def show_directions():

                #selected = list_box.get(ANCHOR)
                idx = df[df['Recipe title'] == selected].index[0]

                #ingredients
                directions = df['Directions'][idx]
                label_title_name.config(text = 'DIRECTIONS', font = (None, 15), wraplength = 500)
                label_title_name.pack(pady = 5)
                label_content.config(text = directions, wraplength = 500, anchor = 'w', font = (None, 10))
                label_content.pack(pady = 5)


               
            #ingredient button    
            but_ing.config(text = 'Ingredients', height = 1, width = 7, command = show_ingredients)
            but_ing.pack(side = TOP)

            #directions button
            but_dir.config(text = 'Directions', height = 1, width = 7, command = show_directions)
            but_dir.pack(side = TOP)

            

        except:
            #get rid of labels
            label_name.config(text = '')
            label_name.pack()
            
            #get rid of buttons
            but_ing.forget()
            but_dir.forget()
            
            #clear the everything
            label_title_name.config(text = '')
            label_title_name.pack()
            label_content.config(text = '')
            label_content.pack()
            
            label_pic.forget()            
    
    Button(frame2, text = 'Show recipe', command = show_selected).pack(side = BOTTOM)  

#main window size and title
main_window = Tk()
main_window.geometry('800x500')

#title of main window
main_window.title('Camping Recipe App')

#Frame 1, Search label textbox and button. 
# main_window is parent frame..Create a frame on it for the search label
frame1 = Frame(main_window) #this frame is for the textbox search label and the button

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


#frame3 for title and food picture
frame3 = Frame(main_window) #this frame is for the listbox
frame3.place(x = 200, y = 350)
label_name = Label(frame3)
label_pic = Label(frame3)

#frame 4 for ingredients directions and cook time
frame4 = Frame(main_window)
frame4.place(x = 800, y = 250)
label_title_name = Label(frame4, justify = 'right')
label_content = Label(frame4)

#frame 5 for buttons 
frame5 = Frame(main_window)
frame5.place(x = 550, y = 500)
but_ing = Button(frame5)
but_dir = Button(frame5)


#fontsize
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(size = 10)


#pack the frame on top
frame1.pack(side = TOP)



#keeps the app running
main_window.mainloop()
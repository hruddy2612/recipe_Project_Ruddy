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
    frame2.place(x = 20, y = 350)

    #recipe search result list box size
    search_results= Listbox(frame2, width = 30, height = 5)
    
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
                label_title_name.pack
                label_content.config(text = ing, wraplength = 500, font = (None, 10))
                label_content.pack


            def show_directions():

                #selected = list_box.get(ANCHOR)
                idx = df[df['Recipe title'] == selected].index[0]

                #directions 
                directions = df['Directions'][idx]
                label_title_name.config(text = 'DIRECTIONS', font = (None, 15), wraplength = 500)
                label_title_name.pack
                label_content.config(text = directions, wraplength = 500, font = (None, 10))
                label_content.pack

            def show_others():
                
                #selected = list_box.get(ANCHOR)
                idx = df[df['Recipe title'] == selected].index[0]
                
                #get cook time prep time and serves
                cook_time = df['Cook time'][idx]
                prep_time = df['Prep time'][idx]
                serves = df['Serves'][idx] #change serves # to Serves
                
                label_title_name.config(text = 'OTHER DETAILS', font = (None, 15), wraplength = 500)
                label_title_name.pack 
                #label_title_name.place(relx = 0, rely = 0)
                
                #TEXT
                txt = 'Cook time: ' + str(cook_time) + ' minutes' +'\n\n' + 'Prep time: ' + str(prep_time) + ' minutes' + '\n\n' + 'Number of Serves: ' + str(serves) + ' people' + '\n' 
                
                label_content.config(text = txt, wraplength = 500, anchor = 'w', font = (None, 10), justify = 'left',)
                label_content.pack
                #label_content.place(relx = 0.5, rely = 0.2)
               
            #ingredient button    
            but_ing.config(text = 'Ingredients', height = 1, width = 7, command = show_ingredients)
            but_ing.pack(side = TOP)

            #directions button
            but_dir.config(text = 'Directions', height = 1, width = 7, command = show_directions)
            but_dir.pack(side = TOP)

            #other button
            but_other.config(text = 'Other details', height = 1, width = 7, command = show_others)
            but_other.pack(side = TOP)
            

        except:
            #get rid of labels
            label_name.config(text = '')
            label_name.pack()
            but_other.forget()
            
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
main_window.geometry('1200x800')


#title of main window
main_window.title('Camping Recipe App')

#Frame 1, Search label textbox and button. 
# main_window is parent frame..Create a frame on it for the search label
frame1 = Frame(main_window) #this frame is for the textbox search label and the button

#adding label to search box
Label(frame1, text = 'Search Recipes:', font = (None, 10)).pack(side = LEFT, padx = 10)


#get the entry 
entered_recipe = StringVar()

#text box in frame1 next to search recipe (where recipe name is typed)
enter_recipe = Entry(frame1, width = 15, textvariable = entered_recipe)

#'search recipes' is inside search bar
#enter_recipe.insert(0, 'Search Recipe')

#position text box
enter_recipe.pack (side = LEFT)

#search button button
search_button = Button(frame1, text ='Search', command = print_similar_recipes) 
search_button.pack(side=RIGHT)

#frame3 for title and food picture
frame3 = Frame(main_window) #this frame is for the listbox
frame3.place(x = 450, y = 30)
label_name = Label(frame3)
label_pic = Label(frame3)

#frame 4 for ingredients directions and cook time
frame4 = Frame(main_window)
frame4.place(x = 450, y = 300)
label_title_name = Label(frame4, justify = 'left')
label_content = Label(frame4, justify = 'left')

#frame 5 for buttons 
frame5 = Frame(main_window)
frame5.place(x = 780, y = 200)
but_ing = Button(frame5)
but_dir = Button(frame5)
but_other = Button(frame5)

# define new frame 10 and put text area and scroll bar in it
textframe=Frame(main_window)
textframe.place(x = 20, y = 20)   

# create and pack the text area
text=Text(textframe, height=20, width=40,wrap=WORD)
text.pack(side=LEFT, fill=BOTH)

# yview callback gets called when the scroll bar or its arrows are moved
text_scroll=Scrollbar(textframe, command=text.yview)
text_scroll.pack(side=RIGHT,fill=Y)

# this connects changes in the scroll bar to changing the text area
# i.e. the text area will show a smaller window into the full text
text.configure(yscrollcommand=text_scroll.set)

text.insert(END, "Available Recipes\n-----------------------------\nBREAKFAST\n\nBreakfast Sandwich\nStrawberry French Toast\nApple Cinnamon Pancakes\nApple Sweet Potato Hash\n\nLUNCH\n\nHalloumi Tacos\nGyro Kebob\nChicken & Vegetable Kebobs\nFish Tacos\nKale Avocado Sandwich\nCashew Chicken Wrap\nSummer Spring Rolls\nChili Mac\n\nDINNER\n\nLentil Sloppy Joes\nCilantro Lime Chicken Tacos\nGlazed Salmon\nChicken Pad Thai\nPumpkin Mac\nChili\nMushroom Burger\nShrimp Boil Packets\n\nDESSERT\n\nBlueberry Cobbler\nGrilled Peaches\nSmores\nAutumn Plum Skillet Tart\n\n")

#fontsize
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(size = 10)

#pack the frame on top
#frame1.pack(side = TOP, pady = 20)
frame1.place( x = 0, y = 300)

#keeps the app running
main_window.mainloop()




'''#frame 6 Breakfast list
frame6 = Frame(main_window)
frame6.place(x = 0, y = 0)
Label(frame6, justify = 'left', text = 'BREAKFAST \nBreakfast Sandwich\nStrawberry French Toast' ).pack(side=LEFT, padx= 20, pady = 20)

#frame 7 Lunch list
frame6 = Frame(main_window)
frame6.place(x = 200, y = 0)
Label(frame6, justify = 'left', text = 'LUNCH \nChicken & Vegetable Kebobs\nFish Tacos\nKale Avocado Sandwich' ).pack(side=LEFT, padx = 20, pady = 20)

#frame 8 Dinner list
frame8 = Frame(main_window)
frame8.place(x = 0, y = 100)
Label(frame8, justify = 'left', text = 'DINNER \nChili\nMushroom Burger\nShrimp Boil Packets' ).pack(side=LEFT, padx = 20, pady = 0)

#frame 9 Dessert list
frame9 = Frame(main_window)
frame9.place(x = 200, y = 100)
Label(frame9, justify = 'left', text = 'DESSERT \nGrilled Peaches\nSmores' ).pack(side=LEFT, padx = 20, pady = 0)'''
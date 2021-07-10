#!/usr/bin/env python
# coding: utf-8

#import libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



#prints directions line by line
def print_directions(directions):
    
    split = 0
    #loop through all the characters to find where we have '1.' and '2.' and '3.'
    for i in range(len(directions) - 1): 
        
        if (directions[i].isnumeric()) and (directions[i+1] == '.'):
            
            print(directions[split:i], '\n')
            
            split = i  



def find_similar_recipe(user_input):
    
    #store similar recipes to what user inputs
    recipes = []    
    
    #split the user input
    inp = user_input.lower().split()
    
    #make the recipe name lowercase
    recipe_list = df['Recipe title'].tolist()
    
    recipe_list_adjusted = [''.join(s.split()).lower() for s in recipe_list]
    
    #find if the any words in the user input matches the recipe list
    for i in inp:
        
        for r, recipe in enumerate(recipe_list_adjusted):
            
            if i in recipe:
                
                recipes.append(recipe_list[r])
    #one result per title will print out           
    return np.unique(recipes)

# function that asks for user input and prints recipes

def print_recipe():
    
    #get the user input
    user_input = input('Type your recipe\n\n')

    
    #check if its available
    available_recipes = find_similar_recipe(user_input)
    
    #if recipe is available, print it
    if available_recipes is not None:
        print('\n\nAvailabel recipes')
        print('------------')
        
        for r in available_recipes:
            print(r)
    
    else:
        print('None available')
    
    
    return

#run the program
print_recipe()


# Main

#import CSV file to pandas (make sure excell is in csv format)
df = pd.read_csv ("/Users/heatherruddy/Downloads/HCI Python/Recipe Project/recipe_Project_Ruddy/recipe2.csv")

#print 5 rows of data
df.head(5)
print(df)

#print columns 
col_list = df.columns
print(col_list)

#print a row
df.loc[3]


while True:

    # Show all stored recipe titles to user:
    titles = list(df["Recipe title"])
    print("Available recipes:")
    for t in titles:
        print(t)
    print()

    #user input area for recipe they're searching
    user_input = input("Search Recipies by Title\n")

    # This is a more coplex version of your is_recipe_available() if it would return True/False
    best_match = return_best_match(user_input, titles)
    if best_match == None:
        print(user_input, "not found, try again") 
        continue
    else:
        print("match found:", best_match)
        match_df = get_recipe_(best_match, df) # as we've pre-checked that we have a match, this should never return an empty df
        #print(match_df)  # Not super clean but at least we retain the column headings
        # in the GUI, this would end up in different areas/fields/boxes
        for s in list(match_df): # list of values
            print(s)

        # images: 
        # I suggest having a img folder with a jpg for each recipe, each with the title:
        # I would remove spaces or ` to get a gurateed valid file name 
        # example: "img/mushroomburger.jpg"
        #          "img/smores.jpg"
        #          "img/fishtacos.jpg"
        s = best_match.replace(" ","") # remove spaces
        s = s.replace("'", "") # remove single quote
        # etc. for all punctation like chars
        image_path = "img/" + s + ".jpg"

        if exists(image_path):  # do we have this image?
            plot_image(image_path)
        else:
            print(image_path, "not found - skipping")

        break 



'''
#is the recipe available
def is_recipe_available(user_input,df):
    
    recipe_list = df["Recipe title"]
    
    #if else loop for if a recipe is available
    if user_input in recipe_list:
        print("Recipe is available")
        
    else:
        print("Recpie is not available")
'''
'''
#print entire recipe 
def print_recipe(user_input, df):
    r = df.loc[df["Recipe title"] == user_input]
    r.reset_index(drop=True, inplace=True)
    print(r) # Debug
    if r.empty:
	    print("Not found")
    else:
	    print(r.loc[0].tolist())
'''



'''#user leaves recipe review
def leave_review(user_review):
    
    #if else loop for acceptable review length
    if len(user_review) < 200:
        print("Thank you for your review.")
    else: 
        print("Error. Your review exceeds the character limit.")
'''
'''
#user adds a note to a recipe
def leave_note(user_note):
    
    #if else loop to determine if not is correct length
    if len(user_note) < 200:
        print("Your note has been saved.")
    else:
        print("Error. Your note was too long.")
'''

'''
#import an image for a recipe
def plot_image(image):
    
    img = mpimg.imread(image)
    imgplot = plt.imshow(img)
    plt.show()'''

'''def return_best_match(search_term, word_list):
    Given a search term, which is the closest match from a list of strings?
    if not reasonably good match is found, None is returned
    Based on a difference metric, here i'm using the Jaro-Winkler metric from this package:
    https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-distance
    
    similarity_list = []
    for word in word_list:
        similarity = Levenshtein.jaro_winkler(search_term, word) # https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-jaro_winkler
        similarity_list.append([similarity, word])  # 0: similarity, 1: word

    sorted_similarity_list = sorted(similarity_list, reverse=True) # sort decending, largest similarity on top
    best_match = sorted_similarity_list[0] # list with largest similarity

    if best_match[0] < 0.5: # no good enough metric was found
        return None
    else:
        return best_match[1] # word with best metric (> 0.5)
'''
 



#import libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv ("/Users/heatherruddy/Downloads/HCI Python/Recipe Project/recipe_Project_Ruddy/recipe2.csv")

#is the recipe available
def is_recipe_available(user_input,df):
    
    recipe_list = df["Recipe title"]
    
    #if else loop for if a recipe is available
    if user_input in recipe_list:
        print("Recipe is available")
        
    else:
        print("Recpie is not available")

#print entire recipe 
def print_recipe(user_input, df):
    r = df.loc[df["Recipe title"] == user_input]
    r.reset_index(drop=True, inplace=True)
    print(r) # Debug
    if r.empty:
	    print("Not found")
    else:
	    print(r.loc[0].tolist())

#user leaves recipe review
def leave_review(user_review):
    
    #if else loop for acceptable review length
    if len(user_review) < 200:
        print("Thank you for your review.")
    else: 
        print("Error. Your review exceeds the character limit.")

#user adds a note to a recipe
def leave_note(user_note):
    
    #if else loop to determine if not is correct length
    if len(user_note) < 200:
        print("Your note has been saved.")
    else:
        print("Eror. Your note was too long.")

#print entire recipe 
def print_recipe(user_input, df):
    '''search title column in df for  user_input (string)
    if found, print out full recipe, otherwise inform user that not found
    '''
    r = df.loc[df["Recipe title"] == user_input]
    r.reset_index(drop=True, inplace=True)
    print(r) # Debug

    if r.empty:                 # I'd advise against printing out stuff inside a function
	    print("Not found")      # better to return something, and have the caller catch it.
    else:                       # It can then be up to the caller to print it out, or show it in a GUI, or whatever
	    print(r.loc[0].tolist())# Basically it's more flexible b/c it lets the caller decide what to do

#import an image for a recipe
def plot_image(image):
    
    img = mpimg.imread(image)
    imgplot = plt.imshow(img)
    plt.show()

def return_best_match(search_term, word_list):
    '''Given a search term, which is the closest match from a list of strings?
    if not reasonably good match is found, None is returned
    Based on a difference metric, here i'm using the Jaro-Winkler metric from this package:
    https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-distance
    '''
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



#Main Code 


#print 5 rows of data
df.head(5)
print(df)
#print columns 
print(df.columns)

#user input area for recipe they're searching
user_input = input("Search Recipes \n")

#print the recipe based on above user input, but
#this does not work, I dont know what this error means
is_recipe_available(user_input,df)


#user input for leaving a review
user_review = input("Leave a Review\n")

#image path that I want to import
image = "/Users/heatherruddy/Downloads/HCI Python/Recipe Project/recipe_Project_Ruddy/mushroom_burger.jpg"





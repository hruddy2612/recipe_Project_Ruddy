#import libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Levenshtein # word similarity metrics: pip install python-Levenshtein
from os.path import exists

# CH: do you imports first than def all your functions (or import them from a module),
# them do all your main code below the defs. It's not technically wrong to mix import, defs and main code
# but it's hard to read your code, especially if it gets longer.



#is the recipe available?
def is_recipe_available(user_input, df):  # space after comma
    '''Consider adding a doc string'''
    recipe_list = df["Recipe title"]
    
    #if else loop for if a recipe is available    
    if user_input in recipe_list:                 
        print("Recipe is available")
    else:
        print("Recpie is not available")
# The issue here is that the caller of that function doesn't get anything back that indicates 
# sucess or fail. Instead, return either True or False and let the caller deal with
# how to react. E.g. on False, the caller could ask for anotehr inout as the current
# clearly isn't in the DB.


#print entire recipe 
def print_recipe(user_input, df):
    '''search title column in df for  user_input (string)
    if found, print out full recipe, otherwise inform user that not found
    '''
    r = df.loc[df["Recipe title"] == user_input]
    r.reset_index(drop=True, inplace=True)
    print(r) # Debug

    if r.empty:                 # I'd avise against printing out stuff inside a function
	    print("Not found")      # better to return something, and have the caller catch it.
    else:                       # It can then be up to the caller to print it out, or show it in a GUI, or whatever
	    print(r.loc[0].tolist())# Basivcally it's more flexible b/c it lets the caller decide what to do

# CH my version
def get_recipe_(title_search, df):  # be more precise when naming your args. Input could be any number of things.
    '''search title column in df for  user_input (string)
    if found, return a 1 row data frame with all columns
    otherwise returns None
    Note: to make it easier, I convert the input into lowercase, as that seems to be the rule in your csv file DB
    '''
    lc = title_search.lower()  # lowercase search term

    # Does search term exactly match a title in the DB?
    r = df.loc[df["Recipe title"] == lc]  # returns empty df or df with one more rows
    
    #print(r) # Debug

    if r.empty:
	    return None
    else:
        # We have at least one hit
        r.reset_index(drop=True, inplace=True) # reset index so we can grab the first row via row index = 0
        return_row = r.loc[0] # could return the row directly but that way we can look at it in the debugger
        return return_row 

# CH (experimental): 
def return_best_match(search_term, word_list):
    '''Given a search term, which is the closest match from a list of strings?
    if not reasonalby good match is found, None is returned
    Based on a difference metric, here i'm using the Jaro-Winkler metric from this package:
    https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-distance
    '''
    similarity_list = []
    for word in word_list:
        similarity = Levenshtein.jaro_winkler(search_term, word) # https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-jaro_winkler
        similarity_list.append([similarity, word])  # 0: simlarity, 1: word

    sorted_similarity_list = sorted(similarity_list, reverse=True) # sort decending, largest similary on top
    best_match = sorted_similarity_list[0] # list with largest similarity

    if best_match[0] < 0.5: # no good enough metric was found
        return None
    else:
        return best_match[1] # word with best metric (> 0.5)

#user leaves a recipe review


# This works but is a bit pointless as is b/c you're not doing anything with the review.
# Also, you don't actually know what recipe was reviewed!
# You need to think about a way to store these reviews in some sort of datastructure
# (Also, again, this won't handle a > 200 chars case b/c the caller of this function
# won't know when it occured and thus should ask for re-entry. Better: just silently truncate
# a > 200 input)
# 
def leave_review(user_review):
    
    #if else loop for acceptable review length
    if len(user_review) < 200:
        print("Thank you for your review.")
    else: 
        print("Error. Your review exceeds the character limit.")

# Suggestion: 
def store_review(user_review, title):
    '''Leave a review (up to 200 chars) for a specific title (which is assumend to be valid!)
    '''

    print("Thank you for your review.")

    # Truncate if too long
    if len(user_review) < 200:
        print("Warning: Your review exceeds the 200 character limit and was truncated")
        user_review = user_review[:200]
    # Somehow store review for this title in a review DB 
    # ...

# CH: same issues here:
#user adds a note to a recipe
def leave_note(user_note):
    
    #if else loop to determine if not is correct length
    if len(user_note) < 200:
        print("Your note has been saved.")
    else:
        print("Eror. Your note was too long.")



def plot_image(image):

    # ??? you get the path to the image in the image arg, but then your just hardcod it here
    #img = mpimg.imread("/Users/heatherruddy/Downloads/HCI Python/HCI584 - lecture 02 - Visual Studio setup, working with git/Recipe_project_heather_ruddy/mushroom_burger.jpg")
    img = mpimg.imread(image)mush br
    imgplot = plt.imshow(img)
    plt.show()

#
# MAIN
#

# just use a relative path
#df = pd.read_csv ("/Users/heatherruddy/Downloads/HCI Python/Recipe Project/recipe_Project_Ruddy/recipe2.csv")
df = pd.read_csv ("recipe2.csv") # assumes csv file is in the same folder as this .py file


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

#user input for leaving a review
#user_review = input("Leave a Review\n")




# image path that I want to import
#image = "/Users/heatherruddy/Downloads/HCI Python/HCI584 - lecture 02 - Visual Studio setup, working with git/Recipe_project_heather_ruddy/mushroom_burger.jpg"
#plot_image(image)   
#import libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv ("/Users/heatherruddy/Downloads/HCI Python/HCI584 - lecture 02 - Visual Studio setup, working with git/Recipe_project_heather_ruddy/recipe2.csv")

#print 5 rows of data
df.head(5)
print(df)
#print columns 
print(df.columns)

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

#user input area for recipe they're searching
user_input = input("Search Recipies \n")

#print the recipe based on above user input, but
#this does not work, I dont know what this error means
is_recipe_available(user_input,df)

#user leaves a recipe review

def leave_review(user_review):
    
    #if else loop for acceptable review length
    if len(user_review) < 200:
        print("Thank you for your review.")
    else: 
        print("Error. Your review exceeds the character limit.")

#user input for leaving a review
user_review = input("Leave a Review\n")

#user adds a note to a recipe
def leave_note(user_note):
    
    #if else loop to determine if not is correct length
    if len(user_note) < 200:
        print("Your note has been saved.")
    else:
        print("Eror. Your note was too long.")


# image path that I want to import
image = "/Users/heatherruddy/Downloads/HCI Python/HCI584 - lecture 02 - Visual Studio setup, working with git/Recipe_project_heather_ruddy/mushroom_burger.jpg"
#importing image function
def plot_image(image):
    
    img = mpimg.imread("/Users/heatherruddy/Downloads/HCI Python/HCI584 - lecture 02 - Visual Studio setup, working with git/Recipe_project_heather_ruddy/mushroom_burger.jpg")
    imgplot = plt.imshow(img)
    plt.show()

       
plot_image(image)   
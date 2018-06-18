import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from helper_functions import show_images, show_images_by_digit
from helper_functions import fit_random_forest_classifier, do_pca, plot_components

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns

def display_gif(fn):
    return '<img src="{}">'.format(fn)


def check_question_one(solution_1_dict):
    a = 7
    b = 66
    c = 387
    d = 18
    e = 0.23
    f = 0.05

    my_sol = {
        'The number of cars in the dataset': c,
        'The number of car features in the dataset': d,
        'The number of dummy variables in the dataset': a,
        'The proportion of minivans in the dataset': f,
        'The max highway mpg for any car': b
    }
    
    if my_sol == solution_1_dict:
        print("Nice job!  Looks like your dataset matches what we found!")
        return display_gif('https://bit.ly/2K9X0gD')
    
    if my_sol['The number of cars in the dataset'] != solution_1_dict['The number of cars in the dataset']:
        print("Sorry, but it looks like you missed the first one.  The number of cars in the dataset should match the number of rows in the dataset.  Try again!\n\n")
    
    if my_sol['The number of car features in the dataset'] != solution_1_dict['The number of car features in the dataset']:
        print("Sorry, but it looks like you missed the second one.  The number of car features in the dataset should match the number of columns in the dataset.  Try again!\n\n")
    if my_sol['The number of dummy variables in the dataset'] != solution_1_dict['The number of dummy variables in the dataset']:
        print("Sorry, but it looks like you missed the third one.  The dummy variables are columns with only 1 and 0 values in the dataset.  Try again!")
    if my_sol['The proportion of minivans in the dataset'] != solution_1_dict['The proportion of minivans in the dataset']:
        print("Sorry, but it looks like you missed the fourth one.  The proportion of minivans in the dataset can be found by using the describe method on your dataframe or directly on the minivans column of the dataset.")
    if my_sol['The max highway mpg for any car'] != solution_1_dict['The max highway mpg for any car']:
        print("Sorry, but it looks like you missed the last one.  The max highway mpg in the dataset can be found by using the describe method on your dataframe or using the max function in numpy.")        
        
    if my_sol != solution_1_dict:
        return display_gif('https://bit.ly/2Hog74V')


def check_question_two(solution_2_dict):
    a = True
    b = False

    my_sol = {
        'The components span the directions of maximum variability.': a,
        'The components are always orthogonal to one another.': a,
        'Eigenvalues tell us the amount of information a component holds': a
    }
    
    try:
        if my_sol == solution_2_dict:
            print("That's right these are all true.  Principal components are orthogonal, span the directions of maximum variability, and the corresponding eigenvalues tell us how much of the original variability is explained by each component.")
        else:
            print("Oops! That doesn't look quite right! One or more of the statements you marked False is actually True. Try again!")
            
    except:
        print("Oops! That doesn't look quite right! One or more of the statements you marked False is actually True. Try again!")
        
        
def check_question_five(solution_5_dict):
    a = 'car weight'
    b = 'sports cars'
    c = 'gas mileage'
    d = 0.4352
    e = 0.3061
    f = 0.1667
    g = 0.7053

    my_sol = {
        'The first component positively weights items related to': c, 
        'The amount of variability explained by the first component is': d,
        'The largest weight of the second component is related to': b,
        'The total amount of variability explained by the first three components': g
    }
    
    if my_sol == solution_5_dict:
        print("That's right!  Looks like you know a lot about PCA!")
    if my_sol['The first component positively weights items related to'] != solution_5_dict['The first component positively weights items related to']:
        print("Oops!  Looks like you missed the first question.  Notice that there are two bars that are large, positive, while the rest are mostly negative.  What are the two bars related to?\n\n")
        
    if my_sol['The amount of variability explained by the first component is'] != solution_5_dict['The amount of variability explained by the first component is']:
            print("Oops!  Looks like you missed the second question.  If you look in the table, you will see the variance explained in the first column.  Then the principal component is provided as the weights that show up in each associated row.\n\n")     
            
    if my_sol['The largest weight of the second component is related to'] != solution_5_dict['The largest weight of the second component is related to']:
        print("Oops!  Looks like you missed the third question.  If you look in the table, you will see the variance explained in the first column.  Looking at the bar chart, you can see that the largest weight for the second component is the blue bar on the far left.  This is the first column in the original set of features.\n\n")

    if my_sol['The total amount of variability explained by the first three components'] != solution_5_dict['The total amount of variability explained by the first three components']:
        print("Oops!  Looks like you missed the last question.  If you add all of the variability explained in the first column of the table, how much is explained by the first component?")    

        
def question_check_six(num_comps):
    if num_comps == 6:
        print("Nice job!  That's right!  With 6 components, you can explain more than 85% of the variability in the original dataset.")
        return display_gif('https://bit.ly/2cKTiso')
    else:
        print("Oops!  That doesn't look quite right.  Try again.")
        return display_gif('https://bit.ly/2AC30ww')
        
        
        
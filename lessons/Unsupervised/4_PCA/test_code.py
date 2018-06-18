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

train = pd.read_csv('./data/train.csv')

# save the labels to a Pandas series target
y = train['label']

# Drop the label feature
X = train.drop("label", axis=1)

def question_two_check(input1, input2):
    match1 = (input1 == y)
    match2 = (input2 == X)
    if all(match1) and all(match2):
        print("That looks right!")
    else:
        print("Oops!  That doesn't look like what was expected for X and y.  X should be a matrix of only the pixels, and y should only hold the label column.")

        
def question_3_check(solution_three):
    a = True
    b = False
    c = 6.13
    d = 'The total amount of variability in the data explained by the first two principal components'
    e = None
    my_sol = {
    '10.42' : d, 
    'The first component will ALWAYS have the most amount of variability explained.': a,
    'The total amount of variability in the data explained by the first component': c,
    'The sum of the variability explained by all the components can be greater than 100%': b
}
    
    if my_sol == solution_three:
        print("Looks good!  The amount of variability explained by each principal component gives us an idea of how much of the original variability in the original data is retained by each component.  Nice job matching these up!")

    if my_sol['10.42'] != solution_three['10.42']:
        print("Oops!  Looks like you missed the first one.  Notice that 9.85 is the sum of the two bars shown in the plot.  This means that the total amount of variability explained by the first two principal components is 9.85.  5.74% can be explained by the first component, and the rest is explained by the second component.\n\n")
    if my_sol['The first component will ALWAYS have the most amount of variability explained.'] != solution_three['The first component will ALWAYS have the most amount of variability explained.']:
        print("Oops!  Looks like you missed the second one.  It is actually the case that the first component will ALWAYS be the largest.  This is because PCA tries to find the direction of maximum variance first. In fact, the components will always be in order from largest amount of variability explained first to smallest amount of variability explained as the last component.\n\n")
    if my_sol['The total amount of variability in the data explained by the first component'] != solution_three['The total amount of variability in the data explained by the first component']:
        print("Oops!  Looks like you missed the third one.  The amount of variability explained by each component is shown by the bars in the chart.  The total amount of variability explained by the combined components up to each component is shown by the line.  This gives us an idea of how much is explained so far, and how much each additional component is contributing.\n\n")
    if my_sol['The sum of the variability explained by all the components can be greater than 100%'] != solution_three['The sum of the variability explained by all the components can be greater than 100%']:
        print("Oops!  The last answer doesn't look right.  Your principal components are always reducing the original space of your features until you have as many principal components as you had original features.  Therefore, the sum of the amount of variability explained by all the components can never exceep 100%")
        
        
def question_5_check(solution_five):

    my_sol = {
    'This component looks like it will assist in identifying zero': 0,
    'This component looks like it will assist in identifying three': 3
    }
              
    if my_sol == solution_five:
        print("Nice job!  That matches our solution as well!  The index of the first principal component appears to have really high weights where a zero would appear.  Alternatively, the fourth (third indexed component) appears to downweight where a three would appear to make it stand out.")
    else:
        print("Oops!  That doesn't look quite right.  Please use the indices as numbers for the values, so the first component should be 0, the second component would be 1, and so on.")

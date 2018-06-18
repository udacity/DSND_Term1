import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import seaborn as sns


def check_one(answers_one):
    '''
    INPUT:
    answers_one - a dictionary with key-value pairs associated with question 1
    
    OUTPUT:
    nothing returned
    print a statement related to the correctness of the answers
    '''
    a = '0.65'
    b = '0'
    c = 'Age'
    d = '0.35'
    e = 'Glucose'
    f = '0.5'
    g = "More than zero"

    answers_one_1 = {
        'The proportion of diabetes outcomes in the dataset': d,
        'The number of missing data points in the dataset': b,
        'A dataset with a symmetric distribution': e,
        'A dataset with a right-skewed distribution': c, 
        'This variable has the strongest correlation with the outcome': e
    }
    
    if answers_one == answers_one_1:
        print("Awesome! These all look great!")
    
    if answers_one['The proportion of diabetes outcomes in the dataset'] != answers_one_1['The proportion of diabetes outcomes in the dataset']:
        print("Oops!  That doesn't look like the proportion of 1's in the outcomes column.  I saw closer to 35% using the describe() method.")

    if answers_one['The number of missing data points in the dataset'] != answers_one_1['The number of missing data points in the dataset']:
        print("Oops!  That doesn't look like the right number of missing values.  I actually couldn't find any missing values")
        
    if answers_one['A dataset with a symmetric distribution'] != answers_one_1['A dataset with a symmetric distribution']:
        print("Oops!  Of the two columns above, Glucose is actually the symmetric column.  You can see this by running the .hist() method on your dataframe.")
     
    if answers_one['A dataset with a right-skewed distribution'] != answers_one_1['A dataset with a right-skewed distribution']:
        print("Oops!  Of the two columns above, Age is actually the right-skewed column.  You can see this by running the .hist() method on your dataframe.")
        
    if answers_one['This variable has the strongest correlation with the outcome'] != answers_one_1['This variable has the strongest correlation with the outcome']:
        print("Oops!  Besides Outcome itself, the column that is most correlated with the Outcome variable is actually Glucose.")
        

def print_metrics(y_true, preds, model_name=None):
    '''
    INPUT:
    y_true - the y values that are actually true in the dataset (numpy array or pandas series)
    preds - the predictions for those values from some model (numpy array or pandas series)
    model_name - (str - optional) a name associated with the model if you would like to add it to the print statements 

    OUTPUT:
    None - prints the accuracy, precision, recall, and F1 score
    '''
    if model_name == None:
        print('Accuracy score: ', format(accuracy_score(y_true, preds)))
        print('Precision score: ', format(precision_score(y_true, preds)))
        print('Recall score: ', format(recall_score(y_true, preds)))
        print('F1 score: ', format(f1_score(y_true, preds)))
        print('\n\n')
    
    else:
        print('Accuracy score for ' + model_name + ' :' , format(accuracy_score(y_true, preds)))
        print('Precision score ' + model_name + ' :', format(precision_score(y_true, preds)))
        print('Recall score ' + model_name + ' :', format(recall_score(y_true, preds)))
        print('F1 score ' + model_name + ' :', format(f1_score(y_true, preds)))
        print('\n\n')
        
        
def check_best(best_model):
    '''
    INPUT:
    best_model - a string of the best model
    
    OUTPUT:
    print a statement related to if the best model matches what the solution found
    '''
    a = 'randomforest'
    b = 'adaboost'
    c = 'supportvector'

    if best_model == b:
        print("Nice!  It looks like your best model matches the best model I found as well!  It makes sense to use f1 score to determine best in this case given the imbalance of classes.  There might be justification for precision or recall being the best metric to use as well - precision showed to be best with adaboost again.  With recall, SVMs proved to be the best for our models.")
       
    else:
        print("That wasn't the model I had in mind... It makes sense to use f1 score to determine best in this case given the imbalance of classes.  There could also be justification for precision or recall being the best metric to use as well - precision showed to be best with adaboost.  With recall, SVMs proved to be the best for our models.")
        
        
def check_q_seven(sol_seven):
    '''
    INPUT:
    solution dictionary for part seven
    OUTPUT:
    prints statement related to correctness of dictionary
    '''
    a = 'Age'
    b = 'BloodPressure'
    c = 'BMI'
    d = 'DiabetesPedigreeFunction'
    e = 'Insulin'
    f = 'Glucose'
    g = 'Pregnancy'
    h = 'SkinThickness'



    sol_seven_1 = {
        'The variable that is most related to the outcome of diabetes' : f,
        'The second most related variable to the outcome of diabetes' : c,
        'The third most related variable to the outcome of diabetes' : a,
        'The fourth most related variable to the outcome of diabetes' : d
    }

    if sol_seven == sol_seven_1:
        print("That's right!  Some of these were expected, but some were a bit unexpected too!")
              
    else:
        print("That doesn't look like what I expected, but maybe your feature importances were different - that can definitely happen.  Take a look at the best_estimator_.feature_importances_ portion of your fitted model.")
              
         
def q1_check(models_dict):
    '''
    INPUT:
    models_dict - a dictionary with models and what types of problems the models can be used for
    
    OUTPUT:
    nothing returned
    prints statements related to the correctness of the dictionary
    '''
    a = 'regression'
    b = 'classification'
    c = 'both regression and classification'

    models = {
        'decision trees': c,
        'random forest': c,
        'adaptive boosting': c,
        'logistic regression': b,
        'linear regression': a,
    }
    
    if models == models_dict:
        print("That's right!  All but logistic regression can be used for predicting numeric values.  And linear regression is the only one of these that you should not use for predicting categories.  Technically sklearn won't stop you from doing most of anything you want, but you probably want to treat cases in the way you found by answering this question!")
    
    if models['logistic regression'] != models_dict['logistic regression']:
        print("Oops!  In most cases, you will only want to use logistic regression for classification problems.")
        
    if models['linear regression'] != models_dict['linear regression']:
        print("Oops!  Linear regression should actually only be used in regression cases. Try again.")
        
    if (models['decision trees'] != models_dict['decision trees']) or (models['random forest'] != models_dict['random forest']) or (models['adaptive boosting'] != models_dict['adaptive boosting']):
        print("Oops!  Actually random forests, decision trees, and adaptive boosting are all techniques that can be used for both regression and classification.  Try again!")
    
    

    
def q6_check(metrics):
    '''
    INPUT:
    metrics - a dictionary with metrics and what types of problems the metrics can be used for
    
    OUTPUT:
    nothing returned
    prints statements related to the correctness of the dictionary
    '''
    a = 'regression'
    b = 'classification'
    c = 'both regression and classification'

    #
    metrics_ch = {
        'precision': b,
        'recall': b,
        'accuracy': b,
        'r2_score': a,
        'mean_squared_error': a,
        'area_under_curve': b, 
        'mean_absolute_area': a 
    }
    
    if metrics_ch == metrics:
        print("That's right! Looks like you know your metrics!")
       
    if (metrics['precision'] != metrics['precision']) or (metrics['recall'] != metrics['recall']) or (metrics['accuracy'] != metrics['accuracy']) or (metrics['area_under_curve'] != metrics['area_under_curve']):
        print("Oops!  Actually, there are four metrics that are used for classification.  Looks like you missed at least one of them.")
    
    if metrics != metrics_ch:
        print("Oops!  Something doesn't look quite right.  You should have three metrics for regression, and the others should be for classification.  None of the metrics are used for both regression and classification.")
        
        
def check_ten(best_fit):
    '''
    INPUT:

    OUTPUT:
    
    '''
    a = 'decision tree'
    b = 'random forest'
    c = 'adaptive boosting'
    d = 'linear regression'


    best_fitting = {
        'mse': b,
        'r2': b,
        'mae': b
    }

    if best_fit == best_fitting:
        print("That's right!  The random forest was best in terms of all the metrics this time!")
       
    else:
        print("Oops!  Actually the best model was the same for all the metrics.  Try again - all of your answers should be the same!")
    
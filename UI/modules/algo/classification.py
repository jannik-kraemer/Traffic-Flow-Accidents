from sklearn.naive_bayes import MultinomialNB
import pickle
import os
import pandas
import numpy as np

def prediction(data_x_validation):
    print(os.system('dir'))
    with open('model.ml', 'rb') as fml:
        loaded_model = pickle.load(fml)

    predictions = loaded_model.predict(pandas.DataFrame(data_x_validation))
    return predictions
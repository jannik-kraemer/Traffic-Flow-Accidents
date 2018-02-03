# Main File
import numpy as np
import pandas as pd
import modules.dataset as ds

dataset = ds.Dataset('data/accidents_2012_to_2014.csv')
data = dataset.get()

print("Length of dataset: ", dataset.length())

import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_csv("formatted/data_2012_to_2014.csv")

X = dataset.iloc[:, 6:12].values
y = dataset.iloc[:, 12].values



print("X: ", X)
print("Y: ", y)
import pandas as pd
class Dataset:
    def __init__(self, file):
        self.data = pd.read_csv(file)

    def get(self):
        return self.data

    def length(self):
        return len(self.data)
    


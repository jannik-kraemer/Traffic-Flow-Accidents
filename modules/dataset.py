import pandas as pd
from IPython.display import display, HTML


class Dataset:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_csv(file)

    def get(self):
        return self.data

    def length(self):
        return len(self.data)
    
    def export_to_html(self, path, rows):
        print("[Dataset] Creating dataset table... to " + path + "!")
        self.dataFile = open(path, mode='w')
        self.dataFile.writelines("<div style='font-family: sans-serif'>")
        self.dataFile.writelines("<h1> Dataset: <b>"  + self.file + "</b></h1>")
        self.dataFile.write(self.data.head(n=int(rows)).to_html())
        self.dataFile.writelines("</div>")
        self.dataFile.close()
        print("[Dataset] Export complet!")

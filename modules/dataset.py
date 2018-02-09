import pandas as pd
from IPython.display import display, HTML

def export(data, path, rows=5, type="HTML"):
    if(type.upper() == "HTML"):
        print("[Dataset] Creating dataset table... to " + path + "!")
        dataFile = open(path, mode='w')
        dataFile.writelines("<div style='font-family: sans-serif'>")
        dataFile.writelines("<h1> Dataset: <b>"  + path + "</b></h1>")
        dataFile.write(pd.DataFrame(data).head(n=int(rows)).to_html())
        dataFile.writelines("</div>")
        dataFile.close()
        print("[Dataset] Export complet!")
    elif(type.upper() == "CSV"):
        print("[Dataset] Creating csv file ... ( " + path + ")")
        csvFile = open(path, mode='w')
        csvFile.write(pd.DataFrame(data).to_csv())
        print("[Dataset] Export complet!")
    else:
        print("Error")







class Dataset:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_csv(file)

    def get(self):
        return self.data

    def length(self):
        return len(self.data)
    
    def setDataset(self, newData):
        self.data = newData
    
    def export_to_html(self, path, rows):
        print("[Dataset] Creating dataset table... to " + path + "!")
        dataFile = open(path, mode='w')
        dataFile.writelines("<div style='font-family: sans-serif'>")
        dataFile.writelines("<h1> Dataset: <b>"  + self.file + "</b></h1>")
        dataFile.write(pd.DataFrame(self.data).head(n=int(rows)).to_html())
        dataFile.writelines("</div>")
        dataFile.close()
        print("[Dataset] Export complet!")
    
    def export_to_csv(self, path):
        print("[Dataset] Creating csv file ... ( " + path + ")")
        self.csvFile = open(path, mode='w')
        self.csvFile.write(pd.DataFrame(self.data).to_csv())
        print("[Dataset] Export complet!")

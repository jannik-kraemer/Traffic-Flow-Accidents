import modules.dataset as ds

dataset = ds.Dataset('data/accidents_2012_to_2014.csv')
data = dataset.get()

dFile = input("Enter file path: ")

dataset.export_to_csv(dFile)
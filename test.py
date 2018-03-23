# import pandas as pd
# from modules import timeStamp
# # import matplotlib.pyplot as plt
# import urllib.request, json 

# apiKey = "1333680d8879f3272cd3e24b0f941693"
# coord = "49.6119545,6.1190247"

# requestUrl = "https://api.darksky.net/forecast/" + apiKey + "/" + coord + "," + timeStamp.getTime("09/02/2018 - 23:01")
# print(requestUrl)
# with urllib.request.urlopen(requestUrl) as url:
#     data = json.loads(url.read().decode())
#     print(data['currently'])




# # data = pd.read_csv('formatted/data_2012_to_2014.csv')

import modules.apiTranslator.Wheater as wheater
print(wheater.get(coord="49.6119545,6.1190247"))

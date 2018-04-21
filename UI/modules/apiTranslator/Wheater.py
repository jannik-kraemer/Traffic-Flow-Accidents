import modules.timeStamp as timeStamp
import urllib.request, json 
import modules.apiTranslator.Attributes as Attributes

# example for time: "09/02/2018 - 23:01"

class Data():
    def __init__(self, coord, time):
        requestUrl = "https://api.darksky.net/forecast/" + Attributes.apiKey + "/" + str(coord) + "," + timeStamp.getTimestamp(time)
        with urllib.request.urlopen(requestUrl) as url:
            self.data = json.loads(url.read().decode())
            
    def get(self):
        return self.data
    def translate(self, key):
        return self.data[key]


def check(inputTime, baseTime, secondBaseTime):
    if(int(inputTime) >= int(baseTime) and int(inputTime) <= int(secondBaseTime)):
        # return "Daylight"
        return 1
    else:
        return 0
        # return "Darkness"
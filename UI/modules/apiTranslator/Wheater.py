import modules.timeStamp as timeStamp
import urllib.request, json 
import modules.apiTranslator.Attributes as Attributes

# example for time: "09/02/2018 - 23:01"

class Data():
    def __init__(self, coord, time):
        print(time)
        requestUrl = "https://api.darksky.net/forecast/" + Attributes.apiKey + "/" + str(coord) + "," + timeStamp.getTimestamp(time) + "?units=si"
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

def conditions(coord, inputTime):
    data = Data(coord, inputTime)
    wheater = data.get()
    print(wheater['currently'])
    highWind = False
    currently = wheater['currently']
    if currently['windSpeed'] > 10.8:
        highWind = True
    print(currently['icon'])
    if currently['icon'] == 'rain':
        if highWind == True:
            return 2
        else:
            return 1
    elif currently['icon'] == 'snow':
        if highWind == True:
            return 6
        else:
            return 4
    elif currently['icon'] == 'fog':
        return 5
    else:
        if highWind == True:
            return 3
        else:
            return 0
        return 0
    return 0

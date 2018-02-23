import modules.timeStamp as timeStamp
import urllib.request, json 
import modules.apiTranslator.Attributes as Attributes

# example for time: "09/02/2018 - 23:01"

def get(coord, time):
    requestUrl = "https://api.darksky.net/forecast/" + Attributes.apiKey + "/" + coord + "," + timeStamp.getTime(time)
    with urllib.request.urlopen(requestUrl) as url:
        data = json.loads(url.read().decode())
        return data

def translate(key, value):
    
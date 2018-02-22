import modules.timeStamp as timeStamp
import urllib.request, json 
import modules.apiTranslator.Attributes as Attributes

def get(coord):
    requestUrl = "https://api.darksky.net/forecast/" + Attributes.apiKey + "/" + coord + "," + timeStamp.getTime("09/02/2018 - 23:01")
    with urllib.request.urlopen(requestUrl) as url:
        data = json.loads(url.read().decode())
        return data


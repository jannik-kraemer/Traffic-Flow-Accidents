from django.shortcuts import render
from modules.apiTranslator import Wheater
from modules import timeStamp
from django.template import Context, Template
from modules.algo import calc
from modules.algo import classification

def get(request):

    # Get all args
    lat1 = request.GET.get('lat1', '')
    lng1 = request.GET.get('lng1', '')
    lat2 = request.GET.get('lat2', '')
    lng2 = request.GET.get('lng2', '')
    date = request.GET.get('date', '')
    time = request.GET.get('time', '')


    # Define options
    opt1 = {}
    opt1['lat'] = lat1
    opt1['lng'] = lng1
    opt2 = {}
    opt2['lat'] = lat2
    opt2['lng'] = lng2

    # Calculate radius for circle
    lat, lng = calc.rad(opt1, opt2)
    # Calculate distance
    radius = calc.distance((lat1, lng1), (lat, lng))

    # Weather
    # Weather.Data = API Request
    wetter = Wheater.Data(str(lat) + "," + str(lng),date + " " + time)

    # sunrise & sunset time
    sunrise = wetter.translate('daily')['data'][0]['sunriseTime']
    sunset = wetter.translate('daily')['data'][0]['sunsetTime']
    
    # Target timestamps
    targetTimeStamp = timeStamp.getTimestamp(date + " " + time)

    # Debug -> 
    # print("Checking values: ")
    # print(Wheater.check(targetTimeStamp, sunrise, sunset))

    # Input to the Prediction module
    dataInput = [[1, int(timeStamp.getDayOfWeek(date)), int(Wheater.check(targetTimeStamp, sunrise, sunset)), 3, 30, 1,  int(Wheater.conditions(str(lat) + "," + str(lng), date + " " + time))]]

    # Return Prediction
    result = classification.prediction(dataInput)
    
    if(result == 3):
        result = "High"
    elif(result == 2):
        result = "Medium"
    else:
        result = "Low"
    # Django VIEW render -> HTML Interface
    return render(request, "index.html", context={"lat": lat, "lng": lng, "lat1": lat1, "lat2": lat2, "lng1": lng1, "lng2": lng2, "radius": radius, "result": result})
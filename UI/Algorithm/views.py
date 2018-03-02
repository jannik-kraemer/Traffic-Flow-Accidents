from django.shortcuts import render
from modules.apiTranslator import Wheater
from modules import timeStamp
from django.template import Context, Template
from modules.algo import calc


def view(request):
    t = Template('This is your <span>{{ message }}</span>.')
    c = Context({'message': 'Your message'})
    html = t.render(c)

def output(request,user):
    print(user)
def get(request):
    lat1 = request.GET.get('lat1', '')
    lng1 = request.GET.get('lng1', '')
    lat2 = request.GET.get('lat2', '')
    lng2 = request.GET.get('lng2', '')
    date = request.GET.get('date', '')
    time = request.GET.get('time', '')

    opt1 = {}
    opt1['lat'] = lat1
    opt1['lng'] = lng1

    opt2 = {}
    opt2['lat'] = lat2
    opt2['lng'] = lng2

    lat, lng = calc.rad(opt1, opt2)
    wetter = Wheater.Data(str(lat) + "," + str(lng),date + " " + time)
    print(wetter.get())
    # print(Wheater.get(lat + "," + lng,date + " " + time))
    # print(timeStamp.getTimeFromTimestamp())

    sunrise = wetter.translate('daily')['data'][0]['sunriseTime']
    sunset = wetter.translate('daily')['data'][0]['sunsetTime']
    targetTimeStamp = timeStamp.getTimestamp(date + " " + time)

    print("Checking values: ")
    print(Wheater.check(targetTimeStamp, sunrise, sunset))

    # c = Context({"lat": lat, "lng": lng})
    return render(request, "index.html", context={"lat": lat, "lng": lng, "lat1": lat1, "lat2": lat2, "lng1": lng1, "lng2": lng2})
from django.shortcuts import render
from modules.apiTranslator import Wheater
from django.template import Context, Template

def view(request):
    t = Template('This is your <span>{{ message }}</span>.')
    c = Context({'message': 'Your message'})
    html = t.render(c)

def output(request,user):
    print(user)
def get(request):
    lat = request.GET.get('lat', '')
    lng = request.GET.get('lng', '')
    print(Wheater.get(lat + "," + lng, "09/02/2018 - 23:01"))
    # c = Context({"lat": lat, "lng": lng})
    return render(request, "index.html", context={"lat": lat, "lng": lng})
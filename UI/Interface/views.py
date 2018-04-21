from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, lat=0, lng=5):
        return render(request, 'index.html', context={"version": "V.1.0"})
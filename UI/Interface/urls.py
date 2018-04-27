from django.conf.urls import url
from Interface import views

urlpatterns = [
    url('', views.HomePageView.as_view())
]
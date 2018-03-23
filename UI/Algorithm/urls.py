from django.conf.urls import url
from Algorithm import views

urlpatterns = [
    url(r'^$', views.get),

]
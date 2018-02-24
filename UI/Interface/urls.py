from django.conf.urls import url
from Interface import views

urlpatterns = [
    url('', views.HomePageView.as_view()),
    url('result<int:lat>&<int:lng>/', views.HomePageView.as_view()),
]
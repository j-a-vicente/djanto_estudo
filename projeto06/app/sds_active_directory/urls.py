from django.urls import path

# Views de lista
from .views import  ad_dashboard




urlpatterns = [
    path('ad_dashboard/',ad_dashboard.as_view() , name='ad_dashboard'),
]
 
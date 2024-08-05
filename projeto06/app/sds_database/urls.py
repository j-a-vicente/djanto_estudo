from django.urls import path

# Views de lista
from .views import  DataBaseList




urlpatterns = [
    path('DataBaseList/',DataBaseList.as_view() , name='DataBaseList'),
]
 
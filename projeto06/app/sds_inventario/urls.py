from django.urls import path

# Views de lista
from .views import  ServerHostList




urlpatterns = [
    path('serverhost_list/',ServerHostList.as_view() , name='serverhost_list'),
]
 
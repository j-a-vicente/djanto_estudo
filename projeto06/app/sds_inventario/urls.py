from django.urls import path

# Views de lista
from .views import  ServerHostList, ServerHostDetalhe




urlpatterns = [
    path('serverhost_list/',ServerHostList.as_view() , name='serverhost_list'),
    path('ServerHostDetalhe/<int:pk>/',ServerHostDetalhe.as_view() , name='ServerHostDetalhe'),
]
 
from django.urls import path

# Views de lista
from .views import  ad_dashboard, ad_group, ad_user




urlpatterns = [
    path('ad_dashboard/',ad_dashboard.as_view() , name='ad_dashboard'),
    path('ad_group/',ad_group.as_view() , name='ad_group'),
    path('ad_user/',ad_user.as_view() , name='ad_user'),
]
 
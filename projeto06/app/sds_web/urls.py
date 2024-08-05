from django.urls import path
from django.contrib.auth import views as auth_views
from .views import view_index


urlpatterns = [
    path('',view_index.as_view() , name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')    
]


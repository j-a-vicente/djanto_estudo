from django.urls import path
from .views import ModuloList, ModuloUpdateView, get_modulo_form
from . import views

urlpatterns = [
    path('moduloList/', ModuloList.as_view(), name='moduloList'),
    path('get-modulo-form/', get_modulo_form, name='get_modulo_form'),
    path('modulo_update/<int:pk>/', views.ModuloUpdateView.as_view(), name='modulo_update'),
]

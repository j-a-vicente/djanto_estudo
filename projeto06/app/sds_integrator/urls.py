from django.urls import path
from .views import ModuloList, get_modulo_form, ModuloDatafontList, get_datafont_form, ModuloDatafontCreateView, ModuloDatafontUpdateView
from . import views

urlpatterns = [
    path('moduloList/', ModuloList.as_view(), name='moduloList'),
    path('get-modulo-form/', get_modulo_form, name='get_modulo_form'),
    path('modulo_update/<int:pk>/', views.ModuloUpdateView.as_view(), name='modulo_update'),
    path('datafont/', ModuloDatafontList.as_view(), name='datafont_list'),
    path('datafont/criar/', ModuloDatafontCreateView.as_view(), name='datafont_create'),
    path('datafont_editar/<int:pk>/', ModuloDatafontUpdateView.as_view(), name='datafont_update'),
    path('datafont/form/', get_datafont_form, name='get_datafont_form'),  
]


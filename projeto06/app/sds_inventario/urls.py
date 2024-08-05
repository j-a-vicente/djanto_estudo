from django.urls import path
from .views import ServerHostList, ServerHostDetalhe

urlpatterns = [
    path('serverhost_list/', ServerHostList.as_view(), name='serverhost_list'),
    path('serverhost_detail/<int:pk>/', ServerHostDetalhe.as_view(), name='serverhost_detail'),  # Nova URL para detalhes
]

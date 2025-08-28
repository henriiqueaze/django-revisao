from django.urls import path
from .views import get_clients, delete_client, restore_client, hard_delete_client

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
    path('clients/<int:pk>/delete/', delete_client, name='delete_client'),
    path('clients/<int:pk>/restore/', restore_client, name='restore_client'),
    path('clients/<int:pk>/hard-delete/', hard_delete_client, name='hard_delete_client'),
]

from django.urls import path
from .views import (
    get_clients, delete_client, restore_client, hard_delete_client,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    order_trash, restore_order, hard_delete_order, ClientCreateView, ClientUpdateView
)

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', delete_client, name='delete_client'),
    path('clients/<int:pk>/restore/', restore_client, name='restore_client'),
    path('clients/<int:pk>/hard-delete/', hard_delete_client, name='hard_delete_client'),

    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('orders/trash/', order_trash, name='order_trash'),
    path('orders/<int:pk>/restore/', restore_order, name='order_restore'),
    path('orders/<int:pk>/hard-delete/', hard_delete_order, name='order_hard_delete'),
]

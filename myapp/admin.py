from django.contrib import admin
from .models import Client, Order

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birth_date', 'is_deleted', 'created_at')
    list_filter = ('is_deleted',)
    search_fields = ('name', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total', 'status', 'is_deleted', 'created_at')
    list_filter = ('status', 'is_deleted')
    search_fields = ('client__name',)

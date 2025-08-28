from django.shortcuts import render, redirect, get_object_or_404
from .models import Client

def get_clients(request):
    clients = Client.objects.all().select_related()
    return render(request, 'clients.html', {'clients': clients})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('get_clients')

def restore_client(request, pk):
    client = get_object_or_404(Client.all_objects, pk=pk)
    client.restore()
    return redirect('get_clients')

def hard_delete_client(request, pk):
    client = get_object_or_404(Client.all_objects, pk=pk)
    client.hard_delete()
    return redirect('get_clients')

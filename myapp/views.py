from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import OrderForm, ClientForm

from .models import Client, Order
from .forms import OrderForm

def get_clients(request):
    clients = Client.objects.all().select_related()
    return render(request, 'clients.html', {'clients': clients})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, "Cliente removido (soft-delete).")
    return redirect('get_clients')

def restore_client(request, pk):
    client = get_object_or_404(Client.all_objects, pk=pk)
    client.restore()
    messages.success(request, "Cliente restaurado.")
    return redirect('get_clients')

def hard_delete_client(request, pk):
    client = get_object_or_404(Client.all_objects, pk=pk)
    client.hard_delete()
    messages.success(request, "Cliente removido permanentemente.")
    return redirect('get_clients')


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        qs = Order.objects.select_related('client').order_by('-created_at')
        status = self.request.GET.get('status')
        q = self.request.GET.get('q')
        client = self.request.GET.get('client')

        if status:
            qs = qs.filter(status=status)
        if client:
            try:
                client_id = int(client)
                qs = qs.filter(client__id=client_id)
            except ValueError:
                pass
        if q:
            qs = qs.filter(
                Q(notes__icontains=q) |
                Q(client__name__icontains=q)
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['status_choices'] = Order.STATUS_CHOICES
        ctx['clients'] = Client.objects.all()
        ctx['q'] = self.request.GET.get('q', '')
        ctx['status_filter'] = self.request.GET.get('status', '')
        ctx['client_filter'] = self.request.GET.get('client', '')
        return ctx


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'

    def get_success_url(self):
        messages.success(self.request, "Order criada com sucesso.")
        return reverse('order_list')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'

    def get_success_url(self):
        messages.success(self.request, "Order atualizada com sucesso.")
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    context_object_name = 'order'

    def get_success_url(self):
        messages.success(self.request, "Order movida para lixeira (soft-delete).")
        return reverse_lazy('order_list')

    def delete(self, request, *args, **kwargs):
        """Use soft-delete (model.delete já faz soft-delete)."""
        obj = self.get_object()
        obj.delete()
        return redirect(self.get_success_url())


def order_trash(request):
    deleted = Order.all_objects.filter(is_deleted=True).select_related('client').order_by('-updated_at')
    return render(request, 'orders/order_trash.html', {'deleted': deleted})

def restore_order(request, pk):
    order = get_object_or_404(Order.all_objects, pk=pk)
    order.restore()
    messages.success(request, "Order restaurada da lixeira.")
    return redirect('order_trash')

def hard_delete_order(request, pk):
    order = get_object_or_404(Order.all_objects, pk=pk)
    order.hard_delete()
    messages.success(request, "Order removida permanentemente.")
    return redirect('order_trash')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('get_clients')

    def form_valid(self, form):
        messages.success(self.request, "Cliente criado com sucesso.")
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'

    def get_success_url(self):
        messages.success(self.request, "Cliente atualizado com sucesso.")
        return reverse('get_clients')

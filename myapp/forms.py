from django import forms
from .models import Order, Client

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'total', 'status', 'notes']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'total': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'birth_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

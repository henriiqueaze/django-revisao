from django import forms
from .models import Order

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

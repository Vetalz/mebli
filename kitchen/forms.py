from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['number_phone', 'budget']
        widgets = {
            'number_phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Ваш бюджет'}),
        }

from django import forms
from .models import Clients_peretyazhka
from django.utils.translation import ugettext_lazy as _


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients_peretyazhka
        fields = ['name', 'number_phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Ваше имя')}),
            'number_phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }
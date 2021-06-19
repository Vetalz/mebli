from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Gallery, Clients
from .forms import ClientsForm
from django.core.mail import send_mass_mail
from django.contrib import messages
from django.conf import settings


def index(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно отправлены')
            form = ClientsForm()
            phone = request.POST.get('number_phone')
            budget = request.POST.get('budget', 0)
            if budget != 0:
                text = f'Телефон: {phone}\nБюджет: {budget}грн\n🤟😎🤟'
            else:
                text = f'Телефон: {phone}\n🤟😎🤟'

            message = ('💲Потенциальный клиент)💲', text, 'vitaly482@gmail.com', settings.EMAIL_TARGET)
            send_mass_mail((message,))
        else:
            messages.error(request, 'Данные не отправлены')
    else:
        form = ClientsForm()

    photos = Gallery.objects.all()
    context = {
        'photos': photos,
        'title': 'Кухни на заказ',
        'form': form,
    }
    return render(request, 'kitchen/index.html', context)


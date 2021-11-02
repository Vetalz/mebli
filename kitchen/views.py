import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Gallery, Clients
from .forms import ClientsForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string


def index(request):
    anchor = None
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            anchor = request.POST.get('form_number')
            form.save()
            messages.success(request, _('Данные успешно отправлены'))
            form = ClientsForm()
            phone = request.POST.get('number_phone')
            budget = request.POST.get('budget')
            if budget:
                text = f'Телефон: {phone}\nБюджет: {budget}грн\n🤟😎🤟'
            else:
                text = f'Телефон: {phone}\n🤟😎🤟'

            email_html = render_to_string('kitchen/email.html', {'title': 'Кухни на заказ', 'phone': phone, 'budget': budget})
            send_mail('💲Потенциальный клиент)💲', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
                      html_message=email_html)
        else:
            messages.error(request, _('Данные не отправлены'))
    else:
        form = ClientsForm()

    photos = Gallery.objects.all()
    context = {
        'photos': photos,
        'title': _('Кухни на заказ'),
        'form': form,
        'anchor': anchor
    }
    return render(request, 'kitchen/index.html', context)


def quiz(request):
    context = {
        'plan': request.POST['plan'],
        'material': request.POST['material'],
        'table': request.POST['table'],
        'fittings': request.POST['fittings'],
        'size': request.POST['size'],
        'phone': request.POST['phone']
    }
    text = 'Заполнен quiz'
    email_html = render_to_string('kitchen/email2.html', context)
    send_mail('💲Потенциальный клиент)💲', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
              html_message=email_html)
    return JsonResponse({'status': 'OK'})

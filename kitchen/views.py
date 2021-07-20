from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Gallery, Clients
from .forms import ClientsForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from blog.models import Article


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
    articles = Article.objects.filter(is_published=True)[:3]
    context = {
        'photos': photos,
        'title': _('Кухни на заказ'),
        'form': form,
        'anchor': anchor,
        'articles': articles
    }
    return render(request, 'kitchen/index.html', context)


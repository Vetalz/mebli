from django.shortcuts import render
from .forms import ClientsForm
from .models import Gallery_peretyazhka, Clients_peretyazhka
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string


def peretyazhka(request):
    anchor = None
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            anchor = request.POST.get('form_number')
            form.save()
            messages.success(request, _('Данные успешно отправлены'))
            form = ClientsForm()
            name = request.POST.get('name')
            phone = request.POST.get('number_phone')
            if name:
                text = f'Имя: {name}\nТелефон: {phone}\n🤟😎🤟'
            else:
                text = f'Телефон: {phone}\n🤟😎🤟'

            email_html = render_to_string('peretyazhka/email_peretyazhka.html',
                                          {'title': 'Перетяжка мебели', 'name': name, 'phone': phone})
            send_mail('💲Потенциальный клиент)💲', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
                      html_message=email_html)
        else:
            messages.error(request, _('Данные не отправлены'))
    else:
        form = ClientsForm()

    photos = Gallery_peretyazhka.objects.all()
    context = {
        'photos': photos,
        'title': _('Перетяжка мебели'),
        'form': form,
        'anchor': anchor
    }
    return render(request, 'peretyazhka/peretyazhka.html', context=context)

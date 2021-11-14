from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForms
from . import services
from django.utils.translation import gettext_lazy as _


def home(request):
    CODE = request.LANGUAGE_CODE
    model = Contact()
    form = ContactForms(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    products = services.get_products(CODE)
    experts = services.get_experts(CODE)
    testimonials = services.get_testimonials(CODE)
    ctx = {
        "products": products,
        "experts": experts,
        "testimonials": testimonials,
        'nav': _("food"),
        'nav1': _("home"),
        'nav2': _("about"),
        'nav3': _("menu"),
        'nav4': _("expert"),
        'nav5': _("testimonial"),
        'nav6': _("contact"),
        'welcome': _('WELCOME_TEXT'),
        'welcome_desc': _('WELCOME_DESC'),
        'title3': _('TITLE_3'),
        'title4': _('TITLE_4'),
        'title5': _('TITLE_5'),
        'title6': _('TITLE_6'),
        'nav2_desc': _('NAV2_DESC'),
        'nav3_desc': _('NAV3_DESC'),
        'nav4_desc': _('NAV4_DESC'),
        'nav5_desc': _('NAV5_DESC'),
        'nav6_desc': _('NAV6_DESC'),
        'send_mess': _('SEND_MESS'),
        'name': _('NAME'),
        'email': _('EMAIL'),
        'send': _('SEND'),
        'message': _('MESSAGE'),
        'rest': _('REST'),
        'all': _('ALL'),
    }
    return render(request, 'restaraunt/index.html', ctx)

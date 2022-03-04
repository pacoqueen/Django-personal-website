# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random

from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Project, Badge

from django.utils.translation import ugettext_lazy as _

from hitcount.views import HitCountDetailView

from django.shortcuts import render

# HTTP Error 404
def custom_page_not_found_view(request, exception):
    return render(request, "mainpage/errors/404.html", {}, status=404)

# HTTP Error 500
def custom_page_server_error(request):
    return render(request, "mainpage/errors/500.html", {}, status=500)

def get_random_background():
    """Devuelve un nombre de fichero de entre los directorios de fondos
    para el banner `action`."""
    static = settings.STATIC_ROOT
    if not static:
        try:
            static = settings.STATICFILES_DIRS[0]
        except IndexError:
            static = os.path.join(settings.PROJECT_ROOT, 'staticfiles')
    bgdir = os.path.join(static, "mainpage", "images", "backgrounds")
    bgs = os.listdir(bgdir)
    res = random.choice(bgs)
    return res

def get_object_for_count(title="qinn.es"):
    """
    hitcount need one object. I will use one that for sure is present
    **in my instace**.
    If not possible, it uses one project. If not projects created, it will fail.
    """
    try:
        proyecto = Project.objects.filter(title=title)[0]
    except IndexError:
        try:
            proyecto = Project.objects.all()[0]
        except IndexError:
            proyecto = None
    return proyecto


class ProjectListBadgesAndFormView(SuccessMessageMixin, ListView, FormView,
                                   HitCountDetailView):
    model = Project # data from database
    template_name = 'mainpage/main.html'
    context_object_name = 'list_projects' # name of the var in html template
    queryset = Project.objects.all().order_by("-pub_date")#  list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/' # After submiting the form keep staying on the same url
    success_message = _('Message successfully submitted!')

    # Needed for hitcount:
    count_hit = True
    object = get_object_for_count("qinn.es")
    # TODO: Can I check from view if analytic cookie consent is accepted?

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            cd['name'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['bogado@qinn.es'],
            fail_silently=False
        )
        return super(ProjectListBadgesAndFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProjectListBadgesAndFormView, self).get_context_data(**kwargs)
        context.update({
            'badges': Badge.objects.order_by("order"),
            'random_bg': get_random_background(),
        })
        return context

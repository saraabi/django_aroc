from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import (Feature, Overview, Page, 
    Staff, Subscriber)

class Home(SuccessMessageMixin, CreateView):
    model = Subscriber
    fields = ('first_name', 'last_name', 'email', 'phone', 
        'category', 'is_subscribed_sms')
    success_message = 'Information Received - Thank You!'
    success_url = reverse_lazy('home')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['overview'] = Overview.objects.first()
        context['features'] = Feature.objects.filter(
            is_active=True)
        context['pages'] = Page.objects.filter(
            is_active=True)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', 
            css_class='btn-primary w-100'))
        return form

class StaffList(ListView):
    model = Staff

class PageDetail(DetailView):
    model = Page

    

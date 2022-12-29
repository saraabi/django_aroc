import json
import urllib

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import (Feature, Overview, Page, 
    Staff, Subscriber)

class RecaptchaMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['captcha_key'] = settings.RECAPTCHA_KEY
        return context
    
    def get_captcha_token(self, form=None):
        if form.cleaned_data.get('recaptcha'):
            return form.cleaned_data.get('recaptcha')
        else:
            return self.request.POST.get('recaptcha')
        
    def validate_captcha(self, recaptcha_response):
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode())

    def get_json_response(self, response):
        return JsonResponse({'data': response})

    def form_valid(self, form):
        result = self.validate_captcha(
            self.get_captcha_token(form)
        )
        if result['success']:
            return super().form_valid(form)
        else:
            form.add_error('email', 'Sorry, an error occurred.\
                Please try again.')
            return self.form_invalid(form)

class Home(SuccessMessageMixin, RecaptchaMixin, CreateView):
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



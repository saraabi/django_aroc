from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import Home, PageDetail, StaffList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', StaffList.as_view(), name='about'),
    path('learn', TemplateView.as_view(
        template_name='learn.html'), name='learn'),
    path('youth', TemplateView.as_view(
        template_name='youth.html'), name='youth'),
    path('page/<slug>', PageDetail.as_view(),
        name='page_detail'),
    # path('subscriber', SubscriberCreate.as_view(), name='subscriber_create'),
]

from django.contrib import admin

from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'category',
    )
    list_display_links = list_display
    list_filter = (
        'category',
        'is_subscribed_sms'
    )
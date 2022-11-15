from django.contrib import admin

from .models import Staff, StaffCategory, Subscriber

admin.site.site_header = 'AROC Web Administration'

@admin.register(StaffCategory)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'order_id',
    )
    list_display_links = list_display

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'category',
    )
    list_display_links = list_display
    list_filter = (
        'category',
    )

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

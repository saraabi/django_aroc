from django.db import models

from django_aroc.storage_backends import PrivateMediaStorage
from django_aroc.storage_backends import PublicMediaStorage

class Overview(models.Model):

    hero_text = models.TextField(blank=True)
    donate_text = models.TextField(blank=True)
    newsletter_text = models.TextField(blank=True)
    quote = models.TextField(blank=True)
    donate_link = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    def __str__(self):
        return 'AROC'

class Subscriber(models.Model):
    CATEGORY_CHOICES = (
        ('community', 'Community'),
        ('donor', 'Donor'),
        ('partner', 'Partner'),
        ('other', 'Other')
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=200,     
        choices=CATEGORY_CHOICES)
    is_subscribed_sms = models.BooleanField(default=False, 
        verbose_name='Subscribe To SMS Alerts')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class StaffCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('order_id',)
        verbose_name_plural = 'staff categories'

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(StaffCategory, on_delete=models.SET_NULL, 
        null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('category',)
        verbose_name_plural = 'staff'

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(storage=PublicMediaStorage(), 
        upload_to='img/', blank=True, null=True)
    is_header_link = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
     
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=10)
    button_text = models.CharField(max_length=40, blank=True)
    image = models.ImageField(storage=PublicMediaStorage(), 
        upload_to='img/', blank=True, null=True)
    page = models.OneToOneField(Page, 
        on_delete=models.SET_NULL, blank=True, null=True)
    url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

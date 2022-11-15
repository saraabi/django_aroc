from django.db import models

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
    is_subscribed_sms = models.BooleanField(default=False, verbose_name='Subscribe To SMS Alerts')

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
    is_header_link = models.BooleanField(default=False)

    def __str__(self):
        return self.name
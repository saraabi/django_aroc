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
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
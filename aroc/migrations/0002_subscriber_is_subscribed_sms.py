# Generated by Django 4.1.3 on 2022-11-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='is_subscribed_sms',
            field=models.BooleanField(default=False),
        ),
    ]

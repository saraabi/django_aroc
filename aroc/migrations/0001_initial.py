# Generated by Django 4.1.3 on 2022-11-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(choices=[('community', 'Community'), ('donor', 'Donor'), ('partner', 'Partner'), ('other', 'Other')], max_length=200)),
            ],
        ),
    ]

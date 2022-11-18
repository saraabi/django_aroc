# Generated by Django 4.1.3 on 2022-11-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroc', '0006_feature_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='quote_author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0007_country_languag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='url',
        ),
        migrations.AddField(
            model_name='country',
            name='url',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-19 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0010_auto_20200519_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='pron',
            new_name='pronounce',
        ),
    ]
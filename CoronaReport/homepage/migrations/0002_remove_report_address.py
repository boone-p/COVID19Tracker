# Generated by Django 3.0.4 on 2020-03-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='address',
        ),
    ]
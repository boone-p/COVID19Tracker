# Generated by Django 3.0.4 on 2020-03-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_report_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='address',
        ),
        migrations.RemoveField(
            model_name='report',
            name='time',
        ),
        migrations.AddField(
            model_name='report',
            name='city',
            field=models.CharField(default='address', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='state',
            field=models.CharField(default='time', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='street',
            field=models.CharField(default='street', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='zipcode',
            field=models.CharField(default='zip', max_length=5),
            preserve_default=False,
        ),
    ]
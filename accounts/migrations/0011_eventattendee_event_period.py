# Generated by Django 3.1.1 on 2020-09-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200915_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendee',
            name='event_period',
            field=models.CharField(choices=[('m', 'Morning'), ('mm', 'Midmorning'), ('a', 'Afternoon')], max_length=50, null=True, verbose_name='Event Period'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-12 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]

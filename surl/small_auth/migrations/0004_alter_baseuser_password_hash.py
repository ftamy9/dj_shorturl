# Generated by Django 4.2.4 on 2023-08-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_auth', '0003_delete_smalltoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='password_hash',
            field=models.CharField(max_length=64),
        ),
    ]

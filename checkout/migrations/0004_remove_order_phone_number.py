# Generated by Django 3.2 on 2022-07-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220720_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]

# Generated by Django 3.2 on 2022-07-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220722_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

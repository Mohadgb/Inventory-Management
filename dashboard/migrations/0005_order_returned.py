# Generated by Django 5.1 on 2024-08-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_order_date_of_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]

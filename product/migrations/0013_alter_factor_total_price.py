# Generated by Django 4.0.6 on 2022-07-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_factor_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='total_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

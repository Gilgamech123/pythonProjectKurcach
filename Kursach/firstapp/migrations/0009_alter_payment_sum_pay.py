# Generated by Django 3.2.8 on 2021-12-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_alter_dogovor_sum_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='sum_pay',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]

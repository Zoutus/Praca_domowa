# Generated by Django 4.2.2 on 2023-06-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0004_alter_measurement_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]

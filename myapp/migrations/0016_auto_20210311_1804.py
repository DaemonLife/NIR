# Generated by Django 3.1.7 on 2021-03-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210311_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер подгруппы'),
        ),
    ]

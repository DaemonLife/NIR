# Generated by Django 3.1.7 on 2021-03-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210311_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_time',
            name='friday',
            field=models.CharField(default=0, max_length=3, verbose_name='Пятница'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_time',
            name='monday',
            field=models.CharField(default=0, max_length=3, verbose_name='Понедельник'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_time',
            name='saturday',
            field=models.CharField(default=0, max_length=3, verbose_name='Суббота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_time',
            name='thursday',
            field=models.CharField(default=0, max_length=3, verbose_name='Четвер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_time',
            name='wednesday',
            field=models.CharField(default=0, max_length=3, verbose_name='Среда'),
            preserve_default=False,
        ),
    ]

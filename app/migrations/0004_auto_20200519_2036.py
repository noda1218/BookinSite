# Generated by Django 2.2.12 on 2020-05-19 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200519_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間'),
        ),
    ]

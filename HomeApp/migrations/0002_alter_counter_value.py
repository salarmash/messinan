# Generated by Django 5.1 on 2024-08-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='value',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='مقدار'),
        ),
    ]

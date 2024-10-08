# Generated by Django 5.1 on 2024-08-19 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=225, verbose_name='زیرعنوان')),
                ('description1', models.TextField(verbose_name='توضیح 1')),
                ('description2', models.TextField(verbose_name='توضیح 2')),
            ],
            options={
                'verbose_name': 'هدر ',
                'verbose_name_plural': 'هدر خدمات',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Service', verbose_name='تصویر پیش نمایش')),
                ('title', models.CharField(max_length=225, verbose_name='عنوان')),
                ('short', models.CharField(max_length=225, verbose_name='پیش نمایش')),
                ('fullImage', models.ImageField(blank=True, null=True, upload_to='Service', verbose_name='تصویر بزرگ')),
                ('description', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': ' مطلب',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=225, verbose_name='عنوان')),
                ('value', models.TextField(verbose_name='متن')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ServiceApp.service')),
            ],
            options={
                'verbose_name': ' آیتم',
                'verbose_name_plural': 'آیتم ها',
            },
        ),
    ]

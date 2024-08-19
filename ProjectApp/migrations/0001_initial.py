# Generated by Django 5.1 on 2024-08-19 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Project', verbose_name='تصویر')),
                ('finalImage', models.ImageField(blank=True, null=True, upload_to='Project', verbose_name='تصویر نهایی')),
                ('description0', models.TextField(verbose_name='متن1')),
                ('description1', models.TextField(verbose_name='متن1')),
                ('description2', models.TextField(verbose_name='متن1')),
                ('description3', models.TextField(verbose_name='متن1')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='ProjectApp.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Project', verbose_name='تصویر')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'گالری',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='لیبل')),
                ('value', models.CharField(max_length=255, verbose_name='مقدار')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'آیتمها',
            },
        ),
    ]

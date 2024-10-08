# Generated by Django 5.1 on 2024-08-19 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام نویسنده')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='تصویر پروفایل')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='تصویر')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('popular', models.BooleanField(default=False)),
                ('content_desc', models.TextField(verbose_name='متن اول')),
                ('content_des2', models.TextField(verbose_name='متن دوم')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='BlogApp.author', verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='BlogApp.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مطلب',
                'verbose_name_plural': 'وبلاگ',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='تصویر')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='BlogApp.blog')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'گالری',
            },
        ),
    ]

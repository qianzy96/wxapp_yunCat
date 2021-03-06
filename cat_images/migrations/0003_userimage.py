# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-29 12:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cat_images', '0002_auto_20170927_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=128, verbose_name='发现地点')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('describe', models.CharField(blank=True, max_length=256, verbose_name='描述')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_update/%Y/%m', verbose_name='图片')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传用户')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('login', models.CharField(max_length=1024)),
                ('avatar_url', models.CharField(max_length=1024)),
                ('html_url', models.CharField(max_length=1024)),
                ('repos_url', models.CharField(max_length=1024)),
                ('followers_url', models.CharField(max_length=1024)),
                ('following_url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=1024)),
                ('full_name', models.CharField(max_length=1024)),
                ('html_url', models.CharField(max_length=1024)),
                ('description', models.CharField(max_length=20000)),
                ('stargazers_count', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=1024)),
                ('forks_count', models.IntegerField(default=0)),
                ('watchers', models.IntegerField(default=0)),
                ('author_id', models.IntegerField(default=0)),
            ],
        ),
    ]
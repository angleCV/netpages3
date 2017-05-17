# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acticle_title', models.CharField(max_length=200)),
                ('article_content', models.CharField(max_length=1000)),
                ('article_img', models.ImageField(upload_to='')),
                ('article_cate', models.IntegerField()),
                ('commit_date', models.DateField(verbose_name='dateCommit')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-28 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartsMainApp', '0006_auto_20180726_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='trick_winner',
            field=models.IntegerField(default=-1),
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartsMainApp', '0002_auto_20180726_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_played',
            field=models.DateField(null=True),
        ),
    ]

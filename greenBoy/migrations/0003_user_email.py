# Generated by Django 2.2.7 on 2019-11-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenBoy', '0002_auto_20191108_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
    ]
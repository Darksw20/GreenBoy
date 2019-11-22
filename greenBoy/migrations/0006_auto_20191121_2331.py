# Generated by Django 2.2.7 on 2019-11-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenBoy', '0005_auto_20191121_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphs',
            name='fk_id_green',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greenBoy.Greenhouse'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

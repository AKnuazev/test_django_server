# Generated by Django 3.0.8 on 2020-07-08 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Организация', '0001_initial'),
        ('Проект', '0003_auto_20200708_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='проект',
            name='заказчик',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Организация.Организация'),
        ),
    ]

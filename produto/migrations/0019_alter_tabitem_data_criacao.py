# Generated by Django 5.0.6 on 2024-09-17 19:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0018_alter_tabitem_data_criacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tabitem",
            name="data_criacao",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Data de Criação"
            ),
        ),
    ]

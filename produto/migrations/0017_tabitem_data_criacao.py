# Generated by Django 5.0.6 on 2024-09-17 18:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0016_tabitem_adicionado_por"),
    ]

    operations = [
        migrations.AddField(
            model_name="tabitem",
            name="data_criacao",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Data de Criação"
            ),
        ),
    ]
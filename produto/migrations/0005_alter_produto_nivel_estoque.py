# Generated by Django 5.0.6 on 2024-07-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0004_alter_produto_nivel_estoque"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="nivel_estoque",
            field=models.BooleanField(verbose_name="Nivel do Estoque"),
        ),
    ]
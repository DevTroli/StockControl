# Generated by Django 5.0.6 on 2024-10-25 10:43

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categoria", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "ordering": ("categoria",),
            },
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nivel_estoque",
                    models.BooleanField(default=False, verbose_name="Nível do Estoque"),
                ),
                (
                    "produto",
                    models.TextField(
                        max_length=100, unique=True, verbose_name="Produto"
                    ),
                ),
                (
                    "preco_custo",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=7,
                        verbose_name="Preço de Custo",
                    ),
                ),
                (
                    "preco_venda",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=7,
                        verbose_name="Preço de Venda",
                    ),
                ),
                (
                    "margem_vendas",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=6,
                        null=True,
                        verbose_name="Margem de Vendas",
                    ),
                ),
                ("estoque", models.IntegerField(verbose_name="Estoque Atual")),
                (
                    "estoque_minimo",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Estoque Mínimo"
                    ),
                ),
                (
                    "codigoBarra",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        null=True,
                        verbose_name="Codigo de Barra",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="produto.categoria",
                    ),
                ),
            ],
        ),
    ]

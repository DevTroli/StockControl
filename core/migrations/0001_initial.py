# Generated by Django 5.0.6 on 2024-10-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TimeStampedModel",
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
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criadoi em:"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-12 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
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
                ("index", models.CharField(max_length=100, verbose_name="Индекс")),
                ("name", models.CharField(max_length=200, verbose_name="Название")),
            ],
            options={
                "ordering": ["index"],
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=127)),
                (
                    "parent",
                    models.ForeignKey(
                        blank="True",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.category",
                    ),
                ),
            ],
        ),
    ]
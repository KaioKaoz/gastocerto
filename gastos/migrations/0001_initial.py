"""
Migration inicial — cria a tabela Gasto.
"""

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gasto",
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
                    "descricao",
                    models.CharField(max_length=200, verbose_name="Descrição"),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Valor (R$)",
                    ),
                ),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("alimentacao", "Alimentação"),
                            ("transporte", "Transporte"),
                            ("saude", "Saúde"),
                            ("educacao", "Educação"),
                            ("lazer", "Lazer"),
                            ("moradia", "Moradia"),
                            ("outros", "Outros"),
                        ],
                        default="outros",
                        max_length=20,
                        verbose_name="Categoria",
                    ),
                ),
                (
                    "data",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Data de registro",
                    ),
                ),
            ],
            options={
                "verbose_name": "Gasto",
                "verbose_name_plural": "Gastos",
                "ordering": ["-data"],
            },
        ),
    ]

"""
Modelos de dados do app gastos.
"""

from django.core.exceptions import ValidationError
from django.db import models


class Categoria(models.TextChoices):
    ALIMENTACAO = "alimentacao", "Alimentação"
    TRANSPORTE = "transporte", "Transporte"
    SAUDE = "saude", "Saúde"
    EDUCACAO = "educacao", "Educação"
    LAZER = "lazer", "Lazer"
    MORADIA = "moradia", "Moradia"
    OUTROS = "outros", "Outros"


class Gasto(models.Model):
    """Representa um gasto pessoal registrado pelo usuário."""

    descricao = models.CharField(
        max_length=200,
        verbose_name="Descrição",
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor (R$)",
    )
    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.OUTROS,
        verbose_name="Categoria",
    )
    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de registro",
    )

    class Meta:
        ordering = ["-data"]
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} [{self.categoria}]"

    def clean(self):
        if self.valor is not None and self.valor <= 0:
            raise ValidationError({"valor": "O valor deve ser maior que zero."})
        if self.descricao and not self.descricao.strip():
            raise ValidationError({"descricao": "A descrição não pode ser vazia."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

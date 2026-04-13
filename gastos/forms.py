"""
Formulários do app gastos.
"""

from django import forms

from .models import Categoria, Gasto


class GastoForm(forms.ModelForm):
    """Formulário para criação e edição de gastos."""

    class Meta:
        model = Gasto
        fields = ["descricao", "valor", "categoria"]
        widgets = {
            "descricao": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: Almoço no trabalho",
                }
            ),
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: 25.50",
                    "step": "0.01",
                    "min": "0.01",
                }
            ),
            "categoria": forms.Select(
                attrs={"class": "form-control"}
            ),
        }
        labels = {
            "descricao": "Descrição",
            "valor": "Valor (R$)",
            "categoria": "Categoria",
        }

    def clean_valor(self):
        valor = self.cleaned_data.get("valor")
        if valor is not None and valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")
        return valor

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao", "").strip()
        if not descricao:
            raise forms.ValidationError("A descrição não pode ser vazia.")
        return descricao


class FiltroForm(forms.Form):
    """Formulário de filtro por categoria na listagem."""

    categoria = forms.ChoiceField(
        choices=[("", "Todas as categorias")] + Categoria.choices,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Filtrar por categoria",
    )

"""
Views do app gastos.
"""

from decimal import Decimal

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FiltroForm, GastoForm
from .models import Categoria, Gasto


def lista_gastos(request):
    """Lista todos os gastos com filtro opcional por categoria."""
    form_filtro = FiltroForm(request.GET or None)
    gastos = Gasto.objects.all()

    categoria_selecionada = ""
    if form_filtro.is_valid():
        categoria_selecionada = form_filtro.cleaned_data.get("categoria", "")
        if categoria_selecionada:
            gastos = gastos.filter(categoria=categoria_selecionada)

    total = gastos.aggregate(total=Sum("valor"))["total"] or Decimal("0.00")

    resumo = (
        Gasto.objects.values("categoria")
        .annotate(subtotal=Sum("valor"))
        .order_by("categoria")
    )
    resumo_dict = {
        Categoria(r["categoria"]).label: r["subtotal"] for r in resumo
    }

    return render(
        request,
        "gastos/lista.html",
        {
            "gastos": gastos,
            "form_filtro": form_filtro,
            "total": total,
            "resumo": resumo_dict,
            "categoria_selecionada": categoria_selecionada,
        },
    )


def adicionar_gasto(request):
    """Exibe o formulário e processa a criação de um novo gasto."""
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_gastos")
    else:
        form = GastoForm()

    return render(request, "gastos/form.html", {"form": form, "titulo": "Adicionar Gasto"})


def editar_gasto(request, pk):
    """Exibe o formulário e processa a edição de um gasto existente."""
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == "POST":
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect("lista_gastos")
    else:
        form = GastoForm(instance=gasto)

    return render(request, "gastos/form.html", {"form": form, "titulo": "Editar Gasto"})


def remover_gasto(request, pk):
    """Exibe confirmação e processa a remoção de um gasto."""
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == "POST":
        gasto.delete()
        return redirect("lista_gastos")

    return render(request, "gastos/confirmar_remocao.html", {"gasto": gasto})
from .services import buscar_cotacoes  # ← nova importação


def lista(request):
    categoria = request.GET.get("categoria", "")
    gastos = Gasto.objects.all()
    if categoria:
        gastos = gastos.filter(categoria=categoria)

    total = sum(g.valor for g in gastos)
    cotacoes = buscar_cotacoes()  # ← nova chamada

    return render(request, "gastos/lista.html", {
        "gastos": gastos,
        "total": total,
        "categoria_filtro": categoria,
        "cotacoes": cotacoes,  # ← passa para o template
    })

# ... resto das views permanecem iguais

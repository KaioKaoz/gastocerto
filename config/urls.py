"""
URLs principais do projeto GastoCerto.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("gastos.urls")),
]

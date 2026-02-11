# -*- coding: utf-8 -*-
"""Dashboard Premium - Ingestão, tratamento e KPIs."""

from .ingestao import carregar_excel
from .tratamento import tratar
from .kpis import (
    calcular_kpis,
    total_por_categoria,
    evolucao_mensal,
    distribuicao_percentual,
    tabela_detalhada,
)

__all__ = [
    "carregar_excel",
    "tratar",
    "calcular_kpis",
    "total_por_categoria",
    "evolucao_mensal",
    "distribuicao_percentual",
    "tabela_detalhada",
]

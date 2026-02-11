# -*- coding: utf-8 -*-
"""Módulo de Ingestão - Lê Excel e normaliza colunas para o dashboard."""

import re
from pathlib import Path
from typing import Any

import pandas as pd

COLUNA_ALIASES = {
    "data": ["data", "date", "dt", "data_emissao", "emissao", "mes"],
    "categoria": ["categoria", "category", "tipo", "grupo", "segmento", "produto"],
    "valor": ["valor", "value", "valor_total", "total", "venda", "receita", "valor_venda"],
    "quantidade": ["quantidade", "qtd", "qty", "quant", "volume"],
}


def _normalizar_nome(nome: str) -> str:
    if not isinstance(nome, str) or pd.isna(nome):
        return "coluna_desconhecida"
    n = str(nome).strip().lower()
    n = re.sub(r"\s+", "_", n)
    n = re.sub(r"[^a-z0-9_]", "", n)
    return n or "coluna_desconhecida"


def _identificar_coluna(nome_norm: str) -> str | None:
    for canonico, aliases in COLUNA_ALIASES.items():
        if nome_norm in aliases:
            return canonico
        if any(nome_norm.startswith(a) or a in nome_norm for a in aliases):
            return canonico
    return None


def carregar_excel(filepath: str | Path) -> pd.DataFrame:
    """Carrega Excel (primeira aba) e normaliza colunas principais."""
    path = Path(filepath)
    df = pd.read_excel(path, engine="openpyxl")
    df.columns = [str(c).strip() for c in df.columns]

    # Normalizar para nomes canônicos
    mapear = {}
    for col in df.columns:
        norm = _normalizar_nome(col)
        canon = _identificar_coluna(norm)
        if canon and canon not in mapear.values():
            mapear[col] = canon

    for orig, nova in mapear.items():
        if orig != nova:
            df = df.rename(columns={orig: nova})

    return df

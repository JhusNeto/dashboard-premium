# -*- coding: utf-8 -*-
"""Módulo de Tratamento - Limpeza e conversões para o dashboard."""

import pandas as pd


def _coluna_valor(df: pd.DataFrame) -> str:
    preferidas = ["valor", "valor_total", "total", "venda", "receita"]
    for p in preferidas:
        if p in df.columns:
            return p
    numericas = df.select_dtypes(include=["number"]).columns.tolist()
    return numericas[0] if numericas else ""


def _coluna_categoria(df: pd.DataFrame) -> str | None:
    for c in ["categoria", "tipo", "grupo", "segmento", "produto"]:
        if c in df.columns:
            return c
    for c in df.columns:
        if df[c].dtype == "object" and df[c].nunique() <= 100:
            return c
    return None


def _coluna_data(df: pd.DataFrame) -> str | None:
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            return c
    for c in ["data", "date", "dt", "emissao", "mes"]:
        if c in df.columns:
            return c
    return None


def tratar(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica tratamento: datas, valores numéricos, remove vazios."""
    df = df.copy()

    # Converter datas
    col_data = _coluna_data(df)
    if col_data:
        df[col_data] = pd.to_datetime(df[col_data], errors="coerce")

    # Converter valores
    col_valor = _coluna_valor(df)
    if col_valor:
        df[col_valor] = df[col_valor].astype(str).str.replace(",", ".", regex=False)
        df[col_valor] = pd.to_numeric(df[col_valor], errors="coerce")

    # Remover linhas sem valor
    if col_valor:
        df = df.dropna(subset=[col_valor])
        df = df[df[col_valor] > 0]

    return df.reset_index(drop=True)

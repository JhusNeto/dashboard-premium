# -*- coding: utf-8 -*-
"""Módulo de KPIs - Cálculos para cards, gráficos e tabela."""

from typing import Any

import pandas as pd


def _coluna_valor(df: pd.DataFrame) -> str:
    for c in ["valor", "valor_total", "total", "venda", "receita"]:
        if c in df.columns:
            return c
    num = df.select_dtypes(include=["number"]).columns
    return num[0] if len(num) else ""


def _coluna_categoria(df: pd.DataFrame) -> str | None:
    for c in ["categoria", "tipo", "grupo", "segmento", "produto"]:
        if c in df.columns:
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


def calcular_kpis(df: pd.DataFrame) -> dict[str, Any]:
    """Retorna KPIs: total_geral, registros, ticket_medio, categoria_lider."""
    col_valor = _coluna_valor(df)
    col_cat = _coluna_categoria(df)
    if not col_valor or df[col_valor].empty:
        return {"total_geral": 0, "registros": 0, "ticket_medio": 0, "categoria_lider": "-"}

    total = float(df[col_valor].sum())
    registros = len(df)
    ticket = total / registros if registros else 0

    cat_lider = "-"
    if col_cat and col_cat in df.columns:
        agrupado = df.groupby(col_cat)[col_valor].sum().sort_values(ascending=False)
        if not agrupado.empty:
            cat_lider = str(agrupado.index[0])

    return {
        "total_geral": round(total, 2),
        "registros": registros,
        "ticket_medio": round(ticket, 2),
        "categoria_lider": cat_lider,
    }


def total_por_categoria(df: pd.DataFrame) -> list[dict[str, Any]]:
    """Retorna lista [{categoria, total, percentual, registros}]."""
    col_valor = _coluna_valor(df)
    col_cat = _coluna_categoria(df)
    if not col_valor:
        return []
    if not col_cat:
        return [{"categoria": "Geral", "total": float(df[col_valor].sum()), "percentual": 100.0, "registros": len(df)}]

    ag = df.groupby(col_cat).agg(
        total=(col_valor, "sum"),
        registros=(col_valor, "count"),
    ).reset_index()
    ag = ag.rename(columns={col_cat: "categoria"})
    total_geral = ag["total"].sum()
    ag["percentual"] = (ag["total"] / total_geral * 100).round(2) if total_geral else 0
    ag = ag.sort_values("total", ascending=False).reset_index(drop=True)

    return ag.to_dict("records")


def evolucao_mensal(df: pd.DataFrame) -> list[dict[str, Any]]:
    """Retorna [{mes_ano, total}] ordenado por data."""
    col_valor = _coluna_valor(df)
    col_data = _coluna_data(df)
    if not col_valor or not col_data:
        return []

    df = df.copy()
    df["_mes_ano"] = pd.to_datetime(df[col_data]).dt.to_period("M").astype(str)
    ag = df.groupby("_mes_ano")[col_valor].sum().reset_index()
    ag = ag.rename(columns={"_mes_ano": "mes_ano", col_valor: "total"})
    ag = ag.sort_values("mes_ano").reset_index(drop=True)
    ag["total"] = ag["total"].round(2)

    return ag.to_dict("records")


def distribuicao_percentual(df: pd.DataFrame) -> list[dict[str, str | float]]:
    """Mesmo que total_por_categoria para Pie chart: [{categoria, percentual}]."""
    lista = total_por_categoria(df)
    return [{"categoria": x["categoria"], "percentual": x["percentual"]} for x in lista]


def tabela_detalhada(df: pd.DataFrame) -> list[dict[str, Any]]:
    """Retorna registros para tabela (top 100 ou todos)."""
    col_valor = _coluna_valor(df)
    col_cat = _coluna_categoria(df)
    col_data = _coluna_data(df)

    cols = [c for c in [col_cat, col_data, col_valor] if c and c in df.columns]
    if not cols:
        return []

    sub = df[cols].head(100).copy()
    sub[col_valor] = sub[col_valor].round(2)
    sub = sub.rename(columns={col_cat: "categoria", col_valor: "valor", col_data: "data"})
    if "data" in sub.columns and pd.api.types.is_datetime64_any_dtype(sub["data"]):
        sub["data"] = sub["data"].dt.strftime("%Y-%m-%d")
    return sub.to_dict("records")

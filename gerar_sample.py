#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera sample_input.xlsx para demonstração do dashboard."""
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent

def main():
    categorias = ["Varejo", "Atacado", "E-commerce", "Serviços", "Outros"]
    base = datetime(2024, 1, 1)
    rows = []
    for i in range(150):
        data = base + timedelta(days=random.randint(0, 300))
        cat = random.choice(categorias)
        valor = round(random.uniform(80, 4500), 2)
        rows.append({"Data": data, "Categoria": cat, "Valor": valor})
    df = pd.DataFrame(rows)
    out = ROOT / "sample_input.xlsx"
    df.to_excel(out, index=False, sheet_name="Vendas")
    print("Gerado:", out)

if __name__ == "__main__":
    main()

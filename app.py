#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard Premium - Web app com upload de Excel, KPIs e gráficos.
Uso: python app.py
"""

import json
import os
from pathlib import Path

from flask import Flask, render_template, request, jsonify, session, redirect, url_for

from src.ingestao import carregar_excel
from src.tratamento import tratar
from src.kpis import (
    calcular_kpis,
    total_por_categoria,
    evolucao_mensal,
    distribuicao_percentual,
    tabela_detalhada,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dashboard-premium-dev")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.route("/")
def index():
    """Página de upload."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Processa Excel e retorna JSON com KPIs, gráficos e tabela."""
    if "file" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"erro": "Arquivo não selecionado"}), 400

    if not file.filename.lower().endswith((".xlsx", ".xls")):
        return jsonify({"erro": "Use arquivo Excel (.xlsx ou .xls)"}), 400

    try:
        path = UPLOAD_FOLDER / file.filename
        file.save(path)
        df = carregar_excel(path)
        df = tratar(df)

        if df.empty:
            return jsonify({"erro": "Planilha vazia ou sem dados válidos"}), 400

        resultado = {
            "kpis": calcular_kpis(df),
            "total_por_categoria": total_por_categoria(df),
            "evolucao_mensal": evolucao_mensal(df),
            "distribuicao_percentual": distribuicao_percentual(df),
            "tabela": tabela_detalhada(df),
        }
        session["dashboard_data"] = resultado
        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/dashboard")
def dashboard():
    """Página do dashboard com gráficos."""
    data = session.get("dashboard_data")
    if not data:
        return redirect(url_for("index"))
    return render_template("dashboard.html", data=json.dumps(data))


if __name__ == "__main__":
    app.run(debug=True, port=5000)

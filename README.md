# Dashboard Premium

Web app profissional com upload de Excel, KPIs, gráficos interativos (Chart.js) e tabela detalhada. Layout moderno com Bootstrap e CSS customizado.

## Funcionalidades

- Upload de planilha Excel (.xlsx, .xls)
- Tratamento automático de dados (datas, valores, categorias)
- KPIs: Total geral, Registros, Ticket médio, Categoria líder
- Gráficos: Bar (por categoria), Line (evolução mensal), Pie (distribuição)
- Tabela responsiva com os dados

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Acesse: http://localhost:5000

## Estrutura

```
dashboard-premium/
├── app.py
├── requirements.txt
├── sample_input.xlsx
├── static/
│   ├── css/styles.css
│   └── js/charts.js
├── templates/
├── src/
│   ├── ingestao.py
│   ├── tratamento.py
│   └── kpis.py
└── assets/
```

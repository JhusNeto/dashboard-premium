# 📈 Dashboard Premium (Python + Flask + Chart.js)

Web App profissional para análise de planilhas: KPIs, gráficos interativos e tabela detalhada.

## 📌 Visão Geral

Este projeto demonstra como criar um dashboard corporativo completo usando apenas Python e tecnologias web leves.
A aplicação permite que o usuário:

- faça upload de uma planilha Excel
- tenha seus dados automaticamente tratados
- visualize KPIs essenciais
- veja gráficos interativos
- explore uma tabela completa

É exatamente o tipo de solução contratada em plataformas como Workana, Upwork e 99Freelas, para áreas como:

- Financeiro
- Comercial
- Operações
- BI/Analytics
- Marketing
- Gerentes que precisam de dashboards rápidos e sob medida

## 🚀 Principais Recursos

### ✓ 1. Upload de planilhas Excel (.xlsx/.xls)

Campos esperados:

- **data**
- **categoria**
- **valor**

A aplicação normaliza:

- formatos de data
- valores numéricos
- categorias inconsistentes

### ✓ 2. KPIs automáticos

Exibidos como cards modernos:

- Total Geral
- Registros
- Ticket Médio
- Categoria Líder

### ✓ 3. Gráficos Interativos (Chart.js)

- **Bar chart** – Total por categoria
- **Pie chart** – Distribuição percentual
- **Line chart** – Evolução mensal

Todos os gráficos são responsivos e atualizados dinamicamente.

### ✓ 4. Tabela Responsiva Detalhada

Com:

- categoria
- total
- percentual
- quantidade/registros (opcional)

Tabela estilizada com Bootstrap.

### ✓ 5. Design Moderno e Profissional

- Layout baseado em Bootstrap 5
- Navbar fixa com título + botão de upload
- Cards com sombra suave
- Paleta premium:
  - Azul escuro (#1e3a5f)
  - Azul médio (#2a6fb0)
  - Cinza (#e5e7eb, #6b7280)
  - Branco (#ffffff)
- CSS custom com espaçamentos e responsividade

## 🧠 Arquitetura do Projeto

```
dashboard-premium/
│
├── app.py                      # App Flask principal
├── requirements.txt
├── sample_input.xlsx           # Planilha de exemplo
│
├── static/
│   ├── css/styles.css          # Estilo customizado
│   └── js/charts.js            # Configuração dos gráficos
│
├── templates/
│   ├── layout.html             # Layout base
│   ├── index.html              # Tela de upload
│   └── dashboard.html          # Dashboard final
│
├── src/
│   ├── ingestao.py             # Leitura e normalização
│   ├── tratamento.py           # Limpeza e cálculos
│   └── kpis.py                 # Lógica dos KPIs
│
└── assets/                     # Prints e GIF do projeto
```

## 💻 Execução Local

**Instalar dependências**
```bash
pip install -r requirements.txt
```

**Rodar o app**
```bash
python app.py
```

Acesse: **http://localhost:5000**

## 📁 Arquivo de Exemplo

O repositório inclui:

- **sample_input.xlsx** (planilha de demonstração)

Faça o upload e o dashboard será gerado instantaneamente.

## 🔖 Tecnologias

- Python
- Flask
- Pandas
- Chart.js
- Bootstrap 5
- HTML/CSS/JS

## 📄 Licença

Livre para uso e adaptação em projetos comerciais.

/**
 * Dashboard Premium - Gráficos Chart.js
 */
var DashboardCharts = (function() {
  var barChart, pieChart, lineChart;

  function formatCurrency(val) {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(val || 0);
  }

  function renderKPIs(kpis) {
    var container = document.getElementById('kpiCards');
    if (!container) return;
    container.innerHTML = [
      { label: 'Total Geral', value: formatCurrency(kpis.total_geral), col: 3 },
      { label: 'Registros', value: kpis.registros.toLocaleString('pt-BR'), col: 3 },
      { label: 'Ticket Médio', value: formatCurrency(kpis.ticket_medio), col: 3 },
      { label: 'Categoria Líder', value: kpis.categoria_lider, col: 3 }
    ].map(function(k) {
      return '<div class="col-6 col-lg-' + k.col + '"><div class="kpi-card"><div class="kpi-value">' + k.value + '</div><div class="kpi-label">' + k.label + '</div></div></div>';
    }).join('');
  }

  function renderBar(data) {
    var ctx = document.getElementById('chartBar');
    if (!ctx) return;
    var labels = data.map(function(d) { return d.categoria; });
    var values = data.map(function(d) { return d.total; });
    var colors = ['#1e3a5f', '#2a6fb0', '#4a8fce', '#6ba8e8', '#8fc4f0', '#b3d9f7'];
    barChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Total',
          data: values,
          backgroundColor: labels.map(function(_, i) { return colors[i % colors.length]; })
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  }

  function renderPie(data) {
    var ctx = document.getElementById('chartPie');
    if (!ctx) return;
    var labels = data.map(function(d) { return d.categoria; });
    var values = data.map(function(d) { return d.percentual; });
    var colors = ['#1e3a5f', '#2a6fb0', '#4a8fce', '#6ba8e8', '#8fc4f0', '#b3d9f7', '#d4ebfa'];
    pieChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: values,
          backgroundColor: labels.map(function(_, i) { return colors[i % colors.length]; })
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: 'right' } }
      }
    });
  }

  function renderLine(data) {
    var ctx = document.getElementById('chartLine');
    if (!ctx) return;
    var labels = data.map(function(d) { return d.mes_ano; });
    var values = data.map(function(d) { return d.total; });
    lineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Total',
          data: values,
          borderColor: '#2a6fb0',
          backgroundColor: 'rgba(42, 111, 176, 0.1)',
          fill: true,
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  }

  function renderTable(tabela) {
    var thead = document.getElementById('tableHead');
    var tbody = document.getElementById('tableBody');
    if (!thead || !tbody || !tabela.length) return;
    var cols = Object.keys(tabela[0]);
    thead.innerHTML = '<tr>' + cols.map(function(c) { return '<th>' + c + '</th>'; }).join('') + '</tr>';
    tbody.innerHTML = tabela.map(function(row) {
      return '<tr>' + cols.map(function(col) {
        var v = row[col];
        if (typeof v === 'number') v = v.toLocaleString('pt-BR');
        if (v && typeof v === 'string' && v.match(/^\d{4}-\d{2}/)) v = v.slice(0, 10);
        return '<td>' + (v ?? '') + '</td>';
      }).join('') + '</tr>';
    }).join('');
  }

  return {
    init: function(data) {
      if (!data) return;
      renderKPIs(data.kpis || {});
      renderBar(data.total_por_categoria || []);
      renderPie(data.distribuicao_percentual || []);
      renderLine(data.evolucao_mensal || []);
      renderTable(data.tabela || []);
    }
  };
})();

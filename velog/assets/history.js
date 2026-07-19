(function () {
  "use strict";
  var charter = window.Cheongrok;
  var colors = ["#087865", "#428f7d", "#7a6ba6", "#c07945", "#b85c68", "#64864b", "#497eaa", "#8d6b42", "#536d68"];

  async function load() {
    try {
      var response = await fetch("/api/records");
      if (!response.ok) throw new Error();
      var records = await response.json();
      records.sort(function (a, b) { return (a.date || "").localeCompare(b.date || ""); });
      renderSummary(records);
      renderTrend(records);
      renderMatrix(records);
      renderArchive(records);
    } catch (error) {
      ["trend-chart", "matrix", "all-records"].forEach(function (id) { document.getElementById(id).innerHTML = '<p class="empty error-text">서버에 연결할 수 없습니다. <code>python server.py</code>를 실행해 주세요.</p>'; });
    }
  }

  function rankOf(record, id) {
    var found = (record.ranking || []).find(function (item) { return item.id === id; });
    return found ? Number(found.rank) : null;
  }

  function renderSummary(records) {
    var latest = records[records.length - 1];
    var averages = charter.items.map(function (item) {
      var ranks = records.map(function (record) { return rankOf(record, item.id); }).filter(Boolean);
      return { name: item.name, value: ranks.length ? ranks.reduce(function (a, b) { return a + b; }, 0) / ranks.length : 99 };
    }).sort(function (a, b) { return a.value - b.value; });
    var values = [
      ["누적 기록", records.length + "건"],
      ["최근 기록", latest ? charter.formatDate(latest.date).replace(/\. /g, ".") : "—"],
      ["일관된 강점", records.length ? averages[0].name : "—"],
      ["다음 점검", records.length ? averages[averages.length - 1].name : "—"]
    ];
    document.getElementById("summary-grid").innerHTML = values.map(function (value) { return '<div class="summary-item"><span>' + value[0] + '</span><strong>' + charter.escapeHtml(value[1]) + '</strong></div>'; }).join("");
  }

  function renderTrend(records) {
    var container = document.getElementById("trend-chart");
    var legend = document.getElementById("chart-legend");
    if (!records.length) { container.innerHTML = '<p class="empty">아직 분석할 기록이 없습니다.</p>'; legend.innerHTML = ""; return; }
    var width = Math.max(760, records.length * 86 + 110), height = 330, left = 48, right = 25, top = 20, bottom = 45;
    var x = function (index) { return records.length === 1 ? width / 2 : left + index * (width - left - right) / (records.length - 1); };
    var y = function (rank) { return top + (rank - 1) * (height - top - bottom) / 8; };
    var svg = '<svg class="trend-svg" viewBox="0 0 ' + width + ' ' + height + '" role="img" aria-label="기준별 순위 변화 선 그래프">';
    for (var rank = 1; rank <= 9; rank++) svg += '<line x1="' + left + '" y1="' + y(rank) + '" x2="' + (width - right) + '" y2="' + y(rank) + '" stroke="#e2e8e3"/><text x="12" y="' + (y(rank) + 4) + '">' + rank + '위</text>';
    records.forEach(function (record, index) { svg += '<text x="' + x(index) + '" y="' + (height - 12) + '" text-anchor="middle">' + charter.escapeHtml((record.date || "").slice(5)) + '</text>'; });
    charter.items.forEach(function (item, itemIndex) {
      var points = records.map(function (record, index) { var rank = rankOf(record, item.id); return rank ? x(index) + "," + y(rank) : null; }).filter(Boolean);
      if (points.length > 1) svg += '<polyline points="' + points.join(" ") + '" fill="none" stroke="' + colors[itemIndex] + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>';
      records.forEach(function (record, index) { var rank = rankOf(record, item.id); if (rank) svg += '<circle cx="' + x(index) + '" cy="' + y(rank) + '" r="3" fill="' + colors[itemIndex] + '"><title>' + charter.escapeHtml(item.name + " " + rank + "위") + '</title></circle>'; });
    });
    container.innerHTML = svg + "</svg>";
    legend.innerHTML = charter.items.map(function (item, index) { return '<span class="legend-item"><i class="legend-line" style="background:' + colors[index] + '"></i>' + charter.escapeHtml(item.name) + '</span>'; }).join("");
  }

  function renderMatrix(records) {
    var recent = records.slice(-8);
    if (!recent.length) { document.getElementById("matrix").innerHTML = '<p class="empty">아직 분석할 기록이 없습니다.</p>'; return; }
    var head = recent.map(function (record) { return "<th>" + charter.escapeHtml((record.date || "").slice(5)) + "</th>"; }).join("");
    var body = charter.items.map(function (item) {
      var cells = recent.map(function (record) { var rank = rankOf(record, item.id); return '<td>' + (rank ? '<span class="rank-cell ' + (rank <= 5 ? "good" : "") + '">' + rank + '</span>' : "—") + '</td>'; }).join("");
      return "<tr><td>" + charter.escapeHtml(item.name) + "</td>" + cells + "</tr>";
    }).join("");
    document.getElementById("matrix").innerHTML = "<table><thead><tr><th>기준</th>" + head + "</tr></thead><tbody>" + body + "</tbody></table>";
  }

  function renderArchive(records) {
    var container = document.getElementById("all-records");
    if (!records.length) { container.innerHTML = '<p class="empty">아직 저장된 기록이 없습니다.</p>'; return; }
    container.innerHTML = records.slice().reverse().map(function (record) {
      return '<article class="record-row"><time datetime="' + charter.escapeHtml(record.date) + '">' + charter.formatDate(record.date) + '</time><div><h3>' + charter.escapeHtml(record.title || "제목 없는 기록") + '</h3><div class="chips">' + charter.rankingChips(record.ranking) + '</div>' + (record.note ? '<p class="record-note">' + charter.escapeHtml(record.note) + '</p>' : '') + '</div></article>';
    }).join("");
  }
  load();
})();

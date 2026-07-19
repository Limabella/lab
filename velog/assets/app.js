(function () {
  "use strict";

  var charter = window.Cheongrok;
  var order = charter.items.map(function (item) { return item.id; });
  var draggedIndex = null;
  var list = document.getElementById("ranking-list");
  var form = document.getElementById("record-form");

  function itemById(id) { return charter.items.find(function (item) { return item.id === id; }); }

  function move(from, to) {
    if (to < 0 || to >= order.length || from === to) return;
    order.splice(to, 0, order.splice(from, 1)[0]);
    renderRanking();
    var target = list.querySelector('[data-index="' + to + '"]');
    if (target) target.focus();
  }

  function renderRanking() {
    list.innerHTML = "";
    order.forEach(function (id, index) {
      if (index === 5) {
        var divider = document.createElement("div");
        divider.className = "rank-divider";
        divider.innerHTML = "<span>강점</span><i></i><span>개선할 기준</span>";
        list.appendChild(divider);
      }
      var item = itemById(id);
      var row = document.createElement("article");
      row.className = "rank-row " + (index < 5 ? "strong" : "improve");
      row.draggable = true;
      row.tabIndex = 0;
      row.dataset.index = index;
      row.setAttribute("aria-label", (index + 1) + "위 " + item.name);
      row.innerHTML =
        '<span class="drag-grip" aria-hidden="true">⠿</span>' +
        '<span class="rank-number">' + String(index + 1).padStart(2, "0") + '</span>' +
        '<div class="rank-copy"><strong>' + charter.escapeHtml(item.name) + '</strong><p>' + charter.escapeHtml(item.desc) + '</p></div>' +
        '<span class="zone-badge">' + (index < 5 ? "강점" : "개선") + '</span>' +
        '<div class="rank-actions"><button type="button" data-direction="up" aria-label="' + charter.escapeHtml(item.name) + ' 위로 이동">↑</button><button type="button" data-direction="down" aria-label="' + charter.escapeHtml(item.name) + ' 아래로 이동">↓</button></div>';
      row.querySelector('[data-direction="up"]').disabled = index === 0;
      row.querySelector('[data-direction="down"]').disabled = index === order.length - 1;
      list.appendChild(row);
    });
  }

  list.addEventListener("click", function (event) {
    var button = event.target.closest("button[data-direction]");
    if (!button) return;
    var row = button.closest(".rank-row");
    var from = Number(row.dataset.index);
    move(from, button.dataset.direction === "up" ? from - 1 : from + 1);
  });
  list.addEventListener("keydown", function (event) {
    var row = event.target.closest(".rank-row");
    if (!row || !event.altKey || (event.key !== "ArrowUp" && event.key !== "ArrowDown")) return;
    event.preventDefault();
    var from = Number(row.dataset.index);
    move(from, event.key === "ArrowUp" ? from - 1 : from + 1);
  });
  list.addEventListener("dragstart", function (event) {
    var row = event.target.closest(".rank-row");
    if (!row) return;
    draggedIndex = Number(row.dataset.index);
    row.classList.add("dragging");
    event.dataTransfer.effectAllowed = "move";
  });
  list.addEventListener("dragover", function (event) {
    var row = event.target.closest(".rank-row");
    if (!row) return;
    event.preventDefault();
    list.querySelectorAll(".drag-over").forEach(function (el) { el.classList.remove("drag-over"); });
    row.classList.add("drag-over");
  });
  list.addEventListener("drop", function (event) {
    var row = event.target.closest(".rank-row");
    event.preventDefault();
    if (row && draggedIndex !== null) move(draggedIndex, Number(row.dataset.index));
    clearDrag();
  });
  list.addEventListener("dragend", clearDrag);

  function clearDrag() {
    list.querySelectorAll(".dragging,.drag-over").forEach(function (el) { el.classList.remove("dragging", "drag-over"); });
    draggedIndex = null;
  }

  function setStatus(message, type) {
    var status = document.getElementById("status");
    status.textContent = message;
    status.className = "status visible " + type;
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    var date = document.getElementById("rec-date").value;
    var title = document.getElementById("rec-title").value.trim();
    var note = document.getElementById("rec-note").value.trim();
    var button = document.getElementById("btn-save");
    var ranking = order.map(function (id, index) {
      return { rank: index + 1, id: id, name: itemById(id).name, zone: index < 5 ? "good" : "bad" };
    });
    button.disabled = true;
    button.textContent = "저장하는 중…";
    try {
      var response = await fetch("/api/records", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ date: date, title: title, note: note, ranking: ranking, savedAt: new Date().toISOString() }) });
      var result = await response.json();
      if (!response.ok || !result.ok) throw new Error(result.error || "저장 실패");
      setStatus("저장했습니다. 누적 기록 " + result.total + "건", "success");
      loadRecent();
    } catch (error) {
      setStatus(error.message === "Failed to fetch" ? "서버에 연결할 수 없습니다. python server.py를 실행해 주세요." : error.message, "error");
    } finally {
      button.disabled = false;
      button.textContent = "평가 기록 저장";
    }
  });

  document.getElementById("btn-reset").addEventListener("click", function () {
    order = charter.items.map(function (item) { return item.id; });
    renderRanking();
    setStatus("기본 순서로 되돌렸습니다.", "neutral");
  });

  async function loadRecent() {
    var container = document.getElementById("recent-records");
    try {
      var response = await fetch("/api/records");
      if (!response.ok) throw new Error();
      var records = await response.json();
      if (!records.length) { container.innerHTML = '<p class="empty">아직 저장된 기록이 없습니다. 첫 평가를 남겨 보세요.</p>'; return; }
      container.innerHTML = records.slice().sort(function (a, b) { return (b.date || "").localeCompare(a.date || ""); }).slice(0, 4).map(recordHtml).join("");
    } catch (error) {
      container.innerHTML = '<p class="empty error-text">서버에 연결할 수 없습니다. <code>python server.py</code>를 실행해 주세요.</p>';
    }
  }

  function recordHtml(record) {
    return '<article class="record-row"><time datetime="' + charter.escapeHtml(record.date) + '">' + charter.formatDate(record.date) + '</time><div><h3>' + charter.escapeHtml(record.title || "제목 없는 기록") + '</h3><div class="chips">' + charter.rankingChips(record.ranking) + '</div>' + (record.note ? '<p class="record-note">' + charter.escapeHtml(record.note) + '</p>' : '') + '</div></article>';
  }

  var now = new Date();
  document.getElementById("rec-date").value = now.getFullYear() + "-" + String(now.getMonth() + 1).padStart(2, "0") + "-" + String(now.getDate()).padStart(2, "0");
  renderRanking();
  loadRecent();
})();

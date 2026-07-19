(function () {
  "use strict";

  var items = [
    { id: "structure", name: "글 구조", desc: "연구형 65% · 개발형 30% · 블로그형 5%" },
    { id: "logic", name: "논리의 흐름", desc: "요약 · 문제 제기 · 원인 분석 · 해결의 연결" },
    { id: "ai", name: "AI 활용 방식", desc: "맥락 없는 붙여넣기 없이 검증하고 재구성" },
    { id: "data", name: "정량적 데이터화", desc: "시각화와 수치로 판단의 근거를 제시" },
    { id: "tone", name: "감정 균형", desc: "긍정 · 중립 · 비판을 상황에 맞게 조율" },
    { id: "problem", name: "문제의식", desc: "사회적 연결과 현실의 맥락을 반영" },
    { id: "politics", name: "정치성 절제", desc: "대통령 · 정당 중심의 분석은 필요한 만큼만" },
    { id: "engineering", name: "공학적 구현", desc: "사회적 관찰을 실제 작동하는 해법으로 연결" },
    { id: "citation", name: "인용과 출처", desc: "APA 방식과 적정한 인용 비중을 유지" }
  ];

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function formatDate(value) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(value || "")) return value || "날짜 없음";
    var parts = value.split("-");
    return parts[0] + ". " + parts[1] + ". " + parts[2] + ".";
  }

  function rankingChips(ranking) {
    return (ranking || []).map(function (item) {
      var zone = item.zone === "good" || Number(item.rank) <= 5 ? "good" : "improve";
      return '<span class="chip ' + zone + '">' + escapeHtml(item.rank) + '. ' + escapeHtml(item.name) + '</span>';
    }).join("");
  }

  window.Cheongrok = { items: items, escapeHtml: escapeHtml, formatDate: formatDate, rankingChips: rankingChips };
})();

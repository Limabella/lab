# Cheongrok charter and storage contract

## Writing model

- Structure each post as observation → analysis → implementation.
- Aim for research 65%, development 30%, and blog narrative 5%.
- Prefer evidence and context over intuition and trend-following.
- Verify AI output, citations, numbers, images, and code before incorporating them.

## Nine evaluation criteria

| ID | Criterion | Review focus |
| --- | --- | --- |
| `structure` | 글 구조 | Research/development/blog balance and visible three-part flow |
| `logic` | 논리의 흐름 | Summary → problem → cause → solution continuity |
| `ai` | AI 활용 방식 | Verification and authorial reconstruction instead of pasted output |
| `data` | 정량적 데이터화 | Data, measurements, and visualization supporting claims |
| `tone` | 감정 균형 | Appropriate balance of positive, neutral, and critical language |
| `problem` | 문제의식 | Connection to real and social context |
| `politics` | 정치성 절제 | Political framing used only when analytically necessary |
| `engineering` | 공학적 구현 | Reproducible implementation connected to observation |
| `citation` | 인용과 출처 | Primary sources, APA-style attribution, and proportionate quotation |

Ranks 1–5 are current strengths. Ranks 6–9 are priorities for the next post.

## Record contract

`records.json` contains an array. A record uses:

```json
{
  "date": "YYYY-MM-DD",
  "title": "optional title, maximum 120 characters",
  "note": "optional review memo, maximum 3000 characters",
  "ranking": [
    { "rank": 1, "id": "structure", "name": "글 구조", "zone": "good" }
  ],
  "savedAt": "ISO-8601 timestamp"
}
```

Require all nine unique IDs and ranks 1–9. The server replaces an existing record with the same date and writes `note/YYYY/YYYY-MM-DD.md`. Legacy records may omit `note`; render them without failure.

## Pre-review checklist

- Identify the problem and intended reader.
- Plan the observation, analysis, and implementation sequence.
- Gather primary sources and quantitative evidence.
- Define reproducible implementation conditions and limitations.

## Post-review checklist

- Verify logical continuity and factual support.
- Verify all sources and AI-assisted content.
- Confirm social context connects to implementation.
- Reduce unsupported emotional or political claims.
- Identify one or more actions for the next post.

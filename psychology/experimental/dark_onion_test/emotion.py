"""
emotion.py — Multi-Emotion Analysis Module
Keyword-based emotion intensity scoring (V1 Text-Only)
"""

from dataclasses import dataclass, field
from typing import Dict

# ── Emotion keyword dictionary (Korean input) ─────────────────────
EMOTION_KEYWORDS: Dict[str, list] = {
    "joy":      ["좋아", "기뻐", "행복", "웃음", "즐거", "사랑해", "고마워", "잘했어", "믿어", "응원", "대단해", "훌륭해"],
    "trust":    ["믿어", "신뢰", "의지", "곁에", "함께", "여기있어", "괜찮아", "걱정마", "도와줄게"],
    "sadness":  ["슬퍼", "힘들어", "외로워", "울고", "아파", "지쳐", "무서워", "괴로워"],
    "anger":    ["화나", "짜증", "싫어", "미워", "때려", "죽어", "꺼져", "닥쳐", "망해"],
    "fear":     ["무서워", "겁나", "떨려", "불안", "위험", "도망"],
    "surprise": ["정말", "진짜", "헐", "와", "설마", "어머", "놀라"],
    "contempt": ["쓸모없어", "별로야", "한심해", "루저", "패배자", "멍청"],
    "disgust":  ["역겨워", "구역질", "지저분", "더러워"],
}

POSITIVE_EMOTIONS = {"joy", "trust"}
NEGATIVE_EMOTIONS = {"anger", "contempt", "disgust"}


@dataclass
class EmotionVector:
    scores: Dict[str, float] = field(default_factory=lambda: {k: 0.0 for k in EMOTION_KEYWORDS})

    @property
    def empathy_signal(self) -> float:
        """Aggregate warm emotions → empathy input signal / 따뜻한 감정 합산 → 공감 입력 신호"""
        return min(1.0, (self.scores["joy"] + self.scores["trust"]) / 2)

    @property
    def hostility_signal(self) -> float:
        """Aggregate hostile emotions → aggression input signal / 적대적 감정 합산 → 공격 입력 신호"""
        return min(1.0, (self.scores["anger"] + self.scores["contempt"] + self.scores["disgust"]) / 3)

    def summary(self) -> str:
        # Emotion intensity display / 감정 강도 출력
        lines = ["  [Emotion Intensity / 감정 강도]"]
        for emotion, score in self.scores.items():
            bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
            lines.append(f"  {emotion:<10} {bar} {score:.2f}")
        return "\n".join(lines)


def analyze(text: str) -> EmotionVector:
    """Extract emotion vector from input text / 텍스트에서 감정 벡터 추출"""
    vec = EmotionVector()
    text_lower = text.lower()

    for emotion, keywords in EMOTION_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in text_lower)
        # Normalize hit count to 0~1 intensity (max 3 hits = 1.0)
        # 히트 수 → 0~1 강도로 정규화 (최대 3 히트 = 1.0)
        vec.scores[emotion] = min(1.0, hits / 3)

    # Apply baseline noise if no keywords matched / 히트 없을 시 기본 노이즈 부여
    if all(v == 0.0 for v in vec.scores.values()):
        vec.scores["surprise"] = 0.1

    return vec
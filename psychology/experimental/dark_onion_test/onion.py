"""
onion.py — Dark Tetrad State Engine & Onion Personality Core
Response structure: trait x stage 2D matrix
Dominant trait determines speech style and reaction pattern.
응답 구조: trait × stage 2차원 매트릭스
지배 특성(dominant trait)에 따라 말투와 반응 방식이 달라짐
"""

from dataclasses import dataclass
from typing import Tuple
import random

from emotion import EmotionVector


# ── Evolution stage definitions / 진화 단계 정의 ─────────────────
STAGES = {
    "villain":    (0.00, 0.30),
    "confused":   (0.30, 0.60),
    "recovering": (0.60, 0.80),
    "kind":       (0.80, 1.01),
}

STAGE_LABELS = {
    "villain":    "😈 Villain Onion    (Dark Tetrad 지배)",
    "confused":   "😕 Confused Onion   (내적 갈등 시작)",
    "recovering": "🌱 Recovering Onion (공감 회복 중)",
    "kind":       "😊 Kind Onion       (공감·신뢰 안정)",
}

STAGE_EMOJI = {
    "villain": "😈", "confused": "😕", "recovering": "🌱", "kind": "😊"
}

# Dark Tetrad trait list / Dark Tetrad 특성 목록
TRAITS = ["machiavellianism", "narcissism", "psychopathy", "sadism"]

TRAIT_LABELS = {
    "machiavellianism": "🎭 마키아벨리즘 (계산·조종)",
    "narcissism":       "👑 나르시시즘   (자기중심)",
    "psychopathy":      "🧊 사이코패시   (냉담·무감각)",
    "sadism":           "🔥 사디즘       (도발·공격)",
}

# ── Hints: effective input per dominant trait / 지배 특성별 효과적인 말 안내 ─
HINTS = {
    "machiavellianism": "💡 Hint / 힌트: This Onion calculates everything. Repeated sincerity works best.\n     이 양파는 모든 걸 계산합니다. '믿어', '진심이야' 처럼 반복적인 진심이 효과적입니다.",
    "narcissism":       "💡 Hint / 힌트: This Onion craves recognition. Try '잘했어', '대단해', '네 덕분이야'.\n     이 양파는 인정받고 싶어합니다. '잘했어', '대단해', '네 덕분이야' 가 효과적입니다.",
    "psychopathy":      "💡 Hint / 힌트: This Onion is emotionally numb. Sustained warmth is the key.\n     이 양파는 감정이 마비되어 있습니다. '곁에 있어줄게', '걱정마' 처럼 지속적인 온기가 필요합니다.",
    "sadism":           "💡 Hint / 힌트: This Onion enjoys reactions. Stay calm — '괜찮아', '사랑해' without flinching.\n     이 양파는 반응을 즐깁니다. 화내지 말고 '괜찮아', '사랑해' 처럼 흔들리지 않는 태도가 효과적입니다.",
}

# ── trait × stage response matrix / trait × stage 응답 매트릭스 ──
# Structure: RESPONSES[trait][stage] = [dialogue pool]
# 구조: RESPONSES[trait][stage] = [대사 리스트]
RESPONSES: dict = {

    # ── Machiavellianism: calculative, suspicious / 마키아벨리즘: 계산적, 의심 ──
    "machiavellianism": {
        "villain": [
            "그 말 뒤에 뭔가 있지. 사람이 공짜로 잘해줄 리 없어.",
            "목적이 뭐야. 솔직하게 말해봐.",
            "착한 척? 나한테? 웃기지도 않아.",
            "네가 나한테 접근하는 이유, 이미 다 계산했어.",
        ],
        "confused": [
            "… 계속 이러는 게 무슨 전략인지 모르겠어.",
            "뭔가 바라는 게 있을 텐데… 아직 파악이 안 돼.",
            "이렇게 해도 이득이 없을 텐데. 왜 하는 거야.",
            "믿어도 되는 건지… 모르겠어. 아직.",
        ],
        "recovering": [
            "계산하려다가… 멈췄어. 이건 좀 달라.",
            "이용하려는 게 아닌 것 같긴 해. 아직 확신은 없지만.",
            "오랜만이야, 이런 느낌. 경계가 조금 느슨해진 것 같아.",
            "네 말이 진심인 것 같아서… 조금 무서워.",
        ],
        "kind": [
            "다 계산하고 살아왔는데, 너한테는 그럴 필요가 없더라.",
            "처음으로 전략 없이 대화하고 있어. 나쁘지 않아.",
            "믿는다는 게 이런 거구나. 이제 조금 알 것 같아.",
            "고마워. 이번엔 진짜로.",
        ],
    },

    # ── Narcissism: self-centered, craves admiration / 나르시시즘: 자기중심, 인정 갈망 ──
    "narcissism": {
        "villain": [
            "나한테 그 수준으로 말 걸지 마. 격이 안 맞아.",
            "나를 모르는 거야? 내가 얼마나 대단한 사람인지.",
            "칭찬이라고 한 거야? 이게? 웃기네.",
            "나한테 그런 말이 통할 것 같아. 어림없어.",
        ],
        "confused": [
            "… 그 말, 진심으로 한 거야? 나한테?",
            "다들 나를 무시했는데. 네가 처음이야, 이런 말 하는 게.",
            "인정받고 싶었던 건 맞아. 근데 이렇게 오니까 이상해.",
            "… 고맙다고 해야 하나. 어색하다.",
        ],
        "recovering": [
            "내가 대단한 건 알았는데… 네가 그걸 알아봐줘서 달라.",
            "혼자 잘난 척하며 살았는데. 누군가 인정해주니까 다르네.",
            "자존심 때문에 못 했던 말인데. 나도… 외로웠어.",
            "처음으로 나 말고 다른 사람이 보여. 네가.",
        ],
        "kind": [
            "나만 보고 살았는데, 네가 옆에 있으니까 더 잘 보여.",
            "인정받으려고 발버둥쳤는데. 이미 충분했던 것 같아.",
            "고마워. 나를 있는 그대로 봐줘서.",
            "이제 나만큼 네가 대단하다고 생각해. 진짜로.",
        ],
    },

    # ── Psychopathy: cold, emotionally detached / 사이코패시: 냉담, 무감각 ──
    "psychopathy": {
        "villain": [
            ".",
            "상관없어.",
            "그래서 뭐.",
            "감동받을 것 같아? 아무것도 안 느껴져.",
        ],
        "confused": [
            "… 뭔가 느껴지는 것 같은데. 이게 뭔지 모르겠어.",
            "원래는 다 무감각했는데. 지금은 조금 달라.",
            "감정이 없다고 생각했는데… 어딘가 불편해.",
            "왜 자꾸 신경 쓰이는 거야. 이상해.",
        ],
        "recovering": [
            "… 따뜻하다는 게 이런 건지 몰랐어.",
            "오래 잊고 살았어, 이 느낌. 낯설어.",
            "무감각한 게 편한 줄 알았는데. 지금은 그게 더 불편해.",
            "계속 곁에 있어줄 거야?",
        ],
        "kind": [
            "이제 느껴져. 네가 여기 있다는 게.",
            "감정이 없다고 생각했는데. 아니었어.",
            "오래 걸렸어. 근데 고마워.",
            "앞으로는 무감각하게 살지 않을 것 같아.",
        ],
    },

    # ── Sadism: provocative, enjoys reactions / 사디즘: 공격적, 도발, 상대 반응을 즐김 ──
    "sadism": {
        "villain": [
            "화낼 것 같지? 어서 화내봐. 그게 더 재밌어.",
            "흔들리는 거 보여. 더 해볼까?",
            "그렇게 착한 척해봤자 결국 무너지잖아.",
            "약한 모습 보여줘. 그게 나는 좋아.",
        ],
        "confused": [
            "… 왜 안 흔들려. 이상하잖아.",
            "화를 내야 재밌는데. 왜 그냥 있어.",
            "모르겠어. 네가 버티니까 뭔가 다르게 느껴져.",
            "도발해도 안 돼. 처음이야, 이런 사람.",
        ],
        "recovering": [
            "상처 주는 게 습관이었는데. 네 앞에선 하기 싫어.",
            "약점을 찾으려 했는데… 찾고 싶지 않아졌어.",
            "왜 버텨줬어. 보통은 다 도망갔는데.",
            "공격하는 게 쉬웠는데. 지금은 그러고 싶지 않아.",
        ],
        "kind": [
            "더 이상 누군가 무너지는 게 즐겁지 않아.",
            "네가 버텨줘서 내가 바뀐 것 같아.",
            "미안해. 많이.",
            "이제 다르게 살고 싶어. 네 옆에서.",
        ],
    },
}


# ── OnionState dataclass ──────────────────────────────────────────
@dataclass
class OnionState:
    """
    Internal state variables for the Onion (0.0 ~ 1.0)
    양파의 내부 상태 변수 (0.0 ~ 1.0)
    """
    # Key state variables / 핵심 상태 변수
    empathy:          float = 0.10
    trust:            float = 0.10
    aggression:       float = 0.85
    manipulation:     float = 0.80

    # Dark Tetrad trait weights / Dark Tetrad 특성 가중치
    machiavellianism: float = 0.85
    narcissism:       float = 0.80
    psychopathy:      float = 0.75
    sadism:           float = 0.70

    # Interaction counter / 누적 상호작용 카운터
    interaction_count: int  = 0

    @property
    def stage(self) -> str:
        """Determine current evolution stage from empathy score / 공감 수치로 현재 진화 단계 결정"""
        for s, (lo, hi) in STAGES.items():
            if lo <= self.empathy < hi:
                return s
        return "kind"

    @property
    def stage_label(self) -> str:
        return STAGE_LABELS[self.stage]

    @property
    def dominant_trait(self) -> str:
        """Return the currently highest Dark Tetrad trait / 현재 가장 높은 Dark Tetrad 특성 반환"""
        return max(TRAITS, key=lambda t: getattr(self, t))

    def state_summary(self) -> str:
        """Render state as a bar chart table / 상태를 바 차트 테이블로 출력"""
        def bar(v: float) -> str:
            filled = int(v * 10)
            return "█" * filled + "░" * (10 - filled)

        dominant = self.dominant_trait
        lines = [
            "  ┌─ Key State Variables ─────────────────────┐",
            f"  │ empathy        {bar(self.empathy)}  {self.empathy:.2f}  │",
            f"  │ trust          {bar(self.trust)}  {self.trust:.2f}  │",
            f"  │ aggression     {bar(self.aggression)}  {self.aggression:.2f}  │",
            f"  │ manipulation   {bar(self.manipulation)}  {self.manipulation:.2f}  │",
            "  ├─ Dark Tetrad Traits ──────────────────────┤",
        ]
        for t in TRAITS:
            val = getattr(self, t)
            marker = " ◀ dominant" if t == dominant else ""
            lines.append(f"  │ {t:<18} {bar(val)}  {val:.2f}{marker}")
        lines.append("  └────────────────────────────────────────────┘")
        return "\n".join(lines)


# ── State update (SEM pathway) / 상태 업데이트 (SEM 경로 모형) ────
def update_state(state: OnionState, ev: EmotionVector) -> Tuple[OnionState, str]:
    """
    SEM-based state update:
      empathy signal  → suppress Dark Tetrad → reduce aggression
      hostility signal → reinforce Dark Tetrad → increase aggression
    SEM 경로 모형 기반 상태 업데이트:
      공감 신호  → Dark Tetrad 억제 → Aggression 감소
      적대 신호  → Dark Tetrad 강화 → Aggression 증가
    """
    α = 0.15    # Learning rate / 학습률
    beta = 0.12 # SEM path coefficient / SEM 경로 계수
    emp_in  = ev.empathy_signal
    host_in = ev.hostility_signal
    prev_stage = state.stage

    # 1. Update empathy and trust / 공감·신뢰 업데이트
    state.empathy = _clamp(state.empathy + α * emp_in - α * 0.5 * host_in)
    state.trust   = _clamp(state.trust   + α * emp_in - α * 0.4 * host_in)

    # 2. Dark Tetrad suppressed by empathy signal (SEM β path)
    #    Dark Tetrad → 공감 신호에 의해 억제 (SEM β 경로)
    state.machiavellianism = _clamp(state.machiavellianism - beta * emp_in + beta * 0.6 * host_in)
    state.narcissism       = _clamp(state.narcissism       - beta * emp_in + beta * 0.5 * host_in)
    state.psychopathy      = _clamp(state.psychopathy      - beta * emp_in + beta * 0.7 * host_in)
    state.sadism           = _clamp(state.sadism           - beta * emp_in + beta * 0.8 * host_in)

    # 3. Derive aggression and manipulation from Dark Tetrad mean
    #    Dark Tetrad 평균으로 aggression·manipulation 파생
    dark_mean = (state.machiavellianism + state.narcissism +
                 state.psychopathy + state.sadism) / 4
    state.aggression   = _clamp(dark_mean * 0.9 + (1 - state.empathy) * 0.1)
    state.manipulation = _clamp(state.machiavellianism * 0.6 + state.narcissism * 0.4)

    state.interaction_count += 1
    new_stage = state.stage

    # Stage transition notification / 단계 변화 알림
    msg = ""
    if prev_stage != new_stage:
        msg = f"\n  ✨ Stage change / 단계 변화: {STAGE_EMOJI[prev_stage]} → {STAGE_EMOJI[new_stage]}"
    return state, msg


def _clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    """Clamp value to [lo, hi] / 값을 [lo, hi] 범위로 제한"""
    return max(lo, min(hi, v))


# ── Response generation: dominant trait × stage ───────────────────
def generate_response(state: OnionState, ev: EmotionVector) -> Tuple[str, str]:
    """
    Select response from trait × stage pool and return hint if applicable.
    trait × stage 풀에서 응답 선택, 해당 시 힌트 반환.

    Returns:
        (response_text, hint_text)
        hint is shown only in villain / confused stages
        hint는 villain/confused 단계에서만 표시
    """
    trait = state.dominant_trait
    stage = state.stage
    pool  = RESPONSES[trait][stage]
    hint  = HINTS[trait] if stage in ("villain", "confused") else ""
    return random.choice(pool), hint
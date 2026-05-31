"""
app.py — Dark Onion Research Simulator (V1 Text-Only)
Run / 실행: python app.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from emotion import analyze
from onion import OnionState, update_state, generate_response, STAGE_EMOJI, TRAIT_LABELS
from save_manager import save, load

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║        🧅 Dark Onion Research Simulator  v1.0               ║
║   A Text-Based Personality Rehabilitation Prototype          ║
║   Use warm words to evolve the Onion into Kind Onion.        ║
║   따뜻한 말로 양파를 Kind Onion으로 진화시켜 보세요.          ║
╠══════════════════════════════════════════════════════════════╣
║  Commands / 명령어:  /status  /reset  /save  /load  /quit   ║
╚══════════════════════════════════════════════════════════════╝
"""

HELP_EXAMPLES = """
  💡 Example inputs / 예시 입력:
     "잘했어, 믿어."           → joy + trust signal
     "고마워, 곁에 있어줘."    → trust signal
     "응원해, 사랑해."         → joy signal
     "꺼져, 싫어."             → anger signal (Dark Tetrad reinforced / Dark Tetrad 강화)
"""


def print_turn(state: OnionState, ev, response: str, hint: str, stage_change: str) -> None:
    print("\n" + "─" * 64)
    print(ev.summary())
    print()
    print(state.state_summary())
    print()
    # Current stage and dominant trait display / 현재 단계 및 지배 특성 출력
    print(f"  Current Stage / 현재 단계:   {state.stage_label}")
    print(f"  Dominant Trait / 지배 특성:  {TRAIT_LABELS[state.dominant_trait]}")
    if stage_change:
        print(stage_change)
    print()
    print(f"  🧅 Onion: \"{response}\"")
    if hint:
        print(f"\n  {hint}")
    print("─" * 64)


def run() -> None:
    print(BANNER)
    print(HELP_EXAMPLES)

    # Session selection: new or resume / 새 세션 or 이어하기 선택
    choice = input("  New game / 새 게임 (n)  |  Load session / 이전 세션 불러오기 (l)  [n/l]: ").strip().lower()
    state = load() if choice == "l" else OnionState()

    print(f"\n  Starting stage / 시작 단계: {state.stage_label}\n")

    while True:
        try:
            user_input = input("  You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Exiting / 종료합니다.")
            break

        if not user_input:
            continue

        # ── Command handler / 명령어 처리 ────────────────────────
        if user_input == "/quit":
            print("  Exiting / 종료합니다.")
            break

        elif user_input == "/status":
            print(f"\n  Current stage / 현재 단계: {state.stage_label}")
            print(state.state_summary())
            print(f"  Total interactions / 누적 상호작용: {state.interaction_count}\n")
            continue

        elif user_input == "/reset":
            state = OnionState()
            print("  🔄 Reset complete / 초기화 완료 (Villain Onion으로 재시작)\n")
            continue

        elif user_input == "/save":
            save(state)
            continue

        elif user_input == "/load":
            state = load()
            print(f"  Current stage / 현재 단계: {state.stage_label}\n")
            continue

        # ── Normal input processing / 일반 입력 처리 ─────────────
        ev = analyze(user_input)
        state, stage_change = update_state(state, ev)
        response, hint = generate_response(state, ev)
        print_turn(state, ev, response, hint, stage_change)

        # Ending condition: full recovery / Kind Onion 도달 시 엔딩
        if state.stage == "kind" and state.empathy >= 0.95:
            print("\n  🎉 Ending: The Onion has fully recovered! / 엔딩: 양파가 완전히 회복되었습니다!")
            print("  Kind Onion: \"이제 괜찮아. 네 덕분이야.\"\n")
            save(state)
            break


if __name__ == "__main__":
    run()

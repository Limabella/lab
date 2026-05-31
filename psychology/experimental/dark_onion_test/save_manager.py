"""
save_manager.py — Session State Save / Load Manager
세션 상태 저장 / 불러오기
"""

import json
import os
from dataclasses import asdict
from onion import OnionState

SAVE_PATH = os.path.join(os.path.dirname(__file__), "data", "onion_save.json")


def save(state: OnionState) -> None:
    """Persist current state to JSON / 현재 상태를 JSON으로 저장"""
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(asdict(state), f, ensure_ascii=False, indent=2)
    print(f"Saved / 저장 완료: {SAVE_PATH}")


def load() -> OnionState:
    """Load state from JSON, return fresh state if no save found / JSON에서 상태 불러오기, 없으면 초기 상태 반환"""
    if not os.path.exists(SAVE_PATH):
        return OnionState()
    with open(SAVE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("Previous session loaded / 이전 세션 불러오기 완료")
    return OnionState(**data)
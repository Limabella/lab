#!/usr/bin/env python3
"""청록 헌장 평가 일지용 로컬 서버.

실행: python server.py
접속: http://localhost:8081
"""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "records.json"
NOTE_DIR = ROOT / "note"
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ITEM_IDS = {
    "structure", "logic", "ai", "data", "tone",
    "problem", "politics", "engineering", "citation",
}


def configured_port() -> int:
    value = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PORT", "8081")
    try:
        port = int(value)
    except ValueError as exc:
        raise SystemExit(f"Port must be a number: {value}") from exc
    if not 1 <= port <= 65535:
        raise SystemExit(f"Port must be between 1 and 65535: {port}")
    return port


def load_records() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"기록 파일을 읽을 수 없습니다: {exc}") from exc
    if not isinstance(data, list):
        raise RuntimeError("records.json의 최상위 값은 배열이어야 합니다.")
    return data


def save_records(records: list[dict]) -> None:
    """같은 폴더의 임시 파일에 쓴 뒤 교체해 중간 저장 손상을 막는다."""
    handle, temporary_name = tempfile.mkstemp(
        dir=ROOT, prefix="records-", suffix=".tmp", text=True
    )
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary_name, DATA_FILE)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def markdown_text(record: dict) -> str:
    """평가 레코드를 사람이 읽고 편집하기 쉬운 Markdown으로 변환한다."""
    title = record.get("title") or "제목 없는 기록"
    safe_title = str(title).replace("\r", " ").replace("\n", " ")
    ranking = sorted(record.get("ranking", []), key=lambda item: item.get("rank", 99))
    strengths = [item for item in ranking if item.get("zone") == "good" or item.get("rank", 99) <= 5]
    improvements = [item for item in ranking if item not in strengths]

    def lines(items: list[dict]) -> str:
        return "\n".join(
            f"- {item.get('rank')}위 · {item.get('name', item.get('id', ''))}"
            for item in items
        ) or "- 없음"

    note = str(record.get("note", "")).strip() or "아직 작성된 검토 메모가 없습니다."
    return (
        "---\n"
        f"date: {record['date']}\n"
        f'title: "{safe_title.replace(chr(34), chr(92) + chr(34))}"\n'
        f"savedAt: {record.get('savedAt', '')}\n"
        "source: cheongrok-evaluation\n"
        "---\n\n"
        f"# {safe_title}\n\n"
        "## 검토 메모\n\n"
        f"{note}\n\n"
        "## 잘 지킨 기준\n\n"
        f"{lines(strengths)}\n\n"
        "## 다음 글에서 개선할 기준\n\n"
        f"{lines(improvements)}\n\n"
        "## 다음 행동\n\n"
        "- [ ] 관찰 → 분석 → 구현의 연결을 다시 확인한다.\n"
        "- [ ] 수치와 인용의 출처를 검증한다.\n"
        "- [ ] 개선 기준을 다음 글의 작성 계획에 반영한다.\n"
    )


def save_note(record: dict) -> Path:
    """날짜를 키로 연도별 Markdown 노트를 원자적으로 저장한다."""
    year_dir = NOTE_DIR / record["date"][:4]
    year_dir.mkdir(parents=True, exist_ok=True)
    destination = year_dir / f"{record['date']}.md"
    handle, temporary_name = tempfile.mkstemp(
        dir=year_dir, prefix=f"{record['date']}-", suffix=".tmp", text=True
    )
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as file:
            file.write(markdown_text(record))
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary_name, destination)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)
    return destination


def validate_record(body: object) -> dict:
    if not isinstance(body, dict):
        raise ValueError("요청 본문은 객체여야 합니다.")
    date = body.get("date")
    title = body.get("title", "")
    note = body.get("note", "")
    ranking = body.get("ranking")
    if not isinstance(date, str) or not DATE_PATTERN.fullmatch(date):
        raise ValueError("날짜는 YYYY-MM-DD 형식이어야 합니다.")
    if not isinstance(title, str) or len(title) > 120:
        raise ValueError("제목은 120자 이하여야 합니다.")
    if not isinstance(note, str) or len(note) > 3000:
        raise ValueError("검토 메모는 3000자 이하여야 합니다.")
    if not isinstance(ranking, list) or len(ranking) != len(ITEM_IDS):
        raise ValueError("평가 기준 9개의 순위가 필요합니다.")
    ids = {item.get("id") for item in ranking if isinstance(item, dict)}
    ranks = {item.get("rank") for item in ranking if isinstance(item, dict)}
    if ids != ITEM_IDS or ranks != set(range(1, 10)):
        raise ValueError("평가 기준 또는 순위가 올바르지 않습니다.")
    return {
        "date": date,
        "title": title.strip(),
        "note": note.strip(),
        "ranking": ranking,
        "savedAt": body.get("savedAt", ""),
    }


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"  {self.address_string()}  {fmt % args}")

    def do_GET(self) -> None:
        if urlparse(self.path).path == "/api/records":
            try:
                self.send_json(load_records())
            except RuntimeError as exc:
                self.send_json({"ok": False, "error": str(exc)}, status=500)
            return
        super().do_GET()

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/records":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 100_000:
                raise ValueError("요청 크기가 올바르지 않습니다.")
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            record = validate_record(body)
            records = load_records()
            index = next(
                (i for i, item in enumerate(records) if item.get("date") == record["date"]),
                None,
            )
            if index is None:
                records.append(record)
            else:
                records[index] = record
            save_records(records)
            note_path = save_note(record)
            self.send_json({
                "ok": True,
                "total": len(records),
                "note": str(note_path.relative_to(ROOT)).replace("\\", "/"),
            })
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self.send_json({"ok": False, "error": str(exc)}, status=400)
        except RuntimeError as exc:
            self.send_json({"ok": False, "error": str(exc)}, status=500)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Allow", "GET, POST, OPTIONS")
        self.end_headers()

    def send_json(self, data: object, status: int = 200) -> None:
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    os.chdir(ROOT)
    port = configured_port()
    server = ThreadingHTTPServer(("localhost", port), Handler)
    print("\n  [ready] 청록 헌장 평가 일지")
    print(f"    http://localhost:{port}")
    print(f"    기록 파일: {DATA_FILE}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  서버를 종료합니다.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

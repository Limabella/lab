#!/usr/bin/env python3
"""
청록 헌장 평가 일지 — 로컬 서버
실행: python server.py
접속: http://localhost:8000
"""
import json, os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "records.json")


def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_records(records):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"  {self.address_string()}  {fmt % args}")

    def do_GET(self):
        if urlparse(self.path).path == "/api/records":
            self._json(load_records())
        else:
            super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path == "/api/records":
            length = int(self.headers.get("Content-Length", 0))
            body   = json.loads(self.rfile.read(length))
            recs   = load_records()
            date   = body.get("date", "")
            idx    = next((i for i, r in enumerate(recs) if r.get("date") == date), -1)
            if idx >= 0:
                recs[idx] = body
            else:
                recs.append(body)
            save_records(recs)
            self._json({"ok": True, "total": len(recs)})
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors(); self.end_headers()

    def _json(self, data):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self._cors(); self.end_headers()
        self.wfile.write(payload)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")


if __name__ == "__main__":
    # server.py 위치(velog/)로 CWD 고정
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ← 이 줄 추가

    port   = port = 8081
    server = HTTPServer(("localhost", port), Handler)
    print(f"\n  ✓  청록 헌장 평가 일지")
    print(f"     http://localhost:{port}")
    print(f"     데이터 저장 위치: {DATA_FILE}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  서버 종료 (Ctrl+C)")

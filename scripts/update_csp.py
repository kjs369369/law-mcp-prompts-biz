"""index.html의 인라인 JavaScript 변경 후 CSP 해시를 갱신합니다."""
import base64
import hashlib
import re
from pathlib import Path

page = Path(__file__).resolve().parents[1] / 'index.html'
html = page.read_text(encoding='utf-8')
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
if len(scripts) != 1:
    raise ValueError('인라인 스크립트 1개를 기대합니다. CSP 정책을 검토하세요.')
digest = base64.b64encode(hashlib.sha256(scripts[0].encode()).digest()).decode()
html, count = re.subn(r"script-src 'sha256-[^']+'", f"script-src 'sha256-{digest}'", html)
if count != 1:
    raise ValueError('CSP script-src 정책 1개를 기대합니다.')
page.write_text(html, encoding='utf-8')
print('CSP script hash updated')

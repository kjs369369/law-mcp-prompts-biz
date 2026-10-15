# -*- coding: utf-8 -*-
"""기존 ink/cream/gold 팔레트의 1200×630 공유 이미지. Python + Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
INK, PAPER, CREAM, GOLD = '#1A1A1A', '#FFFFFF', '#F5F0E8', '#C9A961'


def font(size, bold=False):
    """운영체제별 한글 글꼴을 찾고, 없으면 깨진 이미지 대신 오류를 반환."""
    candidates = [
        (Path('C:/Windows/Fonts') / ('malgunbd.ttf' if bold else 'malgun.ttf'), 0),
        (Path('/System/Library/Fonts/AppleSDGothicNeo.ttc'), 6 if bold else 4),
        (Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if bold else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'), 1),
    ]
    for path, index in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size, index=index)
    raise FileNotFoundError('한글 글꼴이 필요합니다: 맑은 고딕, Apple SD Gothic Neo 또는 Noto Sans CJK')


def main():
    img = Image.new('RGB', (1200, 630), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((900, 0, 1200, 630), fill=CREAM)
    d.rectangle((0, 0, 1200, 8), fill=GOLD)
    d.text((64, 62), 'SERIES 2 · 사업 운영과 산업안전 실무', font=font(24, True), fill=GOLD)
    d.text((64, 120), '법령 MCP', font=font(64, True), fill=INK)
    d.text((64, 202), '실무 프롬프트 60선', font=font(64, True), fill=INK)
    d.rectangle((64, 300, 830, 303), fill=INK)
    d.text((64, 330), '1인기업 · 강사 · 프리랜서 · 소상공인', font=font(27), fill=INK)
    d.text((64, 375), '안전관리 담당자 · 산업안전기업 업무 20종 추가', font=font(27, True), fill=INK)
    d.text((64, 440), '안전관리 체계  /  현장 위험관리', font=font(24), fill=INK)
    d.text((64, 480), '보건·사고대응  /  컨설팅·계약·결과보고', font=font(24), fill=INK)
    d.text((64, 572), '메이랜드AI비즈랩 & AICLab · 김진수 소장', font=font(22), fill='#555555')
    d.text((931, 162), '60', font=font(160, True), fill=GOLD)
    d.text((946, 355), 'PROMPTS', font=font(31, True), fill=INK)
    d.rectangle((947, 411, 1147, 414), fill=INK)
    d.text((947, 439), '12개 분야', font=font(27, True), fill=INK)
    d.text((947, 486), '사례 · 검색 · 복사', font=font(22), fill=INK)
    out = BASE / 'og-image.png'
    img.save(out, 'PNG', optimize=True)
    print(f'saved: {out.name} (1200×630)')


if __name__ == '__main__':
    main()

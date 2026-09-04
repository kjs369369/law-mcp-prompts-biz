# -*- coding: utf-8 -*-
"""
OG 이미지(1200x630) 생성 — 법령 MCP 실무 프롬프트 40선 (시리즈 2)
index.html 의 ink/cream/gold 미니멀 팔레트 적용

사용법: python make_og.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
W, H = 1200, 630

# index.html :root 변수와 동일
INK = (26, 26, 26)        # --ink   #1A1A1A
PAPER = (255, 255, 255)   # --paper
CREAM = (245, 240, 232)   # --cream #F5F0E8
GOLD = (201, 169, 97)     # --gold  #C9A961
MUTED = (138, 138, 138)   # --muted #8A8A8A
RULE = (229, 229, 229)    # --rule  #E5E5E5
BODY = (85, 85, 85)

FONTS = Path("C:/Windows/Fonts")


def font(name, size):
    for cand in (FONTS / name,
                 Path("/usr/share/fonts/truetype/noto") / name,
                 Path("/usr/share/fonts/opentype/noto") / name):
        if cand.exists():
            return ImageFont.truetype(str(cand), size)
    return ImageFont.load_default()


f_black = lambda s: font("NotoSansKR-Black.ttf", s)
f_bold = lambda s: font("NotoSansKR-Bold.ttf", s)
f_med = lambda s: font("NotoSansKR-Medium.ttf", s)
f_reg = lambda s: font("NotoSansKR-Regular.ttf", s)


def text_w(d, s, fnt):
    return d.textbbox((0, 0), s, font=fnt)[2]


def chip_row(d, items, x0, y, fsize=19, h=44):
    """크림 배경 칩을 한 줄로 그린다. 마지막 x 좌표를 반환."""
    fnt = f_bold(fsize)
    x = x0
    for label in items:
        w = text_w(d, label, fnt) + 34
        d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2,
                            fill=CREAM, outline=RULE, width=1)
        d.text((x + 17, y + (h - fsize) // 2 - 3), label, font=fnt, fill=INK)
        x += w + 10
    return x


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # 우측 크림 블록
    d.rectangle([W - 300, 0, W, H], fill=CREAM)
    # 상단 골드 라인
    d.rectangle([0, 0, W, 8], fill=GOLD)

    L = 76  # 좌측 여백

    # eyebrow
    d.text((L, 84), "SERIES 2 · 1인기업 · 강사 · 프리랜서 · 소상공인",
           font=f_bold(23), fill=GOLD)

    # 타이틀
    d.text((L, 134), "법령 MCP 실무 프롬프트", font=f_black(62), fill=INK)
    y2 = 214
    d.text((L, y2), "40선", font=f_black(62), fill=GOLD)
    d.rectangle([L, y2 + 92, L + 560, y2 + 95], fill=INK)

    # 설명
    d.text((L, 344), "법무팀이 없는 사람을 위한 프롬프트 모음.",
           font=f_reg(26), fill=BODY)
    d.text((L, 380), "AI가 국가법령정보(법제처)를 직접 조회하게 만든 뒤 씁니다.",
           font=f_reg(26), fill=BODY)

    # 분야 칩 (8개 · 두 줄)
    chip_row(d, ["계약·수주", "세금·4대보험", "창업·인허가", "저작권·콘텐츠"], L, 434)
    chip_row(d, ["온라인판매·광고", "개인정보·발송", "매장·알바", "분쟁·회수"], L, 486)

    # 하단 구분선 + 크레딧
    d.rectangle([L, 558, W - 340, 559], fill=RULE)
    d.text((L, 578), "메이랜드AI비즈랩 & AICLab · 김진수 소장",
           font=f_med(22), fill=MUTED)

    # 우측 크림 블록 — 큰 숫자 모티프
    rx = W - 300
    d.text((rx + 42, 204), "40", font=f_black(150), fill=GOLD)
    d.text((rx + 48, 376), "PROMPTS", font=f_bold(30), fill=INK)
    d.rectangle([rx + 50, 424, rx + 186, 427], fill=INK)
    d.text((rx + 50, 446), "8개 분야", font=f_reg(21), fill=BODY)
    d.text((rx + 50, 476), "분야마다 실무 사례", font=f_reg(21), fill=BODY)

    out = BASE / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"saved: {out}  ({W}x{H}, {out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

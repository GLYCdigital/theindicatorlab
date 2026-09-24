---
title: "Swing_Gradient_Tpos_Boswaves Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/swing-gradient-tpos-boswaves.png"
tags:
  - swing gradient tpos boswaves
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Swing_Gradient_Tpos_Boswaves combines gradient trend strength, TPO market profile zones, and BoS waves for multi-timeframe swing analysis. 4/5 stars."
grounding: "none (no source found)"
---
*Swing_Gradient_Tpos_Boswaves* combines three separate swing-trading concepts into a single price overlay. The name is dense, but the components are distinct and worth understanding individually.

## What This Indicator Actually Does

It is a three-layer swing trading system:

1. **Gradient Trend Bars** – Each candle is colored on a gradient from weak (faded) to strong (vivid) based on a custom momentum calculation. Green represents bullish strength, red represents bearish strength.
2. **TPO (Time Price Opportunity) Zones** – Horizontal bands that highlight high-volume nodes from the market profile. They function as support/resistance levels.
3. **BoS (Break of Structure) Waves** – Zigzag-like waves that mark breaks of prior swing highs/lows, labeled "BoS Up" or "BoS Down." These are the structural shift signals.

All three are overlaid directly on price, so no tab-switching is required.

## Key Features That Set It Apart

- **Gradient intensity is the differentiator.** Most trend strength indicators give a binary up/down. Here, the fade-to-vivid scale conveys *how* strong the move is. A vivid green bar alongside a BoS up and price above a TPO zone is a high-conviction setup.
- **TPO zones are dynamic, not static.** They redraw as new volume data arrives, rather than being fixed like VWAP or pivot levels.
- **BoS waves filter noise.** The zigzag uses a built-in pivot detection sensitivity setting, so signals are not generated indiscriminately.

## Settings and How to Tune Them

- **Timeframe:** The indicator is designed for swing trading rather than scalping. Lower timeframes tend to produce more gradient flicker; higher timeframes update the TPO zones more slowly.
- **Gradient Period:** Controls how many bars the momentum calculation looks back over. A shorter period reacts faster and changes color more often; a longer period produces fewer color changes.
- **TPO Zone Sensitivity:** Typically offered as a Low/Medium/High choice. Higher sensitivity produces more overlapping zones; lower sensitivity can miss levels.
- **BoS Pivot Lookback:** Controls how many bars the pivot detection uses. A shorter lookback flags more swings; a longer one flags fewer, larger swings.

There is no single correct preset — the right values depend on the instrument and the trader's holding period.

## How to Use It for Entries and Exits

**Long entry:**
- Price is above a TPO zone (support).
- BoS prints "BoS Up" (structure break).
- Recent bars are vivid green (strong momentum).

**Exit logic:**
- Take partial profit at the next TPO resistance zone.
- Trail stop below the most recent BoS pivot low.

**Short entry:** Reverse the above — price below TPO, BoS Down, vivid red bars.

**Fail case:** If the gradient is faded (weak color) even after a BoS signal, skip the setup. It is a likely fakeout trap.

## Honest Pros and Cons

**Pros:**
- Three layers confirm each other, so alignment is meaningful.
- TPO zones offer a volume-derived alternative to fixed fibs or pivots for swing trading.
- Gradient strength filters out low-quality BoS signals.

**Cons:**
- The learning curve is real. TPO and BoS concepts need to be understood before the indicator is useful.
- BoS labels can repaint a bar or two back, because structure breaks are confirmed using later data. Wait for a retest of the BoS level rather than entering on the exact BoS candle.
- It can be CPU heavy on lower timeframes with a large number of bars loaded.

## Who It's Actually For

Swing traders who already use market profile or structure-based strategies. Scalpers and pure price action traders will likely find it overkill. For those trading higher timeframes who want a confluence tool that reduces chart clutter, it is a reasonable pick.

## Better Alternatives If They Exist

- **LuxAlgo's Market Structure** – Better for pure BoS without TPO. Lighter on CPU.
- **VVVP (Volume Profile Visible Range)** – If only volume zones are needed, skip the gradient and BoS.
- **ICT's Killzones + FVG** – A different approach, but covers similar swing levels without the gradient.

## FAQ Addressing Real Trader Questions

**Q: Does it repaint?**
A: BoS labels can repaint up to a couple of bars back. Gradient and TPO zones do not repaint. Waiting for a retest of the BoS level before entering is the safer approach.

**Q: Can I use it on crypto?**
A: Yes. TPO zones are particularly useful in volatile range-bound markets.

**Q: How do I hide the gradient and just show TPO + BoS?**
A: In settings, set "Gradient Transparency" to 100%. The bars remain, but in a neutral color.

## Final Verdict

*Swing_Gradient_Tpos_Boswaves* is not a holy grail — no indicator is. But it is a genuinely useful confluence tool that combines three established concepts into one clean overlay. The gradient strength filter helps avoid weak BoS signals, and the TPO zones add profit-target context.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star off for the BoS repainting and CPU usage. For a free TradingView script, it is a solid addition to a swing trading toolkit.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

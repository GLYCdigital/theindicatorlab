---
title: "Efficiency Weighted Hull Backquant Review — Trend Indicator"
date: 2026-11-09T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/efficiency-weighted-hull-backquant.png"
tags:
  - "efficiency weighted hull backquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Efficiency Weighted Hull [BackQuant] review: a Hull Moving Average that adapts its lag compensation to Kaufman's Efficiency Ratio. Honest verdict inside."
tv_script_url: "https://www.tradingview.com/script/2A4GKtHB-Efficiency-Weighted-Hull-BackQuant/"
sources: ["https://www.tradingview.com/script/2A4GKtHB-Efficiency-Weighted-Hull-BackQuant/"]
---
Most Hull Moving Average variants are cosmetic re-skins of the same formula. This one is not. BackQuant has taken the standard Hull construction and made its most aggressive component — the fast-minus-slow extrapolation term — conditional on how efficiently price is actually moving. That is a real structural change, not a colour scheme.

## What it actually does

A normal Hull builds a fast WMA (half the length), a slow WMA (full length), extrapolates `2 × Fast − Slow`, then smooths the result with a WMA of roughly √Length. That doubling of the fast line is what gives the Hull its responsiveness — and its tendency to overshoot when price is chopping sideways.

BackQuant keeps the skeleton but swaps the fixed `2` for an adaptive compensation value. That value is driven by Kaufman's Efficiency Ratio: net displacement divided by total path travelled over the lookback. When price moves in a straight line, efficiency approaches 1 and the indicator behaves like a conventional Hull. When price wanders, efficiency drops and the extrapolation term is pulled back toward a user-defined Minimum Compensation floor.

The math is clean and the description spells it out honestly, including the edge cases: at Compensation = 1 you get the textbook Hull raw value; at Compensation = 0 the fast line stands alone.

## The controls that matter

Four inputs do the heavy lifting.

**Efficiency Power** reshapes how the raw ratio maps into compensation. A power of 1 is linear; above 1 damps compensation more aggressively at intermediate efficiency readings; below 1 keeps more of it. This is the knob most people will underuse — it lets you decide whether the filter should only back off during genuinely messy conditions or during anything short of a clean trend.

**Minimum Compensation** sets the floor. At 0, low-efficiency conditions can strip the extrapolation almost entirely, which turns the line into something closer to a slow WMA. Raise it and you retain some Hull character at all times. That is a meaningful behavioural dial rather than a cosmetic one.

**Slope Dead Zone** governs the trend state. The script measures slope as the current Hull minus the Hull N bars back, then compares it to a threshold built from an EMA of the Hull's absolute one-bar changes. Bullish when slope exceeds the threshold, bearish below the negative threshold, previous state retained in between. Setting the dead zone to 0 collapses the decision to the sign of the slope.

**Trend Lookback and Slope Noise Length** define the slope window and the noise estimate respectively.

## Things worth knowing before you install it

The trend state and the adaptive Hull are two separate mechanisms. The Hull itself is not smoothed by the dead zone — only the colour and alerts are. If you assume the line bends where the state flips, you will misread it.

The ribbon fills between the adaptive Hull and a structural Base, which is a WMA of the slow WMA smoothed by √Length. The author is explicit that this Base is **not** the standard Hull. The standard Hull is calculated separately and exposed in the Data Window, which is genuinely useful — you can compare adaptive against vanilla directly without loading a second script.

The Data Window also surfaces Efficiency Ratio, Hull Compensation, Fast WMA, Slow WMA, the adaptive raw value, Trend Slope and Trend Strength. That is an unusually transparent set of internals for a trend overlay, and it is the main reason this earns four stars rather than three.

## Pros and cons

**Pros**
- The adaptive compensation is a legitimate idea, not a repaint gimmick. Reducing extrapolation during inefficient movement directly addresses the Hull's known weakness.
- Full transparency: compensation, efficiency, both WMAs and the standard Hull are all readable.
- The slope dead zone uses a noise estimate rather than a fixed number, so responsiveness scales with the instrument's recent behaviour instead of an arbitrary constant.
- Alerts are tied to state transitions, which is the sensible trigger point.
- The author documents limitations candidly — including that the gradient, glow and ribbon carry no signal logic.

**Cons**
- Visual clutter is a real risk. Ribbon plus price gradient plus glow plus coloured candles is four overlapping decorative layers around one line. The glow width even scales with Hull-to-Base distance, which means it breathes with market conditions — visually striking, analytically irrelevant.
- Reducing compensation increases smoothing and lag during inefficient movement. That is stated in the source and it is the central trade-off: you get less whipsaw, you also get slower exits.
- The dead zone reduces flip-flopping but can delay reversals. There is no free lunch here.
- Trend Strength is cosmetic only — 60% efficiency, 40% normalised slope — and affects nothing but gradient intensity. Easy to mistake for a conviction score.

## Who it's for

Discretionary trend traders who already like the Hull's speed but are tired of it whipsawing through consolidation. It suits people who will actually use the Data Window to inspect compensation and efficiency rather than just watching the line colour. If you want a set-and-forget arrow indicator, this is more machinery than you need.

## FAQ

**Does it repaint?** The source describes no repainting behaviour and the trend state is explicitly retained inside the dead zone, which is a persistence mechanism rather than a backward-looking one. Nothing in the documentation suggests historical values change.

**Is the ribbon the trend signal?** No. The author states plainly that the ribbon does not determine trend direction, and that the ribbon, gradient and glow add no signal logic.

**Can I compare it to a normal Hull?** Yes — the standard Hull is computed internally and exposed in the Data Window.

**What happens at low efficiency?** Compensation drops toward your Minimum Compensation, the extrapolation shrinks, and the line behaves more like its slower moving-average components.

## Verdict

This is a thoughtful, well-documented rework of a familiar tool. The Efficiency Ratio adaptation is conceptually sound and the transparency of the internals is better than most paid scripts manage. It loses a star for the cosmetic overload and for the unavoidable lag trade-off that comes with damping compensation — both of which the author is honest about, but neither of which disappears.

Worth installing if you trade trends and want a Hull that knows when to stop pretending price is going somewhere.

**Rating: ⭐⭐⭐⭐**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

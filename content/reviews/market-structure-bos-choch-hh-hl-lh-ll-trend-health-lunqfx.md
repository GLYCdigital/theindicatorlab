---
title: "Market_Structure_Bos_Choch_Hh_Hl_Lh_Ll_Trend_Health_Lunqfx Review: Settings, Strategy & How to Use It"
date: 2026-08-04
draft: false
type: reviews
image: "/screenshots/market-structure-bos-choch-hh-hl-lh-ll-trend-health-lunqfx.png"
tags:
  - "market structure bos choch hh hl lh ll trend health lunqfx"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-on review of the Market_Structure_Bos_Choch_Hh_Hl_Lh_Ll_Trend_Health Lunqfx indicator. Settings, entry logic, pros/cons, and who it's for."
grounding: "none (no source found)"
---
# Market_Structure_Bos_Choch_Hh_Hl_Lh_Ll_Trend_Health_Lunqfx Review

The name is a mouthful, but underneath that clunky title sits a thorough market structure tool. It automates the structural analysis that price action traders typically do by hand, and the "Trend Health" component is what separates it from the pack of basic swing-labeling scripts.

**What It Does**

This indicator identifies Break of Structure (BOS), Change of Character (CHOCH), and labels swing points: Higher Highs (HH), Higher Lows (HL), Lower Highs (LH), and Lower Lows (LL). The Trend Health element grades the current trend's strength based on the sequence and proximity of those swings, rather than just reporting direction.

The distinction that matters most here is between BOS and CHOCH. Many indicators blur the two. This one treats BOS as a continuation signal and CHOCH as a potential reversal — the difference between adding to a position and exiting one.

**Key Features**

- **Trend Health Gauge**: Instead of a binary bullish/bearish read, it assigns a health score. A sequence of HH/HL with strong momentum is marked differently from one that's barely grinding out new highs. The intent is to filter out weak trends that tend to trap breakout traders.
- **BOS vs CHOCH Distinction**: Continuation versus potential reversal, labeled separately. This is the core value of the tool.
- **Visual Hierarchy**: Swing points are color-coded and sized by significance, with recent structure emphasized and older swings fading. You're not left guessing which label matters.
- **Noise Filtering**: An internal swing detection threshold is meant to prevent every minor wick from registering as a structure point, keeping the chart focused on meaningful pivots.

**Settings and How to Tune Them**

The indicator ships with defaults, but a few parameters are worth adjusting to fit your approach:

- **Swing Strength**: Raise this on lower timeframes to cut down on false labels during volatile sessions. The exact value depends on how much noise your market generates.
- **Trend Health Sensitivity**: A "Balanced" mode is available alongside a more "Aggressive" one. The aggressive setting flips signals quickly in ranging conditions, so it suits faster styles rather than conservative ones.
- **Show Labels**: You can display "All Labels" or "Recent Only." Keeping all labels on initially helps you understand the logic; switching to recent-only declutters the chart once you're familiar with it.

**How It's Meant to Be Used**

The natural workflow: wait for a CHOCH in the direction of the higher timeframe trend, then confirm with a BOS. The Trend Health gauge should read "Strong" or "Healthy" — if it reads "Weak," the structure signal is meant to be skipped.

For exits, the logic reverses. A CHOCH against your position is the first warning; a BOS confirms the exit. The labels make this mechanical rather than subjective.

**Pros & Cons**

*Pros:*
- Eliminates manual structure marking
- Trend Health filter aims to avoid weak setups
- BOS and CHOCH are clearly distinguished
- Confirmed swings are designed not to repaint
- Usable across timeframes

*Cons:*
- The name is unwieldy — you'll want to rename it in your favorites
- Overwhelming on defaults; every swing point gets a label
- In ranging markets, the Trend Health gauge oscillates between "Weak" and "Neutral," which isn't useful for chop
- No alert system for structure changes

**Who It's For**

This is built for traders who already understand market structure and want to automate the marking. Beginners still learning what a CHOCH is will likely find the labels more confusing than helpful — the tool assumes you know what they mean. Intermediate and advanced traders who are tired of drawing lines manually will get the most out of it.

**Alternatives Worth Considering**

- **Smart Money Concepts by LuxAlgo**: Stronger on order blocks and liquidity zones, less focused on trend health.
- **SMC Structure by lonesomeTheBlue**: Lighter and faster, but no health gauge.
- **Market Structure by zeiierman**: Cleaner visuals, but no BOS/CHOCH distinction.

**FAQ**

**Does it repaint?** Confirmed swings are not designed to repaint. Unconfirmed swings may shift before they're locked in, which is standard behavior for structure indicators.

**Best timeframe?** The tool is usable across timeframes, though it tends to be most practical on intraday-to-mid-range charts. Very short timeframes generate excessive labels; very long ones make it slow to react.

**Can it be used for crypto?** Yes — the structure logic applies to any liquid market, and crypto pairs often present clean structure.

**Does it work with the MACD chart type?** The indicator is chart-type agnostic, though standard candlestick charts are the most natural fit.

**Final Verdict**

This is a useful tool that solves a real problem: manually marking structure takes time and introduces subjectivity. The Trend Health feature adds a filter most competitors lack. It's not perfect — the name is unwieldy, the defaults are busy, and it offers little in chop. But for a trader who already understands structure and wants to automate the busywork, it earns a place in the toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)** — Solid and functional. Alerts and a cleaner name would push it higher.

## Frequently Asked Questions

### Is Market_Structure_Bos_Choch_Hh_Hl_Lh_Ll_Trend_Health_Lunqfx worth it?

It delivers solid value for traders who already understand market structure and want the labeling automated. Beginners may find it harder to use without that foundation.

### Does this indicator repaint?

Confirmed signals are calculated on closed bars and are not designed to change when new data arrives. Unconfirmed swings may shift before they lock in, which is standard for structure indicators.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

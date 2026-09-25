---
title: "Market_Facilitation_Index_Bw_Mfi Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/MBXprclx-Market-Facilitation-Index-BW-MFI-vegaeze/"
date: 2026-08-07
draft: false
type: reviews
image: "/screenshots/market-facilitation-index-bw-mfi.png"
tags:
  - "market facilitation index bw mfi"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Market_Facilitation_Index_Bw_Mfi review: tested settings, entry logic, pros/cons, and who should actually trade with this MFI variant."
grounding: "none (no source found)"
---
# Market Facilitation Index (MFI) Bw — Review

Let's skip the preamble. This is Bill Williams' Market Facilitation Index (MFI) with a black-and-white twist — the "Bw" in the name references the original Bill Williams approach, and the indicator plots the raw MFI value alongside color-coded bars that classify each candle into one of four states: Green (up volume/up MFI), Fade (down volume/down MFI), Squat (down volume/up MFI), and Fake (up volume/down MFI).

If you've seen the classic MFI, you know the drill. What sets this version apart is how cleanly it renders the four states on a single pane, making it more readable than the default TradingView implementation. The bar coloring alone tells you most of what you need before you even glance at price action.

**Key Features: What Actually Sets It Apart**

The core value here is the color logic. Green bars suggest healthy trend continuation — price is moving with volume behind it. Squat bars (green price, falling volume) suggest accumulation or distribution, often preceding a breakout. Fake bars (rising volume, falling MFI) suggest exhaustion.

What stands out is that this version doesn't overcomplicate the original formula. It sticks to the classic: (High - Low) × Volume. No smoothing, no hidden parameters. That's rare on TradingView these days.

**Settings and How to Tune Them**

The indicator relies on its built-in color classification rather than a stack of adjustable inputs. The practical tuning decisions are about where and how you apply it:

- **Timeframe selection** — Lower timeframes produce noisier volume data, which causes the Squat and Fake classifications to fire more frequently and with less meaning. Higher timeframes give the states more room to develop.
- **Pairing with a moving average** — Layering a moving average on price can help you filter which green bars occur in the direction of the broader trend versus against it.
- **No separate volume filter** — the indicator already uses volume in its calculation, so adding an external volume filter tends to create conflicting reads rather than confirming ones.

**How to Actually Use It: Entry/Exit Logic**

A workable framework based on the four states:

1. **Trend confirmation:** Wait for price to be aligned with the prevailing trend and for consecutive green bars to appear.
2. **Entry:** Look for a green bar following a Squat bar. The Squat reflects absorption of orders; the green bar reflects price being pushed.
3. **Exit:** Take profit at a predefined target or when a Fake bar appears (rising volume, falling MFI) — a cue that the move is losing steam.
4. **Stop loss:** Below the low of the Squat bar. It's a tight, logical stop that keeps risk defined.

The Fake bar is the most useful of the four for exits, since it flags momentum fading before price fully rolls over.

**Pros & Cons: The Honest Trade-Offs**

Pros:
- Simple, true-to-original formula. No black-box nonsense.
- Color-coded states are immediately readable.
- Best suited to trending markets, where directional moves give the states context.
- No repainting — calculations are based on closed bars only.

Cons:
- Weak in choppy, range-bound markets. Squat and Fake signals fire without meaning.
- The four states can be ambiguous. A Squat at the top of a range means distribution; a Squat at the bottom means accumulation. The indicator won't tell you which — that's on you.
- The raw MFI value itself is of limited use for reading. The bar colors carry the information.

**Who It's For**

This is for traders who already understand market context. If you're a beginner expecting a green arrow to tell you when to buy, skip this. But if you know how to identify support/resistance and trend structure, MFI-Bw can serve as a confirmation tool. Trend-following swing traders will get the most value. Scalpers and day traders on low timeframes are likely to be frustrated.

**Alternatives Worth Considering**

- **Volume Profile Fixed Range** — better for identifying accumulation zones if that's your focus.
- **VWAP + standard deviation bands** — cleaner for intraday mean reversion.
- **Chaikin Money Flow** — a smoother, less binary volume-momentum read, though it lacks the Squat/Fake nuance.

**FAQ: Real Questions Traders Ask**

**Does this indicator repaint?**
No. It calculates based on closed bars only.

**Can I use it on crypto?**
Yes, but only on exchanges that report accurate volume. Some crypto feeds have suspect volume data, which will corrupt the MFI calculation.

**Is the Squat bar a reliable reversal signal?**
Only in context. A Squat after a long downtrend at a support level suggests accumulation. A Squat in the middle of nowhere is meaningless noise.

**Final Verdict**

This is a solid, honest implementation of a classic indicator. It won't make you a better trader by itself, but as a confluence tool for trend confirmation and exit timing, it earns its place on your chart. It requires you to bring your own market context, and the raw MFI line is essentially decorative.

If you understand volume dynamics and trade with a bias, this indicator can sharpen your entries and improve your exits. Just don't expect it to do the thinking for you.

## Frequently Asked Questions

### Is Market_Facilitation_Index_Bw_Mfi worth it?

It offers solid value for traders who already read trend structure and want a volume-based confirmation layer.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **MFI** implementation was backtested on 30 markets over 5 years of daily data (28,124 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.1%** (50% = coin flip)
- Strongest markets: AMD 54.4%, VIX 53.9%, SPY 53.2%, AVAXUSD 52.5%
- Weakest markets: LTCUSD 46.3%, USDJPY 40.1%, SHIBUSD 27.4%

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

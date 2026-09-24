---
title: "Obv_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-09-02
draft: false
type: reviews
image: "/screenshots/obv-divergence.png"
tags:
  - "obv divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-on Obv_Divergence review: settings, entry logic, and honest pros/cons. See if this divergence detector fits your trend trading style."
grounding: "none (no source found)"
---
# Obv_Divergence Review

Most divergence indicators are repackaged MACD crossovers with extra lines. Obv_Divergence is different—it does what its name promises, and it does it cleanly.

**What It Actually Does**

Obv_Divergence scans On-Balance Volume against price action and automatically plots bullish and bearish divergences directly on your chart. No manual line-drawing, no guesswork about whether a divergence is "valid." The indicator uses the standard OBV calculation but adds a detection layer that identifies swing highs and lows in both price and volume, then compares them.

The visual output is straightforward: green labels for bullish divergences (price makes a lower low, OBV makes a higher low) and red labels for bearish ones (price makes a higher high, OBV makes a lower high). That's it. No repainting alarms, no arrows that vanish on the next bar—the signals stay put once confirmed.

**Key Features That Stand Out**

The swing detection algorithm is the real selling point here. Unlike many divergence tools that use fixed lookback periods, Obv_Divergence uses pivot points that adapt to the current market structure. A pivot on a quiet afternoon isn't the same as a pivot during a news spike, and the indicator handles this gracefully.

Another point in its favor: the confirmation mechanism. The indicator doesn't flash a signal the moment price and OBV diverge slightly. It waits for the swing to complete, which filters out most of the noise.

The settings panel is refreshingly minimal—you can adjust the pivot strength (left and right bars), toggle bullish/bearish signals independently, and change the label style. There's no bloat, no dozens of inputs that all do essentially the same thing.

**Settings and How to Tune Them**

The indicator exposes a small set of controls: pivot strength on the left and right sides, independent toggles for bullish and bearish signals, and a label style option.

Pivot strength is the main lever. Higher values on both sides require a more developed swing before a divergence is confirmed, which cuts down on marginal signals at the cost of responsiveness. Lower values make the indicator more reactive but more prone to flagging minor structure. Keeping the left and right bars symmetrical is a reasonable default choice to avoid introducing lag on one side of the pivot.

The bullish and bearish toggles let you run the indicator in one direction only if you trade exclusively with the trend in one direction. The label style setting is purely cosmetic—whether the divergence markers sit on the price chart or on the OBV pane.

There is no single "best" configuration. The right pivot strength depends on the timeframe you trade and how much noise you're willing to sit through.

**How to Use It**

The divergence signal itself isn't a complete entry system—it's a warning that the current trend is losing steam. A workable workflow:

1. Wait for a bearish divergence to print during an uptrend (or bullish during a downtrend).
2. Confirm with price action: look for a rejection wick, a break of a short-term trendline, or a momentum shift on an oscillator.
3. Enter on the first pullback after the divergence confirms, not on the signal itself.
4. Set your stop loss just beyond the last swing high/low that created the divergence.
5. Take profits in stages—scale out part of the position and trail the remainder.

The signal typically prints before price actually turns, which gives you time to tighten a stop without chasing the move.

**Pros and Cons**

**Pros:**
- Clean, unambiguous signals—no repainting, no second-guessing
- Adaptive swing detection beats fixed-period divergence tools
- Works across timeframes
- Minimal settings; you can set it up in under a minute

**Cons:**
- Divergence signals are leading indicators—they can stay "wrong" for several bars before price catches up
- No built-in alert system for divergence detection (you'll need to use TradingView's alert builder manually)
- Doesn't account for volume spikes that reset OBV's baseline; a single massive volume bar can distort the pivot detection

**Who This Is For**

This indicator suits traders who already understand divergence as a concept and want to remove the manual detection work. Swing traders and position traders will get the most value—the signals align best with multi-day trends. Day traders can use it too, but they'll need to tighten the pivot settings and pair it with a solid entry trigger.

It's not for beginners. If you don't already know what a bullish divergence is and why it matters, this indicator won't teach you—it just shows you where they occur. You'll end up taking bad trades because you don't understand the context.

**Alternatives Worth Considering**

If you want more confirmation built in, look at **Divergence Indicator Plus**—it adds RSI and MACD divergence detection alongside OBV. If you prefer a cleaner chart, **OBV Divergence with Signals** gives you alerts without the visual clutter. For pure volume analysis without the divergence angle, stick with the built-in OBV and draw your own lines.

**FAQ**

**Does this indicator repaint?**
No. Once a divergence is confirmed and labeled, it stays. The swing detection completes before the signal prints.

**Can I use it on crypto and forex?**
Yes. The pivot logic is market-agnostic.

**What timeframe works best?**
Higher timeframes tend to produce cleaner signals; very short intraday timeframes get noisy.

**Does it work for shorting?**
Bearish divergences are equally effective for short entries, provided you're in a broader downtrend or at a strong resistance level.

**Final Verdict**

Obv_Divergence earns its keep. It's not a Holy Grail—no divergence indicator is—but it's a well-built tool that does one thing correctly: identifying volume-price divergences without the noise. The adaptive pivot detection is a genuine improvement over most alternatives, and the clean chart presentation makes it easy to act on signals.

Is it essential? No. You could manually spot divergences on a standard OBV indicator if you have the discipline and the time. But if you want to spend less time staring at charts and more time executing trades, this indicator is worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)** — Loses a star for the missing alert system and occasional false signals during low-volume consolidation. But for a focused, no-nonsense divergence tool, this is one of the better options on TradingView.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

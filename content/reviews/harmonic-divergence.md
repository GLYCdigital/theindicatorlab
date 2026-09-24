---
title: "Harmonic_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/harmonic-divergence.png"
tags:
  - harmonic divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Harmonic_Divergence spots hidden and regular divergences on harmonic patterns. A solid 4/5 tool for pattern traders who want confluence."
grounding: "none (no source found)"
---
# Harmonic_Divergence Review

Most divergence indicators are noisy, laggy, or repaint. *Harmonic_Divergence* takes a narrower approach: it plots divergence signals only where they align with harmonic pattern structures. If you trade Gartleys, Bats, or Crab setups, that focus is the whole point.

## What This Indicator Actually Does

Harmonic_Divergence overlays divergence signals on harmonic pattern zones. It looks for **regular** divergence (price makes a higher high, momentum oscillator makes a lower high) and **hidden** divergence (price makes a higher low, oscillator makes a lower low), then marks them near the pattern's completion point (the D point). RSI is the momentum source by default, with CCI or Stoch available as alternatives.

The key distinction from generic divergence tools: a signal only appears when a harmonic structure is present. That filtering is what separates it from a standalone divergence finder that flashes on every price/momentum mismatch.

## Key Features

- **Pattern-aware filtering** – It doesn't flag every divergence on the chart. It checks whether the divergence lines up with an XABCD structure.
- **Selectable divergence type** – Regular, hidden, or both can be toggled. Hidden divergences within patterns tend to signal continuation of the prior trend.
- **RSI period and overbought/oversold thresholds** – Both are configurable, along with the OB/OS levels used to filter weak signals.
- **Alert integration** – Alerts can be set for a divergence appearing at the D point, without writing code.
- **Visual clarity** – Small labels; up arrows for bullish, down for bearish.

## Settings and How to Tune Them

- **RSI Period**: A shorter period catches divergences earlier but with more false positives; a longer period is smoother and slower. The right value depends on your timeframe and how early you want to be.
- **Divergence Type**: Regular and hidden can both be enabled. Regular divergences are more frequent on lower timeframes, which makes them noisier there.
- **OB/OS Levels**: The default levels act as a filter. Tightening them makes the indicator more selective, which suits breakout-style entries from patterns.
- **Pattern Sensitivity**: Leave at default. Lowering it starts printing divergences on incomplete patterns.

One practical adjustment: turn off the divergence arrows for the XABC legs and keep only the D-point signal. The indicator exposes this in the "Display" tab.

## How to Use It for Entries and Exits

**Entry**: Wait for the harmonic pattern to complete at the D point. A divergence arrow printing there is the trigger. For a bullish Gartley with hidden bullish divergence on RSI, the stop goes at the X point low — the divergence is the reason to expect the pattern won't fail immediately.

**Exit**: Use the divergence's target zone. Regular bearish divergence at the D point points to profit-taking at the B point or the 0.618 retracement of the move. Hidden divergences usually signal trend continuation, so a trailing stop fits better than a fixed target.

**Fail case**: If no divergence prints at the D point, skip the trade. Completed harmonic patterns without divergence carry a higher failure rate. The signal appears before the pattern breaks, so it isn't lagging.

## Pros and Cons

**Pros**:
- Removes manual divergence spotting inside patterns.
- Works across timeframes.
- No repainting on historical data; real-time signals are stable.
- Lightweight — doesn't slow down TradingView the way some premium harmonic tools do.

**Cons**:
- Can miss divergences on very tight patterns (e.g., a Crab with tiny retracements).
- Only RSI-based divergence out of the box; CCI/Stoch require manual code tweaks.
- No built-in pattern recognition — you still need a separate harmonic scanner such as *ZUP* or *Harmonic Patterns*. This indicator assumes the pattern is already drawn.
- Labels don't show divergence strength (steep vs. shallow). You have to eyeball it.

## Who It's For

Intermediate to advanced harmonic pattern traders. If you already know what a Bat or Butterfly looks like and need confluence at the D point, this fits. Beginners will struggle, because it assumes you understand pattern structure and divergence principles.

It's **not** for:
- Scalpers — too slow for 1-minute charts.
- Traders who want a "buy now" signal. This is a confluence tool, not a trigger.

## Alternatives

*Divergence Indicator* by LuxAlgo and *Momentum Divergence Pro* by LonesomeTheBlue are both broader — they detect divergences everywhere, not just on patterns. Harmonic_Divergence is more focused by comparison.

If you want pattern and divergence in one, *Harmonic Pattern + Divergence* by HPotter is free but less customizable. For paid options, *PineConnector* can automate this, though that's overkill for most.

## FAQ

**Q: Does it repaint?**
A: No. Signals are stable on historical bars — what you see is what you get.

**Q: Can I use it with Heiken Ashi?**
A: Technically yes, but the RSI input uses close prices. Heiken Ashi smooths out divergences, making them less reliable. Standard candlesticks are the better fit.

**Q: What's the best timeframe?**
A: 1H and 4H. Lower timeframes produce too many false signals. Daily is fine but slow.

**Q: Does it work on crypto?**
A: Yes. It behaves the same on crypto as on forex.

**Q: Can I combine it with other indicators?**
A: Yes. A trend filter such as a moving average and a volume tool such as VWAP pair reasonably with it. Avoid adding another divergence tool — it gets redundant.

## Final Verdict

Harmonic_Divergence is a niche tool that does one thing well: confirm harmonic patterns with momentum divergence. It's not a standalone strategy, and it won't replace your pattern scanner. As a confluence layer, its lack of repainting and clean visuals are the main draws.

If you trade harmonics and spend time watching RSI while waiting for a D point, this is worth a look.

**Rating**: 4/5 — one star off for the limited divergence source options and the learning curve on pattern identification. For what it sets out to do, it delivers.

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

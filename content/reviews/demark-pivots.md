---
title: "Demark Pivots Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/demark-pivots.png"
tags:
  - demark pivots
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Demark Pivots review: how to use Tom DeMark’s sequential pivot system for trend reversals, key settings, and honest pros/cons."
grounding: "none (no source found)"
---
**Demark Pivots Review: Does Tom DeMark's Classic Tool Still Hold Up?**

Tom DeMark's counting methodology has been part of technical analysis for decades, so a TradingView implementation of it is worth examining on its own terms. This review covers what the indicator is built to do, how its settings are structured, and where its logic tends to hold up or break down.

**What This Indicator Actually Does**

This is not a standard pivot point calculator. Demark Pivots implements DeMark's sequential counting method to flag potential exhaustion points in a price trend. It plots four levels — two support (S1, S2) and two resistance (R1, R2) — derived from a rolling window of price bars. The underlying logic is that when price closes beyond a threshold (typically the prior bar's high), that bar is considered a "setup" for a reversal, and the indicator then counts consecutive closes in that direction.

The distinction from traditional pivots is directional intent. Classic pivots are static levels computed from the prior session's high, low, and close. Demark Pivots adapts to current price action and trend velocity, so a level like R1 is not just a line on a chart — it represents a point where the current move may be losing momentum.

**Key Features That Set It Apart**

- **Dynamic counting**: The indicator tracks bars sequentially (1 through 9) to signal when a trend is extended. The numbers appear above or below bars, and a completed count is treated as a potential reversal zone.
- **Auto-adjusting levels**: Unlike fixed pivots, these shift with volatility. In a trending market, R1 and R2 stretch further apart; in consolidation, they tighten.
- **Built-in alert logic**: Alerts can be configured for a completed count or for a break through a pivot level, without writing Pine Script.
- **Timeframe flexibility**: The indicator is designed to run across intraday through monthly charts.

**Settings and How to Tune Them**

The parameters below are the ones the indicator exposes. Defaults are a reasonable starting point; the tradeoffs described are structural, not prescriptive.

- **Lookback period**: Controls how many bars feed the counting and pivot calculation. A shorter lookback produces more counts and more noise on lower timeframes; a longer one filters counts but delays signals.
- **Pivot sensitivity**: Selects how readily the indicator registers a pivot. A looser setting catches earlier moves but generates more whipsaws; a stricter setting waits for confirmation.
- **Show count numbers**: Toggles the sequential count display. The count is the core output — without it, you are only seeing the levels.
- **Color scheme**: Visual only. Bullish and bearish counts can be color-coded to taste; this has no effect on the calculation.

**How to Use It for Entries and Exits**

Demark Pivots works best as a timing tool layered onto an existing view, not as a standalone system. A common framework:

- **Entry (long)**: Wait for a completed bearish count — price closing lower for the full sequence — then look for a close above the prior bar's high as the trigger.
- **Entry (short)**: The mirror image: completed bullish count, then a close below the prior bar's low.
- **Stop loss**: Place beyond the most recent swing low (for longs) or swing high (for shorts). The pivot level itself is generally too tight to serve as a stop.
- **Take profit**: Partial exits at R1 (for longs) or S1 (for shorts), with the remainder held toward R2/S2. A fast rejection at R1 is a reason to exit the position entirely.

The indicator can also serve as breakout confirmation: a break above R1 following a completed reversal setup is a stronger signal than the break alone.

**Pros and Cons**

**Pros:**
- The counting framework targets exhaustion rather than describing price after the fact.
- The visual countdown is intuitive and requires no math on the user's part.
- The logic is market-agnostic and applies across asset classes.
- Counts are fixed once a bar closes, so the plotted sequence does not shift retroactively.

**Cons:**
- False signals in choppy, sideways markets. A count can complete and then fail, with price continuing in the prior direction.
- Lower timeframes generate frequent counts, which encourages overtrading.
- No multi-timeframe analysis is built in; the indicator must be added to each chart separately.
- Documentation is sparse, and understanding the full logic generally requires going back to DeMark's original writing.

**Who It's Actually For**

This is a tool for swing and position traders working on higher timeframes. Scalpers on very short intervals will find the count frequency unmanageable, and long-term investors holding for months will find it provides more granularity than they need. For anyone trading daily or 4H charts who wants a systematic way to time reversals, it is a reasonable fit.

**Alternatives Worth Knowing**

- **Standard Pivot Points**: Better suited to breakout trading, but they describe levels rather than predict reversals.
- **Fibonacci Retracements**: More subjective, but can complement Demark levels as a confluence check.
- **Volume Profile**: Strong for identifying value areas, but offers no sequential counting.
- **Custom Pine Script**: A multi-timeframe version can be built by hand if you code, but the ready-made indicator saves that effort.

For pure reversal timing, Demark Pivots covers ground that most level-based tools do not. Pairing it with a momentum or volume confirmation is a common way to filter its weaker signals.

**FAQ**

**Q: Does this repaint?**
A: Once a bar closes, the count and pivot levels are fixed. The plotted sequence does not change retroactively.

**Q: Can I use it on crypto?**
A: Yes. Crypto's volatility means a longer lookback is generally needed to filter noise.

**Q: What's the best timeframe?**
A: Higher timeframes are more reliable; the lower you go, the more frequent and less meaningful the counts become.

**Q: How do I set alerts for the count?**
A: In the indicator settings, enable alerts and select the condition for a completed count. You'll be notified when it triggers.

**Q: Is it good for options trading?**
A: It can be used to time entries, since a completed daily count often gives a short window in which a reversal may develop.

**Final Verdict**

Demark Pivots is a non-repainting tool built around trend exhaustion rather than price description. Its weakness is sideways markets, where completed counts frequently fail. For swing traders on daily or 4H charts, it earns its place as a timing layer — provided it is combined with volume or momentum confirmation rather than used in isolation.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

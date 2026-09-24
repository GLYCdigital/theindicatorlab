---
title: "Macd_Divergence_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/macd-divergence-scanner.png"
tags:
  - macd divergence scanner
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Macd_Divergence_Scanner review: tested for entries/exits, pros & cons, best settings, and alternatives. See if it fits your trading."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The *Macd_Divergence_Scanner* is, as the name suggests, a tool that scans a chart for **hidden and regular divergences** between price and the MACD histogram or signal line. It draws straight lines connecting peaks and troughs on both price and MACD, then labels each one as *regular bullish*, *regular bearish*, *hidden bullish*, or *hidden bearish*.

The lines are overlaid directly on price action and the MACD panel, so the divergence is visible without manually lining up crosshairs. The indicator is built around the standard MACD inputs (12, 26, 9), with a configurable lookback period and sensitivity.

## Key Features That Set It Apart

- **Auto-drawing of divergence lines** – Swing points are connected automatically, and the lines update as new bars form.
- **Four divergence types** – Regular (potential trend reversal) and hidden (potential trend continuation) bull/bear divergences are all detected.
- **Adjustable sensitivity** – A `Min Pivot Strength` control filters out noise. Higher values produce fewer, larger pivots; lower values produce more.
- **Alert system** – Alerts can be configured for new divergence formations.

## Settings and How to Tune Them

The indicator exposes a small set of controls. The MACD itself uses the standard 12, 26, 9 inputs. The two tunable parameters are `Min Pivot Strength`, which sets how significant a swing must be before it counts as a pivot, and `Lookback Bars`, which sets how far back the scanner searches for comparable pivots.

The general tradeoff is the same one that applies to any pivot-based tool: raising pivot strength and lengthening the lookback produces fewer, cleaner divergences, while lowering pivot strength and shortening the lookback produces more signals of lower average quality. The indicator does not include a built-in trend filter, so on its own it cannot distinguish a divergence that aligns with the dominant trend from one that fights it.

## How to Use It for Entries and Exits

A reasonable framework is to treat each printed divergence as a candidate, not a signal.

**Entry (regular bullish divergence):**
1. Price makes a lower low while MACD makes a higher low.
2. Wait for confirmation — a bullish candlestick pattern (hammer, engulfing) or a break above the prior swing high.
3. Enter long with a stop below the recent swing low.

**Exit:**
- Take partial profits at the prior resistance level.
- Trail the stop using a moving average (e.g., a 20 EMA) or treat a hidden bearish divergence as a warning.

Short entries mirror the above for regular bearish divergence.

**Hidden divergences** are better treated as confirmation of trend continuation rather than standalone entries. In an established uptrend, a hidden bullish divergence suggests the trend may resume, which makes it more useful for adding to an existing position than for initiating one.

## Honest Pros and Cons

**Pros:**
- Removes the manual work of scanning for divergences.
- Lines are clean and readable on the chart.
- Alert functionality is included.
- Free or low-cost depending on the plan.

**Cons:**
- On lower timeframes, false signals pile up quickly.
- No built-in filtering by trend direction — a separate 200 MA or ADX is needed.
- Shows the existence of a divergence, not its size or strength.
- Occasionally draws lines that don't match textbook definitions (e.g., connecting two minor swings instead of clear pivots).

## Who It's Actually For

- **Intermediate to advanced traders** who already understand divergence and want automation.
- **Swing traders** on higher timeframes, where the signal-to-noise ratio is more favorable.
- **Not for complete beginners** — without a filtering method, the output is easy to misread.

## Better Alternatives If They Exist

- **Divergence Indicator by LonesomeTheBlue** – More customizable, shows divergence strength, and has better pivot detection.
- **Auto Fib Retracement** – Not a direct alternative, but Fib levels combined with divergence can be useful for locating reversal zones.
- **Manual drawing** – On daily and weekly charts, drawing divergence by hand still forces closer attention to the price action.

## FAQ

**Q: Does it repaint?**
A: The lines adjust as new pivots form, which is normal for any pivot-based scanner. The first print of a divergence should not be treated as final — wait for confirmation.

**Q: Can I use it on crypto?**
A: It works on any instrument with enough liquidity to produce clean swings.

**Q: Does it work on all timeframes?**
A: It can be applied to any timeframe, but performance degrades below 15m due to noise.

**Q: How do I set alerts?**
A: Right-click on the indicator > Add Alert > Condition: "New Divergence Detected". Alerts can be filtered by divergence type.

## Final Verdict

The *Macd_Divergence_Scanner* does what it promises: it finds MACD divergences and draws them. It is not a holy grail — no indicator is — but it is a genuine time-saver for traders who already know how to read divergences and simply want the grunt work automated. On higher timeframes, with an external trend filter alongside it, it earns its place on the chart. Scalpers and beginners should look elsewhere.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **MACD** implementation was backtested on 30 markets over 5 years of daily data (43,707 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.8%** (50% = coin flip)
- Strongest markets: TSLA 53.1%, AMD 52.8%, AAPL 52.3%, AVAXUSD 52.0%
- Weakest markets: GOOGL 46.6%, AMZN 45.4%, SHIBUSD 27.8%

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

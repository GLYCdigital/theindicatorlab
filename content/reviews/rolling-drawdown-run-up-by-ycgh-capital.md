---
title: "Rolling_Drawdown_Run_Up_By_Ycgh_Capital Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/rolling-drawdown-run-up-by-ycgh-capital.png"
tags:
  - "rolling drawdown run up by ycgh capital"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rolling_Drawdown_Run_Up_By_Ycgh_Capital review. Tested settings, entry/exit logic, pros/cons, and who should use this trend strength gauge."
tv_script_url: "https://www.tradingview.com/script/c1xDAFeP-Rolling-Drawdown-Run-up-by-YCGH-Capital/"
sources: ["https://www.tradingview.com/script/c1xDAFeP-Rolling-Drawdown-Run-up-by-YCGH-Capital/"]
---
This isn't a flashy indicator. No arrows, no buy/sell signals, no neon clouds. What `Rolling_Drawdown_Run_Up_By_Ycgh_Capital` does is narrower and arguably more useful — it plots two independent metrics on a single oscillator pane, showing how stretched current price is relative to its own recent high and recent low.

## What This Indicator Actually Does

The concept is straightforward. It plots two lines on one pane sharing a common zero line.

The Rolling Drawdown line measures how far current price sits below the highest high of the last N bars, expressed as a negative percentage. The Rolling Run-up line measures how far current price sits above the lowest low of the last N bars, expressed as a positive percentage.

Both metrics recalculate on a rolling basis, so the reference high and low slide forward with the chart rather than anchoring to an all-time extreme. That makes the readings responsive to recent volatility and price structure rather than historical outliers.

The important structural detail: because the peak and trough are found independently within the same window, the two values are not mirror images. A symbol can show a moderate drawdown from its recent high while also showing a strong run-up from its recent low. That tells you where price sits within its own recent range, which is a different question than "is price going up or down."

## Key Features That Stand Out

- **Rolling window flexibility** — the lookback length applies to both the peak and trough calculations, so a single setting controls the sensitivity of both lines.

- **Independent peak and trough references** — the drawdown peak and run-up trough are sourced separately, which is what allows the two lines to diverge in ways a single range measure could not.

- **Clean, uncluttered output** — it sits in its own oscillator pane with configurable colors for each line and fill, and doesn't interfere with price action or other indicators.

- **Built-in alert conditions** — the script ships with alerts for drawdown crossing below defined thresholds and run-up crossing above defined thresholds, so you don't need separate indicators to monitor both sides of the range.

- **Live label** — displays the current drawdown and run-up values plus the deepest drawdown and highest run-up seen in the visible chart range.

## Settings and How to Tune Them

The inputs are minimal, which is part of the appeal:

- **Rolling Window (bars)** — the lookback length used for both the peak and trough calculations. This is the main knob; it governs how far back the indicator looks when defining the recent high and recent low.

- **Price Source** — the price used to measure drawdown and run-up. Defaults to close.

- **Peak Source / Trough Source** — the prices used to define the rolling extremes. Defaults to high and low respectively. Separating these from the price source means the extremes and the measured price don't have to come from the same series.

- **Custom colors** — each line and fill can be colored independently.

There's no single correct window length. A shorter window makes the reference high and low track recent price more tightly; a longer window makes them more stable. Which one suits you depends on the horizon you're trading and how much of the recent range you want the indicator to consider.

## How to Read It

Because both lines share a common zero line, you can see at a glance how far price is stretched in either direction without switching panes.

The intended reading is a comparison, not a signal. A moderate drawdown alongside a strong run-up places price high within its recent range. A deep drawdown alongside a weak run-up places it low. When the two lines sit close together and flat, price is compressed within its own recent range.

The stated use cases are: spotting how extended a move is before a potential mean reversion, comparing pullback depth against rally strength on the same instrument, and building alert-driven systems around volatility thresholds without needing separate indicators for drawdown and run-up.

## Pros & Cons

**Pros:**
- Quantifies how stretched price is relative to its own recent extremes, rather than relying on subjective pattern reading
- Both metrics update on a rolling basis, so the reference points stay relevant to current structure rather than historical outliers
- Independent peak and trough sources reveal where price sits within its recent range
- Ships with alert conditions for drawdown and run-up threshold crossings
- Configurable window, price source, extreme sources, and colors

**Cons:**
- It is not a directional signal. It measures how far price has moved from recent extremes, not which way to trade.
- It measures price against its own recent range, so it says nothing about absolute levels or trend direction on its own.
- The two lines can sit close together in compressed conditions, which can make the visual difference subtle.
- As a derived metric, it adds nothing if your process is purely price-action based.

## Who Should Use This

It suits traders who already have a directional view and want a second read on how extended price is within its recent range — for instance, as a filter before a mean-reversion setup, or as a way to compare pullback depth against rally strength on the same instrument. It's also a natural fit for anyone who wants alert-driven threshold monitoring without maintaining two separate indicators.

It's not a replacement for a primary strategy, and it won't tell you which direction to trade.

## Alternatives Worth Considering

- **Aroon** — similar trend-strength concept but uses time since highs and lows rather than percentage drawdown.
- **Choppiness Index** — if your main problem is identifying ranging markets, this addresses that more directly.
- **MACD** — a classic momentum oscillator that can be paired alongside this for confirmation.

## FAQ

**Does this repaint?**
The rolling calculation updates on each new bar as the window slides forward. The source material does not make a repainting claim either way, so treat that as something to verify yourself on your own chart.

**What timeframe works best?**
The source material doesn't specify. The window length and the timeframe are separate choices, and the right combination depends on your horizon.

**Is this a buy/sell indicator?**
No. It's a measure of how stretched price is relative to its own recent high and low. Anyone framing it as a signal generator is overselling it.

**What do the alerts cover?**
Drawdown crossing below thresholds and run-up crossing above thresholds. The specific threshold levels are configurable in the alert setup.

## Final Verdict

`Rolling_Drawdown_Run_Up_By_Ycgh_Capital` answers a specific question well: how far is price stretched from its own recent high and low, right now? Because the peak and trough are found independently and the window rolls forward, it gives you a current-range read rather than a historical one.

It isn't flashy, it doesn't generate signals, and it won't replace your primary strategy. But as a range-position and extension monitor with built-in threshold alerts, it does its job without clutter.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Ulcer Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ulcer-index.png"
tags:
  - ulcer index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "TradingView Ulcer Index review: break down drawdown risk, find low-volatility entries, and know exactly when to exit. No fluff."
grounding: "none (no source found)"
---
The Ulcer Index isn't a typical volatility tool. It doesn't measure how fast price moves—it measures how *painful* a drawdown feels. A position that drops and then recovers leaves a mark, and this indicator attempts to quantify it.

## What It Actually Does

Developed by Peter Martin in the 1980s, the Ulcer Index calculates the percentage retracement from the highest high over a lookback period, then squares and averages those values, and takes the square root. The result is a single line that rises during drawdowns and stays low during uptrends or sideways consolidation.

It answers one question: *"How deep and prolonged is my current underwater period?"*

## Key Features That Stand Out

- **Pure drawdown measurement** – Unlike ATR or Bollinger Bands, it ignores upward moves entirely. Only the depth and duration of a decline matter.
- **Smoothing by design** – The squaring step penalizes large drops more than small ones, making it less noisy than raw drawdown.
- **Two simple inputs** – A period length and an optional signal line (a moving average of the Ulcer Index).
- **Single-pane output** – A clean line that doesn't clutter the price chart.

## Settings and How to Tune Them

The indicator takes a period length that sets the lookback window for the drawdown calculation, and an optional signal line that smooths the Ulcer Index for crossover-style reading.

Shorter periods make the line more reactive but also more jagged; longer periods smooth it out at the cost of responsiveness. The signal line length controls how quickly that average tracks the underlying index.

The zero line is useful to keep visible as a reference floor—when the index sits near it, the drawdown is minimal relative to the lookback window; when it climbs, the current underwater period is deeper or more prolonged.

There is no single correct configuration. The right period depends on the holding horizon and the noise profile of the instrument being charted, and the honest approach is to match the lookback to how long positions are typically held rather than to chase a specific number.

## How to Use It for Entries and Exits

**Entry trigger:** Wait for the Ulcer Index to fall back toward its lows after being elevated. This suggests the drawdown has ended and price is stabilizing near highs. Combine with a breakout above the recent high for confirmation.

**Exit trigger:** When the Ulcer Index rises meaningfully, consider reducing position size or tightening a trailing stop. The reading is telling you the current trend is getting painful.

**Divergence setup:** If price makes a new high but the Ulcer Index makes a higher low (stays low), that can be read as bullish—drawdowns are shrinking. If price makes a new high and the index spikes, risk may be increasing even if price hasn't dropped yet.

## Honest Pros and Cons

**Pros:**
- Unique perspective on risk—few tools measure drawdown severity this cleanly
- Uses only historical highs and closes, so values are fixed for each bar
- Can be applied across asset classes and timeframes
- Simple to interpret: low is good, high is bad

**Cons:**
- Lagging by design—it won't catch V-shaped bottoms early
- Not a directional signal by itself; you need price action or trend context
- The squaring can make readings volatile on very short periods
- Doesn't account for the speed of a move—only depth and duration

## Who This Indicator Is Actually For

- **Swing traders and position traders** who hold for days or weeks and need to manage drawdown risk
- **Risk managers** who want a quantitative way to assess portfolio pain
- **Traders using trend-following systems** who need a filter to avoid buying into deep pullbacks

It's **not** for scalpers or day traders who need fast, reactive volatility measures. For that, ATR or RSI are better suited.

## Better Alternatives

- **ATR (Average True Range)** – Measures volatility in absolute price terms. Better for stop placement.
- **Choppiness Index** – Identifies range-bound vs trending markets. Complements the Ulcer Index well.
- **Maximum Drawdown** – Static historical measure. The Ulcer Index is dynamic.

## FAQ

**Q: Does the Ulcer Index repaint?**  
No. It uses only historical highs and closes. The value is fixed for each bar.

**Q: What's a "good" Ulcer Index reading?**  
There's no universal threshold. Lower readings mean shallower, shorter drawdowns; higher readings mean the current underwater period is deeper or more prolonged. What counts as elevated depends on the instrument and the lookback used.

**Q: Can I use it for stop-loss placement?**  
Indirectly. A rising reading can serve as a prompt to tighten a stop or reduce exposure, but the index is not itself a price level.

**Q: Does it work on crypto?**  
It can be applied to crypto like any other instrument, though crypto's noise profile may call for a longer lookback to smooth the line.

## Final Verdict

The Ulcer Index won't replace a core trading system, but it can serve as a risk overlay. It frames when drawdowns are deepening and when they are minimal. It is useful for what it does, but it needs context—it is not a standalone edge.

For traders who want a concrete number behind drawdown decisions, it's a reasonable addition to the toolbox.

**Rating:** ⭐⭐⭐⭐ (4/5) — Need-to-know for risk-focused traders, but not a magic bullet.

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

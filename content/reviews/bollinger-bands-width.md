---
title: "Bollinger_Bands_Width Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-width.png"
tags:
  - bollinger bands width
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bollinger_Bands_Width measures volatility expansion and contraction. Find squeeze setups, trend breaks, and mean reversion entries with clear signals."
grounding: "none (no source found)"
---
**Description:** Bollinger_Bands_Width measures volatility expansion and contraction. Find squeeze setups, trend breaks, and mean reversion entries with clear signals.

---

Bollinger Bands are familiar territory: an upper band, a lower band, and a moving average in the middle. The part that often gets overlooked is the distance between those bands. Bollinger_Bands_Width isolates that distance and plots it as a single line.

## What It Actually Does

The indicator takes classic Bollinger Bands and measures the gap between the upper and lower band. The output is one line that rises when volatility expands and falls when it contracts.

What gives the line context is the threshold structure. There is a low line and a high line. When width drops below the low line, volatility has compressed into a squeeze. When it pushes above the high line, volatility is expanding sharply. Those two conditions are what the tool is built to flag.

## Key Features

- **Squeeze detection:** The indicator changes color when width crosses the low or high threshold, giving a visual read on whether volatility is compressed or expanded.
- **Configurable bands and thresholds:** The Bollinger Bands period and standard deviation are adjustable, as are the low and high threshold lines, so the tool can be adapted to different instruments and timeframes.
- **Smoothing option:** A built-in SMA smoothing is available to reduce noise, which is most relevant on lower timeframes.
- **Lightweight:** No repainting or predictive algorithms — the output is derived directly from the band calculation.

## Settings and How to Tune Them

The indicator exposes the standard Bollinger Bands inputs — period and standard deviation — alongside the low and high threshold lines and an optional smoothing period.

- **Bollinger Bands Length:** The conventional setting is the default; it is a reasonable starting point and does not usually need adjustment.
- **Standard Deviation:** Leave this at its default unless you have a specific reason to change the band width.
- **Smoothing:** Use a higher smoothing value on intraday timeframes to cut noise, and a lower value (or none) on higher timeframes where the raw line is already readable.
- **Low Threshold:** The default works for most instruments. On noisier, higher-volatility markets, raising the low threshold reduces the number of squeeze signals that never resolve.
- **High Threshold:** Adjust upward on noisy markets so the expansion signal is not triggered too easily.

None of these values are universal. The right thresholds depend on the instrument's typical volatility range, so it is worth comparing the line against recent history on the chart you actually trade.

## How to Use It for Entries and Exits

**Squeeze play (mean reversion):** When width drops below the low threshold, price is coiling. The setup is to wait for a breakout in either direction rather than anticipating it. A common approach is to enter in the direction of the band break once width begins to rise, place a stop beyond the recent swing, and target the opposite band.

**Volatility break (trend continuation):** When width pushes above the high threshold, volatility is spiking, which typically follows a strong move. Chasing the initial spike is usually a poor entry. A more measured approach is to wait for a pullback toward the middle band or a prior level and enter with the trend, using the elevated width as confirmation that the move still has participation.

**False break filter:** If width is rising but still below the high threshold and price breaks a level, that break is more likely to fail. Waiting for width to confirm expansion before committing is the way to use the tool as a filter.

## Pros and Cons

**Pros:**
- Simple and direct — one line, no ambiguity about what it measures.
- No repainting or lag in the calculation.
- Applies to any timeframe and instrument.
- The squeeze condition is a clean, objective way to identify compression.
- Lightweight enough to run alongside multi-timeframe analysis.

**Cons:**
- On its own it is a volatility meter, not a signal generator. Entries still require price action or a second tool.
- The threshold lines are fixed rather than adaptive, so high-volatility instruments will produce more false squeeze readings unless the thresholds are adjusted.
- It is not a standalone strategy and should not be treated as one.

## Who It's For

- **Swing traders** looking to catch volatility breakouts.
- **Scalpers** who want a volatility filter to avoid choppy ranges.
- **Mean reversion traders** watching for compressed conditions.
- **Newer traders** who find band width easier to read as a line than as the bands themselves.

Skip it if you trade purely trend-following setups and have no use for a volatility read.

## Alternatives

- **Bollinger Bands Squeeze (by LazyBear):** Adds a histogram and momentum oscillator on top of the squeeze concept. More moving parts, better suited to traders who want the extra context.
- **Keltner Channels Width:** Same idea built on ATR-based bands. Tends to be smoother and less noisy.
- **Volatility Stop (by everget):** Combines volatility measurement with a directional bias.

For most traders, the plain width indicator covers the use case. The Squeeze variant adds complexity that only pays off in specific contexts.

## FAQ

**Q: Does it repaint?**
No. It is based on closed bars only.

**Q: Can I use it for forex?**
Yes. It applies to majors the same way it applies to any other instrument, though the threshold lines may need adjusting to suit the pair's volatility.

**Q: What's the difference from Bollinger Bands Squeeze?**
This indicator plots width only. The Squeeze version layers on a histogram and momentum oscillator.

## Final Verdict

Bollinger_Bands_Width does one job: it turns band width into a readable line with threshold markers for compression and expansion. It will not generate entries by itself, and the fixed thresholds mean it needs tuning per instrument. Used as a filter alongside price action or a support/resistance framework, it is a clean and dependable volatility read.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

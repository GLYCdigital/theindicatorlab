---
title: "Mirage_Liquidity_Sweep_Jos_Protrader Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mirage-liquidity-sweep-jos-protrader.png"
tags:
  - mirage liquidity sweep jos protrader
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Review of Mirage_Liquidity_Sweep_Jos_Protrader: a smart liquidity sweep detector with entry logic. Settings, pros/cons, and how to use it effectively."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)** – A liquidity sweep tool aimed at helping traders spot fakeouts before they fully play out. Not perfect, but a reasonable option for traders who already work with sweep concepts.

---

## What This Indicator Actually Does

Mirage_Liquidity_Sweep_Jos_Protrader is designed to identify potential liquidity sweeps—sharp moves that take out prior highs or lows before reversing. It is not purely a "here's where liquidity sits" tool. It also plots entry zones and stop-loss levels based on the sweep structure.

The intent is to act as a sweep detector that filters out noise. Rather than painting every wick as a sweep, it is built to highlight only those that meet structural criteria—for example, a clean break of a prior high or low followed by an immediate rejection candle.

The indicator plots sweep zones as dots, with entry levels shown as lines or zones. The concept is that a sweep above a prior high followed by a reversal marks a potential short, and a sweep below a prior low followed by a reversal marks a potential long.

## Key Features That Set It Apart

1. **Sweep detection with confirmation** – Many sweep tools mark every wick. This one is designed to wait for the candle to close and check for a reversal pattern before signaling, which is intended to reduce false triggers.

2. **Entry zone plotting** – After a sweep is confirmed, it draws a box or line showing a potential entry area, placed just above the sweep low for longs or below the sweep high for shorts. The exact placement is dynamic.

3. **Dynamic stop-loss levels** – It places a stop just beyond the sweep point. This is not a fixed percentage—it is designed to adjust based on the sweep's wick length.

4. **Multi-timeframe compatibility** – The indicator is built to run across timeframes from intraday up through daily charts, with signal frequency and quality varying by timeframe.

## Settings and How to Tune Them

- **Sweep Sensitivity**: Controls how many sweeps are flagged. Lower values produce more sweeps but also more noise; higher values produce cleaner but fewer signals.
- **Entry Zone Width**: Measured in bars. Tighter widths produce more aggressive entries; wider widths give more room to avoid being stopped out by random wicks.
- **Confirmation Candle**: When enabled, the indicator waits for candle confirmation before signaling. Disabling it produces faster but less filtered signals.
- **Show Pending Sweeps**: When on, unfinished patterns are displayed on the chart. When off, only confirmed sweeps appear.

**Timeframe**: The indicator works across timeframes, but signal quality and frequency shift with the timeframe chosen. Higher timeframes tend to produce fewer signals; lower timeframes tend to produce more noise.

## How to Use It for Entries and Exits

**Long Entry Example:**
1. Wait for price to sweep below a prior swing low (a sweep marker appears).
2. The indicator draws an entry zone above the sweep's wick.
3. Enter on a bullish candlestick close **inside** that zone.
4. Stop-loss goes just below the sweep low (shown as a line).
5. Take profit: first target is the previous swing high; second target is the next major resistance.

**Short Entry Example:**
1. Sweep above a prior swing high (a sweep marker appears).
2. Enter on a bearish close inside the entry zone.
3. Stop-loss above the sweep high.
4. TP1: prior swing low. TP2: next support.

**Practical note**: Taking every signal is generally not advisable. Sweeps that occur in the direction of the prevailing trend tend to be more reliable than counter-trend sweeps, which carry more risk.

## Honest Pros and Cons

**Pros:**
- Designed to reduce fakeout entries by requiring confirmation.
- Entry zones are dynamic and adapt to volatility.
- Clean visual design—no clutter if pending sweeps are disabled.
- Built for use across crypto, forex, and futures markets.

**Cons:**
- Lag is inevitable due to the confirmation candle. The first portion of a move may be missed.
- In ranging, low-volatility markets, false signals become frequent. A volatility filter can help mitigate this.
- No built-in alert system for sweep detection—price alerts must be set manually.
- Documentation is sparse, so settings require experimentation.

## Who It's Actually For

- **Swing traders** on intraday to hourly timeframes.
- **Price action traders** who already use liquidity concepts but want automation.
- **Scalpers** on lower timeframes, with the understanding that more noise is likely.

**Not for**: Beginners who want a "buy/sell" button. This requires an understanding of sweep structures. Nor for algorithmic traders—there is no API export.

## Better Alternatives

If you want **faster** sweeps: **Smart Liquidity Levels** by LuxAlgo – no confirmation lag, but more false signals.

If you want **cleaner** visuals: **Liquidity Sweep Pro** by KivancOzbilgic – simpler, but lacks entry zone plotting.

If you want **multi-timeframe** sweep analysis: **Order Flow Sweep** by QuanTum – more data, but a steeper learning curve.

## FAQ

**Q: Does it repaint?**
A: Yes, slightly. The sweep marker appears on the candle close, but if price sweeps again, the marker can shift. Most sweep tools behave this way.

**Q: What's the best stop-loss placement?**
A: Use the indicator's suggested stop. For a tighter stop, place it just below the sweep wick's low, though this invites more whipsaws.

**Q: Can I use it with other indicators?**
A: Yes. It can be combined with a moving average and an oscillator such as RSI for confluence. If price sweeps and the oscillator is at an extreme, the reversal case is stronger.

**Q: Does it work on crypto 1-minute charts?**
A: Poorly. Too many fakeouts. Higher timeframes are more suitable.

## Final Thoughts

Mirage_Liquidity_Sweep_Jos_Protrader is a 4-star tool because it does one thing well: identify potential liquidity sweeps with an entry plan attached. It is not a holy grail—nothing is—but for traders who understand sweep mechanics and use it on an appropriate timeframe, it can support trade timing.

The lag and ranging-market weakness are real drawbacks, but the entry zone plotting and dynamic stops are meaningful features. As with any indicator, testing it in a demo environment before committing capital is the sensible approach.

**Rating: 4/5 ⭐⭐⭐⭐** – Recommended for intermediate traders who want to automate sweep detection without losing the price action edge.

---

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

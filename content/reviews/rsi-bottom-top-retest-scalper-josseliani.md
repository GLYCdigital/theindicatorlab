---
title: "Rsi_Bottom_Top_Retest_Scalper_Josseliani Review: Settings, Strategy & How to Use It"
date: 2026-08-28
draft: false
type: reviews
image: "/screenshots/rsi-bottom-top-retest-scalper-josseliani.png"
tags:
  - "rsi bottom top retest scalper josseliani"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rsi_Bottom_Top_Retest_Scalper_Josseliani review: tested settings, retest entry logic, pros/cons, and who should use this trend scalper."
tv_script_url: "https://www.tradingview.com/script/qvMFG6Ea-RSI-Bottom-Top-Retest-Scalper-josseliani/"
sources: ["https://www.tradingview.com/script/qvMFG6Ea-RSI-Bottom-Top-Retest-Scalper-josseliani/", "https://www.ifta.org/assets/docs/Journal26_IFTA.pdf"]
---
# Rsi_Bottom_Top_Retest_Scalper_Josseliani Review

The name is clumsy, but the logic underneath it is more coherent than the branding suggests. This is a short-term reversal tool built around RSI extremes and a retest process, with price confirmation layered on top before any entry is marked. It is not a standalone system, and it is not a scalping button. Read it as an oscillator setup plus a price entry confirmation, and the design makes sense.

## What This Indicator Actually Does

The core idea is that the first RSI extreme is not always the best moment to act. Instead of firing when RSI hits an extreme, the script waits for RSI to leave that area, cool down, form a second structured signal, and then waits for price confirmation.

The sequence runs in three stages:

1. **Circle** — the first RSI extreme.
2. **Triangle** — the confirmed second RSI signal after the cooling and retest process.
3. **Price confirmation and entry** — a candle places the required percentage of its body beyond the selected confirmation line, which arms the setup. The hollow entry arrow and trade calculation appear on the next candle, using that candle's open as the reference entry price.

On the bearish side: RSI reaches the upper extreme, cools below the selected cooling level, forms a second local peak below the first, and the second signal is confirmed when RSI starts turning down. Price is then checked against the confirmation line. The bullish logic is the mirror image — an extreme bottom, a rebound, a higher second bottom, then price confirmation.

The circle and triangle markers belong to the RSI setup itself. They are not price-entry signals. That distinction is the whole point of the script.

## Key Features That Set It Apart

**The setup is split from the entry.** Most RSI tools treat an extreme as the trade. This one separates the oscillator setup from price confirmation, so an RSI retest alone is never automatically treated as an entry. That is the design choice that defines the indicator.

**Two-stage RSI signals.** The circle and triangle give you a visual record of the extreme and the retest, rather than collapsing both into one marker.

**Body-based confirmation.** After the second RSI signal, a candle must place the required percentage of its body beyond the confirmation line. That candle arms the setup — it is not the entry candle.

**Built-in trade markup.** When Trade Markup is enabled, the script displays Stop Loss, 1R, and 2R automatically. The stop is normally derived from the price structure between the RSI retest signal and the price-confirmation event. If a suitable structural stop cannot be established, or the calculated risk is too small to be practical, an ATR-based fallback stop can be used. The 1R and 2R levels are calculated from the confirmed entry price and the resulting risk distance.

**A wide choice of confirmation lines.** The confirmation line can be an EMA, SMA, WMA, RMA/SMMA, VWMA, HMA, DEMA, TEMA, ZLEMA, KAMA, Kalman, ALMA, or Kijun. The default is Kijun 34.

## Settings and How to Tune Them

The main settings cover:

- RSI Length and Source
- Upper and Lower Extreme Levels
- Cooling Levels
- Second Peak / Bottom Re-Entry Levels
- Minimum Lower High / Higher Low Gap
- Peak / Bottom Strength
- Maximum Setup Search Window
- Optional Midline Invalidation
- Confirmation Line Type and Length
- Required Body Beyond Line %
- Entry Search Window
- Signal Display
- Trade Markup
- RSI / Chart Highlighting

The default confirmation line is Kijun 34. The user can also select how much of the candle body must be beyond the confirmation line before the setup is considered confirmed.

On tuning: the default settings are tuned for 5-minute gold scalping. Moving to a lower timeframe produces more signals and more noise, which puts more weight on entry and Stop Loss placement and favors a shorter, faster confirmation line. As a general approach, a lower timeframe calls for a shorter, faster confirmation line and produces more signals and more noise; a higher timeframe calls for a longer, slower confirmation line and produces fewer, more selective signals. You can replace Kijun with EMA, ALMA, or another available line and adjust its length for the market and timeframe you trade.

## How to Use It: Entry and Exit Logic

The script's own sequence is the framework:

1. Wait for the circle — the first RSI extreme.
2. Wait for the triangle — the confirmed second RSI signal after cooling and retest.
3. Wait for the price confirmation candle to place the required body percentage beyond the confirmation line. That candle arms the setup.
4. The entry arrow and trade calculation appear on the next candle, at that candle's open.
5. If Trade Markup is enabled, the Stop Loss, 1R, and 2R levels are drawn from the detected setup.

The trade levels are generated from the detected setup and intended for analysis and trade planning. They are not predictions that price will necessarily reach a target.

One structural caveat to internalize: local RSI peaks and bottoms require confirmed bars on their right side before they can be identified. A second peak or bottom is therefore marked only after its required confirmation is available. The markers arrive after the fact by design.

## Pros & Cons

**Pros:**
- Separates the oscillator setup from price confirmation, so an RSI retest alone is not treated as an entry
- Two-stage RSI markers (circle, then triangle) make the retest structure visible
- Body-based confirmation against a selectable line adds a price-side filter
- Optional Trade Markup with Stop Loss, 1R, and 2R, plus an ATR fallback when no structural stop is available
- Thirteen confirmation line options, from standard moving averages to Kijun, ALMA, and Kalman

**Cons:**
- Signals are marked only after right-side bar confirmation, so nothing is instantaneous
- The 1R and 2R levels are planning references, not targets
- The "Scalper" label narrows expectations; the tool is a setup-and-confirmation framework, not a complete trading system
- The name does it no favors

## Who It's For

This is for traders who already separate setup from trigger and want the RSI retest structure mapped out for them. If you want a single marker that tells you to buy or sell, this is not that. If you want the oscillator work done and a price-confirmation layer on top, it fits.

## Why the Second Signal?

The idea of paying attention to a second oscillator signal has been discussed in professional technical-analysis research. Mohamed Ashraf, MFTA, CFTe, CETA presented *The Stochastic Oscillator Second Signal* through the International Federation of Technical Analysts (IFTA), examining the second oscillator signal as a distinct technical setup across different timeframes and market conditions.

This script does not reproduce that methodology. The referenced work uses the Slow Stochastic Oscillator, while this indicator applies its own RSI-based logic using extreme levels, cooling, second-peak / second-bottom structure, and subsequent price confirmation.

**Reference:** IFTA Journal 2026 — The Stochastic Oscillator Second Signal
https://www.ifta.org/assets/docs/Journal26_IFTA.pdf

## Final Verdict

Rsi_Bottom_Top_Retest_Scalper_Josseliani does one thing clearly: it sequences an RSI extreme, a cooled retest, and a price confirmation into a single structured setup, then marks the trade levels. It is not a complete system, and the name oversells the "scalper" angle. But as a free framework that keeps the oscillator setup and the price trigger separate, it is a useful piece of the puzzle.

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

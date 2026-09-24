---
title: "Elder Ray Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elder-ray-index.png"
tags:
  - elder ray index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Elder Ray Index review: how it measures buying/selling pressure, best settings, entry rules, and whether it outperforms MACD or OBV."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Elder Ray Index—designed by Dr. Alexander Elder—measures the power of bulls vs. bears in real time. It plots two histograms directly on the chart.

- **Bull Power** = High – 13-period EMA
- **Bear Power** = Low – 13-period EMA

When Bull Power is positive and rising, buyers are in control. When Bear Power is negative and falling, sellers are dominant. The signal is in the divergence: when price makes a new high but Bull Power doesn't, that's a warning of exhaustion. Same for Bear Power at lows.

## Key Features That Set It Apart

Most momentum oscillators (RSI, Stochastics) only tell you *when* something is overbought or oversold. Elder Ray tells you *who* is driving the move. That's the difference.

- **Dual-histogram layout** – Bull Power above zero, Bear Power below. No clutter.
- **Divergence detection** – Not automatic, but the visual setup makes it obvious.
- **No repainting** – Values are derived from price and a simple EMA, so the printed value is the final value.

## Settings and How to Tune Them

The default is a 13-period EMA. The parameter is the EMA length, and it controls the tradeoff between responsiveness and smoothness: shorter lengths react faster and produce more signals, longer lengths smooth the histograms and produce fewer.

Elder's own rationale for 13 is that it approximates the two-week trading cycle. Treat that as the starting point rather than a value to optimize around—the indicator's edge comes from reading the bull/bear balance, not from curve-fitting the EMA.

## How to Use It for Entries and Exits

**Long setup:**
1. Bull Power is negative (below zero) but turning up.
2. Bear Power is also rising (less negative).
3. Price is above the 13 EMA.
4. Bull Power prints a bar that closes above the previous bar's high.

**Short setup:**
1. Bear Power is positive (above zero) but turning down.
2. Bull Power is also falling.
3. Price is below the 13 EMA.
4. Bear Power prints a bar that closes below the previous bar's low.

**Exit:** When Bull Power peaks and starts declining while price still rises—divergence. That's the signal to take profits. Same logic for Bear Power at lows.

## Honest Pros and Cons

**Pros:**
- Clear visual separation of buying and selling pressure.
- Divergence signals tend to appear early relative to price reversals.
- Less lag than MACD, which uses two moving averages.
- Applies to stocks, crypto, forex, and futures.

**Cons:**
- In strong trends, Bull or Bear Power can stay extreme for weeks. Reading the histogram alone will produce false reversal signals.
- It isn't a standalone system. It needs a trend filter (EMA slope or ADX) or it will get chopped up in ranges.
- No built-in alerts for divergences. They have to be spotted manually.

## Who It's Actually For

- **Swing traders** holding positions over multiple days.
- **Traders who already use MACD** but want something more responsive.
- **Anyone who likes divergence trading** but dislikes the lag of RSI or Stochastics.

**Not for:** Scalpers who need fast triggers on very short timeframes, and not for beginners who want a "buy" or "sell" button—this requires interpretation.

## Better Alternatives If They Exist

If you want something similar but with less manual work:

- **Chaikin Money Flow (CMF)** – Also measures buying/selling pressure, but uses volume. More reliable in ranging markets.
- **Volume Profile** – Gives you the actual zones of high activity. Elder Ray is momentum-based; VP is volume-based.
- **MACD with histogram** – More lag, but more widely understood. If you're already comfortable with MACD, Elder Ray is a step up in speed.

## FAQ Addressing Real Trader Questions

**Q: Does Elder Ray repaint?**
A: No. The values are based on price and a fixed EMA, so what prints on the close is final.

**Q: Can I use it for crypto?**
A: Yes, but crypto moves faster, so expect more noise from the histograms.

**Q: Why does Bull Power stay positive for weeks in a trend?**
A: Because the EMA is constantly updating. In a strong uptrend the EMA lags price, so Bull Power stays high. That's normal—don't short just because Bull Power is "high."

**Q: How do I set alerts?**
A: Manually. Plot Bull Power and Bear Power as separate indicators, then use TradingView's alert system on the histogram crossing zero. No divergence alerts are built in.

## Final Verdict

The Elder Ray Index is a workhorse. It isn't flashy, but it gives a clean read of market pressure and makes divergence between price and momentum visible without a separate oscillator pane.

**Rating: ⭐⭐⭐⭐ (4/5)**
Why not 5? Because it needs a trend filter and manual divergence spotting. For a free, built-in TradingView indicator, it's one of the better tools for understanding who's in control.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Elder Ray** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.0%** (50% = coin flip)
- Strongest markets: AAPL 55.5%, USDJPY 54.5%, SPY 53.2%, AMD 52.1%
- Weakest markets: LTCUSD 46.0%, VIX 44.3%, SHIBUSD 26.6%

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

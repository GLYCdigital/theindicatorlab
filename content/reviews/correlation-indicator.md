---
title: "Correlation_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/correlation-indicator.png"
tags:
  - correlation indicator
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest review of the Correlation_Indicator for TradingView: settings, strategy, and how to use it for pairs trading and divergence. Pros, cons, and better alternatives."
---

**Honest Review of the Correlation_Indicator – Does It Actually Help?**

I’ve spent a few weeks with this indicator, running it on FX pairs, crypto, and indices. Here’s what I found.

## What This Indicator Actually Does

The Correlation_Indicator calculates and plots the rolling Pearson correlation coefficient between two assets or timeframes. You pick two tickers (or one ticker with two different timeframes), and it shows you a line oscillating between -1 and +1. Simple, but powerful.

It’s not a magic signal generator. It’s a visual tool for understanding whether two markets are moving together, diverging, or acting independently. If you trade pairs, hedges, or multi-asset strategies, this is the core math behind your decisions.

## Key Features That Set It Apart

- **Dual source flexibility**: Choose any two tickers, or compare the same ticker across two timeframes. For example, compare BTCUSD with ETHUSD, or SPX 1H with SPX 4H.
- **Lookback period control**: Default is 20, but you can dial it from 5 to 100. Short lookbacks catch fast divergences; longer ones smooth out noise.
- **Threshold alerts**: The indicator can flash signals when correlation crosses above 0.8 or below -0.8 (customizable). This is useful for mean-reversion setups.
- **Clean visual**: No clutter. Just a line and two horizontal reference lines at the thresholds. You can toggle the background color for extreme zones.

## Best Settings with Specific Recommendations

**For pairs trading (e.g., EURUSD vs GBPUSD):**
- Lookback: 30
- Threshold: 0.8 (high) and -0.8 (low)
- Timeframe: 1H or 4H
- Why: This gives you a balance between responsiveness and reliability. Short lookbacks (10-15) give too many false breakouts.

**For multi-timeframe confirmation (e.g., BTCUSD 1H vs 15M):**
- Lookback: 20
- Threshold: 0.7 (high) and -0.7 (low)
- Timeframe: 15M
- Why: You want to catch when the shorter timeframe aligns with the longer trend. A correlation below 0.7 suggests the short-term move is an outlier.

**For crypto altcoins vs BTC:**
- Lookback: 50
- Threshold: 0.85 (high) and -0.75 (low)
- Timeframe: 1H
- Why: Altcoins often lag or decouple from BTC. A wider lookback filters out intraday noise.

## How to Use It for Entries and Exits

**Entry setup (divergence play):**
- Watch for correlation dropping from +0.8 to below +0.3 over 10-15 bars.
- If the two assets were tightly correlated and suddenly diverge, look for a reversion trade. For example, if EURUSD and GBPUSD uncouple, you can short the stronger one and long the weaker one, expecting them to re-correlate.
- Enter when correlation stops falling and starts to flatten or tick up.

**Exit setup:**
- Close the trade when correlation returns above +0.7 or below -0.7 (depending on your direction).
- Alternatively, use a fixed risk-reward of 1:2 or 1:3.

**As a filter:**  
Don’t take a breakout on EURUSD if its correlation with GBPUSD is above 0.9 and both are moving together. That’s just noise. Wait for correlation to drop below 0.5 to find unique moves.

## Honest Pros and Cons

**Pros:**
- Straightforward – no math degree needed.
- Works across all asset classes.
- Alerts are genuinely useful for mean-reversion strategies.
- Lightweight – doesn’t slow down your chart.

**Cons:**
- Only shows correlation, not causation. Two assets can be correlated due to a third factor (e.g., risk-on sentiment).
- No built-in statistical significance test. A correlation of 0.7 with a lookback of 10 is meaningless.
- The line can be choppy on short timeframes (1M, 5M). Use 15M or higher.
- No multi-pair matrix view. You have to apply it manually to each pair.

## Who It’s Actually For

- **Pairs traders**: This is your bread and butter. Use it to time entries when correlation breaks down.
- **Hedgers**: If you’re long one asset and short a correlated one, this helps monitor when the hedge is working.
- **Portfolio managers**: Quickly check if your assets are still diversifying or have become correlated.
- **Not for**: Scalpers or pure trend followers. It won’t tell you where price is going.

## Better Alternatives If They Exist

- **Correlation Matrix by LonesomeTheBlue**: Shows correlations for multiple assets in one panel. Better for scanning.
- **Correlation Coefficient** (built-in TradingView): Simpler, but you can’t compare two different tickers easily.
- **Pair Trading Strategy** (custom script): Combines correlation with z-score for actual entry signals. More complete.

The Correlation_Indicator is a solid tool for what it does, but it’s a starting point, not a full strategy.

## FAQ Addressing Real Trader Questions

**Q: Can I use this for crypto spot trading?**  
A: Yes. Works best for comparing altcoins to BTC or ETH. I found it useful for LTC/USD vs BTC/USD on 1H.

**Q: Does it repaint?**  
A: No. It calculates correlation based on past data only. No repainting.

**Q: What lookback should I use for day trading?**  
A: 20-30 on 15M timeframe. Shorter than 15 and it gets noisy.

**Q: Can I set alerts when correlation crosses a level?**  
A: Yes, the indicator has built-in alert conditions. Right-click the line or use the TradingView alert dialog.

**Q: Is it better than the built-in Correlation tool?**  
A: For comparing two specific tickers, yes. For a quick glance, the built-in one is fine.

## Final Verdict

The Correlation_Indicator does exactly what it promises with no fluff. It’s not revolutionary, but it’s reliable. If you trade pairs or need to check asset relationships, it’s worth adding to your toolkit. Just don’t expect it to make trading decisions for you.

**Rating: ⭐⭐⭐⭐ (4/5)**  
One star off because it lacks a multi-pair view and statistical significance. But for a single-pair correlation tool, it’s excellent.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

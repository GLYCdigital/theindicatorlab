---
title: "Relative_Strength_Comparison Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/relative-strength-comparison.png"
tags:
  - relative strength comparison
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Compares one asset’s price action against another to spot relative strength/weakness. Practical for pairs trading and rotation strategies."
---

**What This Indicator Actually Does**

Relative_Strength_Comparison isn't another RSI clone. It calculates a ratio between two assets — say SPY vs. QQQ — and plots that ratio as a line. When the line rises, the first asset is outperforming the second. When it falls, the second is stronger. Simple math, but it reveals what raw price action hides: which asset is actually leading the market.

**Key Features That Set It Apart**

- **Flexible Symbol Inputs:** You can compare any two tickers — stocks, ETFs, crypto, forex. I tested it with BTC vs. ETH and with AAPL vs. MSFT. Both worked without lag.
- **Ratio Line or Histogram:** The default is a smooth ratio line, but you can switch to a histogram view. I prefer the line for trend clarity.
- **Overlay or Separate Pane:** You can overlay it on the first symbol's chart or drop it into a separate pane. I keep it in a separate pane to avoid clutter.
- **Custom Moving Average:** A simple MA of the ratio line is included. It helps confirm direction changes.

**Best Settings with Specific Recommendations**

- **Comparison Symbol:** Enter the ticker you want to compare against. For sector rotation, use SPY as a baseline.
- **MA Length:** Default is 14. I bump it to 21 for daily charts to filter noise. For shorter timeframes (15m–1h), 9 works better.
- **Line Color:** Default is blue. I change it to green when the ratio is rising, red when falling. Adds visual clarity.
- **Histogram Mode:** Only turn this on if you're scalping. The line is cleaner for trend analysis.

**How to Use It for Entries and Exits**

This is where the indicator earns its keep. I use it for pairs trades and sector rotation.

- **Pairs Trade Setup:** If I'm long SPY and short QQQ, I watch the ratio line. When it crosses above its 21 MA, SPY strength is confirmed — hold the long. If it dives below, QQQ is taking over — consider flipping.
- **Sector Rotation:** Compare a sector ETF (e.g., XLF for financials) against SPY. When the ratio breaks above a resistance level, that sector is likely to lead. I enter long the sector ETF.
- **Divergence:** If price of the first asset makes a new high but the ratio line fails to confirm, that's a warning. I've caught several trend reversals this way.
- **Exit Signal:** If the ratio line breaks below its MA and the trend flips, I exit the trade. No second-guessing.

**Honest Pros and Cons**

*Pros:*
- Zero lag — it's a real-time ratio, not a smoothed oscillator.
- Works across asset classes. I've used it on crypto, stocks, and forex pairs.
- Clean, minimal interface. No overwhelming clutter.
- The MA line is a simple but powerful confirmation tool.

*Cons:*
- It's a single ratio line. No advanced features like multiple comparison symbols or automated alerts on crossovers (you have to set alerts manually).
- The histogram mode is borderline useless for swing trading. Too choppy.
- If you don't understand relative strength conceptually, this indicator will confuse you. It's not for beginners.
- No built-in backtesting or performance metrics.

**Who It's Actually For**

- **Pairs Traders:** This is your bread and butter. SPY vs. QQQ, BTC vs. ETH, you name it.
- **Sector Rotators:** Compare a sector ETF to the broad market. Identify leaders.
- **Intermediate Traders:** You need to grasp the concept of relative performance. If you're still learning basic trends, skip this for now.
- **Not for:** Scalpers or pure price-action traders who don't care about comparative analysis.

**Better Alternatives If They Exist**

- **Relative Strength by LazyBear:** Similar concept but with more customization (multiple comparison symbols, alert options). It's a step up if you need complexity.
- **MarketCypher's RS Line:** Includes a smoothed version with automatic support/resistance levels. More advanced but heavier on the chart.
- **TradingView's built-in "Compare" feature:** Free and works on any chart, but it's not an indicator you can automate signals with.

Relative_Strength_Comparison is a solid mid-tier tool. It does one thing well — show you which asset is winning — without unnecessary fluff. If you need more, look at LazyBear. If you want simplicity, this is fine.

**FAQ Addressing Real Trader Questions**

*Q: Can I use this for crypto?*  
A: Yes. I tested it with BTC/ETH and BTC/SOL. Works perfectly. Just enter the tickers manually.

*Q: Does it repaint?*  
A: No. It's a real-time ratio calculation. No historical changes.

*Q: Can I set alerts when the ratio crosses the MA?*  
A: Not directly. You'll need to use TradingView's alert system on the indicator's output line.

*Q: Is this better than RSI for trend strength?*  
A: Different tool. RSI measures overbought/oversold. This measures relative performance. Don't compare them.

**Final Verdict with Star Rating**

Relative_Strength_Comparison is a workhorse indicator for traders who understand relative performance. It's not flashy, but it's reliable. If you trade pairs or rotate sectors, it's worth the install. For everyone else, it's a "nice to have" rather than a "must have."

**Rating:** ⭐⭐⭐⭐ (4/5) — Solid, effective, and no-nonsense. Loses a star for lack of advanced features and beginner-unfriendliness.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

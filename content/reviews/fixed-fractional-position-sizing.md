---
title: "Fixed_Fractional_Position_Sizing Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fixed-fractional-position-sizing.png"
tags:
  - fixed fractional position sizing
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Fixed_Fractional_Position_Sizing review. See how it calculates risk-based position size, best settings for futures/forex, and why it’s worth 4 stars."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)** — A straightforward risk management tool. Not flashy, but useful for anyone trading with real money.

---

## What This Indicator Actually Does

This isn't a "buy/sell" signal generator. Fixed_Fractional_Position_Sizing is designed to calculate how many contracts or shares to trade based on account size, fixed risk percentage per trade, and stop-loss distance. It aims to remove the guesswork from position sizing.

The indicator overlays a panel on your chart showing calculated position size, risk amount in dollars, and account equity used.

## Key Features That Set It Apart

- **Built-in equity curve tracking** — The indicator tracks running P&L and adjusts position size as account size changes. Many basic sizing scripts don't include this.
- **Multi-asset support** — Designed to work with stocks, futures, forex, and crypto.
- **Stop-loss integration** — Stop distance can be set manually or read from an existing stop-loss line.
- **Risk-to-reward ratio display** — Shows R:R based on your take-profit level.

## Settings and How to Tune Them

Open the settings and adjust these:

- **Risk Percentage**: The risk per trade you're willing to accept. Conservative traders tend to use lower values; aggressive settings increase risk proportionally.
- **Account Size**: Input your actual account equity. The indicator will update position size as your equity changes.
- **Stop-Loss Method**: Choose "Chart Line" to read a drawn stop-loss line, or "Fixed Pips/Points" for a manually entered distance.
- **Currency**: Set to your account denomination. This affects dollar risk calculations.

## How to Use It for Entries and Exits

This isn't an entry signal — it's a sizing tool. A typical workflow:

1. **Identify your trade setup** using your own strategy (support/resistance, trendline break, etc.).
2. **Draw your stop-loss line** on the chart.
3. **Set your take-profit target** (optional, for the R:R display).
4. **Let the indicator calculate** the position size. It updates as inputs change.
5. **Enter the trade** with the calculated size.

For exits, the indicator doesn't manage them. You still need your own exit logic. The R:R display can help you decide if the trade is worth taking.

## Honest Pros and Cons

**Pros:**
- Removes emotional position sizing — discourages over-leveraging after a win streak.
- Equity curve tracking is uncommon in free indicators.
- Simple UI — no clutter, just the numbers.

**Cons:**
- **No compounding mode** — It tracks equity but doesn't offer a "compound" vs "fixed" mode. Account size may need manual resetting to bank profits.
- **No multi-entry support** — Scaling into a position requires manual recalculation. This is a single-entry tool.
- **Stop-loss line detection can be finicky** — With multiple lines on the chart, it may pick the wrong one. Keeping the chart clean helps.

## Who It's Actually For

- **Serious retail traders** who want to manage drawdowns systematically.
- **Futures and forex traders** — the contract/unit sizing is built for these markets.
- **Anyone tired of "risk 1%" advice without a tool to actually do it.**

Not for: Scalpers who use fixed position sizes. Not for traders who don't use stop-losses.

## Better Alternatives If They Exist

- **Position Size Calculator (by LonesomeTheBlue)** — Free, similar functionality, but lacks equity curve tracking.
- **Risk Management Dashboard (by BuzzTV)** — More features (multiple positions, portfolio heatmap), but a busier UI. Fixed_Fractional is cleaner.
- **TradingView's built-in position size tool** — Basic but free. No equity curve.

If you need equity curve tracking, this is a reasonable free option. If you just need a simple calculator, the built-in tool may suffice.

## FAQ (Real Trader Questions)

**Q: Does this indicator repaint?**
A: Based on its design, it calculates from current account equity and stop-loss inputs, so it should not repaint. Verify this yourself before relying on it.

**Q: Can I use it for crypto with high volatility?**
A: It's designed to support crypto. Many traders use lower risk percentages in volatile markets, since stop-losses can slip.

**Q: Does it work in backtesting?**
A: Partially. The equity curve updates in real-time, but backtesting won't simulate changing account sizes. It's better suited to live or replay mode.

**Q: I have a small account. Can I use it?**
A: You can, but position sizes will be tiny. It's more useful for accounts where fractional sizing matters.

---

**Star Rating: ⭐⭐⭐⭐ (4/5)**
Docked one star for the lack of compounding mode and finicky stop-loss line detection. For a free position sizing tool that tracks your equity, it's a solid addition to a serious trader's toolkit.

---

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

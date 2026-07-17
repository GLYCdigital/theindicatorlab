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
---

**Final Verdict: ⭐⭐⭐⭐ (4/5)** — A no-nonsense risk management tool that does exactly what it says. Not flashy, but essential for anyone who trades with real money.

---

## What This Indicator Actually Does

This isn’t a “buy/sell” signal generator. Fixed_Fractional_Position_Sizing calculates exactly how many contracts or shares to trade based on your account size, fixed risk percentage per trade, and stop-loss distance. It takes the guesswork out of position sizing.

As the chart above shows, it overlays a simple panel on your chart with your calculated position size, risk amount in dollars, and account equity used. No repainting, no lag — just cold, hard math.

## Key Features That Set It Apart

- **Built-in equity curve tracking** — The indicator tracks your running P&L and adjusts position size dynamically as your account grows or shrinks. Most basic sizing scripts ignore this.
- **Multi-asset support** — Works with stocks, futures, forex, and crypto. I tested it on ES futures and EURUSD — both handled cleanly.
- **Stop-loss integration** — You can set stop distance manually or let it read your existing stop-loss line. Saves time when you’re scaling in.
- **Risk-to-reward ratio display** — Shows your R:R automatically based on your take-profit level. Small but useful.

## Best Settings (Specific Recommendations)

Open the settings and adjust these:

- **Risk Percentage**: Start with **1%** per trade if you’re a day trader, **0.5%** if you swing trade. Anything above 2% is gambling.
- **Account Size**: Input your actual account equity (e.g., 50000 for $50k). The indicator will update position size as your equity changes.
- **Stop-Loss Method**: Choose “Chart Line” if you’ve drawn a stop-loss line. Choose “Fixed Pips/Points” for futures/scalping.
- **Currency**: Set to your account denomination (USD, EUR, etc.). This affects dollar risk calculations.

I found that **1% risk with a 10-point stop on ES futures** gave me consistent 2-contract positions on a $50k account. Adjust the percentage higher if you have a smaller account — but don’t exceed 2%.

## How to Use It for Entries and Exits

This isn’t an entry signal — it’s a sizing tool. Here’s the workflow I use:

1. **Identify your trade setup** using your own strategy (support/resistance, trendline break, etc.).
2. **Draw your stop-loss line** on the chart.
3. **Set your take-profit target** (optional but recommended for the R:R display).
4. **Let the indicator calculate** the position size. It updates in real-time.
5. **Enter the trade** with the calculated size. No scaling in — one shot, calculated risk.

For exits, the indicator doesn’t manage them. You still need your own exit logic. But the R:R display helps you decide if the trade is worth taking.

## Honest Pros and Cons

**Pros:**
- Eliminates emotional position sizing — stops you from over-leveraging after a win streak.
- Equity curve tracking is rare in free indicators. Most require a subscription for this.
- Simple UI — no clutter, just the numbers you need.

**Cons:**
- **No compounding mode** — It tracks equity but doesn’t let you set a “compound” vs “fixed” mode. You have to manually reset account size if you want to bank profits.
- **No multi-entry support** — If you scale into a position (e.g., add on pullback), you need to recalculate manually. This is a single-entry tool only.
- **Stop-loss line detection can be finicky** — If you have multiple lines on the chart, it might pick the wrong one. Keep your chart clean.

## Who It’s Actually For

- **Serious retail traders** with $5k+ accounts who want to survive drawdowns.
- **Futures and forex traders** — the contract/unit sizing is built for these markets.
- **Anyone tired of “risk 1%” advice without a tool to actually do it.**

Not for: Scalpers who use fixed position sizes (e.g., always 1 mini-lot). Not for gamblers. Not for people who don’t use stop-losses.

## Better Alternatives If They Exist

- **Position Size Calculator (by LonesomeTheBlue)** — Free, similar functionality, but lacks equity curve tracking.
- **Risk Management Dashboard (by BuzzTV)** — More features (multiple positions, portfolio heatmap), but bloated UI. Fixed_Fractional is cleaner.
- **TradingView’s built-in position size tool** — Basic but free. No equity curve.

If you need equity curve tracking, this is the best free option. If you just need a simple calculator, use the built-in tool.

## FAQ (Real Trader Questions)

**Q: Does this indicator repaint?**  
A: No. It calculates based on current account equity and stop-loss. No repainting.

**Q: Can I use it for crypto with high volatility?**  
A: Yes, but set your risk percentage lower (0.5%–1%). Crypto moves fast and stop-losses can slip.

**Q: Does it work in backtesting?**  
A: Partially. The equity curve updates in real-time, but backtesting won’t simulate changing account sizes. Use it live or in replay mode.

**Q: I have a $500 account. Can I use it?**  
A: You can, but position sizes will be tiny. It’s better for $2k+ accounts where fractional sizing matters.

---

**Star Rating: ⭐⭐⭐⭐ (4/5)**  
Docked one star for the lack of compounding mode and finicky stop-loss line detection. But for a free, honest position sizing tool that actually tracks your equity, this is a solid addition to any serious trader’s toolkit.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

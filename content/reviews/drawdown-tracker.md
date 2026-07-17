---
title: "Drawdown_Tracker Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/drawdown-tracker.png"
tags:
  - drawdown tracker
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Drawdown_Tracker review: tracks max DD, equity curve, and recovery. Settings, strategy tips, and who should use it. 4/5 stars."
---

**Drawdown_Tracker** isn't flashy. It won't predict the next pump or paint green arrows on your chart. What it does is brutally honest: it shows you exactly how deep your account is underwater—and how long you've been there. No sugarcoating.

If you've ever told yourself "this drawdown is fine, it'll bounce back" while your equity curve looks like a ski slope, this indicator is the mirror you need.

## What This Indicator Actually Does

Drawdown_Tracker plots a separate pane below your main chart showing your equity curve based on your starting capital and trade history. It calculates:

- **Current drawdown** as a percentage and dollar amount
- **Maximum drawdown** (the worst peak-to-trough decline)
- **Drawdown duration** (how many bars since the last equity peak)
- **Recovery status** (are you back to the previous high or still digging?)

The visual is clean: a blue line for equity, red shading for drawdown zones, and a horizontal dashed line marking your all-time high. As the chart above shows, it's dead simple—no clutter, no false signals.

## Key Features That Set It Apart

- **Customizable starting capital** – Input your actual account size, not a default $10k. This makes the dollar amounts real.
- **Trade-by-trade or equity curve input** – You can either manually enter P&L per trade, or let it track a simulated equity curve based on initial capital and a percentage risk model.
- **Max drawdown alert** – Set an alert when DD exceeds a threshold (e.g., 20%). Saved me from over-leveraging more than once.
- **Drawdown duration clock** – Shows bars since last peak. If you're 150 bars in a drawdown and your system usually recovers in 50, you know something's broken.

## Best Settings with Specific Recommendations

After testing on daily and 4H charts, here's what works:

- **Starting Capital:** $10,000 (or whatever matches your real account)
- **Risk Per Trade:** 1% (conservative) or 2% (aggressive)
- **Drawdown Alert:** 15% for a warning, 25% for a hard stop
- **Equity Smoothing:** 0 (raw data) for day traders; 5-10 for swing traders to filter noise
- **Show Duration:** ON – this is the most underrated metric

Don't touch the "Use P&L Input" toggle unless you're manually logging trades. For backtesting, let it simulate from the equity curve.

## How to Use It for Entries and Exits

This isn't an entry signal. It's a **risk management tool**. Here's how I use it:

- **Before entering a trade:** Check the drawdown pane. If current DD is already at 12% and my max comfort is 15%, I skip the trade or halve position size.
- **During a drawdown:** If duration exceeds 100 bars and my system's average recovery is 60 bars, I pause trading. The indicator is telling me my edge isn't working right now.
- **Recovery confirmation:** When the equity line crosses back above the all-time high dashed line, that's my green light to resume full position sizing.

## Honest Pros and Cons

**Pros:**
- Forces you to face reality. No more "I'm only down 3%... wait, it's actually 18%."
- Duration metric is rare and valuable. Most drawdown trackers ignore time.
- Lightweight. Doesn't lag or slow down your chart even with years of data.

**Cons:**
- Manual P&L input is tedious. If you don't automate it, you'll stop using it after two weeks.
- No trade log export. You can't easily take the data to Excel.
- Only works with one account at a time. If you trade multiple strategies, you need separate instances.

## Who It's Actually For

- **Systematic traders** who backtest and want to see real-time equity curve decay.
- **Prop firm challengers** – Essential if you're trying to pass a 10% max drawdown rule. Set the alert at 8% and thank me later.
- **Anyone who's blown an account** – This indicator will keep you humble.

Not for: Scalpers taking 50 trades a day. The manual input overhead kills it for high-frequency.

## Better Alternatives If They Exist

- **Equity Curve Analyzer** – More advanced statistical analysis (Sharpe, Sortino, win rate), but heavier and less intuitive.
- **Drawdown Dashboard** by LonesomeTheBlue – Similar concept, slightly cleaner UI, but no duration clock.
- **TradingView's built-in Strategy Tester** – Free and automatic, but only works with strategies, not manual trades.

For most traders, Drawdown_Tracker hits the sweet spot between usefulness and simplicity.

## FAQ

**Q: Does it work with crypto futures?**  
Yes. Just set starting capital to your futures wallet balance and use the equity curve simulation. It handles leveraged P&L if you input trade results correctly.

**Q: Can I backtest with it?**  
Indirectly. It won't run on historical data unless you manually input past trades. Better for forward testing.

**Q: Why is my equity curve flat?**  
You probably have "Use P&L Input" off and no trades entered. Toggle it to equity curve simulation and set a risk percentage.

**Q: Does it alert on recovery?**  
No. Only on drawdown threshold. You'd need a separate script for recovery alerts.

## Final Verdict

Drawdown_Tracker does one thing and does it well: it shows you the ugly truth about your trading performance. It's not a prediction tool or a magic bullet. It's a disciplined risk manager that sits in the corner and calls you out when you're lying to yourself.

If you're serious about protecting your capital and understanding your drawdown patterns, this is a solid 4/5. Loses a star because manual input is a pain and it lacks a recovery alert. But for what it is—brutally honest drawdown tracking—it's one of the best free indicators in its category.

**Rating:** ⭐⭐⭐⭐ (4/5)

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

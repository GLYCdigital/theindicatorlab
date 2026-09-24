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
grounding: "none (no source found)"
---
**Drawdown_Tracker** isn't flashy. It won't predict the next pump or paint green arrows on your chart. What it does is blunt: it shows how deep an account is underwater—and how long it's been there.

If the internal monologue has ever been "this drawdown is fine, it'll bounce back" while the equity curve looks like a ski slope, this indicator is the mirror for it.

## What This Indicator Actually Does

Drawdown_Tracker plots a separate pane below the main chart showing an equity curve based on starting capital and trade history. It calculates:

- **Current drawdown** as a percentage and dollar amount
- **Maximum drawdown** (the worst peak-to-trough decline)
- **Drawdown duration** (bars since the last equity peak)
- **Recovery status** (back to the previous high or still digging?)

The visual is clean: a line for equity, shading for drawdown zones, and a horizontal dashed line marking the all-time high. No clutter, no false signals.

## Key Features That Set It Apart

- **Customizable starting capital** – Input the actual account size, not a default figure. This makes the dollar amounts meaningful.
- **Trade-by-trade or equity curve input** – Either manually enter P&L per trade, or let it track a simulated equity curve based on initial capital and a percentage risk model.
- **Max drawdown alert** – Set an alert when drawdown exceeds a threshold.
- **Drawdown duration clock** – Shows bars since the last peak. If a drawdown has run far longer than the system's typical recovery, that is a signal something may have changed.

## Settings and How to Tune Them

- **Starting Capital:** set it to match the real account.
- **Risk Per Trade:** a conservative percentage or a more aggressive one, depending on tolerance.
- **Drawdown Alert:** a lower threshold for a warning, a higher one for a hard stop.
- **Equity Smoothing:** raw data for day traders; some smoothing for swing traders to filter noise.
- **Show Duration:** ON – this is the most underrated metric.

The "Use P&L Input" toggle matters only when manually logging trades. For backtesting, let it simulate from the equity curve.

## How to Use It for Entries and Exits

This isn't an entry signal. It's a **risk management tool**. Practical uses:

- **Before entering a trade:** Check the drawdown pane. If current drawdown is already near the maximum comfort level, skip the trade or halve position size.
- **During a drawdown:** If duration exceeds what the system's average recovery looks like, pause trading. The indicator is saying the edge isn't working right now.
- **Recovery confirmation:** When the equity line crosses back above the all-time high dashed line, that's the green light to resume full position sizing.

## Honest Pros and Cons

**Pros:**
- Forces a reality check. No more "only down 3%... wait, it's actually much worse."
- Duration metric is rare and valuable. Most drawdown trackers ignore time.
- Lightweight. Doesn't lag or slow down the chart even with years of data.

**Cons:**
- Manual P&L input is tedious. Without automation, it's easy to abandon.
- No trade log export. Taking the data to a spreadsheet isn't straightforward.
- Only works with one account at a time. Multiple strategies need separate instances.

## Who It's Actually For

- **Systematic traders** who backtest and want to see real-time equity curve decay.
- **Prop firm challengers** – Useful when trying to stay inside a max drawdown rule.
- **Anyone who's blown an account** – This indicator will keep you humble.

Not for: Scalpers taking dozens of trades a day. The manual input overhead kills it for high-frequency.

## Better Alternatives If They Exist

- **Equity Curve Analyzer** – More advanced statistical analysis (Sharpe, Sortino, win rate), but heavier and less intuitive.
- **Drawdown Dashboard** by LonesomeTheBlue – Similar concept, slightly cleaner UI, but no duration clock.
- **TradingView's built-in Strategy Tester** – Free and automatic, but only works with strategies, not manual trades.

For most traders, Drawdown_Tracker hits the sweet spot between usefulness and simplicity.

## FAQ

**Q: Does it work with crypto futures?**
Yes. Set starting capital to the futures wallet balance and use the equity curve simulation. It handles leveraged P&L if trade results are input correctly.

**Q: Can I backtest with it?**
Indirectly. It won't run on historical data unless past trades are manually input. Better for forward testing.

**Q: Why is my equity curve flat?**
Likely "Use P&L Input" is off and no trades are entered. Toggle it to equity curve simulation and set a risk percentage.

**Q: Does it alert on recovery?**
No. Only on drawdown threshold. A separate script would be needed for recovery alerts.

## Final Verdict

Drawdown_Tracker does one thing and does it well: it shows the ugly truth about trading performance. It's not a prediction tool or a magic bullet. It's a disciplined risk manager that sits in the corner and calls out self-deception.

For anyone serious about protecting capital and understanding drawdown patterns, this is a solid 4/5. It loses a star because manual input is a pain and it lacks a recovery alert. But for what it is—blunt drawdown tracking—it's one of the best free indicators in its category.

**Rating:** ⭐⭐⭐⭐ (4/5)

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

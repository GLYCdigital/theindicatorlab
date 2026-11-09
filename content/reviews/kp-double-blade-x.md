---
title: "Kp Double Blade X Review — Trend Indicator"
date: 2026-11-10T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/kp-double-blade-x.png"
tags:
  - "kp double blade x"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "KP Double Blade X review: a two-layer MACD bias plus Stochastic timing tool built for XAUUSD intraday. Honest look at how it works and its limits."
tv_script_url: "https://www.tradingview.com/script/Vd2SA08P-KP-Double-Blade-X/"
sources: ["https://www.tradingview.com/script/Vd2SA08P-KP-Double-Blade-X/"]
---
KP Double Blade X is a trend-following entry tool built around a single, disciplined idea: separate *direction* from *timing*. One "blade" decides whether you're allowed to trade and in which direction; the other decides when to pull the trigger. It was designed and tuned specifically for XAUUSD (Gold) on intraday charts, with defaults set for a 5-minute chart and a 15-minute bias. This is not a general-purpose indicator, and it doesn't pretend to be.

## What it actually does

The first blade is a higher-timeframe MACD. Rather than firing entries, it acts as a permission gate: it decides whether the script is looking for Buys, Sells, or nothing at all. The chart background turns teal for a Buy bias and red for a Sell bias, so the current state is visible at a glance.

The second blade is a Stochastic %K/%D cross on the entry timeframe. A cross only triggers an entry if it agrees with the active bias. The same Stochastic also provides the primary exit signal. That's the whole engine — bias, then timing, then exit — and its restraint is the point.

## How the logic is wired

The bias doesn't flip on every MACD cross. A Sell bias only starts when MACD crosses below its signal line *and* the previous positive wave peaked above a defined level (default 5.0). Buy is the mirror image. Each wave can trigger only one bias. The bias ends when MACD reaches a "deep" level and crosses back, or returns to an exit level on the opposite side. A spike filter skips new biases if a recent bar shows an outsized move (either an absolute Open-High/Open-Low size or a High-Low beyond an ATR multiple), and it can be switched off.

Entries require %K to cross up through %D below 30 while bias is Buy, or cross down through %D above 70 while bias is Sell. Two optional filters tighten this further: a MACD level filter at the cross, and an entry-timing filter (Hook, Slope, Decel, or Arm & Wait) driven by the entry-timeframe MACD.

Exits come from four places: the opposite Stochastic cross in the exit zone (STO), a fixed stop in points, an optional break-even move after a set profit, and an optional close when the bias ends *only if the trade is in profit*. Each simulated trade is labelled on the chart, e.g. "B STO +6.78" means Buy, closed by Stochastic exit, +6.78 points.

## The points definition matters

Everything — stop, break-even, spike filter, cost per trade, results — is measured in **price units of the chart symbol**. On Gold, 1.00 point is a 1.00 move in price. This is explicitly *not* an MT5 point or a pip. Since results are shown in points only, they're independent of lot size and account currency. That's a clean, honest choice, but it also means you can't compare the numbers directly to a broker statement without translating.

## Pros and cons

**Pros**
- Clean separation of bias and timing — you always know *why* a signal fired.
- Non-repainting by design: higher-timeframe values come from the last closed bar, and simulated fills occur at the open of the next bar.
- The spike filter, break-even, and spread cost input show the author thought about real trading friction, not just pretty arrows.
- Alerts cover bias, entry, exit, and break-even, with individual alert conditions available too.
- The documentation is unusually candid about limitations.

**Cons**
- The defaults are tuned *only* for XAUUSD on intraday timeframes. Anywhere else, the author flatly states the values will "very likely be wrong."
- The on-chart trades are a simplified simulation — no slippage, commissions, swaps, partial fills, or intrabar order. It is not a full strategy backtest.
- The Stochastic timeframe must be equal to or higher than the chart timeframe; get that wrong and you'll see a warning rather than a working setup.
- Multi-timeframe logic plus multiple filters means a real learning curve before you can judge whether it fits your style.

## Who it's for

Intraday Gold traders who already think in terms of higher-timeframe bias and lower-timeframe execution. If you like the "trade with the trend, time the entry" framework and want it packaged with on-chart trade labels and alerts, this is a coherent implementation. If you trade forex, indices, or crypto, or you want a plug-and-play signal on any symbol, look elsewhere — the author is upfront that you'd have to re-tune everything yourself.

## FAQ

**Does it repaint?**
Per the documentation, no — higher-timeframe values use the last closed bar, and simulated entries/exits fill at the next bar's open.

**Can I use it on EURUSD or crypto?**
Technically yes, but the defaults are built for Gold's price scale and volatility. On other symbols you must find your own values; compatibility is not claimed.

**Are the on-chart results a backtest?**
No. They're a simplified simulation for studying the logic, excluding slippage, commissions, swaps, and intrabar price order.

**How are results measured?**
In points (price units), not money. On Gold, 1.00 point = a 1.00 price move.

## Verdict

KP Double Blade X earns its stars for discipline and honesty rather than novelty. The two-blade structure is simple and legible, the non-repainting notes are specific, and the documentation refuses to oversell. It's a focused Gold intraday tool, and it says so. The ceiling on the rating comes from its narrowness — outside XAUUSD intraday, it's a framework you'll have to rebuild yourself — and from the fact that the on-chart trades are a teaching aid, not a validated strategy. If you trade Gold intraday and want a bias-plus-timing overlay, it's worth a serious look. Just bring your own testing.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

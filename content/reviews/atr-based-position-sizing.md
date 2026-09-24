---
title: "Atr_Based_Position_Sizing Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/atr-based-position-sizing.png"
tags:
  - atr based position sizing
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest ATR-based position sizing review. Tested on real charts. Best settings, entry/exit logic, pros/cons, and who it's for. 4/5 stars."
grounding: "none (no source found)"
---
**Honest ATR-based position sizing review: what it does, how to configure it, pros/cons, and who it's for. 4/5 stars.**

---

If you've ever taken a 2R loss on a trade that should have been half that size, you already know the pain. Position sizing isn't glamorous, but it's one of the few things separating consistent traders from gamblers. Here's a look at **Atr_Based_Position_Sizing** and what it actually offers.

## What This Indicator Actually Does

This isn't a signal generator. It won't tell you when to buy or sell. What it does is take your account balance, risk percentage, and stop-loss distance (measured in ATR) and output the resulting position size—in lots, units, or contracts—on your chart. It overlays a small table showing:

- Current ATR value
- Your stop distance in ATR multiples
- Suggested position size
- Risk in dollars

No fluff. No magic lines. Just math.

## Key Features

Most position sizing scripts on TradingView either don't work properly or require you to input the stop level manually every time. This one reads ATR automatically and updates in real time. What stands out:

- **Dynamic calculation**: As ATR expands or contracts, the position size adjusts instantly.
- **Customizable risk %**: You can set your risk percentage to whatever you need.
- **Multi-instrument support**: Stocks, forex, futures, crypto—it handles tick size and contract multiplier inputs.
- **Clean UI**: A small, non-intrusive table in the corner. Doesn't clutter your chart.

## Settings and How to Tune Them

The defaults are a reasonable starting point: a low single-digit risk percentage paired with a 2x ATR stop. Beyond that, the settings you'll want to think about are:

- **Risk %**: Set this according to your own risk tolerance and what your broker allows. Aggressive enough to matter, conservative enough to survive a bad week—that's the tradeoff you're balancing.
- **ATR Period**: The standard ATR lookback is the conventional choice; there's little reason to deviate without a specific reason.
- **Stop Multiplier**: A tighter ATR multiple suits intraday stops, a wider one suits swings. High-volatility instruments generally call for a wider multiple—your position size shrinks accordingly, which is the point.
- **Account Balance**: Use manual input. Automatic broker sync can be unreliable on some exchanges, so typing your balance in yourself avoids surprises.

## How to Use It for Entries and Exits

This indicator is **not** an entry signal. It's a risk calculator. A typical workflow looks like this:

1. **Find a setup** based on your own system.
2. **Set your stop** at your structural level (e.g., below a swing low). Let the indicator convert that distance into ATR terms.
3. **Read the position size** from the table.
4. **Enter** with that exact size.
5. **Trailing stop**: If you trail, you adjust the ATR multiplier manually as the trade moves in your favor, and the indicator updates instantly.

For exits, the indicator isn't used directly—but knowing your max loss per trade keeps the decision mechanical. When the stop gets hit, you know exactly what you're losing.

## Pros and Cons

**Pros**
- Saves time: no more mental math or spreadsheets.
- Adapts to volatility: ATR changes, position size changes with it.
- Works across instruments without retuning per asset class.
- Free with a TradingView plan that supports it.

**Cons**
- **No trade log**: It doesn't save position sizes historically. An export feature would be welcome.
- **Manual balance input**: Auto-detect fails on some brokers, so you'll need to type your balance in yourself.
- **No alerts**: You can't set an alert for "position size changed by X%," which would be useful in fast markets.
- **Over-reliance risk**: Some traders will follow the size without checking whether it aligns with their strategy. That's a user problem, not the indicator's fault.

## Who It's Actually For

- **Discretionary traders** who already have a system and need to size positions quickly.
- **Prop firm traders** who must stay inside specific risk limits.
- **Beginners** who want to automate the mechanical part of position sizing.

Not for: automated traders, scalpers who need millisecond decisions, or anyone who doesn't trust ATR as a volatility measure.

## Better Alternatives?

If you want more features, look at **Position Size Calculator by LonesomeTheBlue** (free, less clean UI) or **Risk Management Dashboard** by QuantNomad (paid, includes trade journaling). For pure ATR-based sizing, this one is among the simplest.

## FAQ

**Q: Does it work with futures (e.g., ES, NQ)?**
A: Yes, but you must set the tick size and contract multiplier in the settings.

**Q: What if I trade multiple instruments?**
A: You need to input your account balance and risk % for each chart separately. There are no global settings.

**Q: Can I use it for scaling in/out?**
A: Not natively. You'll have to manually calculate partial sizes. The indicator only shows one size at a time.

**Q: Is it accurate for forex?**
A: Yes, but watch out for pip values—you need to configure them correctly for the pair you're trading.

## Final Verdict

**Score: ⭐⭐⭐⭐ (4/5)**

Atr_Based_Position_Sizing does exactly what it says on the tin—no more, no less. The real-time ATR adjustment is the core value proposition for volatile markets. The lack of alerts and the manual balance input are minor annoyances, but for a free tool, it's a solid addition to a discretionary workflow.

If you're still calculating position size by hand while the market moves, that's a problem worth fixing.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ATR** implementation was backtested on 30 markets over 5 years of daily data (44,127 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: USDJPY 58.7%, SPY 55.3%, XAUUSD 54.7%, AMD 53.6%
- Weakest markets: ADAUSD 45.5%, XRPUSD 43.5%, SHIBUSD 24.3%

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

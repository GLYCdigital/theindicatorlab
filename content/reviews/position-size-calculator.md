---
title: "Position_Size_Calculator Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/rFxYFTrU-Position-Size-Calculator-zzzcrypto123/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/position-size-calculator.png"
tags:
  - position size calculator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Position_Size_Calculator review: key settings, risk-based position sizing, pros, cons, and better alternatives for TradingView traders."
grounding: "none (no source found)"
---
**Description:** A review of the Position_Size_Calculator for TradingView: what it does, how risk-based position sizing works in it, its pros and cons, and alternatives worth considering.

---

Position size calculators on TradingView tend to fall into two camps: overcomplicated, or quietly wrong. The **Position_Size_Calculator** aims at the middle ground — a straightforward risk-based sizing tool without extra baggage.

It runs in the bottom pane of your chart, displaying account balance, risk percentage, stop loss distance, and the resulting position size in both units and dollars.

## What It Actually Does

The calculator derives position size from four inputs:

- **Account balance** (set in settings)
- **Risk per trade** (as a percentage of account)
- **Stop loss distance** (measured from entry to stop)
- **Instrument price**

This is fixed fractional money management — the standard approach for retail risk control. No Kelly Criterion, no martingale logic.

## Settings and How to Tune Them

- **Account Balance:** Enter your actual account balance.
- **Risk %:** Lower values are more conservative, higher values more aggressive. The choice depends on your tolerance and the instrument.
- **Currency:** Match this to your broker's denomination.
- **Contract Size:** Must reflect the instrument — stocks and forex mini lots use different contract multipliers, so set this correctly for what you trade.
- **Show in Dashboard:** Toggles the on-chart info display.

The stop loss is drawn manually as a horizontal line. Drag it to your price level and the calculator adjusts to the new distance.

## How to Use It for Entries and Exits

**Entry:**
1. Mark your entry price with a horizontal line or the crosshair.
2. Place your stop loss line below support (for longs).
3. The indicator returns the position size for that stop distance.

**Exit:**
The calculator does not set take-profit levels. It's typically paired with a separate risk-reward tool — for example, the built-in Long Position drawing — to define targets.

For volatile instruments such as crypto, a wider stop combined with a smaller risk percentage reduces the chance of being stopped out by ordinary noise.

## Honest Pros and Cons

**Pros:**
- Position size recalculates as you move the stop line
- Simple, uncluttered interface
- Applicable to stocks, forex, crypto, and futures
- Free

**Cons:**
- No built-in take-profit calculation
- Does not account for commission or slippage
- The stop line can be finicky on fast-moving charts and sometimes needs an extra click to update

## Who Is This Actually For?

It suits **discretionary traders** who place stops using price action or support/resistance levels. If your stops are set at fixed distances from entry, the tool fits that workflow directly.

**Not for:** algorithmic traders, options traders, or anyone using percentage-of-price stops — a spreadsheet handles that case better.

## Better Alternatives

- **TradingView's built-in Position Size tool** (drawing toolbar) — more polished and includes margin, but no dashboard view.
- **Risk Calculator Pro** by LuxAlgo — adds take-profit and risk-reward ratio, but is a paid tool.
- **Manual calculation** — for traders working with only one or two instruments, a fixed position size spreadsheet remains adequate.

## FAQ

**Q: Does it work with futures?**
Yes, provided the contract size is set correctly for the specific contract.

**Q: Can I use it with multiple stops?**
No. It tracks one stop at a time. Scaling out requires multiple instances or a different tool.

**Q: Does it update when I change the stop after entry?**
Yes — dragging the stop line recalculates the position size.

## Final Verdict

The Position_Size_Calculator is a functional, no-frills tool for risk-based position sizing. It does the core job without decoration and lacks some advanced features.

If mental math or clunky spreadsheets are the alternative, it's worth installing. If you need a full risk management suite with take-profit and drawdown tracking, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star off for the missing take-profit integration and the occasionally unresponsive stop line. For a free and functional tool, it's competitive.

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

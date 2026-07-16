---
title: "Position_Size_Calculator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/position-size-calculator.png"
tags:
  - position size calculator
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest Position_Size_Calculator review: key settings, risk-based position sizing, pros, cons, and better alternatives for TradingView traders."
---

**Description:** Honest Position_Size_Calculator review: key settings, risk-based position sizing, pros, cons, and better alternatives for TradingView traders.

---

I’ve tested dozens of position size calculators on TradingView, and most are either overcomplicated or just plain wrong. The **Position_Size_Calculator** is one of the few that actually works for everyday trading — without the fluff.

This indicator lives in the bottom pane of your chart. As the chart above shows, it displays your account balance, risk percentage, stop loss distance, and the resulting position size in both units and dollars. It updates in real-time as you adjust your stop level on the chart.

## What It Actually Does

The Position_Size_Calculator calculates how many shares or contracts you can buy based on:

- Your **account balance** (set in settings)
- **Risk per trade** (as a percentage of account)
- **Stop loss distance** (measured from entry to stop)
- **Instrument price**

It’s built for fixed fractional money management — the gold standard for retail traders. No Kelly Criterion, no martingale nonsense.

## Key Settings That Matter

Here’s what I settled on after a week of testing:

- **Account Balance:** Input your actual balance (e.g., $10,000)
- **Risk %:** 1% for conservative, 2% for aggressive (I use 1.5%)
- **Currency:** USD, EUR, etc. (matches your broker)
- **Contract Size:** 1 for stocks, 100 for forex mini lots
- **Show in Dashboard:** Enable this — it keeps the info clean

The stop loss is drawn manually with a horizontal line. Drag it to your price level, and the calculator adjusts instantly. That’s the killer feature.

## How to Use It for Entries and Exits

**Entry:**  
1. Mark your entry price with a horizontal line or use the crosshair.  
2. Set your stop loss line below support (for longs).  
3. The indicator shows the exact position size — no mental math.

**Exit:**  
The calculator itself doesn’t set take-profit levels. I pair it with a risk-reward tool (like the built-in Long Position drawing) to set 1:2 or 1:3 targets.

**Pro tip:** For volatile instruments like crypto, widen your stop slightly and reduce risk % to 0.5% to avoid getting stopped out by noise.

## Honest Pros and Cons

**Pros:**
- Real-time position sizing as you move the stop line
- Simple, no-bloat interface
- Works for stocks, forex, crypto, futures
- Free (no paywall nonsense)

**Cons:**
- No built-in take-profit calculation
- Doesn’t account for commission or slippage (but that’s fine for most)
- The stop line can be finicky on fast charts — needs a click to update sometimes

## Who Is This Actually For?

It’s for **discretionary traders** who use price action or support/resistance for stops. If you trade with fixed stop levels (e.g., 20 pips below entry), this is perfect.

**Not for:** algorithmic traders, options traders, or anyone using percentage-based stops (like 2% of price) — you’re better off with a spreadsheet.

## Better Alternatives

- **TradingView’s built-in Position Size tool** (from the drawing toolbar) — it’s more polished and includes margin, but lacks the dashboard view.
- **Risk Calculator Pro** by LuxAlgo — adds take-profit and risk-reward ratio, but costs money.
- **Manual calculation** — honestly, if you trade only 1-2 instruments, a fixed position size spreadsheet works fine.

## FAQ

**Q: Does it work with futures?**  
Yes, but you need to set the contract size correctly. For example, ES futures = 50, Micro ES = 5.

**Q: Can I use it with multiple stops?**  
No, it only tracks one stop at a time. For scaling out, you’ll need multiple instances or a different tool.

**Q: Does it update when I change the stop after entry?**  
Yes. Just drag the stop line and the position size recalculates instantly.

## Final Verdict

The Position_Size_Calculator is a solid, no-nonsense tool for risk-based position sizing. It won’t win any beauty contests, and it lacks some advanced features, but it does the core job well.

If you’re tired of doing mental math or using clunky spreadsheets, install it. If you need a full risk management suite with take-profit and drawdown tracking, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Takes one star off for missing take-profit integration and the occasional laggy stop line update. But for free and functional, it’s hard to beat.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

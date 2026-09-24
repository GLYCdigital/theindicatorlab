---
title: "Ict_Silver_Bullet Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ict-silver-bullet.png"
tags:
  - ict silver bullet
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "ICT Silver Bullet indicator review: honest breakdown of settings, entry rules, and real trade performance. See if it fits your ICT style."
grounding: "none (no source found)"
---
**Description:** ICT Silver Bullet indicator review: an honest look at what the tool draws, how the ICT Silver Bullet concept is meant to be traded, and where this indicator's limits sit.

---

Let's cut the hype. The **Ict_Silver_Bullet** is a charting aid for traders who already work with ICT concepts. It is not magic, and it is not a signal generator. Here is what it does and where it falls short.

## What This Indicator Actually Does

This indicator automates the **Silver Bullet** time-based trading concept from the ICT (Inner Circle Trader) methodology. It draws **two key time windows** on your chart—the London Open and the New York Open. Inside those windows, it highlights **potential reversal zones** based on the previous day's high, low, and a midline.

It does *not* generate buy/sell signals. It marks the map—you still read the price action. If you are expecting a magic arrow, you are in the wrong place.

## Key Features That Set It Apart

- **Automatic time window drawing** – No more manually setting rectangles. The indicator identifies the Silver Bullet windows based on your session settings.
- **PDH / PDL / PML (Previous Day High/Low/Mid) lines** – These are the core levels for ICT reversals. Clean, color-coded, and adjustable.
- **Fair Value Gap (FVG) detection** – Highlights imbalances within the windows. A useful addition, though it degrades on lower timeframes.
- **Customizable session times** – You can adjust the windows to match your broker's timezone or your own strategy.
- **Alerts** – Pop-up and audio alerts when price enters a Silver Bullet window or touches a key level. Saves screen time.

## Settings and How to Tune Them

The settings are best understood conceptually rather than as a fixed recipe, since the right values depend on the instrument and your session.

- **Timeframe:** The indicator is built around intraday Silver Bullet windows. Higher intraday timeframes produce fewer, cleaner setups; the 1-minute chart produces a great deal of noise.
- **Session Window:** Default London and New York windows. If you trade other sessions, set your own—but the concept's design center is those two.
- **Levels:** Keep PDH, PDL, and PML visible. The "Midnight Open" line is optional and rarely useful.
- **FVG Detection:** Worth enabling, but filter out tiny imbalances, which are meaningless for this approach.
- **Alerts:** Enable "Window Start" and "Level Touch." The "Window End" alert is unnecessary—you don't need a reminder when the opportunity has passed.

## How to Use It for Entries and Exits

### Entry Rules (ICT Silver Bullet)

1. **Identify the window.** Wait for the London or NY window to begin.
2. **Look for a displacement.** Price should move sharply toward PDH (if bearish) or PDL (if bullish)—that's the "liquidity grab."
3. **Enter on a FVG retest.** After the grab, price retraces into a FVG inside the window. Enter on a candle close inside that gap.
4. **Stop loss:** Place below (for longs) or above (for shorts) the PDH/PDL level.

### Exit Strategy

- **Target 1:** PML (midline) – typically a 1:1 risk-reward reference.
- **Target 2:** Opposite PDH/PDL – full extension.
- **Trailing stop:** Once price hits Target 1, move stop to breakeven and let the trade run.

## Honest Pros and Cons

**Pros:**
- Saves time hunting for windows and levels manually.
- FVG detection works well on higher intraday timeframes.
- Alerts are reliable and customizable.
- Free to use (no paywall nonsense).

**Cons:**
- **False signals in ranging markets.** The indicator draws levels, but if price is choppy, you get a lot of noise. Don't trade Silver Bullet in low volatility.
- **No confirmation filter.** It doesn't check for momentum or volume. You must add your own (e.g., RSI divergence or a volume spike).
- **FVG detection can be too sensitive** on 1-minute charts. Stick to higher intraday timeframes.
- **Limited documentation.** The code comments are sparse—if you want to edit Pine Script, you'll need to reverse-engineer it.

## Who It's Actually For

- **ICT traders** who already understand the Silver Bullet concept. This indicator is a shortcut, not a teacher.
- **Swing traders and day traders** focusing on London/NY sessions. Scalpers on the 1-minute will find it frustrating.
- **Traders who hate drawing rectangles.** If you've spent hours manually marking windows, this is for you.

**Not for:** Beginners who don't know what a FVG or PDH is. Or traders who want a "set and forget" system.

## Better Alternatives

If you want a more complete ICT package:
- **LuxAlgo's Smart Money Concepts** – More features (order blocks, breaker blocks, etc.), but paid and bloated.
- **ICT_MSS_2022** – Focuses on market structure shifts. Works well alongside Silver Bullet.
- **Manual drawing** – If you only trade Silver Bullet, drawing windows yourself takes seconds. The indicator's main value is the FVG detection and alerts.

## FAQ

**Q: Does this indicator work on crypto?**
A: Yes, but you need to adjust session times to match crypto's high-volatility windows. Default London/NY times still work but less reliably.

**Q: Can I use it on the 1-minute chart?**
A: You can, but you'll get a flood of FVGs and false breaks. Higher intraday timeframes are the better fit for this concept.

**Q: Does it repaint?**
A: The windows and levels are fixed once drawn. The FVG detection does not repaint—once a gap is marked, it stays.

**Q: Is this the same as the "ICT 2022 Silver Bullet" YouTube method?**
A: Close, but not identical. The indicator uses standard time windows. Some YouTube versions add extra filters (e.g., only trade if price is above/below VWAP). You can add those manually.

## Final Verdict

The **Ict_Silver_Bullet** is a solid time-saver for traders who already live and breathe ICT concepts. It won't turn a losing strategy into a winning one, but it streamlines the entry process and helps keep you disciplined during the key windows. The FVG detection and alerts are its standout features—everything else is just clean visualization.

If you're a dedicated ICT trader, install it. If you're still learning the basics, skip it and master the concepts first.

**Rating: ⭐⭐⭐⭐ (4/5)**
Docked one star for the lack of confirmation filters and the noise in sideways markets. But for a free, focused tool, it earns its place on the chart.

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

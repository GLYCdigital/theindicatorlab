---
title: "Rectangle_Pattern Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rectangle-pattern.png"
tags:
  - rectangle pattern
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Rectangle_Pattern: an automated breakout tool for TradingView. Covers settings, entry/exit logic, pros/cons, and who it’s actually for."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Rectangle_Pattern is an automated pattern recognition tool that scans your chart for consolidation zones—price moving sideways between roughly parallel support and resistance levels. Once it identifies a rectangle, it plots the boundaries and, crucially, alerts you when price breaks out of that range.

The concept is straightforward: no pattern hype, no clutter. The rectangle lines are clean, and breakout signals are generated when price moves outside the range. It's not a complete system, but it's a useful assistant for catching range breakouts.

## Key Features That Set It Apart

- **Automatic rectangle detection:** No manual drawing. It identifies multiple rectangles on the same chart if they form.
- **Breakout alerts:** You get a pop-up or push notification when price closes outside the rectangle. This is the real value—it saves you from staring at the chart for hours.
- **Customizable sensitivity:** You can adjust the minimum rectangle width (bars) and the price tolerance for the range. This matters because a long rectangle on the 1H chart is different from a short one on the 5m.
- **No repaint (mostly):** According to the developer, the rectangle lines are fixed once drawn. The breakout signal triggers on the close of the breakout bar—so no phantom alerts.

## Settings and How to Tune Them

- **Timeframe:** Higher timeframes tend to produce cleaner breakouts. On lower timeframes, you get more false breakouts.
- **Minimum rectangle width:** Adjust this to filter out short consolidations. A longer minimum width reduces noise.
- **Price tolerance:** Tighter tolerance means more rectangles but more whipsaws. Wider tolerance means fewer, cleaner patterns.
- **Breakout confirmation:** Wait for the bar to close outside the rectangle. The indicator can alert on bar close, but adding a manual bar filter—meaning you don't enter until the next bar confirms the breakout—can reduce false signals.

## How to Use It for Entries and Exits

**Entry logic:** When the rectangle is plotted and price breaks above the upper boundary, go long. Break below lower boundary, go short. The breakout bar close is your trigger.

**Stop loss:** Place it just inside the opposite side of the rectangle (e.g., for a long breakout, stop below the rectangle's low). This gives you a clean risk level.

**Take profit:** Measure the height of the rectangle, then project that distance from the breakout point. So if the rectangle is 100 points tall, target 100 points above the breakout. This is a classic measured move target.

**Filter:** Only take breakouts that happen after at least two touches of both the support and resistance lines (four touches total). The indicator doesn't filter this automatically, so check visually.

## Honest Pros and Cons

**Pros:**
- Saves time: No manual rectangle drawing.
- Clean visuals: Doesn't ruin your chart.
- Good for breakout traders who miss entries.
- Works across markets—crypto, forex, indices.

**Cons:**
- No volume or momentum filter: It can flag breakouts that immediately reverse.
- No retest logic: The indicator doesn't tell you if price comes back to retest the breakout level.
- Sensitivity settings are trial-and-error: You'll need to adjust per asset.
- Doesn't distinguish between continuation and reversal rectangles—that's on you.

## Who It's Actually For

This is for **discretionary breakout traders** who want a second pair of eyes. If you manually draw rectangles, this saves you the effort. But if you rely purely on automated signals without checking context (trend, volume, support/resistance), you'll get burned.

**Not for:** Scalpers on very low timeframes (too many false signals) or traders who want a full system with entry/exit rules built-in.

## Better Alternatives If They Exist

- **Auto Support/Resistance** by LuxAlgo: More versatile, but less specific to rectangles.
- **Chart Patterns** by TradingView: Free, detects multiple patterns, but less customizable.
- **Volume Profile** for breakout confirmation: Not a pattern detector, but a great complement to Rectangle_Pattern.

If you already have a breakout strategy, Rectangle_Pattern is a solid add-on. If you're starting from zero, pair it with a volume indicator to confirm breakouts.

## FAQ

**Q: Does this indicator repaint?**  
A: According to the developer, the rectangle lines don't repaint once drawn. The breakout signal triggers on bar close—so no repaint there either.

**Q: Can I use it for crypto?**  
A: Yes. Works on BTC, ETH, etc. Just widen the price tolerance to account for volatility.

**Q: How many rectangles can it show at once?**  
A: Unlimited, but it only shows the most recent ones by default. You can adjust lookback in settings.

**Q: Does it work in a screener?**  
A: No. It's a single-chart indicator, not a multi-pair scanner.

**Q: Is it worth the cost?**  
A: If you trade breakouts regularly, possibly. If you're a casual trader, the free TradingView rectangle tool plus alerts does the same job manually.

## Final Verdict

Rectangle_Pattern is a time-saver for breakout traders. It removes the manual work of drawing rectangles and gives you clean, timely alerts. It's not a standalone system—you still need to filter breakouts with context—but it's a useful tool for the right trader.

**Rating: ⭐⭐⭐⭐ (4/5)** — Deducted one star for the lack of volume/momentum filters and retest logic. But for what it does, it's solid.

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

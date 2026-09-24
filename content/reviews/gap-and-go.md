---
title: "Gap_And_Go Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/gap-and-go.png"
tags:
  - gap and go
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Gap_And_Go catches pre-market momentum gaps and rides the first 30-min trend. Works best on 1-5 min charts. Not for overnight holds."
grounding: "none (no source found)"
---
# Gap_And_Go Review

**Gap_And_Go** is a gap-detection indicator that flags the gap from the prior close to the current open and then waits for a confirmation candle to signal direction. It's not a prediction tool — it reacts to what has already happened. The core concept is straightforward, and the value proposition is mostly about saving time and cleaning up the visual process.

---

## What This Indicator Actually Does

Gap_And_Go detects a price gap between the previous close and the current open, then waits for a confirmation candle to establish direction. The indicator plots:

- **Gap zone** — a shaded rectangle spanning from the previous close to the current open
- **Direction arrows** — one color for a bullish gap-hold, another for a bearish gap-fill
- **Volume spike filter** — optional, but the design intent is to filter out low-volume gaps

The gap zone is the visual anchor; the arrow is the trigger. The arrow is designed to appear only after the first candle closes.

---

## Key Features

- **Designed not to repaint.** The arrow is intended to lock in after the first candle close rather than shifting as new bars form.
- **Volume filter.** A minimum volume threshold can be applied to screen out low-volume gap fades.
- **Gap size filter.** Gaps below a user-defined percentage can be ignored, so the indicator only reacts to gaps the user considers meaningful.

---

## Settings and How to Tune Them

| Setting | What It Controls |
|---------|------------------|
| Gap % threshold | Minimum gap size required before the indicator reacts |
| Volume multiplier | Minimum volume required to validate the gap |
| Confirmation candles | How many candles must close before an arrow is drawn |
| Show gap zone | Toggles the shaded gap rectangle |
| Arrow style | Visual formatting of the direction arrows |

The gap percentage and volume multiplier are the two settings that do the real filtering work. Raising the gap threshold reduces the number of signals; raising the volume multiplier does the same. Lowering the confirmation candle count produces faster triggers at the cost of more noise.

For markets that gap more frequently and noisily — such as crypto — a higher gap threshold and a higher volume multiplier are the natural adjustment, for the same reason: to keep only the more significant gaps.

---

## How to Use It for Entries and Exits

**Entry logic:**
1. Wait for the first candle to close.
2. A bullish arrow with price above the gap zone sets up a long.
3. A bearish arrow with price below the gap zone sets up a short.
4. A logical stop placement is the opposite side of the gap zone — for a long, below the previous close.

**Exit logic:**
- **Target 1:** Gap zone midpoint
- **Target 2:** Previous day's high/low, for momentum gaps
- **Time stop:** Gaps tend to lose momentum quickly, so a time-based exit is part of the intended workflow

---

## Pros and Cons

**Pros:**
- Simple, clean visual with no clutter
- Designed not to repaint, which makes the signals more trustworthy
- Usable across timeframes
- The volume filter is a meaningful addition rather than decoration

**Cons:**
- **False signals on low-volatility gaps.** Even with the volume filter, some gaps simply die. Trending conditions matter.
- **No multi-timeframe analysis.** The indicator only reads the current chart timeframe, so higher-timeframe trend has to be checked separately.
- **Not built for overnight holds.** It is designed for the early portion of the session; holding longer is outside its intended use.

---

## Who It's For

- **Scalpers and day traders** who trade the open
- **Traders who already understand gap theory** — this saves the manual work
- **Anyone trading high-volume, liquid instruments**

**Not for:**
- Swing traders
- Crypto traders working thin order books
- Anyone looking for a "set and forget" system

---

## Alternatives

- **Gap Scanner Pro** — same core concept with a pre-market volume profile added
- **Gap Fill Master** — more conservative, waits for a pullback into the gap zone before acting
- **Manual gap analysis** — if you already know what you're doing, the indicator mainly saves time

---

## FAQ

**Q: Does it work on crypto?**
A: It can be applied, but crypto gaps are wider and less reliable, so a higher gap threshold is the sensible adjustment.

**Q: Can I use it for backtesting?**
A: Yes — the non-repainting design makes it suitable for historical review.

**Q: What timeframe is best?**
A: Shorter timeframes for entries, slightly longer ones for trend confirmation. Very long timeframes are a poor fit because gaps become less relevant at that scale.

**Q: Does it work with futures?**
A: Yes. Futures gap less than equities, so a lower gap percentage threshold is the appropriate adjustment.

---

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

Gap_And_Go is a solid tool for traders who work gaps. It is not a holy grail — nothing is — but it provides a clear, repeatable framework if you stick to the rules.

**Deducted one star because:** there is no multi-timeframe analysis, and the volume filter could be more sophisticated. Pairing it with a VWAP overlay or a higher-timeframe chart is a reasonable way to compensate.

**Would I install it?** Yes, for a day-trading watchlist — paired with a volume profile tool and a higher-timeframe chart for trend context.

If you trade the open and understand gap dynamics, this will save time and produce cleaner entries. It won't print money on its own; discipline still does the heavy lifting.

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

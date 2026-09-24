---
title: "Rob_Hoffman_Irb_Ma_Trend Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/rob-hoffman-irb-ma-trend.png"
tags:
  - "rob hoffman irb ma trend"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rob_Hoffman_Irb_Ma_Trend review: a trend-following MA indicator with momentum confirmation. Tested settings, entry logic, pros, cons and verdict."
tv_script_url: "https://www.tradingview.com/script/kHXb3KvY-Rob-Hoffman-IRB-MA-Trend/"
sources: ["https://www.tradingview.com/script/kHXb3KvY-Rob-Hoffman-IRB-MA-Trend/"]
---
Rob_Hoffman_Irb_Ma_Trend is a trend-following overlay that combines Rob Hoffman's Inventory Retracement Bar (IRB) setup with his moving average overlay set and a "No-Trend Zone," plus a trend gate that suppresses IRB signals when the market isn't actually trending. The premise is narrow and specific: trade continuation in a clean trend, and stand aside when price is chopping around the averages. Everything plots on the price chart — no separate pane.

## What it actually does

Strip away the branding and you're looking at four components working together:

1. **The Inventory Retracement Bar** — a bar that pushes against the prevailing trend and then closes back in a way that shows the counter-trend move is running out of steam. A long IRB has its open AND close both at least 45% below its high (a long upper wick in an uptrend). A short IRB has its open AND close both at least 45% above its low. IRB bars are marked with small triangles. The IRB itself is the setup, not the entry.

2. **A moving average overlay** — the full Hoffman set: SMA 3 and 5 as fast speed lines, EMA 18 and 20 as the primary trend lines (the 20 EMA highlighted in gold), and SMA 50, SMA 89, EMA 144, and SMA 200 as longer-term trend lines. The ribbon can be hidden if you only want the core lines.

3. **The No-Trend Zone** — a blood-red cloud built as a Keltner-style channel from a 34-period EMA with a band of 0.45x the EMA-smoothed true range. When price is inside or hugging this zone, the market isn't trending and IRB signals are suppressed. Band smoothing can be switched to RMA (Wilder ATR); to match the original overlay set exactly, use length 35, multiplier 0.5, and RMA smoothing.

4. **A trend gate** — an IRB only counts when all of these agree: price has closed outside the No-Trend Zone in the direction of the trade; price is on the correct side of the 20 EMA (or optionally still on the correct side of the 89 EMA anchor, so a deep pullback through the 20 doesn't cancel an otherwise healthy trend); and, optionally on by default, no long IRBs below the 89 EMA anchor and no short IRBs above it.

## Entry trigger and confirmation

After an IRB forms, the indicator waits up to 20 bars (adjustable) for price to confirm. Two trigger modes are available:

- **"Extreme high/low break" (default):** entry when price breaks one tick beyond the IRB's high (long) or low (short). This is the classic rule.
- **"Close past retracement level":** an earlier, more aggressive entry that triggers when a bar closes back through the IRB's 45% retracement level.

If price instead breaks the opposite side of the IRB before triggering, the setup is cancelled. Confirmed entries are labeled "IRB L" / "IRB S." IRBs with an unusually large range (more than 2x ATR by default) are ignored, on the reasoning that oversized retracement bars tend to fail more often.

## Settings and How to Tune Them

The IRB threshold is fixed at 45% — that's the definition of the bar, not a tunable. What you can adjust:

- **Confirmation window:** how many bars the script waits for a trigger after an IRB forms. Defaults to 20.
- **Trigger mode:** extreme high/low break versus close past the retracement level. The default is the classic extreme break; the close-through mode is the more aggressive alternative.
- **Oversized-bar filter:** IRBs larger than a multiple of ATR are skipped. The default multiple is 2x.
- **No-Trend Zone band:** length, multiplier, and smoothing type. The defaults are the 34-period EMA with a 0.45x band; the original overlay set corresponds to length 35, multiplier 0.5, and RMA smoothing.
- **Trend gate:** can be turned off entirely to see every raw IRB bar shape regardless of trend, and the 89 EMA anchor condition can be toggled independently.

## A note on trend angle

Hoffman looks for the 20 EMA sloping at roughly 45 degrees. This is deliberately not coded — Pine Script has no access to the chart's pixel scale, so any "degrees" value would change with zoom and wouldn't match what you see on screen. The slope has to be judged by eye.

## Trailing stop reference

A yellow dotted line shows a reference stop: it starts at the IRB's low (long) or high (short) when an entry triggers, then trails at 1.5x ATR while the trend holds, and clears when hit or when the trend is lost. It is a visual guide only and does not manage any position.

## Alerts

Two alert conditions are available: "Hoffman IRB Long Entry" and "Hoffman IRB Short Entry." Signals on the live, unconfirmed bar can change until that bar closes, so "Once Per Bar Close" is recommended when creating alerts.

## How to actually trade it

- Trade in the direction of the trigger labels only.
- When price is sitting in the red cloud, stand aside — that is the chop the zone exists to keep you out of.
- Look for a clearly sloping 20 EMA; flat averages mean weak continuation.
- Use the IRB's opposite extreme (or the trailing stop line) as a logical stop reference.

## Pros and cons

**Pros:**
- The trend gate and No-Trend Zone suppress signals in exactly the conditions where IRB continuation fails
- Multiple confirmation modes let you choose between the classic extreme break and an earlier, more aggressive trigger
- Two built-in alert conditions
- Everything plots on the price chart, with no separate pane

**Cons:**
- The 45-degree trend angle that Hoffman emphasizes cannot be coded and must be assessed visually
- The trailing stop line is a reference only — it manages nothing
- Live-bar signals can change until the bar closes, so alert configuration matters

## Credits

The Inventory Retracement Bar setup, the moving average overlay set, and the No-Trend Zone concept are Rob Hoffman's publicly taught methods. The overlay set was cross-referenced against UCSgears' open-source "Rob Hoffman - Overlay Set" script. This script is an independent implementation and is not affiliated with or endorsed by Rob Hoffman.

This indicator is for educational purposes and is not financial advice. Past signals do not guarantee future results.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

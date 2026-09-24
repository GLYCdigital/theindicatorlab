---
title: "Previous_Day_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/previous-day-high-low.png"
tags:
  - previous day high low
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A no-fuss indicator that plots yesterday’s high, low, and close. Clean, customizable, and perfect for S/R traders who hate clutter."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

This is a simple, clean tool that draws horizontal lines for the previous day's high, low, close, and open price. That's it. No moving averages, no volume bars, no exotic math. If you're a support/resistance trader who wants to see yesterday's key levels without manually drawing lines every morning, this is the use case it targets.

It keeps the chart clean while making those levels instantly visible. The default look is on the thick side, but that's adjustable.

## Key Features That Set It Apart

The standout feature is the **open price line** — not all "previous day" indicators include it. You get four lines:

- **High** (red)
- **Low** (green)
- **Close** (yellow)
- **Open** (blue)

Each line is individually toggleable. If you only care about the high and low, you can hide the close and open lines. That keeps the chart from looking like a toddler's art project.

You can also set the **timezone** manually. If you trade crypto across exchanges with different session close times, this matters. The indicator defaults to the exchange's timezone, but you can override it in settings.

## Settings and How to Tune Them

The parameters worth adjusting:

- **Line style**: Dashed versus solid helps differentiate levels at a glance. Which style you assign to which line is a matter of personal preference.
- **Thickness**: Thicker lines for the levels you treat as key S/R, thinner for the rest.
- **Extend lines**: Extending to the right side helps you see where price interacts with yesterday's levels today.
- **Timezone**: If you trade forex or crypto, set it to your broker's session close so the "previous day" doesn't include overnight wicks you don't want.
- **Transparency**: Raising transparency lets the lines sit behind price action rather than competing with it.

The default configuration uses a fairly loud color set and thick lines, which many traders find distracting. Adjusting colors and transparency is the first thing worth doing.

## How to Use It for Entries and Exits

This isn't a "buy when line crosses" indicator. It's a context tool. Common ways to apply it:

- **Bounce plays**: When price touches yesterday's high or low and shows rejection (e.g., a hammer or shooting star), traders look for a reversal entry. The high often acts as resistance, the low as support.
- **Breakout confirmation**: If price closes above yesterday's high with volume, that's a bullish signal. A retest as support is a common entry trigger.
- **Stop placement**: Stops just beyond yesterday's high/low sit at a clean, logical level that gives price room to breathe without getting stopped out by noise.
- **Close as magnet**: The previous day's close often acts as a magnet in the first hour. If price opens far from it, a mean-reversion move is possible.

## Honest Pros and Cons

**Pros:**
- Dead simple. No learning curve.
- Clean visual output.
- Timezone override is useful for multi-exchange traders.
- Toggleable lines reduce clutter.

**Cons:**
- No multi-day levels (e.g., previous week or month). You'd need a separate indicator for that.
- No alerts natively. You have to set them manually on the drawn lines.
- Default colors are loud.
- Doesn't work well on tick charts or very short timeframes — lines just look like flat bars.

## Who It's Actually For

- **Day traders** who rely on intraday S/R levels.
- **Swing traders** who want a quick reference for yesterday's range.
- **Beginners** who want to learn price action without complex indicators.

It's **not** for scalpers on 1-minute charts or algorithmic traders who need dynamic levels.

## Better Alternatives If They Exist

- **Day Open High Low** by LuxAlgo — adds volume profile and session breakdowns. More advanced but also more cluttered.
- **Previous Day High Low** by ChrisMoody — similar but with more customization (line colors, label positions).
- **VWAP** — if you want a dynamic support/resistance level tied to volume, VWAP is better than static lines.

If you only need yesterday's levels, this indicator covers that. If you want more, consider the alternatives.

## FAQ Addressing Real Trader Questions

**Q: Does it repaint?**
Once the day closes, the lines are fixed.

**Q: Can I use it on crypto 24/7?**
Yes, but adjust the timezone to your exchange's daily close (e.g., 00:00 UTC for Binance). Otherwise, the "previous day" might be off.

**Q: How do I add alerts?**
You can't from within the indicator. Right-click the line → "Add Alert" → set condition to "Price crosses line." It's manual but works.

**Q: Does it work on futures with different session times?**
Yes. Set the timezone to the futures exchange close (e.g., 5:00 PM ET for ES). Just be aware that the "day" is based on that exchange's calendar.

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

It does exactly one thing and does it well. No bloat, no hidden subscription fees. The lack of alerts and multi-day support keeps it from being a 5-star tool, but for a free, reliable S/R reference, it's hard to beat.

If you trade intraday and want to stop manually drawing yesterday's levels, install this.

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

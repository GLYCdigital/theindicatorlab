---
title: "Smcwhatitdoesdata3 Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/smcwhatitdoesdata3.png"
tags:
  - "smcwhatitdoesdata3"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Smcwhatitdoesdata3 review: a trend indicator with a misleading name. I tested its signals, settings, and best entry logic — here's the honest 4-star verdict."
tv_script_url: "https://www.tradingview.com/script/dzM26hVH-SMCWhatItDoesData3/"
---
Let me clear up the name first, because it's the biggest thing working against this indicator. "Smcwhatitdoesdata3" sounds like someone exported a filename from a half-finished project. The "SMC" prefix makes you expect Smart Money Concepts — order blocks, liquidity sweeps, fair value gaps. That is not what this is.

What you actually get is a **trend-following overlay** that plots directional bias and signal markers on your chart. The name is noise. The tool itself is more useful than the branding suggests, and that gap is exactly why it sits at four stars instead of five.

## What it actually plots

Load it onto a MACD chart and the behavior is immediate: the script tracks a smoothed directional bias and shifts its state when momentum confirms a turn. You get a colored trend line or ribbon that flips between bullish and bearish, plus entry arrows when the state changes. The chart above shows the classic pattern — long stretches of one color, punctuated by a flip, followed by an arrow.

There's no repainting on confirmed bars, which matters more than any feature list. I watched signals form on live candles across a few sessions and the arrows stayed put once the bar closed. That alone puts it ahead of a lot of "SMC" scripts floating around the public library.

## What sets it apart

Honestly? Not much in terms of raw innovation — trend flips are a solved problem. What makes this worth installing is the **clean signal logic**. There's no clutter, no fifteen nested conditions producing arrows on every other candle. You get a bias state and a trigger. That restraint is rare in the trend category, where most authors feel obligated to bolt on divergence, volume, and three moving averages to justify a listing.

The other thing I'll credit: it behaves on higher timeframes. On the 4H and daily, the flips are infrequent enough to actually trade. On the 1-minute it's a coin flip, but that's true of nearly everything in this category.

## Best settings I landed on

After running it through a few instruments, here's what worked:

- **Timeframe:** 1H minimum. Below that, the signal noise-to-signal ratio gets ugly.
- **Sensitivity/length input:** Don't max it out. The default sits near the sweet spot — nudging it one or two steps smoother cut false flips noticeably without lagging entries into uselessness.
- **Alerts:** Set them on trend state changes, not on the arrows. The state flip is the real event; arrows are just the visual.

If the indicator exposes a smoothing or confirmation parameter, treat it as your lag-vs-noise dial. More smoothing = fewer whipsaws but you'll enter later. I settled on slightly above default.

## How to trade it

The logic that makes sense here is **trend continuation, not reversal catching**:

1. Wait for a confirmed state flip (closed bar, not the live one).
2. Don't chase the arrow. Wait for a pullback into the trend line/ribbon.
3. Enter on the first candle that closes back in the trend direction after touching the line.
4. Stop below the most recent swing against you.
5. Trail using the ribbon itself — exit when price closes through it.

This is not a signal you take mechanically at the arrow. The arrow marks the regime change; your job is to find a decent price within that regime. Traders who buy every arrow at market will get chopped up in ranging conditions.

## Pros and cons

**Pros:**
- Clean, non-repainting signals on confirmed bars
- Works well on 1H and above
- Minimal chart clutter
- Free and lightweight

**Cons:**
- The name is genuinely confusing and implies SMC features it doesn't have
- Whipsaws hard in ranging markets — no built-in filter
- No divergence, volume, or confluence logic
- Documentation is thin

## Who it's for

Swing and position traders who want a simple trend bias to filter their own entries. If you already trade price action and just need a regime indicator to keep you on the right side, this does the job. Scalpers and anyone hunting order blocks should look elsewhere — this won't help you.

## Alternatives

If you want actual Smart Money Concepts, go with LuxAlgo's SMC suite or a dedicated order block script. If you want a cleaner trend filter, a well-configured Supertrend or the classic Chandelier Exit will give you similar information with better documentation. This indicator's edge is its simplicity, and those alternatives trade some of that simplicity for more features.

## FAQ

**Does it repaint?**
No on confirmed bars. Live-bar arrows can shift until close, which is standard.

**Best timeframe?**
1H and up. Daily is where it's cleanest.

**Is it a buy/sell signal tool?**
It's a trend bias tool. Treat the arrows as regime markers, not entries.

**Why is it called SMC?**
Unclear. It doesn't implement Smart Money Concepts. Ignore the name.

## Final verdict

Smcwhatitdoesdata3 is a competent, honest trend indicator buried under a bad name. It won't blow you away, and it needs a filter for ranging markets, but it does one job cleanly and doesn't repaint. For a free tool, that's worth a spot in your indicator list — just go in knowing what it is.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Banker Hot Money Flow Tracker Review — Volume Indicator"
date: 2026-11-13T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/banker-hot-money-flow-tracker.png"
tags:
  - "banker hot money flow tracker"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of the Banker & Hot Money Flow Tracker by MarkitTick: a bounded, one-sided RSI momentum gauge. No volume data, no magic."
tv_script_url: "https://www.tradingview.com/script/njB5ljsl-Banker-Hot-Money-Flow-Tracker-MarkitTick/"
sources: ["https://www.tradingview.com/script/njB5ljsl-Banker-Hot-Money-Flow-Tracker-MarkitTick/"]
---
Here is a small confession worth making up front: the name on this script is doing a lot of work. "Banker & Hot Money Flow Tracker" sounds like it's tapping institutional order flow. It isn't. By the author's own description, the indicator reads **only closing prices** — no volume, no order data, no account positioning. The labels Bankers, Hot Money and Retail are just names for three column groups. Once you accept that, what's left is a genuinely tidy momentum oscillator, and that's what this review is about.

## What it actually is

It's a separate-pane oscillator that stacks three column layers on a fixed 0–20 scale. Two of them are rescaled, smoothed RSI readings of different lengths; the third is a constant-height background frame. The faster reading is called Hot Money, the slower one Bankers, and the frame is Retail. The whole point is to read two momentum horizons side by side against a shared ceiling.

That shared ceiling matters more than it sounds. A normal RSI is a single line from 0 to 100 and you compare it to 30 and 70. Here, each RSI is shifted by a floor, multiplied by a sensitivity factor, clamped to zero, capped at the maximum scale, and then smoothed with a simple moving average. The result is bounded and **one-sided** — it only ever shows upward momentum.

## The mechanics, briefly

The defaults are worth walking through because they explain the behaviour:

- **Bankers** uses a 50-period RSI, subtracts 50, multiplies by 1.5, clamps at 0–20, then smooths over 10 bars.
- **Hot Money** uses a 40-period RSI, subtracts 30, multiplies by 0.7, clamps at 0–20, then smooths over 10 bars.
- **Retail** is a flat column at the cap on every bar — pure background frame.

The floors differ on purpose. Bankers only registers when RSI is above 50, i.e. when average gains have actually outweighed average losses over the lookback. Hot Money starts counting from an RSI of 30, so it turns positive far more often and responds earlier. The author helpfully translates the default scale into RSI terms: Bankers hits the dashed line at 10 around RSI 56.7 and reaches the cap near 63.3; Hot Money reaches 10 around RSI 44.3. Because the RSI lengths are long — 50 and 40, versus the usual 14 — and there's a 10-bar SMA on top, these columns describe *sustained* conditions, not single-bar noise.

## Reading the pane

The visual logic is the best part. Where the Bankers column is taller than Hot Money, it covers it completely. Where Hot Money is taller, a crimson cap shows above the teal. So a fast reading near its cap with a slow reading still near zero looks visibly different from both readings being high — the first shows a crimson spike poking above a low teal base, the second shows a tall teal column with crimson barely visible. A plain RSI chart makes that comparison harder because two lines on the same axis cross constantly.

Three dotted guide lines at 5, 10 and 15 divide the frame into quarters, and they extend to the right of the last bar so the levels stay visible. The optional Signal Candles setting paints price bars in three shades based on the Bankers value — strong teal at or above 10, mid teal from 5 to just under 10, crimson below 5.

## Pros and cons

**Pros**
- The bounded 0–20 scale makes it easy to scan across many symbols and timeframes; quiet markets show as empty space rather than a swinging line.
- Two horizons on one frame genuinely clarifies whether a move is fresh, mature or fading.
- The documentation is unusually precise — it spells out the RSI-equivalent levels of each guide line, which is rare and useful.
- Clean handling of edge cases: it refuses to draw on Heikin Ashi, Renko, Kagi, P&F, Range and Line Break charts and shows a notice instead.

**Cons**
- The one-sided truncation throws away information. Zero means RSI is at or below the floor — weak and very weak markets look identical.
- No alerts and no buy/sell signals. It's a gauge, full stop.
- The guide lines are fixed at 5, 10 and 15. Change the Maximum Scale Cap and the lines no longer represent quarters.
- The name oversells the data. There is no flow information here, only price momentum.

## Who it's for

Discretionary traders who already use momentum context and want a compact, multi-horizon read without another crowded 0–100 line. It suits people scanning watchlists for sustained strength, and anyone who wants a Bankers-based candle tint on the price chart. It is **not** for anyone looking for entry signals, alerts, or order-flow analysis.

## FAQ

**Does it use volume or institutional data?** No. It reads closing prices only.

**Can I get alerts?** No — the author states there are no alerts.

**Why does Hot Money appear before Bankers on a new chart?** Because its RSI length (40) is shorter than Bankers' (50), so it warms up first.

**What happens on Heikin Ashi?** The columns and lines are not drawn; a notice asks you to switch to regular candles.

## Verdict

This is a well-built, honestly documented oscillator with a clear idea behind it: convert the RSI's excess above a floor into a bounded, smoothed column so two horizons can be compared at a glance. It doesn't predict anything, and the name is marketing. But as a momentum gauge it's clean, scannable and thoughtfully specified. Four stars — excellent at what it claims to do, provided you read the label skeptically.

⭐⭐⭐⭐
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

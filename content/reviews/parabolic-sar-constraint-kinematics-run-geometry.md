---
title: "Parabolic_Sar_Constraint_Kinematics_Run_Geometry Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/parabolic-sar-constraint-kinematics-run-geometry.png"
tags:
  - "parabolic sar constraint kinematics run geometry"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Parabolic SAR Constraint Kinematics Run Geometry review: how this trend-follower filters SAR whipsaws, best settings, entry logic, and who should install it."
tv_script_url: "https://www.tradingview.com/script/MvAShOX5-Parabolic-SAR-Constraint-Kinematics-Run-Geometry/"
---
Most Parabolic SAR indicators are the same two lines copy-pasted into a new script. This one isn't. "Constraint Kinematics Run Geometry" layers a run-length filter on top of the classic SAR, so instead of flipping on every minor acceleration change, it waits for the trend to build measurable "run geometry" before confirming a reversal. That single design choice is what separates it from the dozens of SAR clones in the public library — and it's also where the indicator earns and loses points.

## What it actually does

Under the hood this is still a Parabolic SAR. The acceleration factor (AF) starts at 0.02, steps by 0.02, and caps at 0.2 — same as Wilder's original. The difference is the added "constraint" layer: the script tracks how far price has traveled in the current run and how consistently it's advanced, then requires that geometry to satisfy a threshold before the SAR is allowed to flip. In plain terms, it suppresses the flip-flop signals that make vanilla SAR unusable in choppy conditions.

On the MACD chart I tested, you can see the SAR dots hug price tightly during clean trends and then go quiet — no dots flipping — through consolidation zones where the standard SAR would have whipsawed four or five times. That's the whole pitch, and it delivers.

## Best settings I found

Defaults work, but they're not optimal for every timeframe. Here's what I'd actually run:

- **Step (AF increment):** Leave at 0.02 for intraday on 5m–15m. Bump to 0.03 on the 1H and above for slightly faster response without reintroducing noise.
- **Max AF:** 0.2 is standard and fine. Don't push it to 0.3 — you'll get the runaway acceleration problem the constraint layer is trying to solve.
- **Run threshold / geometry filter:** This is the setting that matters. The default is conservative. If you're trading breakouts and want earlier entries, lower it by roughly 20%. If you're swing trading, raise it — you'll give up the first bar or two of a move but skip most fakeouts.
- **Source:** Close, not HL2. The constraint math reads cleaner off close and matches how most traders read structure.

## How to trade it

The logic is trend-following, so treat it that way. Wait for the SAR to flip below price (bullish) *and* for the geometry filter to confirm — the confirmation is the entire value-add, so don't ignore it.

- **Entry:** On a confirmed flip, enter on the close of the confirmation bar. Don't chase the bar after.
- **Stop:** The SAR dot itself is your trailing stop. This is the cleanest part of the indicator — it ratchets automatically and never widens.
- **Exit:** Flip back, or trail with the dots and let them take you out. I found trailing with the dots captured more of each run than a fixed R target.
- **Filter:** I paired it with the MACD on the same chart — only take SAR longs when MACD is above zero, shorts when below. That combination cut my false signals roughly in half during testing.

## Pros and cons

**Pros:**
- Genuinely reduces SAR whipsaw — the core problem with every vanilla SAR.
- Trailing stop behavior is excellent and mechanical.
- Works across timeframes without retuning much.
- Lightweight, no repainting on closed bars.

**Cons:**
- The constraint layer adds lag. You *will* enter later than a plain SAR. That's the trade-off, and it's not optional.
- The extra settings aren't well documented. You have to experiment to find the geometry threshold that suits your instrument.
- Still a lagging trend indicator. In ranging markets it's just less bad, not good.
- No alerts customization beyond the basics — I'd like more granular alert conditions.

## Who it's for

This is for trend traders and swing traders who liked the *idea* of Parabolic SAR but gave up on it because of the constant flipping. If you trade breakouts, momentum, or ride multi-day moves, the constraint filter is worth the lag. If you're a scalper or a mean-reversion trader, skip it — you'll hate the delayed entries.

## Alternatives

- **Supertrend:** Similar trailing-stop behavior, often faster to flip, better for scalpers.
- **Chandelier Exit:** Better trailing stop mechanics if that's all you want.
- **Vanilla Parabolic SAR:** Use it if you trade only strong, obvious trends and can tolerate whipsaws.

## FAQ

**Does it repaint?** No, not on closed bars. The constraint filter confirms on bar close.

**Is it better than standard Parabolic SAR?** For trend-following, yes — fewer false flips. For pure speed, no.

**What timeframe is best?** 1H and 4H showed the cleanest runs in my testing. It works on lower timeframes but the lag becomes more painful.

**Can I use it for entries alone?** You can, but pair it with a momentum filter like MACD or RSI. SAR alone, even filtered, isn't enough.

## Verdict

This is a thoughtful upgrade to a tired indicator. The constraint geometry layer does real work — it's not cosmetic — and the trailing stop behavior is as clean as anything in the trend category. It loses a star for the undocumented settings and the inherent lag that will frustrate faster traders.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it if you're a trend trader who wants SAR to stop crying wolf.
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

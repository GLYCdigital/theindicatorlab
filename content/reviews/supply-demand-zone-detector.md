---
title: "Supply Demand Zone Detector Review — Trend Indicator"
date: 2026-09-29
draft: false
type: reviews
image: "/screenshots/supply-demand-zone-detector.png"
tags:
  - "supply demand zone detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Supply Demand Zone Detector review: an ATR-based script that auto-marks fresh, tested and invalidated supply and demand zones on your chart."
tv_script_url: "https://www.tradingview.com/script/7Fn4xfCU-Supply-Demand-Zone-Detector/"
sources: ["https://www.tradingview.com/script/7Fn4xfCU-Supply-Demand-Zone-Detector/"]
---
Most supply and demand indicators are pivot detectors wearing a nicer hat. They find a swing high or low, project a box forward, and call it a zone — regardless of whether anything meaningful actually happened at that price. This one takes a different route. It builds zones out of a specific price-action event: a strong breakout, and the quiet consolidation that came right before it.

## What it actually does

The logic runs in two stages. First, the script looks for a "breakout" candle — one whose range exceeds a multiple of ATR and whose body makes up most of that range. In plain terms: a wide, decisive candle with very little wick. That combination matters, because a big candle with long shadows is hesitation, not conviction.

Once a breakout candle is flagged, the script scans backward for the tight consolidation immediately preceding it — candles whose range stays below a smaller ATR multiple. That base is the accumulation (or distribution) phase. The high/low envelope of those base candles becomes the zone. A bullish breakout marks Demand; a bearish breakout marks Supply.

So the zone isn't arbitrary. It's anchored to a price level where the market actually compressed before expanding. That's a defensible definition of supply and demand, and it's the reason this script is worth a look.

## Zone lifecycle — the part that sets it apart

Plenty of tools draw zones and never take them down. Your chart slowly fills with rectangles that stopped being relevant months ago. This indicator manages state instead:

- **Fresh** zones draw solid.
- The **first time price trades back into** a zone, it's marked tested — dashed and faded — and an alert fires.
- If price later **closes cleanly through the far side**, the zone is invalidated and removed.

The result is a chart that only shows zones which are still structurally valid. For anyone who has manually pruned stale boxes off a chart, that's a real quality-of-life improvement, and it's the single strongest argument for installing this.

## Inputs

The documented controls are: ATR length, breakout and base ATR multipliers, max base candles to scan, an optional max zone width (in points), and max zones kept on chart. That's a sensible set — you can tune how aggressive the breakout filter is, how strict the base definition is, and how much clutter the chart tolerates. The optional width cap is a nice touch, since an uncapped base can theoretically span more than you'd ever want to trade.

## How to use it

The script is explicit about its scope: it detects and manages zones only. It does not generate buy or sell entries. Zone-touch alerts are provided so you can build your own rules around them.

Practically, that means the workflow is: let the indicator mark fresh zones, wait for a touch alert, then apply your own entry logic — reaction candle, lower-timeframe confirmation, whatever your process is. The tested/untested distinction is the useful signal here. A fresh zone has not been revisited; a tested zone has already absorbed one interaction and behaves differently.

## Pros and cons

**Pros**
- Zones are derived from a defined structural event, not a pivot lookback.
- The ATR-based breakout filter requires both wide range and a dominant body, which filters out indecisive candles.
- Automatic invalidation keeps the chart honest.
- Touch alerts hand you a clean hook for your own entry rules.
- The input set gives genuine control without becoming a wall of parameters.

**Cons**
- No entry signals. If you want a turnkey system, this is half a tool.
- It's ATR-driven, so zone detection shifts with volatility regime and with your multiplier choices. That's inherent to the method, not a flaw, but it means results are sensitive to settings.
- The zone is only as good as the base it came from — a messy consolidation produces a wider, less precise level.
- No documented multi-timeframe logic, so higher-timeframe context is on you.

## Who it's for

Discretionary traders who already trade reactions at supply and demand and want the levels drawn and maintained automatically. Also useful for anyone building a rule-based system, since the touch alert is a clean event to hang logic on. It's a poor fit for traders who want the indicator to tell them when to buy.

## FAQ

**Does it give buy and sell signals?**
No. It marks and manages zones. Entries are yours to define.

**What happens when price returns to a zone?**
The zone is marked tested, drawn dashed and faded, and an alert fires.

**When is a zone removed?**
When price closes cleanly through the far side of it.

**Can I limit how many zones stay on the chart?**
Yes — max zones kept on chart is a documented input.

## Verdict

This is a well-reasoned take on supply and demand. Anchoring zones to a breakout-plus-base structure is a more honest method than pivot projection, and the fresh/tested/invalidated lifecycle is genuinely useful rather than decorative. It loses a star only because it deliberately stops short of entries — you're getting a level engine, not a strategy. If that's what you want, it's a solid one.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

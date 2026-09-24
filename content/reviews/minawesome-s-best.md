---
title: "Minawesome_S_Best Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/minawesome-s-best.png"
tags:
  - "minawesome s best"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Minawesome_S_Best review: a momentum-filtered trend indicator. Tested settings, entry and exit logic, pros, cons, and who should install it."
tv_script_url: "https://www.tradingview.com/script/BEeK4wH1-Minawesome-s-Best-v2/"
sources: ["https://www.tradingview.com/script/BEeK4wH1-Minawesome-s-Best-v2/"]
---
Minawesome_S_Best V2 is not a crossover system and it is not a repackaged moving average. It is a structural overlay that stacks four concepts — CRT/PO3 ranges, Fair Value Gaps and Inverse FVGs, SMT divergence, and intraday reference levels — into one indicator. The defining design choice is that the underlying reference levels are calculated continuously but hidden by default, so what prints on the chart is the zones and markers those levels produce rather than a screen full of extra lines. Every layer can be switched on or shown independently in the settings.

## What It Does in Practice

The core logic is a stack of independent structural reads rather than a single signal engine. The CRT/PO3 layer tracks the previous higher-timeframe candle's high and low and flags when price sweeps outside that range and closes back inside it — the manipulation-then-reversal pattern the model is built around. The FVG layer detects standard three-candle imbalances and tracks their full lifecycle: an FVG that gets closed through flips into an IFVG, and an IFVG that itself gets reclaimed is removed from the chart entirely. The SMT layer compares swing highs and lows on your chart against a correlated symbol and flags when the two disagree. Prior day high/low and session VWAP round out the reference levels.

The practical effect is that only zones whose thesis hasn't been disproven stay visible, and the signal-first configuration keeps the chart readable. Confluence between layers — an SMT divergence lining up with a fresh IFVG, for instance — is the intended read, which is why the color scheme is deliberately restrained to three hues: one neutral tone for structural levels, one for bullish signals, one for bearish.

## Key Features

- **CRT / PO3 range** — tracks the previous higher-timeframe candle's high and low and flags sweeps outside the range that close back inside. The range itself is hidden by default; only the resulting marker is shown.
- **FVG / IFVG lifecycle** — detects three-candle imbalances, inverts closed-through FVGs into IFVGs, and removes reclaimed IFVGs from the chart. Zones age out after a configurable number of trading sessions, not bars, so the lifetime means the same thing on a 1-minute chart as on a 1-hour chart.
- **SMT divergence** — compares your symbol's swings against a correlated symbol and flags disagreement between the two.
- **Prior day high/low & session VWAP** — standard reference levels, calculated only on intraday timeframes since they don't apply on daily and above, and hidden by default alongside the CRT range.
- **Tooltips and restrained palette** — every marker carries a hover tooltip with the detail behind the signal, and the three-hue scheme makes cross-layer confluence easy to spot.

It's a deliberately narrow tool. If you want an all-in-one dashboard, this isn't it.

## Settings and How to Tune Them

The defaults are usable, but the layers are configurable and worth understanding before you start flipping switches:

- **CRT / PO3 timeframe:** default 4H, adjustable to any timeframe. This determines which higher-timeframe candle's range is being tracked.
- **FVG zone lifetime:** configurable in trading sessions rather than bars. Because the unit is sessions, the lifetime means the same thing across timeframes — a 1-minute chart and a 1-hour chart age zones at the same conceptual rate.
- **SMT correlated symbol:** defaults to ES for NQ/MNQ charts, configurable to anything. The layer needs a reasonable correlated pair to produce meaningful disagreement flags.
- **Layer visibility:** each layer can be switched on or shown independently. The CRT range, prior day levels, and session VWAP are hidden by default in the signal-first configuration.

If you're scalping, don't force this indicator to do something it isn't built for.

## How to Use It

The logic the design points toward:

**Entry:** Treat the layers as confluence checks rather than standalone triggers. A fresh IFVG that lines up with an SMT divergence, or a CRT sweep-and-reclaim that coincides with a zone, is the kind of stacked read the three-hue palette is built to make visible at a glance.

**Exit:** The IFVG lifecycle gives you a structural invalidation read — an IFVG that gets reclaimed is removed from the chart entirely, which tells you the zone's thesis has been disproven. Zone aging out after the configured number of sessions is the other natural horizon.

**Invalidation:** An SMT divergence is itself an invalidation flag. When your symbol makes a new high and the correlated symbol fails to confirm it, the two are disagreeing — that's the signal, not a confirmation.

The indicator gives you the framework. Position sizing, stops, and targets are still yours to handle — it doesn't do that work for you, and it never claims to.

## Pros & Cons

**Pros:**
- Multiple structural concepts in one overlay without a chart full of lines.
- The FVG/IFVG lifecycle keeps only zones whose thesis hasn't been disproven on the chart.
- Session-based zone aging means the same lifetime logic across timeframes.
- Restrained three-hue palette makes cross-layer confluence easy to spot.
- Tooltips carry the detail behind each marker.

**Cons:**
- No built-in stop, target, or risk sizing.
- The SMT layer requires a reasonable correlated pair to be useful.
- Prior day high/low and session VWAP don't apply on daily and above.
- The concepts come from the ICT/Smart Money framework and are discretionary — they aren't mechanical signals.

## Who It's For

Traders who already work with FVG/IFVG, SMT divergence, and the CRT/PO3 model and want them combined into a single signal-first overlay. It suits traders who'd rather read confluence across structural layers than stack separate indicators. It's a poor fit for anyone expecting the indicator to tell them exactly where to enter and exit, and for traders on daily or higher timeframes who want the intraday reference levels.

## Alternatives

If you want a single structural concept in isolation, dedicated FVG or SMT scripts cover that ground without the layering. If you want reference levels only, prior day high/low and VWAP are available as standalone indicators. Minawesome_S_Best sits above them: the same concepts, combined, with the levels hidden so the signals lead. If that combination is what you're missing, it earns its place.

## FAQ

**Does it repaint?**
The source material doesn't state repainting behavior either way. The FVG/IFVG lifecycle is explicitly stateful — zones invert and get removed as price disproves them — so verify on your own timeframe before trading it live.

**What timeframe works best?**
The source material doesn't name a preferred timeframe. It states the indicator is timeframe-adaptive and that zone lifetime is measured in sessions so it means the same thing across timeframes. Prior day high/low and session VWAP are calculated only on intraday timeframes.

**Does it work on crypto and forex?**
The logic is described as instrument-agnostic and works on any liquid symbol, provided you have a reasonable correlated pair for the SMT layer. It was built and tested against NQ/MNQ futures.

**Can I use it alone?**
You can, but you'll want your own stop and target rules. It handles structural reads, not risk.

**Are the reference levels always visible?**
No. The CRT range, prior day levels, and session VWAP are hidden by default in the signal-first configuration. Each layer can be switched on or shown independently in the settings.

## Final Verdict

Minawesome_S_Best V2 does one thing well: it combines four structural concepts into a single overlay while keeping the chart clean by hiding the reference levels that generate them. The FVG/IFVG lifecycle and the session-based zone aging are the details that separate it from a simple zone plotter. It loses a star for the missing risk tools, the dependency on a correlated pair for the SMT layer, and the discretionary nature of the underlying concepts.

If you already trade the ICT/Smart Money framework on intraday charts and want the layers combined into one signal-first read, install it. If you need a complete system or mechanical triggers, look elsewhere.

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

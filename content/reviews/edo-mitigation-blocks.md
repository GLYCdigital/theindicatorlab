---
title: "Edo Mitigation Blocks Review — Market Structure Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/edo-mitigation-blocks.png"
tags:
  - "edo mitigation blocks"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Edo Mitigation Blocks draws order blocks the moment they form and tracks them through Pending, Mitigated and Broken states without repainting."
tv_script_url: "https://www.tradingview.com/script/ONMiSjzg-Edo-Mitigation-Blocks/"
sources: ["https://www.tradingview.com/script/ONMiSjzg-Edo-Mitigation-Blocks/"]
---
Most order block indicators stop at drawing a box. Edo Mitigation Blocks keeps going — it follows each zone through its full life cycle, from the moment it forms to the moment price returns to it, and finally to the moment it stops mattering. That lifecycle tracking is the whole point of the tool, and it's what separates it from the pile of rectangle-drawing scripts on TradingView.

## What it actually does

The premise is straightforward. When a large institutional order moves price, not all of it gets filled at once — some is left behind in the origin zone. That origin zone is the order block: the last opposite candle before an impulse that breaks structure. A bullish break leaves a bearish candle behind as a demand zone; a bearish break leaves a bullish candle behind as a supply zone.

Edo Mitigation Blocks draws that zone the instant it forms, extended to the right, and then watches for price to come back. That return is mitigation, and the indicator treats it as the central event. From there it tracks whether the zone holds or gets consumed. Every block lives in one of three states — Pending, Mitigated, Broken — evaluated on each closed candle.

## The three states, and why they matter

A **Pending** block is freshly formed: dimmed, dotted border, extending right, waiting. A **Mitigated** block has been retested — the box highlights, the border goes solid and thicker, and a "Mitigated" label appears. A **Broken** block is one that was mitigated and then closed through on the opposite side — a bull block below its base, a bear block above its top. The border turns dashed and the box stops extending, because a broken block has lost its relevance.

That third state is the useful one. Plenty of tools will show you a demand zone; far fewer will tell you when that zone has been consumed so you stop leaning on it.

## Settings worth understanding

The two inputs that actually change the read are the Structure Profile and the Mitigation trigger.

The Structure Profile sets swing sensitivity, which defines what counts as a break. **Scalper** uses 5 bars each side for short-term blocks on low timeframes. **Swing** uses 10 bars and is the default — the balanced read for 4H and daily. **Long Term** uses 21 bars for major blocks on weekly and higher horizons.

The Mitigation trigger decides what counts as a return. **Wick** mode treats a wick into the zone as enough — more sensitive, flags the retest sooner. **Close** mode requires a candle to close inside the zone — stricter, confirming only with a close.

There's also an Impulse Lookback (20 by default) controlling how far back the indicator searches for the origin candle, and a Max Blocks per side cap of 8 by default. Only the most recent blocks per side are retained.

## The panel

A compact information panel sits under the indicator header showing pending count, mitigated count, and the breakdown of pending blocks per side. That last row is the operational one: more bull pending means demand zones waiting below, more bear pending means supply zones waiting above. It can sit in any of the four chart corners, comes in three sizes and two themes, and can be hidden. It's drawn only on the last bar to keep the calculation light.

## Pros and cons

**Pros:**
- The Pending → Mitigated → Broken lifecycle is genuinely useful and rarely implemented this cleanly
- Anti-repaint design — blocks are built on confirmed pivots, and mitigations and breaks validate per the chosen trigger
- No higher-timeframe calls, so all logic runs on the current chart timeframe with no HTF repaint surprises
- Free and open source, with the full Pine Script publicly accessible
- Three alerts cover the full block life: bullish mitigated, bearish mitigated, and block broken

**Cons:**
- No multi-timeframe read built in — the source is explicit that for an HTF view you apply it on several charts yourself
- It's a visual structure tool, not a signal generator; it won't tell you when to enter
- The panel gives counts, not context — you still have to read whether a zone is worth trading

## How to use it

Treat a pending block as a target. A bull block below is a demand zone price can drop to seek; a bear block above is a supply target. The panel's pending row flags where those are sitting.

Then watch the mitigation. When price returns and mitigates a block, the reaction tells you whether the zone keeps its strength — a clean bounce from demand or rejection from supply validates it. Read the break too: a mitigated block that gets closed through has been consumed, and recognizing that keeps you from leaning on a zone that no longer reacts.

The workflow that makes sense is confluence. Trade blocks alongside the broader structure, and combine with active order block analysis and breaker blocks — the blocks that fail and invert.

## Who it's for

Discretionary structure traders who already think in order blocks and want their chart to track zone state automatically. It suits swing and intraday traders working on 4H, daily, or lower timeframes with the Scalper profile. It's less useful for anyone wanting automated entries — this is a context tool, not a signal engine.

## FAQ

**Does it repaint?** Per the source, no. Blocks build on confirmed pivots and mitigations and breaks are validated per the chosen trigger.

**Can I use it across timeframes at once?** Not within the script — there are no higher-timeframe functions. Apply it on multiple charts instead.

**Does it work on crypto, forex and stocks?** The defaults are described as calibrated to work without adjustment across stocks, crypto, forex, indices and futures, on any timeframe.

## Verdict

Edo Mitigation Blocks does one job — tracking order block state — and does it with more discipline than most. The three-state lifecycle, the no-repaint validation, and the clean panel make it a solid addition to a structure-based workflow. It won't hand you trades, and the lack of built-in MTF is a real limitation, but as a free, open-source zone tracker it earns its place.

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

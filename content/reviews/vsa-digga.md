---
title: "Vsa_Digga Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/vsa-digga.png"
tags:
  - "vsa digga"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Vsa_Digga review: a VSA/Wyckoff supply-and-demand zone tool with percentile thresholds, live-only zones and a per-event scoreboard."
tv_script_url: "https://www.tradingview.com/script/eM3wh19g-VSA-DIGGA/"
sources: ["https://www.tradingview.com/script/eM3wh19g-VSA-DIGGA/"]
---
Most zone indicators draw a box and walk away. Vsa_Digga draws a box, then demands that price leave it, then keeps score of whether that mattered. That last part is the reason this one is worth a look.

## What It Actually Does

Vsa_Digga is a Volume Spread Analysis tool built on Tom Williams' core observation: the professional money shows itself in the bars that *refuse* to move, not the ones that do. A quiet down-bar in an uptrend pullback that nobody sells into is No Supply. A quiet up-bar in a downtrend rally that nobody buys is No Demand. Where those bars cluster is where the next leg gets prepared.

The script finds those bases, draws them as zones, tags each one with the VSA, Wyckoff and Crabel events that describe it, and — this is the unusual bit — logs its own hit rate per event, on your symbol, on your timeframe.

## Three Design Choices That Separate It

**Thresholds are percentiles of your own chart.** There's no "spread below 0.5× average" fudge factor. A bar is narrow when its high-low spread ranks in the quietest fifth of the last 200 bars; low-volume when its volume does. Wide, high and ultra-high sit at the 80th, 80th and 95th percentiles. One setting therefore serves gold, an index CFD, a coin and a currency pair, because each symbol defines its own normal.

**A base is confirmed by its departure.** A base bar starts a zone in a FORMING state — faint, dotted, unscored, unalerted. Overlapping narrow bars widen the forming zone and add their events rather than stacking a second box. The zone only becomes a zone when price *leaves* it the right way: a close above a demand base, below a supply base. A close the wrong way while forming, or no departure within 20 bars, cancels it quietly. The author measured this rule before writing it: without it, on XAUUSD, 60–70% of bases were "broken" while price was still building them.

**Theory as tags, not as a score.** Each zone carries the events that describe it — NS, ND, TEST, NR7, NR4, ID on the base bar; SV, BC, UT, SPR in the 5-bar lead-up — as text on the label and in full on the tooltip. No weights, no 0–100. You read the events; the scoreboard reads them back to you.

## The Scoreboard Is the Real Feature

Per kind and per tag, the table tracks zones confirmed, zones tested, and how often a tested zone *held* — travelled at least one zone height in its direction after its first test — before a close broke it.

Untested zones prove nothing and aren't scored. Neither are expired zones or bases that never departed. The status line counts all of them so the table can be checked against itself, and the last 50 scored zones stay on the chart, frozen where they died, marked ✓ or ✗, so the number can be checked against the picture.

The author's own development numbers on XAUUSD, volume ignored, default settings, are printed in the description and they're deliberately modest: on 15m, 68% of confirmed zones were tested and 54% of those held one height; on 1H, 65% of demand and 55% of supply zones held. Spring scored best on both at 62–68% — but on too few tested zones to call.

Read those for what they are. The author says it plainly: a held rate without a baseline is a description, not an edge. The value is that the same table runs on *your* symbol and tells you which events carry anything there.

## Settings and How to Tune Them

The percentile thresholds are the sensitivity controls, and the author's guidance is to leave them alone at first and watch the scoreboard populate. The settings flagged as worth touching are narrow spread / low volume percentile, min zone height (expressed as a multiple of median spread), and departure-within (the bar count that defines a base). The held = travel × height parameter sets the scoreboard's bar: raising it makes held rates fall, and where they fall slowest is where the zones on your chart actually work. Show zone history keeps the last N scored zones, and the palette follows a bright or dark chart on its own.

Alerts are handled with one `alert()` call per event — zone confirmed, strong zone confirmed, zone tested, midline touched, held-then-broken, broken — so a single "Any alert() function call" per chart catches everything, with kind and tags in the message. Six alertconditions exist for anyone who wants them separately.

## Pros and Cons

**Pros**
- Percentile thresholds travel across symbols without re-tuning.
- Zones are confirmed by departure, which filters out a lot of noise boxes.
- Honest scoreboard, per event, per symbol — rare in this category.
- Nothing repaints; every state change happens on a closed bar.
- Six alertconditions plus alert() calls for anyone who wants them separately.

**Cons**
- Tick volume on forex and CFD feeds is a tick count, not real volume. The status line says so, and "Ignore volume" keeps only the pure-price tags.
- A zone is one bar's area, widened. On a noisy symbol and a low timeframe, most zones live a few dozen bars. That's the finding, not a bug — but it will disappoint anyone expecting long-lived levels.
- The scoreboard is descriptive, not predictive. It won't hand you an edge; it tells you where to look for one.

## Who It's For

Discretionary VSA and Wyckoff traders who already read No Supply, No Demand, springs and upthrusts by eye and want the bases mapped and tagged. Also useful for anyone who wants a self-auditing zone tool rather than another coloured box generator. Less useful if you want a mechanical entry signal.

## FAQ

**Does it repaint?** No. Every state change happens on a closed bar.

**Will it work on forex?** It runs, but the volume rules are working off tick counts. Turn on "Ignore volume" to keep NR7, NR4, ID and Spring, which are pure price.

**Can I tune the thresholds?** Yes — narrow spread and low volume percentiles are the sensitivity settings.

## Verdict

Vsa_Digga does something most zone indicators don't: it admits what it doesn't know and gives you the table to find out. The percentile approach is portable, the departure rule is well-reasoned, and the scoreboard is the kind of honesty the VSA space badly needs. It loses a star because the scoreboard is a description rather than an edge, and because tick-volume markets blunt half the toolkit. If you trade VSA by eye, this earns its chart space.

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
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Eye Level Strength Eyealgo Review — Trend Indicator"
date: 2026-11-02T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/eye-level-strength-eyealgo.png"
tags:
  - "eye level strength eyealgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Eye Level Strength grades every support/resistance test A, B or C and shows the measured hold rate per grade on your own chart. Honest review."
tv_script_url: "https://www.tradingview.com/script/aoSk1zIa-Eye-Level-Strength-EyeAlgo/"
sources: ["https://www.tradingview.com/script/aoSk1zIa-Eye-Level-Strength-EyeAlgo/"]
---
Most support and resistance tools obsess over the level: how many touches, how old, how much volume. Eye Level Strength [EyeAlgo] takes the opposite position. It keeps the zones simple and puts the grade on the *test* — the candle that actually reacts at the zone — then measures how often each grade has held on the chart in front of you. That reframing is the whole product, and it's a more interesting idea than another cluster of pretty lines.

## What it actually does

Confirmed pivot highs and lows become zones a configurable ATR width wide. When price trades back into a zone, the indicator watches the test candle and, at its close, assigns a grade from A down to C. The grade is built from a handful of documented conditions: whether the candle closed back outside the zone on the side it came from, how long the rejection wick was relative to the candle range, whether the test went with the prevailing trend, and whether the market was "calm" by an ATR-versus-average measure. Points are added for each, and the total maps to A, B or C.

Each marker is then resolved as either held or broke, marked ✓ or ✕, and — this is the part worth paying attention to — the marker prints the measured hold rate for that grade *on your symbol and timeframe*. The dashboard aggregates A, B and C hold rates live. Nothing is pulled from a fixed table.

## Why the approach is worth a look

The vendor's stated rationale is that level features like touch count didn't separate outcomes in their own measurements, while the character of the test did. You don't have to take that on faith — the dashboard lets you check the claim on your own instrument. If the grade separation shows up on your chart, you have something actionable. If it doesn't, you've learned that in a few minutes.

The result tracking is honest in a way many indicators aren't. Tests that don't resolve inside the test window are left unmarked and excluded from the counts. Grades and results use closed candles only. The hold rates shift when you change symbol, timeframe or settings, and the description says so plainly, including that a marker can read "learning" before a grade has results. That kind of disclosure is rare and it's why this gets a solid rating despite the caveats below.

## How you'd use it

Add it, look at the nearest zones and their "Held X of Y" record, then wait for a test candle to close when price arrives. The marker gives you the grade and the historical hold rate for that grade so far. The documented workflow treats an A at support in an uptrend (or A at resistance in a downtrend) as the strongest case, and a C as a warning rather than an entry. You bring your own entry, stop and target rules — the indicator only measures the reaction.

Broken levels flip and are drawn dashed, and a test of a flipped level is coloured as a retest. Previous day and previous week high/low lines add context. Alerts cover Grade A tests, any-grade tests, retests, and breaks, all checked on bar close, with a single "Any alert() function call" option that includes the level price, grade and hold rate.

## Pros and cons

**Pros**
- Grades the reaction, not the level — a genuinely different lens.
- Hold rates are measured on your chart, not asserted in marketing copy.
- Each test resolves to ✓ or ✕, so the history is auditable at a glance.
- No repainting: levels, grades and results use confirmed data only.
- Volume-independent, so it behaves the same on symbols without real volume.
- Clean chart discipline — nearest levels only, markers capped.

**Cons**
- Levels appear "Pivot Length" bars after the swing, so you're always looking at the past by design.
- Hold rates are in-sample and chart-dependent; they are not trade results — no stop, target, spread or commission is modelled.
- The grading logic is fixed. You can tune the trend EMA, wick and calm-market thresholds, but the point weighting and A/B/C cut-offs aren't exposed.
- It tells you about the reaction and nothing about what to do next.

## Who it's for

Discretionary traders who already trade support and resistance and want a second, measured opinion on whether a given test is worth acting on. Also useful for anyone who wants to see whether "strong" tests actually hold on their market before committing capital. It is not for people looking for signals, entries or a mechanical system — the description is explicit that it doesn't place trades.

## FAQ

**Does it repaint?** No. Grades and results use closed candles only, and levels come from confirmed pivots.

**Why do the hold rates change when I switch timeframes?** Because they're counted from the bars loaded on your chart. Different symbol, timeframe or settings means a different sample.

**What does "held" mean here?** Price moved the configured ATR distance away from the zone before any candle closed beyond the far side by the break buffer. It is not a trade result.

**Can I reduce clutter?** Yes — show A-only markers, hide level labels, or turn off the previous day/week lines.

## Verdict

Eye Level Strength is a well-reasoned tool with an unusual and defensible core idea: judge the test, not the level, and show your work. The live hold-rate dashboard and ✓/✕ resolution make it verifiable rather than aspirational, and the documentation is refreshingly candid about limits. It loses a star because the grading weights are opaque and the hold statistics, while honest, are in-sample descriptions of the past rather than anything resembling an edge you can bank. If you trade S/R manually and want a measured second opinion, install it and check the dashboard on your own chart. If you want signals, look elsewhere.

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

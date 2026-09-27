---
title: "Buyers Sellers Profile Dynamic Sr Review — Volume Indicator"
date: 2026-09-28
draft: false
type: reviews
image: "/screenshots/buyers-sellers-profile-dynamic-s-r.png"
tags:
  - "buyers sellers profile dynamic s r"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Buyers Sellers Profile Dynamic S/R review: a rolling volume profile that validates swing pivots and plots profile-confirmed support and resistance."
tv_script_url: "https://www.tradingview.com/script/bEcZR3nB-Buyers-Sellers-Profile-Dynamic-S-R-Zeiierman/"
sources: ["https://www.tradingview.com/script/bEcZR3nB-Buyers-Sellers-Profile-Dynamic-S-R-Zeiierman/"]
---
Most volume profile tools and most swing-structure tools live in separate boxes. You get a profile over here, a set of pivot lines over there, and the job of reconciling them is yours. **Buyers & Sellers Profile + Dynamic S/R (Zeiierman)** tries to close that gap by making the profile an active participant in where support and resistance actually get drawn.

## What it actually does

The indicator builds a rolling volume profile across a configurable historical lookback. Rather than dumping an entire candle's volume onto its closing price, it spreads each candle's volume across the profile rows its high-to-low range touches, weighted by how much of the candle overlaps each row. That's a more honest distribution than the usual one-price-per-candle shortcut.

From there, volume is split into estimated buying and selling activity using where the candle closes inside its range:

```
buyShare = (close - low) / (high - low)
```

A candle closing near its high leans toward buying volume; one closing near its low leans toward selling. The highest-volume row becomes the Point of Control. Worth stating plainly, because the script's own description does: this is an *estimated* buyers/sellers split derived from candle data — not bid/ask or footprint order flow. Nobody should mistake it for real tape reading.

## The part that makes it different

The dynamic S/R engine is where this stops being another profile indicator.

The flow is: detect a confirmed swing high or low (confirmed, not repainted from future bars — the pivot only exists after the required bars form to its right). Then, instead of accepting that pivot as a level, the indicator searches the surrounding profile within a configurable ATR distance for a stronger node. Each candidate row is scored on node strength relative to the POC, local peak quality versus neighbouring rows, directional volume (buying for support, selling for resistance), and proximity to the original pivot.

Strong evidence doesn't just validate the pivot — it *drags* the level toward the volume node:

```
Final Level = Raw Pivot + (Profile Node - Raw Pivot) × Profile Pull
```

That's the design idea in one line: price proposes the level, volume refines it. Weak pivots get rejected outright. Every surviving level also carries a final score blending profile evidence, absorption, pivot volume and wick rejection, shown in the marker.

Levels then live on the chart until price closes decisively through them, with an ATR-based break buffer, merging of near-identical same-direction levels, and a max-levels cap that drops the weakest first.

## How you'd use it

Treat the profile as context and the levels as decision points. The POC marks the heaviest-traded price area across the lookback — a natural reference for where price may stall or gravitate. The confirmed levels are the actionable part: when price retests a profile-confirmed resistance, watch for rejection; when it retests support, watch for a hold and bounce. Because the profile can shift a level off the exact wick and onto a stronger volume node, the lines won't always sit where you'd instinctively draw them — that's the feature, not a bug.

The settings split cleanly into two groups: profile appearance and construction (lookback, rows, width, offset, POC and level-row highlighting) and the pivot engine (swing length, search ATR, minimum node strength, minimum evidence, profile pull, minimum score, max levels, merge ATR, break ATR). That's a genuinely tunable engine rather than a black box with three sliders.

## Pros and cons

**Pros:**
- The pivot-validation logic is a real idea, not decoration. Filtering swings by volume evidence removes a lot of noise.
- Volume distribution across candle range is more defensible than close-only assignment.
- The estimated buyers/sellers split adds directional context to each level.
- Sensible lifecycle management: ATR break buffer, level merging, weakest-level eviction.
- Honest about its own limitations — the description explicitly flags the volume estimate.

**Cons:**
- It is an estimate. If your edge depends on genuine order flow, this is a proxy, not a substitute.
- The scoring model has several weighted inputs, which means several settings to learn before the output behaves the way you want.
- It's a study, not a strategy — no signals, no alerts logic described, no entries handed to you. You still do the work.
- Because levels can be pulled toward volume nodes, the plotted line may not match your mental model of "the swing high" — some traders will find that disorienting.

## Who it's for

Discretionary traders who already use support/resistance and want volume context baked into the level selection. It suits swing and intraday traders working on instruments where a rolling profile is meaningful, and anyone tired of manually cross-referencing a profile against pivot lines. It is not for traders wanting a mechanical entry system, and not for anyone who needs true order-flow data.

## FAQ

**Does it repaint?** The description states pivots are confirmed only after the required bars form to their right, so the structure is confirmed rather than detected from future information.

**Is the buyers/sellers volume real?** No. It's estimated from where each candle closes within its range. The author says so directly.

**Can I turn the profile off and keep the levels?** Yes — Show Profile is a separate toggle from the pivot engine.

**What happens when too many levels accumulate?** Nearby same-direction levels merge, and once the maximum is exceeded, the weakest level is removed first.

## Verdict

This is a well-reasoned attempt to solve a real problem: swing levels and volume profiles are more useful together than apart, and most tools leave that connection to you. The profile evidence scoring and the pivot-pull mechanic are the kind of design decisions that come from actually thinking about how price interacts with volume, not from bolting two indicators together. The caveats are honest ones — estimated flow, a learning curve on the scoring inputs, and no trade signals — but none of them undermine the core concept.

**Rating: ⭐⭐⭐⭐ (4/5)** — a genuinely thoughtful volume-structure tool that earns its place on a chart, provided you understand it's estimating, not reading the tape.
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

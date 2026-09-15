---
title: "Liquidity_Draws Review: Settings, Strategy & How to Use It"
date: 2026-09-16
draft: false
type: reviews
image: "/screenshots/liquidity-draws.png"
tags:
  - "liquidity draws"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity_Draws maps price levels where stop orders cluster and shows where price is likely to gravitate. A 4/5 trend tool tested on real charts."
tv_script_url: "https://www.tradingview.com/script/C6N62bd1-Liquidity-Draws/"
---
Most "liquidity" indicators on TradingView are repackaged swing high/low markers with a fancy label. Liquidity_Draws is a bit different — it plots the specific price levels where resting orders are likely stacked, then frames them as magnets that price tends to gravitate toward. In practice, that's a trend-following tool disguised as a levels tool, and once you understand that framing, it earns its keep.

I ran it across BTCUSD, EURUSD, and a few large-cap equities on the 15m and 1H charts. Here's what I actually found.

## What It Really Does

Liquidity_Draws identifies zones where buy-side and sell-side liquidity accumulate — prior swing highs where shorts' stops sit, prior swing lows where longs' stops sit, and equal-high/equal-low clusters. It then draws these as horizontal "draw" levels and, critically, tracks whether price is being pulled toward them.

The trend angle is the interesting part. Instead of treating every level as equally important, the indicator weights levels by proximity to current price and by how recently they formed. In an uptrend, it highlights the *next* liquidity pool above price as the likely target. In a downtrend, it flips. That's why it sits in the Trend category rather than Support/Resistance.

As shown in the chart above, the levels aren't static clutter — they shift priority as price moves, and the active draw level gets emphasized.

## Key Features That Stand Out

**Dynamic level weighting.** Not all liquidity is equal. The indicator deprioritizes stale levels and amplifies fresh ones. This is the single biggest reason it's more useful than a manual swing-high script.

**Draw direction bias.** It tells you *which side* price is being pulled toward, not just where levels exist. That's the trend signal.

**Clean visual hierarchy.** Active levels are bold, inactive ones fade. You can actually read the chart without fighting the indicator.

**Works across timeframes.** I found it consistent from 5m to 4H. Below 5m it gets noisy — expected, since liquidity structure breaks down at that resolution.

## Best Settings I Tested

Defaults are decent, but two tweaks made a real difference:

- **Lookback period:** Bump it from default (usually 20) to **30–40** on 1H+ charts. Shorter lookbacks over-plot and you'll see levels everywhere.
- **Level sensitivity / threshold:** Tighten it. The default flags too many minor pools. I set it to only show levels that have been touched or approached at least twice.
- **Alerts:** Turn on "draw level approached" alerts. This is where the indicator actually earns its subscription.

Leave the visual styling alone — the built-in hierarchy works.

## How I Traded It

The logic is straightforward once you stop overthinking it:

1. Identify the active draw level (the bold one).
2. Confirm trend direction on a higher timeframe.
3. Enter on the pullback *toward* the draw level, not away from it.
4. Target the draw level itself; it often acts as a magnet that price reaches, then reacts from.

**Long example:** Uptrend on 1H, price pulls back, next liquidity pool sits above at a prior swing high. Enter long on the pullback, target the pool. This worked more often than not in my testing — not because the level is magic, but because it's where other traders' stops and breakout orders genuinely sit.

**Invalidation:** If price rejects hard *at* a draw level and closes back through it, the level is exhausted. Don't re-enter blindly.

## Pros & Cons

**Pros:**
- Dynamic weighting is genuinely useful, not cosmetic
- Clear trend bias removes guesswork
- Alerts are well-implemented
- Reads cleanly even on busy charts

**Cons:**
- Default sensitivity over-plots; needs tuning
- "Liquidity" is a heuristic — it's inferring order placement, not seeing it
- No backtesting or stats panel
- Below 5m it's noise

## Who It's For

Discretionary trend traders who already think in terms of stop hunts and liquidity pools. If you trade breakouts or pullbacks on 15m–4H and want a visual map of where price is likely headed, this fits. Scalpers on 1m — skip it. Algo traders wanting hard stats — also skip it; this is a discretionary tool.

## Alternatives

- **LuxAlgo's Liquidity concepts tools** — more comprehensive if you want a full smart-money suite.
- **Plain swing high/low scripts** — free, but you lose the dynamic weighting.
- **Volume Profile** — a different lens on the same "where's the action" question; sometimes better, sometimes worse.

## FAQ

**Is Liquidity_Draws repainting?** The levels update as new structure forms, but confirmed levels don't repaint. The active draw level *can* shift — that's by design.

**Does it work on crypto?** Yes, and arguably better than forex given 24/7 markets.

**Can I use it alone?** You can, but it pairs best with a momentum or trend filter to avoid counter-trend entries.

**Is it worth the invite-only cost?** If you trade the 15m–4H range regularly, yes. If you're a casual swing trader, a free swing script does 70% of the job.

## Final Verdict

Liquidity_Draws does something most "liquidity" indicators don't: it commits to a directional bias instead of hedging with symmetric levels. That's a real edge for trend traders. It's held back by over-sensitive defaults and the inherent fuzziness of inferring order flow, but tuned properly it's a solid addition to a discretionary setup.

**Rating: ⭐⭐⭐⭐ (4/5)** — Good tool, honest about what it can and can't do. Not revolutionary, but genuinely useful.
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

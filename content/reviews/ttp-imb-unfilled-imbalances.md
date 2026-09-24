---
title: "Ttp_Imb_Unfilled_Imbalances Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/ttp-imb-unfilled-imbalances.png"
tags:
  - "ttp imb unfilled imbalances"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Ttp_Imb_Unfilled_Imbalances review: a practical look at how this ICT-style imbalance tool spots unfilled gaps, best settings, entry logic, and who should use it."
tv_script_url: "https://www.tradingview.com/script/V27gem2X-TTP-IMB-Unfilled-Imbalances/"
sources: ["https://www.tradingview.com/script/V27gem2X-TTP-IMB-Unfilled-Imbalances/"]
---
There's no shortage of imbalance indicators on TradingView, and most of them draw a few boxes and stop there. This script is built around a narrower idea: it tracks *unfilled* imbalances specifically, and it computes them across several timeframes at once rather than only the chart you happen to be on.

### What This Indicator Actually Does

The premise comes from ICT/SMC concepts: when price moves aggressively, it can leave behind an imbalance — a one-way range where little trade occurred. These zones are often treated as levels price may return to before continuing.

What this script draws is three-bar fair value gaps, defined by wicks. A bullish gap exists when the high of the first bar sits below the low of the third; a bearish gap when the low of the first bar sits above the high of the third. The box spans exactly those two extremes. Gaps are computed from four timeframes at once (4H, 1D, 1W, 1M by default, all configurable) and rendered on whatever chart timeframe you are on. Switching chart resolution does not change the levels — a weekly gap keeps the same two prices whether you are viewing 4H or 1D.

### Key Features That Set It Apart

The unfilled-only filter is the headline feature. Rather than keeping every historical gap on the chart, the script removes zones once price has worked into them far enough.

The multi-timeframe handling is the other distinguishing piece. Gaps from higher timeframes are computed and drawn on your current chart, so a weekly imbalance is visible while you are working on an intraday resolution.

Fading is a useful detail: a zone price has already eaten at least half of but which has not reached the closing threshold is drawn faded and labelled with its fill percentage. That separates an untouched imbalance from one that has already been worked, without hiding either.

### Settings and How to Tune Them

- **Filled at (%)** — the closing threshold, default 66.6. A zone stops being drawn once price has overlapped that share of the box's original height, measured from the side price enters by: a bullish gap dies when price falls that far from the top, a bearish gap when price rises that far from the bottom. 100 means only a complete traverse closes a zone; 50 is the classic midpoint rule.
- **A wick is enough to fill** — off requires a bar close beyond the threshold instead, which leaves noticeably more zones alive.
- **Zones per side, per TF** — default 3. Per timeframe, the script draws the nearest unfilled zones above price and the same number below, plus every zone that currently contains price. Those containing zones are the operative ones and are never rationed away.
- **Search range (xN)** — a multiplicative band around current price, default 2. Zones lying entirely outside price/N up to price*N are discarded before anything else. The band is a ratio, not a percentage, and that matters: a symmetric percentage band is lopsided because price moves in multiples — −80% is 0.2x while +80% is only 1.8x. Equal ratios up and down is what a log chart actually shows.
- **Dim a zone once filled (%)** — the fading threshold, default 50.
- **Rungs above chart TF** — the gating ceiling, default 2. Only timeframes at or above the chart's own are computed, and only up to that many rungs above it. On a 4H chart that gives 4H/1D/1W and drops the monthly; on a daily chart, 1D/1W/1M. Timeframes below the chart are never drawn and are not calculated at all. Set the ceiling to 3 to see everything at or above the chart, or to 0 for the chart's own timeframe only.
- **Ignore zones thinner than (%)** — an optional micro-gap filter, off by default.

Border thickness increases with timeframe, so the hierarchy reads at a glance. Partially overlapped zones keep their full original geometry — the box does not shrink, so the imbalance is always visible as it was formed.

### How to Use It

This is a visualisation tool. It marks structural levels and does not generate entry or exit signals, and there is no built-in backtester. Any use of the zones for entries, stops or targets is a discretionary overlay you bring yourself, not something the script provides.

### Pros & Cons

**Pros:**
- The unfilled-only filter reduces chart clutter compared to tools that keep every historical gap.
- Multi-timeframe gaps are computed and drawn on the current chart, with gating so lower timeframes are never calculated.
- Fading and fill-percentage labelling distinguish untouched zones from zones already worked.
- The multiplicative search band is a more sensible filter than a symmetric percentage band.

**Cons:**
- It is reactive, not predictive — it marks where price may react, not where it will.
- No signals, no backtester, no alert logic described in the script's own documentation.
- Buffers only fill as far back as the chart's loaded history reaches. On a 4H chart covering roughly two years, the monthly buffer holds about two dozen months rather than the full setting. This does not affect zones near price, which is all the script draws.

### Notes and Limitations

The still-forming higher-timeframe bar cannot *create* a zone — that would repaint intrabar — but it does count toward *filling* one, so a zone can die live as price moves into it. Everything else is closed-bar only.

The gap scan is linear in the number of bars, and the "has this gap been filled" test is answered with suffix extremes rather than a nested scan over later bars, which is what keeps four timeframes inside the execution budget instead of timing out.

### Who It's For

Traders already comfortable with order flow and market structure concepts will get the most out of it. If imbalances and fair value gaps are new to you, the zones may need additional context before they mean much. For anyone already working with supply/demand or ICT-style levels, it slots into that workflow as a structural map rather than a signal generator.

### Alternatives Worth Considering

- **Smart Money Concepts by LuxAlgo** — broader if you want the full ICT toolkit in one package.
- **Fair Value Gaps by LonesomeTheBlue** — simpler if you want basic FVGs without the unfilled-zone handling.
- **Volume Imbalance (built-in)** — adequate for quick analysis without an external script.

### Final Verdict

The script solves a real problem — isolating unfilled imbalances and computing them across timeframes — without overcomplicating the presentation. The multiplicative search band and the configurable fill threshold show more thought than most imbalance tools bother with. It is a visualisation tool and nothing more, so it belongs alongside your own process rather than in place of one.

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

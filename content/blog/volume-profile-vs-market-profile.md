---
title: "Volume Profile vs Market Profile — What's the Difference? (It's Not What You Think)"
description: "Volume Profile measures money, Market Profile measures time. They look similar on the chart but tell completely different stories. Here's how to read both — and when to trust which."
date: 2026-06-25
draft: false
type: blog
image: "/screenshots/volume-profile.png"
tags:
  - volume profile
  - market profile
  - tpo
  - order flow
  - volume analysis
  - guide
author: "The Indicator Lab"
---

## Same Chart, Completely Different Question

Volume Profile and Market Profile both paint a horizontal histogram on the right side of your chart. Side by side, you could mistake one for the other. But they're answering two fundamentally different questions:

- **Volume Profile** asks: *Where did actual money trade?*
- **Market Profile** asks: *Where did price spend time?*

If you're using them interchangeably, you're reading one of them wrong. Here's what each actually measures — and when the difference matters.

---

## Volume Profile: Where the Money Is

Volume Profile aggregates traded volume at each price level over a given period. The widest part — the **Point of Control (POC)** — is the price where the most contracts or shares changed hands. Above it, the **Value Area** (typically 70% of total volume) marks the range where institutions built their positions.

![Volume Profile on TradingView](/screenshots/volume-profile.png "Volume Profile POC and Value Area")

What makes Volume Profile unique: **you're seeing actual liquidity, not guesswork.** A price level with 50,000 contracts traded is a fact. Support and resistance derived from volume nodes are statistically stronger than any moving average or Fibonacci level — because they represent real capital commitment.

**Key levels to watch:**
- **POC (Point of Control):** Magnet level — price returns here repeatedly. Rejections off the POC are high-probability entries.
- **High Volume Nodes (HVN):** Price has memory at these levels. Treat them as zones where price will stall or reverse.
- **Low Volume Nodes (LVN):** Price moved through these levels quickly — no one wanted to trade there. In a retracement, price rips through LVNs.

→ [Read our full Volume Profile review](/reviews/volume-profile/)
→ [Read our Volume Profile Fixed Range review](/reviews/volume-profile-fixed-range/)

---

## Market Profile: Where Price Got Comfortable

Market Profile — originally developed by J. Peter Steidlmayer at the Chicago Board of Trade — organizes price into **TPOs (Time Price Opportunities)**. Each 30-minute block where price touches a level gets a letter. The result is a bell curve distribution showing where the auction spent the most time.

![Market Profile on TradingView](/screenshots/market-profile.png "Market Profile TPO chart")

The shape tells the story:

| Shape | Market Condition | What It Means |
|---|---|---|
| **Normal distribution** | Balanced, two-sided auction | Range day — fade the extremes |
| **P-shaped (skewed high)** | Buyers in control | Trend day up — don't short |
| **b-shaped (skewed low)** | Sellers in control | Trend day down — don't buy |
| **Double distribution** | News/event gap | Two separate value areas — treat as new regime |

**Market Profile excels at one thing Volume Profile can't do:** showing you the *structure* of the auction. A double distribution tells you something happened mid-session that reset fair value. Volume Profile won't show that — it just accumulates volume across the whole period.

The **Value Area** in Market Profile (also 70%) marks where 70% of TPOs occurred — it's about *time acceptance*, not traded volume. Price that spends 6 hours at a level without heavy volume means something different from a level that traded 50K contracts in 30 minutes.

→ [Read our full Market Profile review](/reviews/market-profile/)

---

## The Critical Difference

Here's where traders get burned: **a volume-heavy level is not the same as a time-heavy level.**

| | Volume Profile | Market Profile |
|---|---|---|
| **Measures** | Volume traded at price | Time spent at price |
| **Best for** | Support/resistance, liquidity zones | Auction structure, market condition |
| **POC means** | Where the most money traded | Where price spent the most time |
| **Value Area based on** | 70% of volume | 70% of TPOs (time) |
| **Strength** | Actual capital commitment | Fair value discovery |
| **Weakness** | Hides auction structure | Ignores trade size |

**Real example:** A level where one institution dumped 10,000 contracts in 2 minutes shows as a massive volume node. Market Profile at that level would be a thin TPO strip — barely registered. If you only read Market Profile, you'd miss the elephant that just walked through the room. If you only read Volume Profile, you'd see the volume but miss that price never *accepted* that level — it was a rejection, not a value area.

---

## When to Use Which

| Scenario | Trust This |
|---|---|
| Finding support/resistance levels | **Volume Profile** — volume nodes are objective |
| Identifying trend vs range days | **Market Profile** — distribution shape tells you instantly |
| Intraday entries | **Market Profile** — TPO structure shows real-time auction |
| Swing trade entries | **Volume Profile** — multi-day POC and Value Areas |
| Detecting absorption/exhaustion | **Volume Profile + CVD** — volume nodes + delta divergence |
| Understanding market sentiment | **Market Profile** — skewed distributions reveal control |

→ [Read our CVD review](/reviews/cvd/) — Cumulative Volume Delta adds buy/sell pressure to volume profile levels

---

## The Stacking Play — Use Both

The pros don't pick one. They layer Volume Profile on top of Market Profile and read the disagreements.

**When Market Profile shows a POC at $100 but Volume Profile shows the POC at $102:** price spent time at $100 (acceptance) but the real money traded at $102 (commitment). That $2 gap is where the edge lives — and where most retail traders never look.

Combine both with **Footprint Charts** if you want max granularity — bid/ask volume at every price level, not just the aggregate.

→ [Read our Footprint Chart review](/reviews/footprint-chart/)

---

## Bottom Line

Volume Profile shows you where the money is. Market Profile shows you where fair value is. They answer different questions, and if you're only using one, you're missing the other half of the auction. Stack both — and pay attention to where they disagree.

---

*Tested on TradingView. Volume Profile is available with a Pro plan. Market Profile requires third-party indicators — [grab a TradingView Pro account here](https://www.tradingview.com/?aff_id=166324) to unlock both.*

---
title: "Quarterly Theory True Opens Takingprophets Review — Trend"
date: 2026-11-07T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/quarterly-theory-true-opens-takingprophets.png"
tags:
  - "quarterly theory true opens takingprophets"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Quarterly Theory True Opens [TakingProphets]: plots session-to-year True Opens, premium/discount stacks and alerts. No signals, no hype."
tv_script_url: "https://www.tradingview.com/script/PrCA8XWU-Quarterly-Theory-True-Opens-TakingProphets/"
sources: ["https://www.tradingview.com/script/PrCA8XWU-Quarterly-Theory-True-Opens-TakingProphets/"]
---
Most "open" indicators do one thing: slap a horizontal line at the daily open and call it a day. Quarterly Theory True Opens [TakingProphets] goes further, plotting the True Open of five nested cycles — session, day, week, month and year — on a single chart. Whether that's useful depends entirely on what you expect it to do.

The author is explicit that it provides no signals and no forecasts. That honesty is worth noting, because a lot of tools in this space pretend to be more than they are.

## What a "True Open" actually is here

Quarterly Theory divides any time cycle into four quarters. The True Open is the open of the second quarter — the reference price the rest of the cycle is measured against. Price below that level is treated as discount for that cycle; price above it is premium.

The indicator works out where Q2 begins for each cycle and plots it:

- **Session:** the open of the candle at 19:30, 01:30, 07:30 or 13:30 New York time, depending on which 6-hour session is in play.
- **Day:** the 00:00 open of the 18:00-to-18:00 trading day (London session, Q2).
- **Week:** the Monday 18:00 open, since Tuesday's trading day is the week's second quarter.
- **Month:** the Sunday 18:00 open before the second Monday (the Monday dated the 8th to the 14th).
- **Year:** the open of the first trading day of April.

All cycles run on New York time with the 18:00 anchor. That's standard for ICT-style work, but if you don't already think in that time zone, expect an adjustment period.

## The engineering detail that matters

The part I find genuinely well thought out is how the opens are sampled. Rather than approximating an open from whatever chart timeframe you happen to be on, the indicator reads each True Open from a data stream whose candles begin exactly on that boundary — the chart timeframe up to 30 minutes, a 30-minute stream above that, daily for week and month, monthly for the year. The plotted price is the open of the real candle at that time, on any chart timeframe.

That sounds like plumbing, but it's the difference between a line that's a few ticks off and one you can actually trust as a reference.

Two more details deserve credit. Gap handling means a True Open only prints when its time falls inside the trading day being opened — no phantom opens for clock times that passed while the market was shut. And opens are fixed once their candle opens, with no look-ahead. For an educational tool, that's the right design.

## Reading the chart

Each cycle gets a line starting at its open's candle. Completed opens stop where their cycle ended; the open in play extends just past the current candle. Labels sit at the line ends with short codes (TSO, TDO, TWO, TMO, TYO) or full names, and you can optionally include the price. When opens overlap at the same price and time, they merge into a single label, highest cycle first — so you might see something like "TDO + TSO London" instead of a pile of unreadable text.

The stack panel is the feature that earns the fourth star. It lists each cycle's True Open price, whether price is above or below it, and the current stack state: premium, discount, or not stacked. The counter tracks how many consecutive cycles line up in the same order starting from the session. When price sits below the session open, which sits below the day open, and so on up the ladder, that's a discount stack. The mirror order is a premium stack.

That's the analytical question Quarterly Theory is really asking — how many cycles agree — and the panel answers it without you eyeballing five lines.

You can also keep the last few completed opens per cycle on the chart for reviewing reactions, and hide opens that are too small for your timeframe.

## Pros and cons

**Pros**
- Five cycles computed from their actual Quarterly Theory definitions, not approximations.
- Exact-open sampling means the printed price matches the real candle regardless of chart timeframe.
- Gap handling and no look-ahead — the opens are honest.
- The stack panel turns a visual exercise into a countable one.
- Label merging keeps cluttered charts readable.
- Alerts on price crossing the session, day and week True Opens.

**Cons**
- No month or year crossing alerts — only session, day and week.
- No strategy module or backtest engine, so you can't quantify anything inside the tool.
- Session and day opens are built for around-the-clock markets; on shorter-session markets some opens simply won't exist.
- The year open won't show on very low timeframes — it appears on 15m and higher.
- It's a reference tool, not an edge. If you want something that tells you what to do, this isn't it.

## How I'd actually use it

The author suggests starting on a 5m or 15m chart to see session, day and week opens together, then journaling price behaviour when several True Opens stack versus when they don't. That's a sensible workflow, and it's the one this tool is built for. Turn on previous opens to review how price reacted at earlier True Opens, use the panel to note premium or discount status, and let the alerts handle crossings so you're not glued to the screen.

The honest limitation: this is a study aid. It documents where the reference levels are. What you do with that is on you.

## Who it's for

ICT-style traders already familiar with Quarterly Theory who want the opens marked without manual drawing. Educators and mentors teaching cycles and quarters will get the most out of it — the label merging and stack panel are clearly built with explanation in mind. Discretionary traders who journal reactions at key levels will find it useful. Anyone looking for entries, signals or a mechanical system should look elsewhere.

## FAQ

**Does it repaint?**
No. Opens are fixed once their candle opens, and the author states no look-ahead is used.

**Will it work on stocks?**
Session and day opens are timed for markets that trade around the clock — futures, forex and crypto. On markets with shorter sessions, some opens may not exist.

**Why can't I see the year open?**
On very low timeframes TradingView may not load enough higher-timeframe history. It shows on 15m and higher.

**Can I backtest it?**
No strategy module or backtest engine is included. It's a study, not a strategy.

## Verdict

⭐⭐⭐⭐

Quarterly Theory True Opens does one job and does it carefully. The exact-open sampling and gap handling are the kind of detail that separates a trustworthy reference tool from a decorative one, and the stack panel adds real analytical value on top. It loses a star for scope: no month or year alerts, no way to quantify anything, and a hard dependency on around-the-clock markets and New York time.

If you already work in this framework, it's a clean, well-engineered replacement for manual drawing. If you're hoping it will tell you when to buy, it won't — and it never claims to.
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

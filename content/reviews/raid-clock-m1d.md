---
title: "Raid Clock M1d Review — Trend Indicator"
date: 2026-10-03
draft: false
type: reviews
image: "/screenshots/raid-clock-m1d.png"
tags:
  - "raid clock m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Raid Clock M1D review: a liquidity-raid timing tool that measures when twelve ICT-style pools get swept and reads the history back as a conditional."
sources: ["https://www.tradingview.com/script/V4GBtM1P-Raid-Clock-M1D/"]
---
Most "liquidity" indicators tell you a level exists. Raid Clock M1D tells you *when* that level tends to get taken — and, more usefully, how often it still gets taken given that it hasn't been taken yet today.

That second part is the whole point of the script, and it's worth understanding before you decide whether you need it.

## What it actually does

The indicator tracks twelve liquidity pools in six pairs: the previous day's, week's, and month's high and low, plus the high and low of the Asia, London, and New York sessions. While a pool is live, it's tested on every closed candle. A wick through the level counts as a raid by default; a close through it is available as an alternative.

The first raid records its thirty-minute slot and whether the candle closed back inside. Nothing is written to the history until a cycle has ended — the author is explicit that counting the running cycle would understate the rate every time.

Then comes the conditional. Given a pool is still unswept at the time currently on the clock, the conditional is the share of comparable past cycles that went on to take it before their own cycle ended. Cycles already raided earlier in the day are removed from both sides. At the moment a pool is set, the conditional equals the headline rate; from there the two diverge as the day runs. That's a genuinely different question from "how often does PDH get swept," and it's the reason this tool exists.

## The archive and the clock

The statistical day runs 18:00 to 18:00 New York and is named for the regular session date it contains, so Sunday evening belongs to Monday. Friday runs into Sunday as one rollover — no fake day invented for a closed market.

On NQ, MNQ, ES, MES, GC, and MGC, the counts were measured once per product on five years of one-minute data — roughly 1,290 statistical days each — and are carried in the script. That means the rates don't depend on how much history your chart loads. Cycles finishing after the archive are added on top.

Two honest caveats the author volunteers: the month holds only 58 complete cycles, a thinner sample than the day or the week. And a cycle whose level was set on one quarterly contract and tested on the next is excluded, since the price step between contracts isn't a raid. The month gets special handling because it crosses a roll about two times in three. Other symbols fall back to loaded history, and the panel says so.

## How you'd actually use it

The panel is the working surface. One row per timed pool: the same live conditional its line carries on the chart, plus the counts behind it, or the time it was taken. Hovering a row gives the price, the rate across all cycles, and whether the line has been removed.

The long panel mode adds one chosen pool broken out across seven windows of the day, with the Monday-to-Friday split on hover. That's where you'd look if you want to know whether a given pool behaves differently on a Friday than a Tuesday.

There are seventeen alerts — the raid of each timed pool, the previous quarter's high and low, equal highs taken, equal lows taken, and a pool still unswept entering its busiest window. That last one is the alert most people will actually want.

## The visual grammar

Levels are drawn from the candle that formed them to a fixed point right of price. Day, week, and equal highs/lows are on by default; month and quarter are one switch each. The quarter and the equal highs/lows are drawn but not timed — five years hold only about twenty quarters, and a pool of equal highs or lows has no cycle to time.

A taken level turns dotted, stops at the candle that took it, and its name moves to the swing that made it with a cross. Session pools draw as lines or tags; a taken one is removed, and one left far from price or long untouched is retired with its reason on the panel's hover. Every coordinate is a timestamp, so nothing drifts off its candle.

## Pros and cons

**Pros**

- The conditional framing is the real contribution. It answers a question a static hit rate can't.
- The archive removes the "how much history do I need to load" problem on the six covered products.
- No repainting on completed cycles, and raids are recorded on confirmed candles only. Higher timeframe values come from the previous closed period.
- Times resolve through the New York clock, so the grid holds across daylight saving on any symbol.
- The self-checking is unusually honest — slot counts, window counts, and raid counts must reconcile, and the panel flags it if they don't.

**Cons**

- It needs a 30-minute chart or finer and says so on a coarser one. That's a real constraint on how you use it.
- The month sample is thin at 58 cycles, and the author says so rather than hiding it.
- Outside the six archived products, you're back to loaded history — the rates become chart-dependent.
- A session pool set on a Friday close outlives one turn of the clock, and its rate is marked with a star rather than presented straight. Correct, but it means one row is always slightly different from the rest.
- It's a measurement tool. No entries, targets, or stops. If you want signals, this isn't it.

## Who it's for

Discretionary intraday traders working ICT-style liquidity concepts on NQ, ES, or GC who want to know whether a level is still worth watching at 10:30 versus 09:35. Also useful for anyone building a ruleset around session opens who needs the historical distribution rather than a vibe.

It is not for swing traders, not for anyone on daily charts, and not for people who want the indicator to tell them what to do.

## FAQ

**Does it repaint?** No completed cycle is revised, and raids are recorded on confirmed candles only.

**Does it work on any symbol?** It runs anywhere, but the archived counts only cover NQ, MNQ, ES, MES, GC, and MGC. Elsewhere it falls back to loaded history and the panel says so.

**Can I change what counts as a raid?** Yes — wick through by default, close through available.

**Does it give buy and sell signals?** No. It counts what a chart already contains.

## Verdict

This is a well-built, unusually candid tool. The author tells you where the sample is thin, excludes the cycles that shouldn't count, and refuses to report a rate for a cycle that hasn't finished. The conditional is a real idea, not a repackaged hit rate.

The reason it isn't five stars is scope: it's a measurement layer, not a system, and its strongest data only covers six products on intraday timeframes. If that's your patch, it's close to essential. If it isn't, you're paying for a framework you won't fully use.

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

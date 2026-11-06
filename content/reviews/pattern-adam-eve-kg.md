---
title: "Pattern Adam Eve Kg Review — Chart Pattern Indicator"
date: 2026-11-07T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/pattern-adam-eve-kg.png"
tags:
  - "pattern adam eve kg"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Pattern-Adam & Eve [KG], a TradingView study that auto-detects the classic V-and-U reversal setup and marks neckline breakouts."
tv_script_url: "https://www.tradingview.com/script/E0rCVI6M-Pattern-Adam-Eve-KG/"
sources: ["https://www.tradingview.com/script/E0rCVI6M-Pattern-Adam-Eve-KG/"]
---
Most pattern indicators are glorified zig-zag drawers: they connect a few pivots and call it a day. Pattern-Adam & Eve [KG] tries something more ambitious. It looks for a specific two-bottom reversal structure — a sharp, spiky low (Adam, the V) followed by a rounder, lazier low (Eve, the U) — both forming near the same price level with a "neckline" peak sitting between them. If price then breaks that neckline, the script fires a breakout signal. Flip the logic and you get the bearish mirror: a V-top plus a dome-top.

That's the whole premise, and it's a legitimate one. The Adam & Eve formation is a staple of classical pattern trading, and automating the search saves you from eyeballing hundreds of charts.

## How it actually decides what's what

The interesting part is the classification logic, because this is where most pattern scripts cut corners. According to the developer, the script uses pivot highs and lows to locate the two bottoms, then checks that they're roughly equal — with the tolerance scaled by ATR, so the acceptable gap widens in volatile conditions and tightens in quiet ones. That's a sensible design choice, since a fixed price tolerance would flag nothing on a high-volatility instrument and everything on a sleepy one.

It also requires the pattern to be deep enough and checks for a prior trend heading into Adam. Both filters matter — a reversal pattern with no trend to reverse is just noise.

Then there's the V-versus-U test, and it's genuinely clever: the script counts how many bars sit inside a band around each bottom. Few bars in the band means a sharp V (Adam); many bars means a rounded U (Eve). It's a crude proxy for shape, but it's cheap, deterministic, and doesn't require curve-fitting splines to price data. The developer calls it a "cute little trick," and that's a fair self-assessment.

## What shows up on your chart

Nothing here is subtle, which is a good thing for a pattern tool. You get the neckline drawn across the formation, shaded triangles and bowls marking Adam and Eve, and text labels ("Adam," "Eve," "V + U," "Neckline Breakout"). Arrows indicate the prior trend and the projected measured move. Triangle markers appear on breakout bars, and alert conditions are built in so you can be notified without staring at the screen.

One feature deserves a mention because you rarely see it: a toggleable reference gallery that draws textbook bullish and bearish examples out in chart space. It's a small thing, but if you've ever forgotten which shape is Adam and which is Eve mid-session, it solves that problem permanently.

## Tuning knobs

The input list is long, and that cuts both ways. You can adjust pivot length, ATR period, the max ATR difference between bottoms, minimum depth, minimum and maximum bars between Adam and Eve, trend lookback, how many bars to wait for a breakout, the V-versus-U band width, colors, and gallery placement.

For a discretionary trader who wants the tool to surface candidates, that's plenty of rope. The risk is over-tuning: with this many parameters, it's easy to fiddle until the pattern only appears on the charts you already know worked. The developer is upfront about this being a detection tool, not a strategy — the disclaimer explicitly warns that an Adam & Eve sighting doesn't guarantee a reversal any more than a hammer guarantees profits. That honesty is worth noting.

## How I'd actually use it

Treat it as a scanner and a visual aid, not a signal generator. Let it flag candidate formations, then do your own work: is the prior trend meaningful, is the neckline at a level that matters, and does the breakout have any follow-through context? The measured-move projection is a reference, not a target. The built-in maximum wait for a breakout is useful because it stops stale patterns from lingering on your chart indefinitely.

## Pros and cons

**Pros:** The ATR-scaled tolerance and bar-count shape test are thoughtful, non-obvious design choices. The visual output is clear and self-documenting. Alerts are included. The reference gallery is a nice touch. And the developer doesn't oversell it.

**Cons:** The bar-count proxy for "roundedness" is approximate — a choppy sideways base can register as Eve without truly looking like one. The parameter count invites overfitting. And like every pattern detector, it will produce false positives; the script identifies shape, not intent.

## Who it's for

Discretionary traders who already trade reversal patterns and want the hunt automated. Swing traders on higher timeframes will get more out of it than scalpers, since the structure needs room to form. If you want a black-box buy/sell signal, this isn't it — and it doesn't pretend to be.

## FAQ

**Does it repaint?** The source doesn't specify, but pivot-based detection inherently confirms after the pivot forms. Treat signals as confirmed-late, not predictive.

**Does it work on any market?** The ATR scaling is designed to adapt across volatility regimes, but the source makes no market-specific claims. Test on your own instruments.

**Can I backtest it?** It's a study with alert conditions, not a strategy script. You'd need to build the strategy logic yourself.

## Verdict

A well-constructed pattern detector with genuine thought behind its classification logic and an honest developer disclaimer. It won't trade for you, and it can be over-tuned into uselessness — but as a visual scanner for a classic setup, it earns its place.

**Rating: ⭐⭐⭐⭐**
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

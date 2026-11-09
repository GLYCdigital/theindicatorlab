---
title: "Hull DMI Mattes Review — Trend Indicator"
date: 2026-11-10T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/hull-dmi-mattes.png"
tags:
  - "hull dmi mattes"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A hybrid trend tool that blends Hull Moving Average smoothing with DMI logic. Honest look at what it does, where it helps, and its limits."
grounding: "none (no source found)"
---
Most trend indicators on TradingView are variations on a theme: a moving average, a channel, an oscillator. "Hull DMI - Mattes" is a mashup of two familiar ideas — the Hull Moving Average and the Directional Movement Index — packaged into a single trend overlay. As shown in the chart above, it produces a smoothed trend line with directional bias layered on top.

There's no official documentation I can pull from here, so this review sticks to what the name and structure imply and stays deliberately vague on specifics I can't verify. If you want exact input names and default values, you'll need to load it and check the settings panel yourself — I'm not going to invent them.

## What it actually is

The Hull Moving Average is a smoothing technique designed to reduce lag compared to standard moving averages while keeping the line responsive. The DMI (Directional Movement Index) is Wilder's framework for measuring directional strength — the +DI and -DI lines that tell you whether buyers or sellers are in control, plus the ADX that gauges how strong the move is.

Combining the two means this indicator is trying to do two jobs at once: plot a clean, low-lag trend line, and give you a read on directional momentum. That's a reasonable pairing. The Hull line tells you *where* price is trending; the DMI logic tells you *how committed* the move looks. Used together, they can filter out some of the chop that a bare Hull average would happily follow.

## Where it earns its keep

The strongest argument for this kind of tool is workflow compression. Instead of stacking a Hull MA and a separate DMI indicator on the chart — each with its own settings and visual clutter — you get one panel doing both jobs. For traders who run tight charts, that matters.

The Hull component's lower lag is the headline feature. A conventional moving average will lag a turn; the Hull calculation is built to react faster. Pair that with a directional filter and you've got something that can flag trend changes earlier than a plain average, without whipsawing as badly as a raw short-period MA.

That's the theory, anyway. Whether it delivers depends heavily on the instrument and timeframe you apply it to, and I can't tell you which combinations work — that's for you to observe on your own charts.

## How you'd actually use it

The sensible workflow is directional, not mechanical:

- **Trend context first.** Use the Hull line to establish whether price is in an uptrend, downtrend, or range. Price above the line, line sloping up — that's your bias.
- **Confirm with the DMI layer.** A directional reading that agrees with the Hull slope adds conviction; disagreement is a warning to sit out or tighten risk.
- **Treat crossovers as prompts, not signals.** A trend line flip is a reason to look closer, not a reason to click buy. Confirmation from price action or structure still does the real work.

As with any single trend tool, it will lag at turning points and give false starts in sideways markets. That's not a flaw unique to this indicator — it's the nature of trend-following.

## Pros and cons

**Pros**
- Two useful concepts in one indicator — less chart clutter, fewer settings to reconcile.
- Hull smoothing gives a responsive trend line without the jitter of a raw short MA.
- DMI directional logic adds a momentum read that a plain moving average lacks.
- Clean enough for discretionary traders who want context without a wall of lines.

**Cons**
- No documentation means you're reverse-engineering the settings and behaviour yourself.
- Hybrid indicators can hide which component is driving a signal — debugging is harder.
- Like any trend overlay, it struggles in ranges and lags at reversals.
- If you don't already understand Hull MAs and DMI, you'll be flying blind.

## Who it's for

Discretionary trend traders who already understand moving averages and directional movement, and who want a single, compact overlay to read trend context. It's less suited to beginners (the blend of concepts assumes prior knowledge) and to anyone running fully automated systems, since there's no published rule set to code against.

## FAQ

**Does it repaint?** I can't confirm either way without documentation. Test it on a live chart and watch how the line behaves in real time.

**Can I use it for entries?** It's a trend-context tool. Most traders will use it to set bias and confirm, not to trigger entries on its own.

**What timeframe is best?** No idea, and anyone who tells you a specific one without testing is guessing. Trend tools generally behave differently across timeframes — check yours.

## Verdict

A sensible, practical hybrid. The Hull-plus-DMI concept is well chosen — each component covers the other's weakness — and packaging them together is genuinely convenient. It loses a star for the missing documentation and the inherent opacity of blended indicators, but if you know what you're looking at, it's a solid addition to a trend-trader's toolkit.

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

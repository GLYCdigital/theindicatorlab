---
title: "Alligator vs Gator Oscillator — Father and Son Compared"
description: "Alligator vs Gator Oscillator: the Gator is the histogram of the Alligator's line gaps. Same data, different view — which is more useful for entries?"
date: 2026-08-14
draft: false
type: blog
image: "/screenshots/alligator.png"
tags:
  - alligator vs gator oscillator
  - bill williams alligator
  - gator oscillator
  - bill williams trading system
  - comparison
author: "The Indicator Lab"
---

## The Family Secret Nobody Tells You

The "Alligator vs Gator Oscillator" question is usually framed as a choice between two Bill Williams tools. It isn't. Here's the part every top-ranking article dances around: **the Gator Oscillator contains zero new information.** It's not a second indicator — it's the Alligator's math, redrawn as a histogram.

Every Gator bar is just the distance between two of the Alligator's lines. If you can subtract, you can build the Gator by hand from the Alligator alone.

Once you accept that, the real question isn't "which is better?" — it's "which *view* of the same data helps you trade?" That's a question with an actual answer.

---

## The Math: Father and Son Share the Same DNA

The Alligator is three smoothed moving averages, each offset into the future:

- **Jaw** (blue) — 13-period SMMA, shifted 8 bars forward
- **Teeth** (red) — 8-period SMMA, shifted 5 bars forward
- **Lips** (green) — 5-period SMMA, shifted 3 bars forward

The offsets do the real work. They're Bill Williams' "confirmation delay" — the lines only untangle after a move has proven itself, which filters out chop.

The Gator Oscillator is the same three lines, subtracted:

- **Top histogram** = Jaw − Teeth (how far the jaw has opened from the teeth)
- **Bottom histogram** = Teeth − Lips (how far the teeth are from the lips)

That's the whole indicator. No new smoothing, no new period, no new logic. The Gator is the Alligator's line-gaps, plotted as bars instead of lines.

![Alligator on TradingView](/screenshots/alligator.png)

→ [Read our full Bill Williams Alligator review](/reviews/alligator/) — the 13/8/5 settings, wake-up entries, and why the forward offsets matter

![Gator Oscillator on TradingView](/screenshots/gator-oscillator.png)

→ [Read our full Gator Oscillator review](/reviews/gator-oscillator/) — how the top/bottom histograms read expansion and contraction

---

## Where the Gator Actually Wins

Since it's the same data, the Gator's only advantages are presentational — but presentational advantages are real:

**1. Awake/asleep at a glance.** The Alligator's sleeping state is three tangled lines — you have to squint to see it. The Gator makes it binary: both histograms green and growing = awake, trending. Both red and shrinking = asleep, stay out. On a multi-chart watchlist, that's a dramatically faster scan.

**2. No price overlap.** The Alligator draws on top of price, which can clutter your chart. The Gator lives in its own pane. If you're already trading off candlesticks and only want the trend-state filter, the Gator keeps your chart clean.

**3. Expansion speed is visible.** Because the bars encode distance, you can see *how fast* the alligator is waking up — bars growing quickly = strong impulse, bars creeping = weak drift. The Alligator shows separation but not velocity.

---

## Where the Alligator Wins (and It's Not Close)

The Gator's weakness is the flip side of its design: **it throws away price.**

- The Alligator tells you *where price sits relative to the lines* — above all three (bullish), below all three (bearish), or tangled inside. That positional information is your entry and exit. The Gator can't show it because it doesn't plot price at all.
- Stops. The standard Alligator trade stops below the Jaw. The Gator has no levels to anchor a stop — you'd be guessing.
- Divergence. Price making a higher high while the Alligator's lines flatten is a visible warning. The Gator's histogram can't diverge from itself.

For actual entries and exits, the Alligator is the complete tool. The Gator is a dashboard light.

---

## The One Legit Setup: Use the Gator as a Filter

The cleanest way to run both: trade the Alligator, screen with the Gator.

On your entry timeframe, use the Alligator's wake-up rules — price above all three lines, Lips crossed above Teeth, enter, trail the Jaw. On your watchlist, use the Gator to rank candidates by whether the histograms are green, expanding, and aligned (top and bottom both positive). You get the filter's speed and the Alligator's precision, without ever double-counting a signal — because there's only one signal.

One thing to avoid: treating Gator green bars as "confirmation" of the Alligator's wake-up. It's the same measurement twice. That's not confluence, it's a mirror — and mirrors are how traders talk themselves into doubling position size.

---

## Bottom Line

The Gator Oscillator is the Alligator's histogram — same data, different shape. The Gator wins on readability and scanning speed; the Alligator wins on everything that involves price, stops, and entries. Use the Gator to find waking alligators, use the Alligator to trade them, and never argue with anyone who tells you they're "different indicators." They're the same animal — one just shows you its teeth.

If you want genuinely independent confirmation of the Alligator's signals, add something that doesn't share its DNA — like [Fractals](/reviews/fractals/) for structure or the [Awesome Oscillator](/reviews/awesome-oscillator/) for momentum. That's real confluence.

---

*All indicators tested on TradingView. Build your own Bill Williams layout with a [TradingView Pro account here.](https://www.tradingview.com/?aff_id=166324)*

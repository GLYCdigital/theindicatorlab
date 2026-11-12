---
title: "Keltner Channels vs Bollinger Bands — Volatility Envelope Showdown"
description: "Keltner is ATR-based, Bollinger is standard deviation. Which one hugs price in a trend, which lies in a range, and why the squeeze fires twice."
date: 2026-11-13
draft: false
type: blog
image: "/screenshots/keltner-bollinger-combo.png"
tags:
  - keltner channels
  - bollinger bands
  - atr
  - volatility bands
  - comparison
  - guide
author: "The Indicator Lab"
---

## Same Shape, Different Physics

Both indicators draw an envelope around a moving average. Both look like price squeezed inside a tube. That's where the similarity ends.

Bollinger Bands measure **standard deviation of price**. Keltner Channels measure **average true range**. One is a statistics tool describing how far price has wandered from its mean. The other is a range tool describing how far price has actually traveled, gaps included.

That single difference explains nearly every practical behavior difference between them — and it's the part most comparison articles skip past on the way to "Bollinger for ranges, Keltner for trends."

![Keltner Channels and Bollinger Bands stacked on the same chart](/screenshots/keltner-bollinger-combo.png)

## What Each Band Is Actually Measuring

Bollinger's math: 20-period SMA of close, ±2 standard deviations of that same close series. Standard deviation is computed *relative to the mean*, so as price accelerates in one direction, the deviation balloons. The band chases the move.

Keltner's math: 20-period EMA of close, ±2× ATR(10) by the classic Linda Raschke setting. ATR is computed from the *high-low range plus gap adjustment*, then smoothed. It's an absolute dollar distance that lags the move rather than chasing it.

The consequence: **Bollinger width expands violently during a breakout. Keltner width expands slowly and steadily.** If you're waiting for price to close back inside the bands after a breakout, Bollinger tells you "already did" while Keltner says "still outside, still trending."

## The Conversion Nobody Mentions

Here's the part that changes how you set these up. A 2× ATR band is roughly equivalent to **1.5 to 1.6 standard deviations**, not 2. ATR is systematically larger than standard deviation on any instrument that gaps or has fat tails — which is all of them.

So if you're trying to make Keltner match your Bollinger 2σ feel, you want a Keltner multiplier around **2.5× ATR**, not 2. Most traders run the default 2 and then conclude Keltner is "too tight" in trends. It isn't too tight — it's calibrated to a different unit.

This is also why the TTM Squeeze fires on the Bollinger-inside-Keltner condition: it's not detecting absolute quiet, it's detecting when statistical deviation has compressed *below* ATR-based range. That's a real, measurable compression — not just a narrow drawing. Read the [TTM Squeeze review](/reviews/ttm-squeeze/) before you trade that signal, because the squeeze release direction is where people get hurt.

## Which Hugs Price Better — Trend or Range

**In a clean trend: Keltner wins.** ATR smoothing doesn't spike on a single large candle, so the band stays parallel to price and gives you a stable pullback reference. Price riding the upper Keltner band for 15 bars is a trend signal. Price riding the upper Bollinger band usually means the band has been dragged upward to meet it — the "walk the band" setup, then a snap back to the middle. If you're using bands as trailing support, [ATR](/reviews/atr/) is the better denominator precisely because it doesn't react to the mean.

**In a range: Bollinger wins.** Standard deviation contracting is exactly the information you want — it tells you participation is dying. Keltner in a tight range just sits there, because ATR includes the wick noise that ranges are made of.

The practical test: put both on and watch which one price *respects as a bounce level* rather than *penetrates as a signal*. In chop, price turns at Bollinger. In trend, price turns at Keltner's mid-line EMA. That mid-line is the most underrated part of the whole indicator — it's a trend filter disguised as a band center.

## Settings That Actually Work

- **Keltner trend-following:** EMA 20, ATR 10, multiplier 2.0. Mid-line = trend filter. Closes beyond the outer band with volume = continuation, not exhaustion.
- **Keltner mean reversion:** multiplier 2.5–3.0. Below that you're buying noise.
- **Bollinger range trading:** 20, 2.0. Standard. Only trade the touch when the mid-line is flat.
- **Bollinger squeeze watch:** 20, 2.0 plus BandWidth — the %B and width readings matter more than the touch itself.

You can see how the two-band overlay behaves in practice in the [Keltner/Bollinger combo review](/reviews/keltner-bollinger-combo/), where both envelopes are stacked on the same pane. It's the fastest way to internalize the lag difference without writing any code.

For the full three-way breakdown including Donchian Channels, see [Bollinger vs Keltner vs Donchian](/blog/bollinger-bands-vs-keltner-channels-vs-donchian/). Individual breakdowns: [Keltner Channels](/reviews/keltner-channels/) and [Bollinger Bands](/reviews/bollinger-bands/).

## The Verdict

Don't pick one. Keltner is your trend structure tool — stable, ATR-anchored, honest about gaps. Bollinger is your compression and mean-reversion tool — statistical, self-normalizing, loud about quiet. Running both tells you *why* volatility is doing what it's doing, which neither one can tell you alone.

The traders who get burned are the ones who pick a favorite and then force it into the wrong regime.

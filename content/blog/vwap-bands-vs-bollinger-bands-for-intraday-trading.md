---
title: "VWAP Bands vs Bollinger Bands for Intraday Trading"
description: "VWAP bands anchor to the session; Bollinger Bands roll over 20 bars. That difference decides which one you fade intraday — and when fading either loses money."
date: 2026-11-16
draft: false
type: blog
image: "/screenshots/vwap-bands.png"
tags:
  - vwap
  - bollinger-bands
  - intraday-trading
  - mean-reversion
author: "The Indicator Lab"
---

## Two Bands, Two Different Definitions of "Normal"

Slap VWAP Bands and Bollinger Bands on the same 5-minute chart and they look like cousins. A center line, an envelope around it, price ping-ponging between the edges. Most comparison articles stop at "VWAP is volume-weighted, Bollinger is not" and call it a day.

That's the least useful part of the answer. The real difference is what each band is measuring: **where volume actually traded today** versus **where price has been for the last 20 bars**. One is anchored. One is rolling. They answer different questions, and they fail in opposite conditions.

![VWAP Bands on an intraday chart](/screenshots/vwap-bands.png)

## Bollinger Bands: A Rolling Statistical Envelope

Standard settings: 20-period SMA, 2 standard deviations. The math is computed on closing prices, equally weighted, and the window slides forward one bar at a time.

Two consequences:

1. **Volume is invisible.** A 20-bar window can contain 4 million shares or 400,000. The band width doesn't care. A quiet drift and a heavy participation move of the same point size get identical treatment.
2. **The mean lags by design.** In a trend, the SMA drags behind price, so price "walks the band" — riding the upper band for 30 bars while people short every touch and donate money to the market.

Bollinger's strength is regime detection, not level detection. Band width contraction (the squeeze) tells you volatility is compressing. That signal is genuinely useful. The band *level* is much weaker as a mean-reversion target because it's just a 20-bar average of wherever price happened to be.

If you want the mechanics in detail, the [Bollinger Bands review](/reviews/bollinger-bands/) covers the standard build; the [Bollinger BandWidth](/reviews/bollinger-bands-width/) indicator is the cleaner way to trade the squeeze without pretending the bands are support and resistance.

## VWAP Bands: A Cumulative Session Anchor

VWAP Bands take the volume-weighted average price and add standard deviation envelopes — usually 1σ, 2σ, 3σ. But the σ here is computed from the session's cumulative volume-weighted variance, not a rolling window.

That gives you three properties Bollinger simply cannot have:

- **The band is anchored to today's actual business.** The 2σ band is roughly "two standard deviations away from where the volume actually changed hands." Institutions benchmark fills to VWAP. That makes the center line a real reference price, not a statistical artifact.
- **Band width grows into the session.** Early in the day, the cumulative sample is thin, so the σ is noisy and the bands are unreliable. By midday the envelope has converged and touches mean something.
- **The last bar is provisional.** As new volume prints, today's VWAP and σ shift. Historically the indicator doesn't repaint, but the live right edge does move. Any band touch in the final minutes of a bar is a moving target.

That's the flaw nobody warns you about: **VWAP band touches in the first 30–45 minutes are statistically meaningless.** Not weak — meaningless. You're computing standard deviation off a handful of bars. It's the most common misuse of the tool.

For the math and the different band builds, see the [VWAP Bands review](/reviews/vwap-bands/) and the [VWAP Standard Deviation Bands](/reviews/vwap-standard-deviation-bands/) write-up.

## The Decision Rule

They're not competitors — use each for what it measures.

**Use VWAP Bands for the level.**
- Fade 2σ touches only after 45 minutes into the session.
- Treat the VWAP center line as the magnet, and the 2σ as the extreme. If price is beyond 2σ and volume is declining, the move is unsupported — that's your fade.
- On trending days price rides the band like Bollinger. Don't fade — the band is telling you the trend is volume-supported.

**Use Bollinger Bands for the regime.**
- BandWidth contraction = expect expansion. Size up on breakout setups, not fades.
- %B tells you where in the envelope price sits, normalized — useful for confluence with the VWAP band position.
- Never fade a Bollinger touch in a trend. The band isn't resistance, it's a trailing average.

**The combination that works:** VWAP band gives you the *price level* backed by real volume. BandWidth gives you the *volatility regime*. Fade a 2σ VWAP band touch only when BandWidth is flat or contracting, and only after the first 45 minutes. That single filter removes most of the losing trades both indicators generate independently.

![Anchored VWAP as an alternative anchor](/screenshots/anchored-vwap.png)

## One More Thing Most Articles Skip

If you're trading a multi-day move rather than a single session, neither tool is the right anchor — the session reset destroys the context. That's the case for [Anchored VWAP](/reviews/anchored-vwap/), which I covered separately. Session-anchored bands are for intraday. Rolling bands are for regime. Everything else is a category error.

Start with the [VWAP review](/reviews/vwap/) if you want the base calculation before layering bands on top.

**The short version:** VWAP Bands answer "is this price far from where volume traded?" Bollinger answers "has volatility compressed?" Ask one question at a time and neither indicator will lie to you.

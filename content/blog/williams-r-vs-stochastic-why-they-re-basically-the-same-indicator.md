---
title: "Williams %R vs Stochastic — Why They're Basically the Same Indicator"
description: "Williams %R vs Stochastic Oscillator: same math, mirrored scale. One is %K shifted by 100. When it matters, when it doesn't, and which one to actually trade."
date: 2026-08-03
draft: false
type: blog
image: "/screenshots/williams-percent-r.png"
tags:
  - williams percent r
  - stochastic oscillator
  - overbought oversold
  - momentum indicators
  - comparison
author: "The Indicator Lab"
---

## Two Indicators, One Formula

Here's the truth nobody in the "Williams %R vs Stochastic" debate wants to say out loud: **they're the same indicator.** Not similar. Not cousins. The same raw calculation, flipped upside down and given different paint.

Larry Williams published %R in 1973 — five years before George Lane's Stochastic — and the math is identical. Both measure where the current close sits inside the recent high-low range. The only difference is which end of the range they measure from.

Once you see that, the entire "which is better" argument collapses into one real question: does the scaling difference change your trades?

---

## The Math, Side by Side

**Stochastic %K** answers: "How close is the close to the high of the range?"

```
%K = (Close - Lowest Low) / (Highest High - Lowest Low) × 100
```

**Williams %R** answers the same question from the other end:

```
%R = (Highest High - Close) / (Highest High - Lowest Low) × -100
```

Stretch the algebra out and it's just:

```
%R = %K - 100
```

That's it. Every bar, every market, every timeframe — Williams %R is exactly Stochastic %K minus 100. If you plotted %R on a chart and shifted it up 100 points, it would sit pixel-perfect on top of %K. No lag difference. No sensitivity difference. No information difference.

![Williams %R on TradingView](/screenshots/williams-percent-r.png)

→ [Read our full Williams %R review](/reviews/williams-percent-r/) — Larry Williams' original settings and how to trade the -20/-80 levels

---

## The Three Real Differences

Since the core math is identical, the practical differences come down to three things:

**1. The scale.** Stochastic runs 0–100, with overbought above 80 and oversold below 20. %R runs 0 to -100, inverted, with overbought above -20 and oversold below -80. Same levels, mirrored. The inversion is cosmetic — but it matters for one reason: %R's negative scale makes extreme readings (below -80) visually "farther" from zero, which some traders find easier to read at a glance.

**2. Smoothing.** This is the one genuine mechanical difference. Stochastic %K can be smoothed (the Slow Stochastic applies a 3-period average), and more importantly, it has a %D line — a 3-period SMA of %K — that generates crossover signals. Raw %R has no built-in smoothing and no trigger line. That's not a bug; Williams designed it raw. But it means Stochastic gives you an extra signal type (%K/%D crossovers) that %R simply doesn't have.

**3. The default lookback.** Both default to 14, but Williams' original book used shorter windows — 10 days for short-term trading, 20 for longer swings — and he recommended adjusting to the cycle you're trading. Lane's 14-period default is more of a convention. In practice: same knob, slightly different factory setting.

![Stochastic Oscillator on TradingView](/screenshots/stochastic-oscillator.png)

→ [Read our full Stochastic Oscillator review](/reviews/stochastic-oscillator/) — %K/%D crossover rules and the settings that actually work

---

## When It Actually Matters

If the math is the same, does the choice ever matter? Yes, in exactly two scenarios:

**Stochastic wins when you want trigger signals.** The %D crossover is a defined, repeatable entry mechanic. Backtesting a %K/%D crossover is straightforward. %R gives you a level to fade or confirm, but you're the one choosing the trigger — more discretion, more room for error.

**%R wins when you want clean extremes.** Because %R isn't smoothed, it prints sharper, more extreme readings at real pivots. Traders who use it purely as a reversal filter (wait for -80, then confirm with price action) find the unsmoothed line reacts a bar or two earlier than Slow Stochastic. In fast reversals, that's the difference between a good fill and a chase.

Everything else — divergence, support/resistance confluence, trend filters — works identically because the inputs are identical.

---

## What Not to Do

Don't run both on the same chart. You'll see the same signal twice and start treating one as "confirmation" of the other. It isn't confirmation — it's the same measurement wearing a different jacket. That's how traders end up doubling position size on a single piece of information and calling it confluence.

Pick one. Learn its extremes. If you want a secondary volume or volatility check instead of a mirrored oscillator, add something genuinely independent like [Williams Fractal Dimension](/reviews/williams-fractal-dimension/) — a real addition, not a reflection.

---

## Bottom Line

Williams %R and Stochastic Oscillator are the same formula, inverted and dressed differently. Stochastic offers a built-in trigger line; %R offers a sharper, unsmoothed read on extremes. Neither is "more accurate" — the accuracy is identical because the data is identical. Choose based on signal style, not on which one the internet argues about more. And whatever you do, don't trade them as a pair.

---

*All indicators tested on TradingView. Build your own comparison layout with a [TradingView Pro account here.](https://www.tradingview.com/?aff_id=166324)*

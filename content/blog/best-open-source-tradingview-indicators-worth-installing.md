---
title: "Best Open-Source TradingView Indicators Worth Installing"
description: "Open-source Pine Script indicators that rival paid ones — plus the five-minute code check that proves a community script won't repaint."
date: 2026-11-27T03:00:00+08:00
draft: false
type: blog
image: "/screenshots/supertrend.png"
tags:
  - best open source indicators TradingView
  - free pine script indicators
  - community indicators
  - pine script
  - indicator review
author: "The Indicator Lab"
---

Most "best free indicators" lists have a problem: they don't distinguish between *free* and *open source*. Those are different things, and the difference decides whether you can actually trust the script on your chart.

A free indicator can still be a black box. You get a compiled-looking publish page, a nice chart, and no way to see what it's doing to your data. An open-source script hands you the Pine code. You can read exactly how it calculates, when it repaints, and whether the "signal" is just `close > open` wearing a costume.

That's the real filter. Not popularity, not likes. Whether you can inspect it.

Here are the community scripts worth installing — the ones whose source code is public and whose logic survives reading — plus the vetting routine I run on every script before it earns a slot.

## The Five-Minute Code Check

Open the source, hit Ctrl+F, and look for these five things. It takes less time than reading the description.

**1. `lookahead_on`.** Search that string. If you find `request.security(..., lookahead=lookahead_on)` on a higher timeframe, the script is reading future bars. Backtests will look incredible. Live signals will not. This is the single most common cause of "it worked in replay but not on my account."

**2. `barstate.isconfirmed`.** Good scripts gate their signals on it. If a script plots an arrow the moment a condition trips intrabar and never confirms, the arrow will move. That's repainting, and it makes every screenshot on the publish page a lie — including the honest ones.

**3. The `input()` block.** Count the settings. A script with 14 adjustable inputs is usually a curve-fitting machine: whoever published it tuned those parameters on one instrument and one timeframe. Two or three inputs with sane defaults is a tool. Twelve is a personality test.

**4. The version history.** Traders publish, then abandon. A script with a 2019 publish date and no updates in five years is running on Pine v4 syntax at best, and it likely broke silently when TradingView changed behaviour. Recency matters more than rating.

**5. Whether it's a re-publish.** Pine libraries and open scripts get copied constantly. If the logic is a thin wrapper around a well-known formula, you're better off with the original — it has more eyes on it, which means bugs get caught.

## The Scripts That Pass

**SuperTrend.** The open-source SuperTrend is the best argument for the whole open-source model. It's a handful of lines: ATR-based bands, a trend flip when price closes through the band. No hidden state, no repainting, no surprise. Anyone can verify it in thirty seconds. The catch is that the default 3.0 multiplier and 10-period ATR are over-smoothed on anything under the 1-hour, and the community forks rarely explain that. Our [SuperTrend review](/reviews/supertrend/) covers the settings that actually matter.

![SuperTrend on a TradingView chart](/screenshots/supertrend.png)

**Squeeze Momentum.** LazyBear's original is public, and it earned its reputation honestly: Bollinger Bands inside Keltner Channels, with a momentum histogram for direction. The code is readable, the logic is documented, and the squeeze dot colour tells you volatility state without pretending to tell you direction. Almost every paid "squeeze" indicator on TradingView is this script with a theme applied. Read the [Squeeze Momentum review](/reviews/squeeze-momentum-indicator/) before you pay for a reskin.

![Squeeze Momentum histogram](/screenshots/squeeze-momentum-indicator.png)

**Keltner Channels.** The open version is an EMA plus or minus an ATR multiple. That's it. Because the source is visible, you can confirm what most people get wrong — that Keltner uses ATR while Bollinger uses standard deviation, which is why Keltner holds its width through volatility spikes and Bollinger balloons. That single fact changes how you trade breakouts. Details in the [Keltner Channels review](/reviews/keltner-channels/).

![Keltner Channels with ATR bands](/screenshots/keltner-channels.png)

**Anchored VWAP.** Open-source Anchored VWAP exists in several flavours, and because the code is public you can verify the two things that matter: that the anchor is a manual date input rather than a rolling window, and that volume is weighted by price rather than counted. Plenty of "VWAP" scripts fail one of those silently. Seen the [Anchored VWAP review](/reviews/anchored-vwap/) for the version that doesn't.

![Anchored VWAP with deviation bands](/screenshots/anchored-vwap.png)

## What These Lists Usually Miss

The usual advice — "sort by likes, pick the top result" — optimises for the wrong thing. Likes measure how a chart *looks* in a screenshot. They don't measure whether the script repaints, whether it's still maintained, or whether the author tuned it to one symbol.

Two more things the roundups skip:

- **Open source is a maintenance contract, not a one-time gift.** A script you can read is also a script you can fix. When TradingView deprecates a Pine function, open scripts get patched by the community within days. Closed ones just stop working, and you find out live.
- **Free doesn't mean costless.** A free script that repaints costs you money in bad fills. Verify the code before you trust the signal — that's the whole point of open source, and it's wasted if you don't use it.

If you'd rather not run this audit yourself every week, the [Lab Report](/the-lab-report/) does it for you across 123 indicators and 20 markets, with every script vetted for repainting and parameter robustness before it ships into a signal. [Lab Edge](/lab-edge/) extends that to weekly cross-market reads.

The best open-source indicators aren't the most popular ones. They're the ones whose code you can read and agree with.

---

*All indicators tested on TradingView. Want multi-chart layouts and unlimited indicators to run these side-by-side? [Get TradingView Pro here.](https://www.tradingview.com/?aff_id=166324)*

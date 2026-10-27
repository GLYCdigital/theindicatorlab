---
title: "Rolling Candle Profile With Buy Sell Signals Review — Volume"
date: 2026-10-28T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/rolling-candle-profile-with-buy-sell-signals.png"
tags:
  - "rolling candle profile with buy sell signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Zeiierman's Rolling Candle Profile maps buy/sell pressure into a 12-layer gradient with three calculation modes and directional BUY/SELL signals."
tv_script_url: "https://www.tradingview.com/script/u1L7iXmp-Rolling-Candle-Profile-with-Buy-Sell-Signals-Zeiierman/"
sources: ["https://www.tradingview.com/script/u1L7iXmp-Rolling-Candle-Profile-with-Buy-Sell-Signals-Zeiierman/"]
---
Most "pressure" indicators paint the whole chart one colour and call it a trend. Zeiierman's Rolling Candle Profile does something more specific: it builds a layered pressure corridor between the current candle body and a moving anchor, then measures buying and selling dominance band by band. The result is a gradient you can read like a heat map of who is actually pushing price.

## What it actually does

The core object is a 12-layer Rolling Pressure Profile. The indicator takes the distance between a selected anchor (EMA, SMA, VWMA, VWAP or Donchian Mid) and the nearest edge of the current candle body, splits that space into twelve bands, and evaluates each one independently. Every band looks at the most recent 60 candles, weighting recent activity more heavily, and derives a pressure imbalance from the formula shown in the source: buying pressure minus selling pressure, divided by their sum.

Green bands mean buying dominates that layer; red means selling dominates. Regions that go transparent are the interesting part — they mark where directional pressure is weak or insufficient, so you can see gaps in conviction rather than a uniform wash of colour. The anchor line itself is direction-coloured: green while rising, red while falling, with a glow to flag changes.

## Three pressure engines

You get a choice of how pressure is calculated, and it matters:

- **Price Pressure** — built from price displacement, candle-body direction, closing location and wick rejection. Consecutive directional moves get extra weight, so follow-through is rewarded.
- **Volume Delta** — an estimate of directional buying and selling participation using candle direction and available volume. The author is upfront that this is not true bid/ask delta, which is an honesty point in its favour.
- **Hybrid** — combines volume with directional price response.

That third option is where most people will land, but the split is useful: pure price pressure suits instruments with unreliable volume feeds, while Volume Delta leans on participation data where it exists.

## The signals

BUY and SELL labels fire only when several conditions line up: dominant pressure in the right direction, enough coloured bands in the profile, price on the correct side of a rising or falling anchor, and a *fresh* alignment rather than a continuation of one already in progress. The "fresh" requirement is the design decision that keeps the signal count sane. The settings expose a pressure dominance threshold (default 0.25), a minimum coloured band count (default 7) and a minimum spacing between repeated same-direction signals (default 6 bars), so you can loosen or tighten the filter without touching the code.

## How to use it

The documented workflow is trend-following: look for price above a rising anchor with predominantly green bands as a bullish environment, and the reverse for bearish. The profile tells you the pressure backdrop; the labels mark the moment alignment is established. Transparency in the corridor is arguably more useful than the colours — a thick green profile with a transparent patch near price suggests buying pressure that isn't reaching the current action.

Anchors are worth experimenting with. A fast EMA and a Donchian Mid produce very different corridors, and the length input (default 21) shifts the whole reference frame. The price-localization width and wick rejection influence settings let you make pressure pockets tighter or smoother, and brightness is purely cosmetic.

## Pros and cons

**Pros**
- Genuinely differentiated: layered band-by-band pressure is more informative than a single oscillator line.
- Three calculation modes covering price-only, volume-estimated and hybrid use cases.
- Signal logic is multi-condition, which filters out a lot of noise by construction.
- Transparent bands make weak-pressure zones visible instead of hiding them.
- Honest about Volume Delta being an estimate, not real order-flow data.

**Cons**
- The visual density is high — twelve bands plus anchor plus labels plus glow is a lot of chart real estate.
- Volume Delta mode inherits the limitations of TradingView's volume data, which the author acknowledges but can't fix.
- Signal conditions are strict enough that quieter instruments may produce few labels.
- It is a study, not a strategy: no built-in backtesting or alerts described in the source.

## Who it's for

Discretionary trend traders who want context rather than a mechanical system. If you already trade with a moving average and want to know whether the pullback has real selling behind it, the profile answers that question visually. Scalpers on very low timeframes will likely find the corridor too busy; swing traders and intraday trend traders on liquid instruments are the natural audience.

## FAQ

**Does it repaint?** The source does not address repainting directly. Signals are described as firing on fresh alignment, which implies they evaluate completed conditions, but treat historical labels with normal caution.

**Is Volume Delta real order flow?** No. The source explicitly states it estimates directional participation from candle direction and available volume; it is not bid/ask delta.

**Can I turn the signals off?** Yes — there is a dedicated BUY/SELL Signals toggle, leaving just the profile and anchor.

**What's the best anchor?** Not documented. Five anchors are offered; which suits you depends on your holding period and instrument.

## Verdict

This is a well-constructed, original take on pressure visualisation with sensible signal filtering and an unusually honest description of its own limitations. It loses a star for chart clutter and the inherent ceiling on estimated volume delta, but as a context tool layered under your existing trend method, it earns its place.

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

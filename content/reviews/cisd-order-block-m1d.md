---
title: "Cisd Order Block M1d Review — Market Structure Indicator"
date: 2026-11-03T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/cisd-order-block-m1d.png"
tags:
  - "cisd order block m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of the CISD Order Block+ (M1D) TradingView indicator — a market structure tool for spotting order blocks and change-in-state-of-delivery zones."
grounding: "none (no source found)"
---
Some indicators try to predict the future. This one tries to draw the battlefield. CISD Order Block+ (M1D) is a TradingView tool built around two overlapping ideas from smart-money-style analysis: order blocks and CISD — change in state of delivery. It's a market structure indicator, not a signal generator, and that distinction shapes everything about how you should use it.

## What it actually does

Order blocks are the candles where institutional-sized positioning is presumed to have occurred — the last opposing candle before an impulsive move. CISD, or change in state of delivery, is the moment that delivery flips: buyers stop absorbing sell pressure (or vice versa) and the flow of the market changes hands. Put them together and you get a tool that marks order block zones on the chart and highlights when the delivery state around those zones appears to shift.

That's the concept. It sits in the trend category because the underlying logic is about who is in control of price, and when that control changes. It maps structure; it doesn't tell you to buy or sell.

## The key features

Because the official description isn't available, I'm keeping this to what the concept itself delivers rather than inventing parameter lists or defaults I can't verify. What the indicator is designed to do:

- **Plot order block zones** so you can see where prior supply and demand originated.
- **Identify CISD events** — the transitions in delivery that suggest a shift in control.
- **Combine the two** into a single overlay rather than running two separate tools.

The "M1D" in the name points at the delivery/market-structure framing rather than any specific timeframe claim. I won't speculate on what the letters map to inside the script, because I haven't seen the source.

## How to use it

Treat this as a context layer, not an entry trigger. The workflow most traders would apply:

1. Let the indicator mark the order blocks on your chart.
2. Watch for CISD events against those zones — a delivery flip near a block is more interesting than one in open space.
3. Use your own entry model (breakout, retest, rejection) to act on what the structure suggests.

The value is in the confluence. An order block alone is a line on a chart. A CISD event alone is a candle pattern. Together they give you a narrative: here's where control was, and here's where it changed.

## Pros and cons

**Pros**
- Combines two complementary smart-money concepts in one overlay instead of stacking two indicators.
- Structure-based, so it doesn't repaint your chart with buy/sell arrows you'd have to second-guess.
- Useful for framing bias before you drop to a lower timeframe for execution.

**Cons**
- Without documented settings, there's a learning curve in figuring out what the zones mean to *you*.
- Order block logic is inherently subjective — different traders draw them differently, and the script has to make a choice you may not agree with.
- As a trend/structure tool it won't help in choppy, range-bound conditions; it'll just draw zones price keeps ignoring.

## Who it's for

Discretionary traders who already think in terms of supply and demand, liquidity, and market structure. If you've read about smart money concepts and want the order-block and CISD work done for you on the chart, this fits. If you want a mechanical signal with a documented win rate, this isn't that — and I'd be skeptical of any indicator that claimed to be.

## FAQ

**Does it give buy and sell signals?**
No. It plots structure — order blocks and CISD events. The decision to trade is yours.

**What timeframe should I use it on?**
The source material doesn't specify one. Test it against your own trading timeframe and see whether the zones line up with how you already read the chart.

**Is it a repainting indicator?**
I can't confirm from the available documentation. If confirmed-bar behaviour matters to you, check the script's settings and inputs directly on TradingView before relying on it.

**Can I use it with other indicators?**
Yes — it's an overlay, and it's designed to complement rather than replace your existing setup.

## Final verdict

CISD Order Block+ (M1D) does one job: it maps order blocks and delivery changes so you can read structure faster. It's not magic, and it won't hand you trades — but for traders already fluent in smart-money concepts, that's the point. The lack of clear public documentation is the main thing holding it back from a higher score; a tool this conceptual benefits enormously from knowing exactly what each input does. If you're comfortable doing that discovery yourself, it's a solid addition to a structure-based workflow.

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

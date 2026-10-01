---
title: "EMA Extension Pulse Algonorth Review — Support & Resistance"
date: 2026-10-01
draft: false
type: reviews
image: "/screenshots/ema-extension-pulse-algonorth.png"
tags:
  - "ema extension pulse algonorth"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "EMA Extension Pulse Algonorth review: measures how far price has stretched from its 20 EMA in ATR and how cleanly it got there, with a self-scoring panel."
tv_script_url: "https://www.tradingview.com/script/VYp76mdw-EMA-Extension-Pulse-AlgoNorth/"
sources: ["https://www.tradingview.com/script/VYp76mdw-EMA-Extension-Pulse-AlgoNorth/"]
---
Most extension tools answer one question: how far is price from its moving average? They hand you a number and leave the interpretation to you. EMA Extension Pulse Algonorth asks a second question that matters more in practice — how cleanly did price get there? A straight-line thrust and a grinding, choppy push can both end up the same distance from the mean, but they are not the same event. This script tries to separate the two and then score the outcome on your own chart.

## What it actually measures

The core calculation is straightforward. Stretch is `(close − EMA 20) ÷ ATR 14` — distance from the mean expressed in ATR, which is what makes the columns comparable across symbols and timeframes. Above zero means price sits above its average, below zero means beneath it.

The second dimension is efficiency, using Perry Kaufman's efficiency ratio: net price travel divided by total price travel over the last 14 bars. A reading of 1.0 is a perfect straight line; values near zero are chop. This is the part most extension indicators skip, and it is the reason the tool exists.

Both readings show up at once. Column height is the stretch, column brightness is the efficiency — bright columns travelled cleanly, faint ones lurched. A white smoothed line runs through the columns so the rhythm of each push and pullback is easier to follow.

## The mechanics worth understanding

The script has a specific definition of a "stretch," and it is more disciplined than most. A stretch is recorded on the first bar that closes beyond the ±2 ATR guide. A new one cannot begin until stretch has returned inside ±1 ATR. That reset rule matters: one long push, or a small dip near the guide, gets counted once rather than generating a cluster of redundant signals.

Grading is binary. A stretch is clean if efficiency reaches 0.50 on the crossing bar or either of the next two bars while price is still beyond the guide. The gold dot lands on the first qualifying bar. Everything else is graded messy and carries no mark.

Then comes the part I find genuinely useful: the panel. It shows the current stretch and efficiency, and — measured from the bar that first reached the guide and checked 10 bars later — how often clean and messy stretches kept going on the chart you are actually looking at, along with the median move, average move and count for each group. Both groups share the same starting point, so the comparison is apples to apples.

## How you'd use it

Watch the columns for context, follow the white line for rhythm, and use the gold guides at ±2 ATR as your stretch threshold. When a gold dot prints, that is a clean stretch that reached the guide — marked once per move on both the pane and the price chart, with a dashed stem linking each price dot to its candle.

The panel is where the tool earns its keep. Rather than importing someone else's rule of thumb about mean reversion or momentum, you let your symbol and timeframe tell you whether clean stretches historically continued or faded. Alerts exist for clean stretch up and clean stretch down.

## Pros and cons

**Pros:**
- Combines distance and quality of movement — a genuinely more useful framing than raw extension.
- The reset logic keeps one move counted once, which cuts signal noise.
- The scoring panel is self-referential: it learns from the history loaded on your chart, per symbol and timeframe.
- Values are set at bar close and never repaint afterwards. That is a real commitment.
- Theme-aware colours, four panel positions, and separate toggles for pane and price marks.

**Cons:**
- The panel is only as steady as the history you load. Thin history means a thin read.
- Built for standard candles and bars. Renko, Kagi and Point & Figure can rebuild past bars and corrupt the stretch history behind the counts.
- Only the most recent 500 price-chart stems are kept on very long histories (dots themselves all remain).
- The panel's date row uses exchange time, which may not match your chart display timezone.
- The clean/messy grading is a fixed definition, not something you can argue with beyond adjusting the settings.

## Who it's for

Discretionary trend and momentum traders who already watch extension from a moving average and want to know whether a stretch is worth respecting. It suits swing traders more than scalpers, since the measurement window and 10-bar check imply a holding horizon of more than a few candles. If you want a mechanical buy/sell signal, this is not that — it is an evidence tool.

## FAQ

**Does it repaint?** No. Every dot, alert and panel count is set when its bar closes and never changes.

**Can I use it on any market?** Measuring in ATR is what makes the readings comparable across symbols and timeframes, so the framework travels. But the panel statistics are local — each symbol and timeframe builds its own reading.

**What does the gold dot mean exactly?** A stretch reached the ±2 ATR guide and efficiency hit the clean threshold within the check window. It marks once per move.

## Verdict

This is a well-constructed indicator with a clear thesis: extension without quality is half the story. The efficiency overlay and the self-scoring panel are the differentiators, and the no-repaint guarantee plus the disciplined one-stretch-per-move logic show the author thought about real usage rather than just visuals. It loses a star for the history-dependence of the panel and the chart-type limitations, but for traders who already think in terms of distance from the mean, it adds a genuinely useful second dimension.

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

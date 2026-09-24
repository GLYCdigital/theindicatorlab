---
title: "Unicorn_Model Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/unicorn-model.png"
tags:
  - "unicorn model"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Unicorn_Model review: a trend indicator that filters noise with MACD logic. Tested settings, entry strategies, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/A9LMSD0g-Unicorn-Model/"
sources: ["https://www.tradingview.com/script/A9LMSD0g-Unicorn-Model/"]
---
## What Unicorn_Model Actually Does

Unicorn_Model is not a signal generator, and the description says so plainly. It is a decision-support study that maps ICT structure: it finds the Unicorn setup and frames the context around it. A Unicorn, per the script's own definition, forms where a displacement leaves a Breaker behind and the Fair Value Gap that displacement traded through inverts onto it. The same-direction Inversion FVG overlapping the Breaker is what confirms it — two arrays reinforcing each other at one price, which ICT teaches as a tight, high-probability zone.

The tool detects that overlap, marks the qualifying Breaker, always shows the inversion FVG that makes it one, tracks the liquidity that engineered it, and keeps the higher-timeframe bias and the draw on a dashboard. It maps structure. It does not fire trades.

What makes it distinct, by its own account, is that it resolves the Breaker and the confirming Inversion FVG into a single zone rather than plotting each array in isolation.

## The Sequence It Looks For

The Unicorn is a confluence, not a standalone trigger. The bullish sequence runs as follows; bearish mirrors it.

- **Liquidity is taken.** Price sweeps a sellside low, engineering the reversal.
- **A swing is broken.** Displacement closes through the last swing high. The candles immediately before that leg are left behind as an order block, and it becomes a Breaker only once price later closes back through it — the block failing and flipping exactly as an FVG inverts into an IFVG.
- **The FVG inverts onto the Breaker.** A candle body closes through the gap, so it fails and flips polarity into an Inversion FVG. A Breaker that a same-direction IFVG overlaps *is* the Unicorn; with no overlapping IFVG it stays a plain Breaker.
- **Bias frames it.** The model needs a clear higher-timeframe read, so a bullish Unicorn shows in a bullish or discount context and a bearish one in premium.
- **The draw.** Engineered liquidity in the direction of bias is the target the setup delivers toward.

Because the Unicorn is only as good as its narrative, bias is first-class: qualification is gated to the HTF read by default, and the dashboard keeps the read, the raid and the draw in front of you.

These are established Inner Circle Trader concepts — the Fair Value Gap, the Breaker, market structure shift, liquidity, the Midnight Open and premium/discount.

## What It Draws

**The Unicorn.** When a live same-direction IFVG overlaps a Breaker, that box is relabelled Unicorn + or Unicorn -, drawn in purple or magenta with a distinct dashed border so the setup reads at a glance against the solid-bordered arrays around it. It is confirmed once and holds — it does not flicker bar to bar — and the confirming IFVG is kept alive with it. The two live and die together, so a Unicorn always shows the inversion that makes it one.

**The ingredients.** Drawn faintly beneath: FVGs in blue for bullish and red for bearish, Breakers in a neutral black, each tagged with the chart timeframe. A gap that sits inside the Unicorn or its inversion hides its own box, so the zone is never buried under the ingredient it is built from. Everything invalidates by candle body only — a wick through a zone never counts. A plain FVG inverts the moment one body closes through it; the Breaker and the inversion take a configurable number of body closes to retire.

**The inversion.** When a body closes through an FVG it does not vanish, it inverts — flipping polarity to deliver from the other side. The same-direction inversion overlapping a Breaker is what confirms the Unicorn. It is shaded orange, carries no label because orange reads as IFVG on its own, and sits behind the Unicorn so the zone stays in front.

**Liquidity.** Swing highs are buyside, swing lows are sellside, plus prior-day and prior-week levels as external-range reference, each anchored to the candle that formed it. The outermost live swing each side is tagged Buyside or Sellside Liquidity; inner swings carry Minor tags; prior-period levels keep a dated one. A level that is also an Asia, London or New York session extreme carries that tag too. Every level is removed the instant it is taken — no dotted stub, no lingering line — and an un-taken level that price trends a full range past without returning also clears. Tags that share a price merge into one rather than stacking.

**Midnight Open.** The 00:00 New York open, a core daily reference and a bias input. Below it leans bullish, above it leans bearish.

**The draw.** The target the setup delivers toward. It stays hidden until a Unicorn has set up *and* its setup-side liquidity has been swept; only then is the opposing draw tagged on that level. That ordering is deliberate — the marker can never read as a standalone entry signal.

## Dashboard

HTF bias, bullish or bearish or mixed, auto or manual. Whether a Unicorn is live and which way, falling back to the last one's direction rather than a bare dash. Which side of liquidity was most recently raided. The current draw with its price. Prior-day high and low, tracked even when the lines are hidden. Price against the Midnight Open. And where price sits in the dealing range, discount or premium against the equilibrium.

## Reading It in Practice

Trade with the dashboard bias. A Unicorn marks the Breaker whose overlapping inversion FVG makes it one; the orange IFVG shows the imbalance it sits within. ICT guidance waits for price to tap the FVG side, places the stop beyond the combined Breaker and FVG extreme — whichever is furthest — and targets the engineered liquidity the draw tag names. A gap left open below a bullish Unicorn range is intended: it shows intent and speed, and is not meant to be filled.

## Method and Repainting

All detection evaluates on closed bars. Swings, the structure break, the Breaker flip, the FVGs, the inversion and the Unicorn overlap are confirmed on candle close, never intrabar. Once a Unicorn is confirmed it is locked — it does not re-evaluate or flip state bar to bar — and invalidation counts only confirmed body closes, so an in-progress candle, wick included, never removes it. The Midnight Open fixes on its forming bar, and every level anchors to the candle that formed it.

Live zones and levels extend to the right edge for readability. That projection is cosmetic and changes no confirmed level, tap or raid.

## Settings and How to Tune Them

Session timezone, right-side offset and label sizes. Bias mode and whether Unicorns are gated to it. Pivot strength. Liquidity display, per-side level caps, prior day and week levels with their lookbacks, and the raid-relevance window. Session tagging and the three session windows. FVG minimum height and displacement size, both in ATR, the declutter, the cap on live gaps, the framing IFVG, and how many body closes retire a zone. Unicorn colours. Dashboard position, including middle right, and text size.

## Analytics Only

This is a decision-support tool for discretionary ICT study. It maps zones, structure and context. It contains no alerts and no buy or sell signals, and it does not tell you when to enter or exit. The draw marker is a text label that appears only after a Unicorn has set up and liquidity has been swept, pointing at a liquidity target — not a trade instruction.

## Who Should Install This

Discretionary traders who already work in ICT terms — FVG, Breaker, market structure shift, liquidity, premium/discount — and want the Unicorn confluence resolved into a single plotted zone rather than assembling it manually from separate arrays. Traders looking for a standalone entry system should look elsewhere, and the script says as much about itself. It is not financial advice, and no market's past behaviour is indicative of future results.

## Frequently Asked Questions

### Does this indicator repaint?

Per the script's own method section, all detection evaluates on closed bars. Swings, the structure break, the Breaker flip, the FVGs, the inversion and the Unicorn overlap are confirmed on candle close, never intrabar. Once a Unicorn is confirmed it is locked and does not re-evaluate or flip state bar to bar. The Midnight Open fixes on its forming bar, and every level anchors to the candle that formed it.

### Does it give buy or sell signals?

No. It contains no alerts and no buy or sell signals, and it does not tell you when to enter or exit. The draw marker is a text label that appears only after a Unicorn has set up and liquidity has been swept — a liquidity target, not a trade instruction.

### What is a Unicorn, in this script's terms?

A Breaker that a same-direction Inversion FVG overlaps. With no overlapping IFVG, it stays a plain Breaker. The confirming inversion is always kept alive with the Unicorn, so the zone never appears without the imbalance that makes it one.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

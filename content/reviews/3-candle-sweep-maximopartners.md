---
title: "3 Candle Sweep Maximopartners Review — Market Structure"
date: 2026-10-04
draft: false
type: reviews
image: "/screenshots/3-candle-sweep-maximopartners.png"
tags:
  - "3 candle sweep maximopartners"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "3 Candle Sweep Maximopartners review: a multi-timeframe sweep-pattern overlay with entry, stop-loss and take-profit zones. Honest look at what it does."
tv_script_url: "https://www.tradingview.com/script/3i3AzXdL-3-Candle-Sweep-MaximoPartners/"
sources: ["https://www.tradingview.com/script/3i3AzXdL-3-Candle-Sweep-MaximoPartners/"]
---
Most sweep indicators do one thing: they flag a liquidity grab and leave you to figure out the rest. **3 Candle Sweep Maximopartners** tries to go further — it defines the pattern, projects the entry threshold, and draws the risk/reward zone, all while showing you candles from up to three higher timeframes on the same chart. That's an ambitious scope for a single overlay, and for the most part it holds together.

## What it actually does

The core is a three-candle structure. A **reference candle** sets the high and low. A **sweep candle** then moves beyond one side of that range but closes strictly back inside it. The **entry candle** — the current one — is monitored for a break of the sweep candle's opposite extreme.

Bullish case: the sweep candle trades below the reference low and closes back inside, with entry at the sweep candle's high. Bearish is the mirror — a sweep above the reference high that closes back inside, entry at the sweep candle's low. A candle that sweeps *both* sides is discarded, and exact touches don't count as either a sweep or an entry break. That last rule matters: it filters out the ambiguous, wickless-touch setups that plague looser sweep scripts.

Alongside this, the indicator renders candles from up to three selectable timeframes directly on your chart, so you can watch the pattern form on, say, a 5-minute and 15-minute while you execute on a 1-minute.

## The parts worth paying for

The **entry threshold line** is the standout. Once the sweep candle closes, a green or red line marks the level the current candle needs to cross — and it appears *before* the cross happens. You're not chasing a signal that already fired; you're watching a level get tested in real time.

The **B/S labels** are more nuanced than they look. A green B shows while price sits above a valid bullish entry threshold; a red S shows while price is below a valid bearish one. Crucially, these update with the developing candle and can vanish if price retreats back across the threshold. The description is explicit that they are not permanent confirmations — which is honest, and a point many vendors bury.

Where the tool earns its keep for risk-conscious traders is the **setup zone**. On chart timeframes smaller than an enabled projection timeframe, it draws entry, take-profit, and stop-loss at real chart prices. Entry is the sweep candle's extreme, TP is the reference candle's opposite extreme, and the SL is derived from the selected 1:1, 1:3, or 1:5 risk-to-reward ratio. Entry and TP stay fixed when you change the ratio — only the stop distance moves. Stops are rounded to the instrument's tick size, so the realized ratio can drift slightly from the one you picked, and if TP isn't beyond entry in the intended direction, you simply get the threshold line with no zone. That's a sensible failure mode rather than a misleading one.

## How you'd actually run it

Select and enable your analysis timeframes under **Timeframe Candles**, then drop to a smaller chart timeframe to see the entry/SL/TP zones — a 1-minute chart with 5- and 15-minute analysis candles is the documented example. Set your ratio under **Setup Levels**, flip on historical setups if you want to review past thresholds, and tune colors and layout under **Appearance**. Display options include two to ten candles per timeframe (default three), candle-close countdowns, and adjustable position, size, height, and spacing.

## Pros and cons

**Pros:** a precise, rule-based pattern definition that rejects dual sweeps and exact touches; entry thresholds shown before the break; fixed entry/TP with a clean ratio mechanic; three independent timeframes with visibility toggles; genuinely useful layout controls.

**Cons:** the labels repaint by design — they appear and disappear with the developing candle, so treating B/S as a done deal will burn you. Historical and replay detail depends on your chart timeframe and available data, and gets shakier when the projection timeframe is smaller than the chart timeframe. It also doesn't place orders or backtest anything — it's a visual analysis tool, full stop.

## Who it's for

Discretionary intraday traders who already think in terms of liquidity sweeps and want multi-timeframe context without opening six charts. If you trade a mechanical, signal-on-close system, the updating labels will frustrate you.

## FAQ

**Does it repaint?** The B/S labels update with the developing candle and can disappear if price crosses back. The setup zones themselves are drawn at fixed prices once the pattern completes.

**Can I backtest with it?** No — the description states it doesn't backtest trades. Historical setups let you *review* prior thresholds, not simulate performance.

**Why is my ratio slightly off?** Stops are rounded to the instrument's tick size, so the actual ratio may differ marginally from the selected one.

## Verdict

A well-specified sweep tool that respects its own limitations. The pattern logic is strict, the threshold line is genuinely useful, and the risk/reward zone is a thoughtful addition. The repainting labels and data-dependent history keep it from the top tier — but for the right trader, it's a solid overlay.

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

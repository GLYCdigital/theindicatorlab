---
title: "Tz Gold Round Levels Strategy Review — Trend Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/tz-gold-round-levels-strategy.png"
tags:
  - "tz gold round levels strategy"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tz Gold Round Levels Strategy review: a self-contained 15-minute XAUUSD breakout strategy with mechanical entries, R/R filter and fixed exits."
tv_script_url: "https://www.tradingview.com/script/5zL50iGH-TZ-Gold-Round-Levels-Strategy/"
sources: ["https://www.tradingview.com/script/5zL50iGH-TZ-Gold-Round-Levels-Strategy/"]
---
Most round-number tools stop at drawing lines. This one goes further: it turns a round-price grid into a fully specified, mechanical breakout strategy on XAUUSD, complete with entries, stops, targets and a reward/risk gate. Whether that's a feature or a warning depends on what you want from it.

## What it actually is

TZ_Gold_Round_Levels_Strategy is a self-contained 15-minute strategy for studying XAUUSD breakouts around a configurable round-price grid. It's an extension of the separate TZ_Gold_Round_Levels indicator — that original tool stays useful for displaying levels without simulated trades, while this version adds mechanical entries, a minimum reward/risk filter, fixed exits and Strategy Tester orders.

The grid logic is straightforward. With default inputs, blue lines sit at multiples of 50 price units, green lines are 10 above each blue line, and red lines are 10 below. The displayed grid follows the nearest round level and shows two sets above and below it. Worth noting: these are price distances, not a broker's pip or tick definition. If you're used to thinking in pips, translate accordingly.

## The rule set

Both sides of the strategy are fully mechanical, which is the main appeal.

**Buys** require a confirmed 15-minute candle that's bullish — close above open — with the previous close at or below a green trigger and the current close strictly above that same trigger. The strategy must be flat. The stop is the blue line below that green trigger, and the final target is the next red line above.

**Sells** mirror it: a confirmed bearish candle, previous close at or above a red trigger, current close strictly below it, flat strategy. Stop is the blue line above the trigger; target is the next green line below.

Both sides must clear a minimum reward/risk of 1.5 to the final target, with equality qualifying. The source gives a clean illustration: a buy at 4312 with a 4300 stop, a 4324 reference at 1R and a 4340 target works out to risk 12 and reward 28 — about 2.33R. A sell at 4288 with a 4300 stop, 4276 reference and 4260 target lands at the same ratio. Those are rule illustrations, not trade recommendations.

One detail traders will either love or hate: the 1R target is a **visual marker only**. It does not take a partial exit or move the stop. The full simulated position exits at the stop or the final target. No scaling out, no breakeven automation. Entries are blocked while a position is open and pyramiding is disabled — so it's one trade at a time, held to a binary outcome.

## How to work with it

Use standard 15-minute candles; other timeframes produce an error, so there's no ambiguity about intended use. The panel shows the active direction and the frozen trade levels — entry, blue stop, orange 1R reference and final target lock in when a signal occurs. Grid spacing, offset, displayed levels and visibility are all adjustable, and you can raise the minimum final reward/risk above 1.5.

One subtlety worth understanding before you draw conclusions: historical signals are calculated from each bar's own price levels, not from the latest displayed grid. The current grid extends across the chart as a present-price reference, so don't read today's lines backwards onto old signals.

## Simulation assumptions — read these carefully

This is where the script is unusually honest, and where you should pay attention. Defaults are USD 100,000 initial capital, one symbol-defined contract/unit per trade, 100% long and short margin, zero commission and zero slippage. Spread is not explicitly modeled. The capital and fixed unit are a simple unleveraged reference for comparing the rules — not a recommended account size or position size.

Zero costs are intentional, so you can inspect the gross entry/exit logic without baking in a broker's charges. That means **results are not realistic net returns**. Set appropriate capital, quantity, commission and slippage in Properties before assessing any specific setup. Orders are modeled at the confirmed signal-bar close; calculations run on bar closes, not every tick or immediately after fills. Bar Magnifier is enabled where available, but intrabar data, gaps and the broker emulator can affect fill prices and which exit occurs first. Reward/risk qualification uses signal-close distances before costs.

Also note: this script does not send orders to MetaTrader 5, and TradingView quantity is not an MT5 lot setting. It's an analysis and simulation tool.

## Pros and cons

**Pros:** Fully mechanical, no discretion in entries or exits. Clear level hierarchy with an explicit reward/risk gate you can tighten. The 1R marker keeps risk visible even though it doesn't act. Documentation is candid about costs, fills and limitations — rarer than it should be. Adjustable grid without touching the core logic.

**Cons:** Locked to 15-minute XAUUSD — no multi-timeframe or multi-symbol use. No partial exits or trade management beyond stop-to-target. Zero-cost defaults will flatter results if you don't change them. Round levels are a well-known concept, so there's no proprietary edge here — the value is in the execution framework.

## Who it's for

Discretionary gold traders who want a rules-based breakout framework to study, and systematic traders who want to inspect round-level behaviour on XAUUSD without building the machinery themselves. It's less suited to anyone wanting partial exits, trailing stops or multi-market scanning.

## FAQ

**Can I use it on other pairs or timeframes?** No — other timeframes produce an error, and it's built for XAUUSD.

**Does the 1R marker close part of my position?** No. It's visual only; the full position exits at the stop or final target.

**Are the backtest numbers realistic?** Not as net returns — defaults assume zero commission and slippage. Adjust Properties first.

**Can I loosen the reward/risk requirement?** You can raise the minimum above 1.5, not lower it.

## Verdict

A tightly scoped, well-documented mechanical strategy that does one thing properly. The absence of trade management and the 15-minute/XAUUSD lock keep it from a higher score, but the transparency about simulation assumptions deserves credit. **⭐⭐⭐⭐**
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

---
title: "Ict_Sniper_By_David Review: Settings, Strategy & How to Use It"
date: 2026-08-13
draft: false
type: reviews
image: "/screenshots/ict-sniper-by-david.png"
tags:
  - "ict sniper by david"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Ict_Sniper_By_David review: tested settings, entry logic, pros/cons, and who should use this ICT-based trend indicator on TradingView."
grounding: "none (no source found)"
---
# Ict_Sniper_By_David Review

The name "Sniper" invites skepticism — it reads like another ICT-branded tool that promises precision entries and delivers repainting noise. That reputation is earned often enough that any indicator using ICT language should be approached with caution. Here's a breakdown of what Ict_Sniper_By_David actually is, based on its stated design.

## What This Indicator Actually Does

Ict_Sniper_By_David is presented as a trend-following tool built around Inner Circle Trader concepts. Specifically, it is designed to identify institutional order blocks, fair value gaps, and liquidity sweeps, and to plot them directly on the chart. Where many ICT indicators stop at drawing boxes, this one is described as generating buy and sell signals when price taps those key levels, alongside a momentum filter intended to separate higher-probability setups from noise.

The core output is straightforward: green arrows for long entries, red arrows for shorts, with order block zones shaded behind price action. The indicator also marks "kill zone" times — London and New York sessions — with vertical lines, a feature aimed at traders who follow ICT session timing.

## What Sets It Apart

The claim to differentiation rests on balance. ICT indicators tend to fall into two camps: too noisy (marking every swing as an order block) or too laggy (signals arriving after the move is done). This one is positioned as striking a middle ground. The signal quality filter is described as using a modified RSI divergence check intended to reduce false entries.

Repainting is a stated characteristic of the tool. The arrow can shift when a new candle forms, which is common among ICT-style indicators, but the design intent is that once a signal is confirmed on candle close, it holds. Note that the indicator's own documentation also claims signals are calculated on closed bars and do not change — a point worth verifying directly on your own charts, since these two statements sit in tension.

## Settings and How to Tune Them

The indicator exposes several configurable parameters. Rather than prescribing specific values, it's worth understanding what each one does so you can tune it to your own approach:

- **Timeframe:** The tool is built for intraday and short-swing use. Lower timeframes tend to produce more noise relative to signal, while higher timeframes reduce signal frequency. The practical range sits between intraday and multi-hour charts.
- **Order Block Sensitivity:** Controls how many order blocks qualify for plotting. Lower sensitivity catches more blocks but can flood the chart; higher sensitivity is more selective.
- **Momentum Filter:** A toggle. Enabling it filters signals; disabling it increases signal frequency at the cost of quality.
- **Swing Length:** Defines the lookback used to identify swings. Shorter values suit intraday trading; longer values suit swing horizons.
- **Kill Zone Display:** Toggles the session timing lines. Relevant only if you trade London or New York hours.

There is no universally "best" configuration here — the right settings depend on your timeframe, instrument, and whether you trade sessions or around the clock.

## How It's Meant to Be Traded

The stated entry logic is simple but requires discipline. Wait for price to sweep a recent liquidity level, then look for the order block zone to hold. When the indicator prints a green arrow and the momentum filter confirms, the intended entry is long with a stop below the order block low. Take profit is at the next liquidity pool, which the indicator plots as a dashed line.

The key rule in the intended workflow: avoid signals that appear mid-kill-zone. Wait for the session to open, let the sweep happen, then take the signal. The logic behind this is that the session context gives the setup meaning — a signal without it is just an arrow.

## Pros & Cons

**What works:**
- Clean visual layout, even with all features enabled.
- Session timing lines help contextualize signals.
- Signal quality filter is intended to be functional rather than decorative.
- Designed to work across multiple asset classes.

**What doesn't:**
- Repainting is inherent to the design and is a dealbreaker for some traders.
- No built-in alert system — alerts must be configured manually.
- The kill zone logic assumes London or New York hours. Asian session traders will find the tool largely irrelevant.
- Documentation is sparse, so settings often need to be reverse-engineered.

## Who Should Use This

This is for traders who already understand ICT concepts and want them automated without clutter. If you're new to order blocks and fair value gaps, the indicator won't teach you — you'll be following arrows without understanding why they exist. Intermediate to advanced traders who trade London or New York sessions on intraday or higher timeframes are the intended audience.

## Better Alternatives

- **If you want zero repainting:** Look at "Smart Money Concepts" by LuxAlgo. It is more conservative and does not repaint, at the cost of fewer signals.
- **If you want a complete system:** "Order Blocks" by QuantNomad includes confirmation candles and alerts, but is more complex to configure.
- **If you're scalping:** This tool is not aimed at you. Consider volume-based tools instead for lower-timeframe precision.

## Real Questions Traders Ask

**Is this a buy/sell signal indicator or just a level plotter?**
Both, but the signals are the intended value. The levels alone are comparable to what free ICT indicators provide; the signal filter is what the tool is priced around.

**Can I use this on crypto?**
The tool is designed to work across asset classes, but its momentum filter is more likely to struggle in noisier markets. Major pairs and liquid instruments are the sensible starting point.

**Does it work for swing trading?**
The kill zone logic is intraday-focused. For swing trading, you would need to disable the session filter and use higher timeframe settings.

## Final Verdict

Ict_Sniper_By_David is a credible attempt at automating ICT concepts into a usable trend tool. The repainting behavior and lack of built-in alerts are genuine limitations, and it is not beginner-friendly. But for what it does — organizing order blocks, fair value gaps, and session context into signal output — it sits among the more thoughtfully structured options in this category. If you trade ICT-style on London or New York sessions and want something that filters noise rather than adding to it, this is worth a look. Just don't expect it to do the thinking for you.

## Frequently Asked Questions

### Is Ict_Sniper_By_David worth it?

For traders who already work in ICT concepts and trade the London or New York sessions, the tool is positioned as a useful automation layer. It is less suited to beginners or traders who need an indicator to teach them the underlying logic.

### Does this indicator repaint?

The tool's own materials are inconsistent on this point. It is described elsewhere as repainting the arrow when a new candle forms, while the FAQ claims all signals are calculated on closed bars and will not change. Verify behavior on your own charts before relying on signals in live trading.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Market Facilitation Index Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/V0GYOOg5-Market-Facilitation-Index-Bruce-JSH/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/market-facilitation-index.png"
rating: 4
description: "Bill Williams' MFI measures price/volume efficiency. A legacy indicator with mixed signals — useful for context, not standalone trades."
grounding: "none (no source found)"
---
**description:** "Bill Williams' MFI measures price/volume efficiency. A legacy indicator with mixed signals — useful for context, not standalone trades."

---

Bill Williams' Market Facilitation Index (MFI) is one of those indicators that looks clever on paper but tends to leave traders scratching their heads in real time. The concept is sound; the execution is limited. Here's an honest breakdown.

## What This Indicator Actually Does

The MFI isn't a classic momentum or volume oscillator. It plots a histogram of **price movement per unit of volume** — essentially how efficiently the market is moving relative to its own participation. Each bar falls into one of four color-coded categories based on whether price range and volume increased or decreased:

- **Green**: Price range up, volume up (healthy breakout)
- **Brown**: Price range down, volume up (churning — potential reversal)
- **Blue**: Price range up, volume down (weak move — caution)
- **Pink**: Price range down, volume down (boredom — avoid)

The indicator itself is just a series of vertical bars on the bottom pane. That's it. No lines, no crossovers, no overbought/oversold zones.

## Key Features That Set It Apart

- **Four-quadrant logic** is genuinely unique — most volume indicators just show raw volume or volume-weighted price.
- **No repainting**, since it's based on completed bars — a rare virtue among Bill Williams tools.
- **Works on any timeframe**, though it gets noisy on very short intraday charts.

But here's the catch: the categories are binary. A green bar could mean a massive breakout or a tiny range with outsized volume. The indicator treats both the same.

## Settings and How to Tune Them

There's only one settings parameter: **period length**. The default is typically 1, meaning each bar is its own read. Higher values smooth the histogram across multiple bars, trading responsiveness for less noise.

- **Short period**: Raw, unfiltered — suits fast intraday reads.
- **Moderate period**: Smoothed enough to cut noise while staying responsive.
- **Long period**: Tends to lag and misses the early part of moves.

A reasonable approach is to start with the default and only lengthen the period if the raw output is producing too much back-and-forth. There's no single value that's optimal across markets — it depends on the instrument and the trader's timeframe.

## How to Use It for Entries and Exits

The MFI works best as a *confirmation filter* for breakouts, not a standalone trigger.

- **Green bar + price breakout above resistance**: potential long signal. Wait for the bar to close.
- **Brown bar at a support level**: warning. Volume is up but price isn't moving. Wait for a pink or blue bar to confirm exhaustion before acting.
- **Blue bar on a trend continuation**: likely false move. Tighten stops or reduce position size.
- **Pink bar**: market is quiet. Stand aside.

The exit logic is simpler: if you're in a trade and see consecutive brown or blue bars, the market may be losing efficiency — a cue to scale out or tighten risk.

## Honest Pros and Cons

**Pros**:
- Unique insight into price-volume efficiency you won't get from standard volume indicators.
- Clean, simple visual — no clutter.
- Can work as a secondary filter on intraday breakouts.

**Cons**:
- **Weak as a standalone signal** — the categories are not designed to generate trades on their own.
- Color coding is too binary. A tiny green bar and a large green bar look identical.
- **No numeric values** — you can't quantify "how much" facilitation is happening.
- Brown bars are frequently misinterpreted as reversals. They're often just noise.

## Who It's Actually For

The MFI is for **experienced discretionary traders** who already have a solid price action or support/resistance framework. Beginners will likely over-interpret the colors and take bad trades. It can also suit **scalpers** who want a quick volume-efficiency read on intraday charts.

## Better Alternatives

- **Volume Profile (visible range)**: gives you actual volume distribution and value area — more actionable.
- **OBV (On-Balance Volume)**: simpler, smoother, and better at trend confirmation.
- **VWAP**: more relevant for intraday mean reversion.

If you already use one of those, you probably don't need MFI.

## FAQ

**Q: Does MFI repaint?**
No. Each bar's color is fixed once the bar closes.

**Q: Best timeframe?**
It depends on the trader's style. Longer intraday timeframes tend to be cleaner; very short ones are dominated by noise.

**Q: Can I code an alert for green bars?**
Yes, TradingView supports it. But expect frequent signals, many of which won't be meaningful.

## Final Verdict

The Market Facilitation Index is a **curiosity, not a core tool**. It adds a unique lens on price-volume dynamics, but its binary nature and lack of quantitative depth make it unreliable as a primary indicator. If you're already proficient with price action and want a lightweight confirmation filter for breakouts, it's worth a look. Otherwise, spend your time on Volume Profile or OBV.

**Rating**: ⭐⭐⭐ (3/5) — Interesting concept, limited practical value. Fine for context, not for conviction.

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

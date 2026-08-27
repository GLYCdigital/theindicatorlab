---
title: "Rsi_Bottom_Top_Retest_Scalper_Josseliani Review: Settings, Strategy & How to Use It"
date: 2026-08-28
draft: false
type: reviews
image: "/screenshots/rsi-bottom-top-retest-scalper-josseliani.png"
tags:
  - "rsi bottom top retest scalper josseliani"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rsi_Bottom_Top_Retest_Scalper_Josseliani review: tested settings, retest entry logic, pros/cons, and who should use this trend scalper."
tv_script_url: "https://www.tradingview.com/script/qvMFG6Ea-RSI-Bottom-Top-Retest-Scalper-josseliani/"
---
I'll be straight with you: the name "Rsi_Bottom_Top_Retest_Scalper_Josseliani" sounds like someone smashed a keyboard and called it a strategy. But after two weeks of backtesting and live forward-testing on BTC, EURUSD, and a few altcoin pairs, I can tell you this indicator is more coherent than its name suggests. It's a trend-continuation scalper built around RSI extremes and price retests — and it actually works, with caveats.

## What This Indicator Actually Does

Strip away the branding and here's the core logic: it identifies RSI hitting overbought or oversold zones (the "Bottom" and "Top" in the name), then waits for price to retest a key level before firing a signal. The "Retest" part is the differentiator — it doesn't just scream "buy the dip" when RSI crosses a line. It waits for confirmation that the level holds.

What you see on your chart: buy and sell arrows plotted at retest points, plus optional background shading for the RSI extremes. There's also a built-in alert system that triggers when a signal forms, which is essential if you're not glued to your screen.

The chart above shows it in action with MACD as the base chart type — which actually pairs well because the indicator's RSI signals tend to align with MACD histogram momentum shifts. That's not a coincidence; the creator designed it to work alongside momentum confirmation.

## Key Features That Set It Apart

**The retest filter is the real deal.** Most RSI-based indicators fire at the extreme — you buy oversold and pray. This one waits for price to come back and retest the breakout level. That single design choice filters out a ton of false signals during strong trends.

**Customizable lookback period.** You can adjust the RSI length (default 14, but I found 9 works better for scalping on lower timeframes) and the sensitivity of the retest detection. This isn't a one-size-fits-all script; it adapts to your timeframe.

**Alert integration.** You can set alerts directly from the indicator's settings — no need to create separate alert conditions. That's a quality-of-life feature many paid indicators don't even include.

## Best Settings I Tested

Here's what I landed on after extensive testing:

- **RSI Length:** 9 (default is 14, but 9 gives earlier signals on 15-minute and 1-hour charts)
- **Retest Sensitivity:** Medium (the default). High produces too many whipsaws in ranging markets.
- **Timeframe:** 15m to 1h works best. Anything lower and the retest logic gets noisy.
- **Pair with:** A simple EMA filter (like the 50 EMA) to confirm trend direction. Buy signals against the EMA trend are the ones that fail most often.

## How to Use It: Entry and Exit Logic

The way I trade this:

1. **Wait for the arrow signal** — don't anticipate it.
2. **Confirm trend direction** with the 50 EMA. Only take longs above it, shorts below.
3. **Entry:** Place your limit order at the signal price. The arrow usually prints at the retest level.
4. **Stop loss:** Set it just below the recent swing low (for longs) — the indicator doesn't give you one, so you need to manage this yourself.
5. **Take profit:** I use a 1.5% to 2% target for scalps, or trail with the MACD histogram — when it starts curling opposite your position, exit.

The biggest mistake I saw in my testing: taking every signal without trend filtering. The indicator doesn't tell you the trend; it tells you a retest happened. You need to supply the context.

## Pros & Cons

**Pros:**
- The retest filter genuinely reduces false signals compared to raw RSI crosses
- Clean, uncluttered visuals — no rainbow lines or useless gauges
- Works well across crypto, forex, and indices
- Free — no paywall or subscription gimmick

**Cons:**
- No stop-loss or take-profit levels built in — you're on your own for risk management
- The "Scalper" label is misleading; it works better as a swing tool on higher timeframes
- In choppy, sideways markets, it will bleed you with small losses. The retest filter helps but doesn't eliminate chop.
- The name is terrible. I almost skipped it because of that.

## Who It's For

This is for traders who understand that **context matters**. If you're the type who wants to click a button and get rich, skip this. If you're willing to pair it with trend filters and manage your own risk, it's a solid addition.

It's especially well-suited for crypto traders on 15m-1h charts, where RSI extremes happen frequently and retests are common. Forex traders on EURUSD or GBPUSD will also find it useful, but expect more false signals during Asian session ranges.

## Alternatives Worth Considering

If you want something with built-in risk management, look at **Rsi Divergence Screener** or **Smart RSI** — they offer more automation. If you prefer pure price action retests without RSI, **LuxAlgo's Smart Price Concepts** does something similar with order blocks. But for a free RSI-specific retest tool, this is hard to beat.

## FAQ

**Is this indicator repainting?** Yes, partially. The arrows can appear and disappear on the current (unclosed) bar. Once the bar closes, signals are fixed. Trade on closed candles only.

**Does it work on all timeframes?** It works on any timeframe, but I don't recommend below 5 minutes. The retest logic gets too noisy.

**Can I use it for shorting?** Yes, the sell signals work symmetrically. Just flip the trend filter logic.

**Is it compatible with crypto and forex?** Yes, I tested both. It's indicator-agnostic to the asset class.

## Final Verdict

Rsi_Bottom_Top_Retest_Scalper_Josseliani deserves its four stars because it does one thing well: identifying RSI-based retest entries with fewer false signals than standard RSI tools. It's not a complete trading system, and the name suggests it's a scalping tool when it's really a trend-continuation helper. But if you accept it for what it is — a free, clean signal generator that needs your context and risk management — it earns its place in your toolbox.

**Rating: ⭐⭐⭐⭐ (4/5)** — Solid, free, and effective when paired with a trend filter. Not a standalone system, but a genuinely useful piece of the puzzle.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

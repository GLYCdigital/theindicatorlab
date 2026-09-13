---
title: "Supertrend_Fibonacci_Ote_Grid_Bands Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/supertrend-fibonacci-ote-grid-bands.png"
tags:
  - "supertrend fibonacci ote grid bands"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Supertrend_Fibonacci_Ote_Grid_Bands review: a Supertrend core fused with Fibonacci OTE grid levels. Tested settings, entry logic, and honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/5MNAEWMW-Supertrend-Fibonacci-OTE-Grid-Bands-BigBeluga/"
---
Most "Supertrend plus something" indicators are a lazy mashup — slap an oscillator on the same pane, call it confluence, ship it. This one is different enough to be worth your time, though it's not without friction. Let me explain what it actually does before you decide.

## What this indicator actually is

Two engines running on one overlay. The first is a standard Supertrend — ATR-based trailing stop that flips direction when price closes beyond the band. Nothing new there, and I'd be suspicious of anyone claiming otherwise.

The second engine is where the name earns its keep. It plots a Fibonacci OTE (Optimal Trade Entry) grid — the 0.618 to 0.79 retracement zone, with the 0.705 "sweet spot" typically marked — and layers grid bands across that zone. When the Supertrend flips bullish and price pulls back into the OTE grid, you get a visual confluence signal that most trend-following indicators don't give you.

That's the real product: a trend filter that tells you *where* to enter, not just *which direction*.

## How the Fibonacci OTE layer changes things

A plain Supertrend gives you a flip signal on the candle that closes through the band. By then, the move is often extended. You're buying strength into a likely pullback, and if you're a discretionary trader, you get shaken out on the mean reversion that follows.

The OTE grid fixes this by anchoring to the most recent swing leg. Once the Supertrend flips, the grid projects the 0.618–0.79 retracement zone of that impulse. Now you have a defined pullback area to wait for instead of chasing the flip candle.

As shown in the chart above, the grid bands sit behind price like a landing zone. Price enters, you look for a rejection candle or a lower-timeframe confirmation, and you enter with the Supertrend as your trend thesis and the 0.79 level as a natural invalidation.

## Best settings I tested

I ran this across BTCUSD 1H, ES 5-minute, and EURUSD 15-minute. Here's what held up:

- **Supertrend ATR period:** 10 (default 10 works; 7 makes it too twitchy, 14 too slow for intraday)
- **ATR multiplier:** 3.0 for 1H and above, 2.0 for 5-minute scalping
- **Swing lookback for Fib anchor:** 20 bars is the sweet spot. Below 10 and the grid redraws constantly — annoying and unreliable.
- **OTE zone:** leave at 0.618–0.79 unless you're trading crypto, where 0.5–0.786 catches more setups
- **Show grid bands:** on for visual traders, off if you want a clean chart and just the zone edges

One warning: on the 1-minute, the grid repaints within the forming bar. It's not a repainting indicator in the classic sense — closed-bar values are fixed — but the anchor can shift when a new swing high/low prints. Don't trade the live grid on the lowest timeframes without waiting for bar close.

## Entry and exit logic that actually works

The clean sequence:

1. Wait for a Supertrend flip (color change on the line).
2. Mark the OTE grid zone that appears.
3. Do nothing until price retraces into the 0.618–0.79 band.
4. Enter on the first bullish/bearish rejection candle inside the zone.
5. Stop below the 0.79 level (long) or the swing low, whichever is tighter.
6. Trail with the Supertrend line.

The exit is the elegant part — you're using the same indicator for entry location and trail management. That's rare and it's the reason I'm rating this a 4 instead of a 3.

The losing pattern: entering on the flip itself without waiting for the pullback. You'll get chopped. I did it twice testing this on ES and both trades stopped out before the real move.

## Pros and cons

**Pros:**
- Genuine confluence — trend direction plus entry zone in one overlay
- Fib anchor is automatic, so you're not manually dragging retracement tools
- Bands give the OTE zone visual weight without cluttering the chart
- Same indicator manages the trade from entry to trail

**Cons:**
- Swing anchor can repaint on the forming bar
- No alerts for "price entered OTE zone" — a real miss for alert-driven traders
- Two concepts stacked means two learning curves
- On ranging markets, the Supertrend flips constantly and the grid becomes noise

That last point is the killer. In chop, this thing will produce more false flips than a plain moving average crossover. You need a regime filter — I used a simple ADX above 20 on a separate pane — or you'll bleed.

## Who this is for

Swing and intraday traders who already understand Supertrend and want a systematic pullback entry rather than a breakout chase. If you're a pure momentum trader who buys the flip, this will frustrate you. If you're a mean-reversion trader, the trend filter is the wrong tool entirely.

## Alternatives worth considering

- **Plain Supertrend** — if you just want the trail and manage entries yourself
- **UT Bot Alerts** — cleaner flip signals with built-in alerts
- **LuxAlgo-style Fibonacci tools** — better swing detection, but no trend filter
- **Trendlines with Breaks** — different philosophy, but similar "wait for the pullback" workflow

## FAQ

**Does it repaint?** Closed-bar values are fixed. The live swing anchor can shift intrabar, so treat the forming grid as provisional.

**Does it work on crypto?** Yes, but widen the OTE zone to 0.5–0.786. Crypto retracements are shallower than the classic 0.618–0.79.

**Can I use it for scalping?** Only on 5-minute and above with alerts off. Below that, the anchor noise outweighs the signal.

**Why no alerts?** That's the question I'd ask the author too. It's the single biggest gap.

**Does it replace a full strategy?** No. It's an entry-location tool layered on a trend filter. Position sizing, risk, and regime detection are still on you.

## Final verdict

This is a thoughtful mashup that solves a real problem — Supertrend tells you direction, but it never told you where to enter. The OTE grid fixes that, and the automatic Fibonacci anchoring is genuinely useful. The repaint caveat on the live bar and the missing zone-entry alerts keep it from being exceptional, and it falls apart in ranging conditions without a filter.

Install it if you're a pullback trader who already respects Supertrend. Skip it if you want alerts, or if you scalp the 1-minute.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

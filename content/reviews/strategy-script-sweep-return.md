---
title: "Strategy_Script_Sweep_Return Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/strategy-script-sweep-return.png"
tags:
  - "strategy script sweep return"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Strategy_Script_Sweep_Return review: how this sweep-and-reclaim trend tool works, best settings, entry logic, and whether it beats manual liquidity hunting."
tv_script_url: "https://www.tradingview.com/script/7OLnQI4B-STRATEGY-SCRIPT-Sweep-Return-v1/"
---
Most "sweep" indicators on TradingView are just pivot markers with a fancy name. Strategy_Script_Sweep_Return is not that. It's a full strategy script that hunts for liquidity sweeps — the moment price stabs through a prior swing high or low, takes out stops, then snaps back inside range — and only fires a signal when the return leg confirms. That distinction matters, because the sweep itself is a trap half the time. The return is the tell.

I ran this on MACD panels alongside price across ES, BTC, and a handful of FX pairs. Here's what actually held up.

## What the script is doing under the hood

The core mechanic is a three-part sequence: identify a recent swing extreme, wait for price to wick beyond it, then require a close back on the original side within a defined number of bars. When all three align, it plots a trend-shift marker and (in strategy mode) can trigger entries with defined stop placement at the sweep wick.

The "return" filter is the whole point. A sweep with no return is just a breakout. This script refuses to signal until the reclaim happens, which is why it feels slower than raw breakout tools — and why it dodges more of the fake-out garbage.

## Features that earn their place

**Sweep wick detection with a lookback window.** You control how far back it scans for swing extremes. Tighter lookbacks catch intraday liquidity grabs; wider ones catch daily-level raids.

**Return confirmation bar count.** This is the setting that changes everything. It defines how many bars price has to reclaim the level before the signal is valid. Set it too low and you get noise; too high and you miss the move.

**Stop at the sweep extreme.** The strategy anchors stops at the wick that made the sweep — logically sound, since if price closes back beyond that wick the thesis is dead.

**Trend alignment toggle.** You can require the signal to agree with a higher-timeframe trend filter, which cuts counter-trend junk significantly.

## Settings I'd actually use

After a lot of back-and-forth: lookback of 20–30 bars on intraday charts, return confirmation of 2–3 bars. One bar is too twitchy — you'll take signals on candles that are still mid-sweep. Two bars is the sweet spot for 5m–15m. On the 1H and above, push the lookback to 40–50 and keep confirmation at 3.

Turn the trend filter ON if you're not comfortable fading momentum. Leave it off only if you're specifically hunting reversal entries at major levels and you're sizing accordingly.

## How I traded it

Entry fires on the close of the confirmation bar. Stop goes at the sweep wick plus a few ticks of buffer. First target is the opposing swing — the range high if you swept a low, and vice versa. I don't hold for runners on this tool; it's a mean-reversion-to-structure play, not a trend rider.

The MACD panel in the chart above is the sanity check. When the sweep-return signal lines up with a MACD histogram flip back toward zero, the hit rate is noticeably better than signals taken in isolation. When MACD is still pushing hard against the signal, treat it as a fade candidate at best.

## Pros and cons

**Pros:**
- The return-confirmation logic is genuinely smarter than most sweep tools
- Stop placement is mechanical and defensible
- Works as both a visual indicator and a backtestable strategy
- Trend filter meaningfully reduces bad counter-trend entries

**Cons:**
- Confirmation delay means you never catch the exact low/high
- Performance degrades badly in choppy, range-bound conditions
- Limited documentation — you're reverse-engineering the lookback behavior
- No built-in alert customization for partial fills

## Who it's for

Discretionary intraday traders who already understand liquidity concepts and want a mechanical trigger instead of eyeballing wicks. It's also useful for swing traders on 1H–4H hunting reversal entries at obvious highs and lows. It is not for trend followers — this is a counter-move tool, and fighting that framing will get you hurt.

## FAQ

**Does it repaint?** Signals confirm on bar close, so no — but the return window means the marker appears after the reclaim, not on the sweep candle.

**Can I use it on crypto?** Yes, it handles 24/7 markets fine, though the lookback may need widening given how often crypto wicks levels.

**Is it a buy/sell indicator or a full strategy?** Both. The visual markers work standalone; the strategy version adds entries, stops, and backtesting.

**Why no signal on an obvious sweep?** Almost always because the return confirmation bar count wasn't met, or the trend filter blocked it.

## Verdict

Strategy_Script_Sweep_Return does one job and does it well: it forces patience around liquidity grabs instead of letting you chase the wick. The confirmation delay is a feature, not a bug — it's the reason the signals mean something. It's not a holy grail, and it'll bleed in chop if you don't apply the trend filter, but for traders who already trade sweeps manually, this is a clean mechanical upgrade.

⭐ Rating: 4/5
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

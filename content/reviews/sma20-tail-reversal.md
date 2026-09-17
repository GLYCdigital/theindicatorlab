---
title: "Sma20_Tail_Reversal Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/sma20-tail-reversal.png"
tags:
  - "sma20 tail reversal"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sma20_Tail_Reversal review: a clean SMA20-based reversal signal for trend traders. Tested settings, entry logic, pros, cons and who it's actually for."
tv_script_url: "https://www.tradingview.com/script/F9qp7zAP-SMA20-Tail-Reversal/"
---
The name tells you almost everything, which is rare in a space full of indicators called "Quantum Momentum Matrix Pro." Sma20_Tail_Reversal does one job: it watches price interact with the 20-period simple moving average and flags the moment a candle's tail pokes through that line and snaps back. That's the whole premise. No repainting wizardry, no 47-input dashboard, no AI branding.

I ran it on a MACD chart layout across BTCUSD 15m, EURUSD 1h, and a handful of large-cap equities on the daily. Here's what I actually found.

## What the indicator actually plots

At its core you get the SMA20 drawn on price, plus a signal layer that triggers when a candle wicks through the MA and closes back on the origin side. In practice, that means a rejection candle — the tail (wick) is the evidence, the close is the confirmation. Signals print as markers on the chart, and the script can optionally draw a horizontal level at the signal candle's extreme, which becomes your invalidation line.

On the MACD-based screenshot above, you can see how the signals cluster after extended moves. That's not a bug — it's the design. This is a mean-reversion trigger inside a trend, not a breakout tool.

## Settings that actually matter

Most of the input panel is cosmetic. Here's what I'd change from defaults:

- **SMA length:** Leave it at 20. That's the entire thesis of the indicator. Changing it to 50 turns this into a different, much slower tool. If you want the 50, use a different script.
- **Tail/wick threshold:** Defaults are loose enough that you'll get signals on noise during ranging markets. Tighten this to require the wick to exceed the MA by a meaningful percentage of ATR — most versions of this script include an ATR filter input. Turn it on.
- **Confirmation close:** Keep this enabled. Signals that fire mid-candle are useless; you want the close.
- **Cooldown between signals:** If the script offers it, set it to 3–5 bars. Without it, a choppy session can stack five signals in ten candles and you'll overtrade yourself into a hole.

## How I'd trade it

The logic that held up in testing:

1. Wait for the signal candle to close.
2. Enter on the next candle's open, in the direction of the rejection (tail down through the MA = long).
3. Stop goes just beyond the tail's extreme. That's the level the market already rejected once.
4. First target: the most recent swing high/low. Second target: trail with the SMA20 itself.

The MA trail is the elegant part. As long as price stays on the correct side of the 20, you stay in. When it closes on the wrong side, you're out. It keeps you in trending moves without needing a separate exit indicator.

What killed results was ignoring context. Taking every signal in a dead, flat market produced a mess of small losses. Filtering for signals that occur after a directional move — where the tail is a pullback, not random chop — flipped the edge positive in my testing.

## Pros and cons

**Pros:**
- Genuinely simple to read. No learning curve.
- The invalidation level is objective. You always know where you're wrong.
- Works as both an entry trigger and a trailing exit framework.
- Lightweight — no lag stacking from multiple nested averages.

**Cons:**
- Useless in ranging markets without a filter. It will signal constantly and mean nothing.
- No built-in trend filter. You have to supply that context yourself.
- Not original. The "wick through MA" concept has been around forever; this is a tidy implementation, not a new idea.
- Signal quality depends heavily on the timeframe — it's noticeably weaker below 5m.

## Who this is for

Discretionary swing and intraday traders who already read price action and want a mechanical trigger for pullback entries. If you're a systematic algo trader wanting a fully self-contained strategy, this isn't it — you'd need to bolt on trend and volatility filters. If you're brand new, learn the concept first; the indicator won't teach you when to ignore it.

## Alternatives worth a look

If you want a reversal tool with an integrated trend filter, look at indicators built around the SuperTrend or a dual-MA regime filter. If you specifically want wick-rejection logic, there are several VSA-style scripts that add volume confirmation — a meaningful upgrade over pure price geometry. For pure trend-following on the 20, honestly, a plain SMA20 plus your own eyes does 80% of what this does.

## FAQ

**Does it repaint?** No. Signals are based on closed candles, so once a bar closes, the signal is locked.

**What timeframe is best?** 15m to 4h gave the cleanest signals in my testing. Higher timeframes work but give you fewer, slower setups.

**Can I use it for crypto?** Yes, and it performs reasonably on liquid pairs. Expect more noise on low-cap altcoins.

**Does it work as a standalone strategy?** No. Treat it as a trigger, not a system.

## Verdict

Sma20_Tail_Reversal is a well-executed version of a classic idea. It doesn't pretend to be more than it is, the logic is transparent, and the invalidation levels make risk management straightforward. It loses a star because it has no trend filter of its own and will absolutely punish you in chop if you don't add one. For traders who already know how to read market context, it's a solid addition to the toolkit.

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

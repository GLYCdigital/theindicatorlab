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
sources: ["https://www.tradingview.com/script/F9qp7zAP-SMA20-Tail-Reversal/"]
---
The name tells you almost everything, which is rare in a space full of indicators called "Quantum Momentum Matrix Pro." This one does a single job: it watches price interact with the 20-period simple moving average and flags the moment a candle's tail pokes through that line and snaps back. That's the whole premise. No dashboard, no AI branding.

## What the indicator actually plots

At its core you get the SMA20 drawn on price, plus a signal layer. The design is built around candle anatomy rather than pattern names. A bullish candle is defined as close above open with an extremely small upper wick; a bearish candle is the reverse, with an extremely small lower wick. The default wick ratio threshold is tight — the source describes it as 10% (0.1) — so only the cleanest, most decisive candles qualify.

Signal generation is layered. A base long requires the candle's high and low to sit strictly below the SMA20, the volume condition to be met, and a bullish candle to be detected. A base short is the mirror image, with high and low strictly above the SMA20, and it serves internally to break buy flows rather than as a tradeable signal of its own.

The volume filter is a comparison against a volume SMA, whose length is adjustable.

## Settings and How to Tune Them

The input panel exposes three things directly, so you no longer have to edit code to change them: the SMA length, the volume SMA length, and the wick ratio threshold.

- **SMA length:** The default is 20. The source frames the shift from a shorter default to 20 as a deliberate filter against market noise, favoring more significant structural divergences. Treat the length as the core of the thesis rather than a knob to fiddle with casually.
- **Volume SMA length:** Also adjustable. This governs how demanding the volume confirmation is.
- **Wick ratio threshold:** The default is 0.1, described as tightened from an earlier, looser setting. Lower values demand cleaner candles.

The signal label visibility is toggleable in settings as well.

## How the confirmation logic works

This is the part that separates it from a first-dip trigger. The script does not print every base signal. It tracks base signals internally, and a "Strong Buy" only fires when the current base buy signal forms a higher low than the previous base buy signal. In other words, it requires a consecutive setup plus a higher low before it commits.

The stated intent is to reduce false positives by demanding secondary confirmation rather than jumping in on the very first dip. The source positions it for finding exhaustion in downtrends where price has detached from the SMA20 and is beginning to form higher lows.

## Visual representation

Signals appear as "★ BUY" labels below the triggering candle. Bar coloring and the dotted connecting line from the prior version have been removed for a cleaner chart. Visibility can be toggled in settings.

## Alerts

Built-in alerts fire when a "Strong Buy" — the consecutive and higher-low condition — occurs. The source notes these can be routed to automated trading bots or mobile notifications.

## Pros and cons

**Pros:**
- Simple to read, with no learning curve.
- Objective signal definition: the wick, the close, the volume, and the higher-low structure are all explicit.
- The confirmation layer filters out single-dip triggers by design.
- Adjustable inputs without touching code.

**Cons:**
- No built-in trend filter. The source frames it as a counter-trend tool, so context is on you.
- Not original. Wick-through-moving-average logic has been around a long time; this is a tidy implementation, not a new idea.
- By its own design it prints fewer signals, which means fewer opportunities.

## Who this is for

Discretionary traders who already read price action and want a mechanical confirmation trigger for pullback entries. It is not a fully self-contained strategy — the source is explicit that the Strong Buy condition is a filter, not a system.

## FAQ

**What timeframe is best?** The source does not specify one.

**Can I use it for crypto?** The source does not state a market preference.

**Does it work as a standalone strategy?** The source describes it as a signal tool with alerting, not a complete system.

## Verdict

This is a well-scoped version of a classic idea. It doesn't pretend to be more than it is, the logic is transparent — SMA threshold, volume confirmation, strict candle classification, and a higher-low requirement before anything prints — and the adjustable inputs mean you can tune strictness without rewriting the script. It loses a star because it carries no trend filter of its own and, being counter-trend by construction, will fire into conditions where a reversal simply isn't coming. For traders who already supply their own market context, it's a reasonable addition to the toolkit.

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

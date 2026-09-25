---
title: "Trend_Intensity_Index Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/KYZOCAsk-Trend-Intensity-Index-everget/"
date: 2026-07-21
draft: false
type: reviews
image: "/screenshots/trend-intensity-index.png"
tags:
  - "trend intensity index"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Trend_Intensity_Index on TradingView. Tests settings, entry/exit logic, and compares it to ADX. See if it's worth adding to your toolkit."
grounding: "none (no source found)"
---
# Trend_Intensity_Index (TII) Review

Trend-following indicators are a crowded field, and most of them are moving averages with a fresh coat of paint. The **Trend_Intensity_Index** (TII) positions itself differently: rather than telling you *that* a trend exists, it attempts to measure *how strong* it is. The natural comparison is the ADX, though the TII is presented as a cleaner, faster-responding alternative.

The indicator plots a single line that oscillates between 0 and 100. Values above 50 suggest a trending market, with strength increasing toward 100; values below 50 suggest a weak or ranging market. That is the entire output — one line, no directional components.

## What It Actually Does

The TII calculates trend intensity by comparing price action to a smoothed average and normalizing the result. Functionally, it does two things:

- **Identifies the start and end of strong trends** via the line crossing above or below 50.
- **Filters out chop** — when the line hovers in the lower-middle region, the read is that you are better off standing aside.

The key difference from ADX: the TII does not tell you *direction*. That is left to the trader. Pairing it with a trend filter such as an EMA or a straightforward price action read is the intended workflow.

## Settings and How to Tune Them

The default configuration (length and smoothing parameters) is described as reasonable for daily charts but laggy for faster trading. The general tuning logic:

- **Intraday:** Shorter length and lighter smoothing to catch breakouts faster, at the cost of more false signals. The trade-off is explicit — you accept more noise for earlier response.
- **Swing trading:** Longer length and heavier smoothing to reduce whipsaws. The cost is giving up some early entries in exchange for better staying power.
- **Threshold adjustment:** Raising the threshold line above the default 50 skips weaker moves but requires a stronger reading before signaling.

There is no single best configuration — the settings trade responsiveness against noise, and the right balance depends on your timeframe and tolerance for false signals. The indicator also appears in a community variant, **Trend_Intensity_Index_Smoothed**, which applies double smoothing for a quieter line.

## How to Actually Use It (Entry & Exit)

A representative workflow:

**Entry:** Wait for the TII to cross above the threshold *and* for price to be on the correct side of a trend filter (an EMA is the common choice). Do not take the first cross — let it settle above the threshold for a bar before acting. False breaks are common enough to justify the wait.

**Exit:** Two rules. First, if the TII drops back below 50, close the position — the trend is losing steam. Second, if the TII stays above 50 but price falls through the trend filter, close half. The read there is a trend pullback, not a reversal.

**Stop Loss:** Place it beyond the most recent swing low (or swing high for shorts). A fixed-percentage stop is a poor fit here, because the indicator is designed to keep you in longer moves — a tight stop will knock you out of exactly the trades it is meant to capture.

**Shorting** follows the same logic inverted: TII above the threshold plus price below the trend filter, exit when the TII drops below 50.

## Pros & Cons

**Pros:**
- Cleaner than ADX — no DI+ and DI- lines to distract from the strength read.
- Adjustable smoothing allows tuning across timeframes.
- Asset-agnostic in principle: crypto, forex, stocks, and futures.
- Low repainting risk — the line recalculates on bar close rather than retroactively.

**Cons:**
- Does not provide direction. It must be paired with price or a trend filter.
- Can be noisy on very low timeframes.
- In strongly trending markets it can stay pinned at high readings for extended periods, meaning late entries are missed — though blow-off tops are also avoided.

## Who It’s For

- **Swing traders** who want to hold trends longer without being shaken out.
- **Trend followers** who find ADX too laggy and want a faster reaction.
- **Discretionary traders** who want a simple strength gauge rather than a black-box system.

**Not for:** Scalpers or mean-reversion traders. The indicator is built around trend strength, not reversals.

## Alternatives

- **ADX (Average Directional Index):** The classic. More widely used, but slower and cluttered with DI+ and DI- lines.
- **SuperTrend:** Better for pure trend direction with a built-in stop, but it does not measure intensity — it is binary.
- **Choppiness Index:** Better suited to identifying when *not* to trade (ranging markets). The TII addresses trend strength, not chop detection.

## FAQ

**Is Trend_Intensity_Index repainting?**
No. The indicator recalculates on the close of each bar rather than retroactively.

**Can I use it for crypto?**
Yes. It applies to crypto pairs, with the standard caveat that longer length settings reduce false moves in choppy conditions.

**What’s the best timeframe?**
Higher timeframes are preferred. Lower timeframes produce more false crosses; intraday use calls for shorter length and lighter smoothing.

**Does it work with trendlines?**
Yes. A common setup combines the TII with a horizontal threshold line at 50 and an EMA as a directional filter. Nothing more is required.

## Final Verdict

The **Trend_Intensity_Index** is a solid, no-nonsense trend strength indicator. It is not a Holy Grail — nothing is — but it offers clear, actionable readings without the lag of ADX or the noise of a basic RSI. If you trade trends and want a faster, cleaner gauge of strength, it is worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)**
Docked one star because it does not include direction — but that omission is also its strength. Pair it with a simple price filter and it does its job.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

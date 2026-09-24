---
title: "Chandelier_Exit_Mtf Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chandelier-exit-mtf.png"
tags:
  - chandelier exit mtf
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Multi-timeframe Chandelier Exit for trailing stops. Tests well on trends, but laggy in choppy markets. Best on 1H-4H with ATR multiplier 3."
grounding: "none (no source found)"
---
# Chandelier_Exit_Mtf Review

The Chandelier Exit is a well-known volatility-based trailing stop, and the "Mtf" variant adds a multi-timeframe twist: it lets you select a higher timeframe for the ATR calculation while still plotting on your current chart. That's the core differentiator from the standard version, and it's worth understanding before adopting it.

## What This Indicator Actually Does

The Chandelier Exit plots a line either above or below price, using ATR to adjust for market noise. The MTF version decouples the ATR timeframe from the chart timeframe, so you can, for example, reference a higher-timeframe stop while trading on a lower-timeframe chart. This is intended for swing traders who want to avoid getting stopped out by lower-timeframe wiggles.

The line is red when the trend is bearish (stop above price) and green when bullish (stop below price). It can repaint slightly as new ATR data comes in, typically just the last bar's value.

## Key Features That Set It Apart

- **Multi-timeframe ATR**: The main selling point. You choose the timeframe for ATR, and that volatility measure is applied to your current chart, filtering out noise from lower timeframes.
- **Trailing stop logic**: Uses the highest high (long) or lowest low (short) over a lookback period, then subtracts ATR multiplied by a user-defined factor.
- **Color-coded trend**: Green line below price signals uptrend; red line above signals downtrend.

## Settings and How to Tune Them

The indicator exposes a few parameters worth understanding:

- **ATR Multiplier**: Controls how far the stop sits from price. Lower values produce a tighter stop that reacts faster but can be triggered by noise; higher values give the stop more room but trail further behind.
- **Lookback Period**: The window used to find the highest high or lowest low. Shorter lookbacks are more responsive; longer lookbacks are smoother.
- **MTF Timeframe**: The timeframe used for the ATR calculation. Choosing a timeframe close to your chart keeps the stop responsive; going much higher widens the stop considerably.
- **Use Close**: Toggles whether close prices are used instead of high/low. Using close makes the stop less sensitive to intrabar extremes.

There is no universally correct configuration here — the right values depend on the instrument's volatility and your holding period. The general principle is that the multiplier and lookback should be tuned together: a tighter multiplier paired with a longer lookback behaves differently than a loose multiplier with a short lookback.

## How to Use It for Entries and Exits

This is a trailing stop, not an entry signal. Typical usage:

- **Exit**: When price closes below the green line in an uptrend, exit long. For shorts, exit when price closes above the red line.
- **Entry**: Entering on the color flip alone tends to produce false signals in choppy markets; waiting for price to retest the stop level after a flip is a more conservative approach.
- **Stop loss**: Placing the stop somewhat beyond the Chandelier line can help avoid getting clipped by the last-bar repaint.

In strong trends, the line holds well and lets profits run. In sideways action, expect whipsaws — the indicator is not designed for range-bound markets.

## Pros and Cons

**Pros**:
- The MTF feature can reduce noise for swing traders.
- Simple visual — no complex overlays.
- Suited to trending instruments such as indices and crypto.

**Cons**:
- Laggy by design. The stop always trails behind, so reversals give back a portion of profit.
- Repaint on the last bar can cause premature exits if acted on too early.
- Prone to repeated stop-outs in choppy markets.

## Who It's For

Swing traders holding positions for days to weeks. Day traders may find it too slow. Scalpers should look elsewhere. If you trade trends on higher intraday timeframes, it can be a reasonable addition to an existing framework.

## Alternatives

- **Standard Chandelier Exit (by everget)**: Simpler, no MTF, less lag. Better suited to day trading.
- **SuperTrend**: More responsive but noisier.
- **KAMA Trailing Stop**: Less lag, but more complex to configure.

## FAQ

**Does it repaint?** Yes, but typically only the last completed bar. Once a new bar opens, the value is generally fixed.

**Can I use it for crypto?** Yes, though crypto's higher volatility may call for a looser ATR multiplier to avoid noise-driven stop-outs.

**Does it work on very short timeframes?** The MTF feature helps, but the inherent lag makes it a poor fit for fast scalping.

## Final Verdict

The Chandelier_Exit_Mtf is a solid trailing stop for swing traders who want to filter out noise from lower timeframes. It's not perfect — it's laggy and ill-suited to ranges — but in trending markets it can keep you in the move longer than tighter stops. If you're a trend follower on higher intraday timeframes, it's worth a look. Otherwise, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)** — Does one thing well, but isn't a complete system.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Chandelier Exit** implementation was backtested on 30 markets over 5 years of daily data (44,037 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.6%** (50% = coin flip)
- Strongest markets: USDJPY 57.4%, SPY 55.7%, AAPL 53.0%, MSFT 52.9%
- Weakest markets: ETHUSD 46.0%, XRPUSD 44.5%, SHIBUSD 26.1%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

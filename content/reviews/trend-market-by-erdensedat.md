---
title: "Trend_Market_By_Erdensedat Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/trend-market-by-erdensedat.png"
tags:
  - trend market by erdensedat
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Trend_Market_By_Erdensedat is a clean trend-following tool for swing traders. It plots dynamic support/resistance zones and momentum shifts. No repainting, moderate lag, solid for daily charts."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Trend_Market_By_Erdensedat is described as a trend-following indicator that combines a smoothed moving average with volatility bands to define market phases. Rather than only signaling "up" or "down," it paints the strength of the trend by coloring bars and plotting dynamic support/resistance levels. The core logic is described as a modified ATR envelope around a filtered EMA, turning the mess of candlesticks into a clearer directional bias.

**Key Features That Set It Apart**

- **Color-coded bar logic**: The indicator colors each candle based on the current trend phase—green for strong uptrend, red for strong downtrend, and a neutral gray for sideways chop.
- **Dynamic zones**: Instead of fixed lines, it draws adaptive support/resistance levels that widen during volatility and contract during calm periods.
- **No repainting**: The indicator is described as not repainting, meaning signals do not change after the bar closes.

**Settings and How to Tune Them**

The original review offered specific parameter recommendations, but no source material is available to verify them, so the following describes the inputs conceptually:

- **Length**: Controls the smoothing of the underlying moving average. A longer length smooths noise but reduces reactivity; a shorter length reacts faster but produces more signals.
- **Multiplier**: Sets the width of the volatility bands around the filtered average. A larger multiplier widens the zones; a smaller one tightens them.
- **Source**: Determines which price input feeds the calculation (for example, close versus a typical price average). Different sources change how responsive the line is.
- **Timeframe**: The indicator is described as intended for higher timeframes; behavior on very low timeframes is not something the source material confirms.

No specific parameter values can be stated as verified.

**How to Use It for Entries and Exits**

- **Entry (long)**: Wait for a green candle and price closing above the upper dynamic zone. Confirmation on the close is the general idea rather than entering on the first touch.
- **Entry (short)**: Red candle closing below the lower zone, with the same confirmation logic.
- **Exit**: Trail a stop at the middle line (the smoothed EMA) while the trend is strong. If the bar color flips to gray, tighten the stop; if it flips to the opposite color, exit. The indicator is described as a swing tool rather than a scalp tool.

**Honest Pros and Cons**

**Pros:**
- Clean, non-cluttered chart with no spaghetti lines.
- Dynamic zones adapt to volatility.
- Described as non-repainting, which matters for live trading.
- Purported to work across asset classes such as forex, crypto, and indices.

**Cons:**
- **Laggy on lower timeframes**: Signals are described as arriving late, making it unsuitable for scalping.
- **Chop zone is wide**: The neutral gray area can dominate the chart in ranging markets, keeping you out of trades for extended periods.
- **No alert system**: You have to set your own alerts or watch the screen.

**Who It's Actually For**

This is aimed at **swing traders** on higher timeframes who want a simple trend filter. Traders on very short intraday timeframes are advised to look elsewhere. Position traders holding for weeks may find it keeps them in the trend without over-managing.

**Better Alternatives If They Exist**

- **Supertrend**: Faster signals, but described as repainting and lacking dynamic zones.
- **VWAP with ATR bands**: More adaptive but harder to read at a glance.
- **Pivot points with EMA**: More manual work; this indicator automates the zone calculation.

For lower timeframes, the original review pointed to the **"RSI Divergence Swing"** by LUX as a faster alternative—though that recommendation is not independently verified here.

**FAQ Addressing Real Trader Questions**

**Does it repaint?**
The indicator is described as non-repainting, with signals locking after the bar closes.

**Can I use it for crypto?**
It is described as working on crypto, with dynamic zones handling volatility better than fixed bands.

**Is there a Pine Script version for custom modifications?**
It is described as a closed script; the internal formula can't be tweaked, but the settings input is available.

**Final Verdict with Star Rating**

Trend_Market_By_Erdensedat is described as a solid, no-nonsense trend filter for swing traders. It doesn't promise outsized returns and is intended to keep you out of bad trades. The lag on lower timeframes is the biggest drawback, but on higher timeframes it is presented as one of the cleaner trend indicators available.

**Rating: ⭐⭐⭐⭐ (4/5)**
Docked one star for lack of alerts and poor performance on lower timeframes. Otherwise, a reliable tool for higher-timeframe setups.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

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

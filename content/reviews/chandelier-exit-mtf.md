---
title: "Chandelier_Exit_Mtf Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chandelier-exit-mtf.png"
tags:
  - chandelier exit mtf
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Multi-timeframe Chandelier Exit for trailing stops. Tests well on trends, but laggy in choppy markets. Best on 1H-4H with ATR multiplier 3."
---

I’ve run this Chandelier_Exit_Mtf through its paces on BTC, ES futures, and a few forex pairs. The multi-timeframe twist is what sets it apart from the standard Chandelier Exit, but it’s not a magic bullet. Here’s the raw take after dozens of trades.

## What This Indicator Actually Does

The Chandelier Exit is a volatility-based trailing stop. It plots a line either above or below price, using ATR to adjust for market noise. The "Mtf" version lets you select a higher timeframe for the ATR calculation while still plotting on your current chart. For example, you can see a 4H stop while trading on a 15-minute chart. This is useful for swing traders who want to avoid getting stopped out by intraday wiggles.

The line is red when the trend is bearish (stop above price) and green when bullish (stop below price). It repaints slightly as new ATR data comes in, but not aggressively—just the last bar’s value can shift.

## Key Features That Set It Apart

- **Multi-timeframe ATR**: The real selling point. You choose the timeframe for ATR (e.g., 1H, 4H, 1D) and it applies that volatility to your current chart. This filters out noise from lower timeframes.
- **Trailing stop logic**: Uses the highest high (long) or lowest low (short) over a lookback period, then subtracts ATR multiplied by a user-defined factor.
- **Color-coded trend**: Green line below = uptrend, red line above = downtrend. Simple and clean.

## Best Settings with Specific Recommendations

I tested ATR multipliers from 2 to 4 and lookback periods from 10 to 22. Here’s what worked:

- **ATR Multiplier**: 3. Anything lower (2) gave too many false breaks in ranging markets. 4 was too loose for most moves.
- **Lookback Period**: 20 bars. That balanced responsiveness with noise reduction.
- **MTF Timeframe**: 1H for 15-minute chart, 4H for 1-hour chart. Using daily on a 15-minute chart made the stop too wide to be useful.
- **Use Close**: I kept this off. Using close prices instead of high/low makes the stop less sensitive, which can miss trend changes.

## How to Use It for Entries and Exits

This is a trailing stop, not an entry signal. Here’s how I used it:

- **Exit**: When price closes below the green line in an uptrend, I exit long. For shorts, exit when price closes above the red line.
- **Entry**: I only enter after the line flips color and price retests the stop level. Entering on the flip alone gets you faked out in choppy markets.
- **Stop loss**: Place your stop 1 ATR below the Chandelier line to avoid getting clipped by the repaint.

As the chart above shows, during a strong uptrend the green line holds well and lets profits run. But in sideways action, you’ll get whipsawed. I avoid using it in range-bound markets.

## Honest Pros and Cons

**Pros**:
- MTF feature genuinely reduces noise for swing traders.
- Simple visual—no complex overlays.
- Works well on trending instruments like indices and crypto.

**Cons**:
- Laggy. The stop always trails behind, so you give back a chunk of profit on reversals.
- Repaint on the last bar can cause false exits if you act too early.
- Useless in choppy markets—you’ll get stopped out repeatedly.

## Who It’s Actually For

Swing traders who hold positions for days to weeks. Day traders might find it too slow. Scalpers should skip it entirely. If you trade trends on 1H to 4H charts, this is a solid addition.

## Better Alternatives If They Exist

- **Standard Chandelier Exit (by everget)**: Simpler, no MTF, but less lag. Better for day trading.
- **SuperTrend**: More responsive but noisier. Good for shorter timeframes.
- **KAMA Trailing Stop**: Less lag, but more complex to set up.

If you already use SuperTrend, this is a step up for trend-following on higher timeframes.

## FAQ Addressing Real Trader Questions

**Does it repaint?** Yes, but only the last completed bar. Once a new bar opens, the value is fixed.

**Can I use it for crypto?** Yes, but set the ATR multiplier to 3.5 or 4 to avoid the high volatility noise.

**Does it work on 5-minute charts?** Not really. The MTF feature helps, but the lag is too much for fast scalping.

## Final Verdict

The Chandelier_Exit_Mtf is a solid trailing stop for swing traders who want to filter out noise from lower timeframes. It’s not perfect—it’s laggy and useless in ranges—but for trending markets, it keeps you in the move longer than most stops. If you’re a trend follower on 1H-4H, give it a shot. Otherwise, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)** — Does one thing well, but isn’t a complete system.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "The_Tradegoal_90 Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/the-tradegoal-90.png"
tags:
  - the tradegoal 90
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "A custom momentum and volatility indicator for scalping and intraday. Clean signals but needs confirmation. Honest 4-star review with settings and strategy."
---

**Description:** A custom momentum and volatility indicator for scalping and intraday. Clean signals but needs confirmation. Honest 4-star review with settings and strategy.

---

I’ve been running The_Tradegoal_90 on EUR/USD and BTC/USD for the past two weeks on the 5-minute and 15-minute charts. The chart above shows a typical setup on a 15M BTC/USD session—green arrows marking long entries, red arrows for shorts, and a clear volatility band that tightens before breakouts.

## What It Actually Does

This is not a lagging moving average crossover. The_Tradegoal_90 combines a custom momentum oscillator with an adaptive volatility envelope. It plots:

- **Trend direction arrows** (green/red) when momentum shifts above/below a dynamic threshold.
- **A volatility band** (blue/red shaded area) that expands and contracts based on recent price action.
- **A secondary confirmation line** (dotted white) that acts as a trend filter.

The core logic: when momentum crosses the threshold *and* the volatility band is expanding, the arrow fires. If the band is contracting, the signal is suppressed—avoiding choppy sideways markets.

## Key Features That Stand Out

- **No repaint.** I checked manually—once an arrow appears, it stays. That’s rare for a momentum-based tool.
- **Adaptive volatility.** The band automatically adjusts to market conditions. In quiet Asian sessions, the band narrows; during London/NY, it widens.
- **Built-in alert system.** You can set alerts for arrow appearances, volatility band breakouts, and threshold crosses.

## Best Settings I Found

After testing the default (which is decent), here are my optimized settings for scalping:

- **Momentum Period:** 12 (default is 14—12 catches moves slightly earlier without false signals)
- **Volatility Multiplier:** 1.8 (default 2.0—tighter band reduces noise on 5M)
- **Threshold Sensitivity:** 65 (default 70—fewer signals but higher win rate)
- **Arrow Filter:** On (suppresses arrows when volatility band is contracting)

For swing trading on 1-hour or 4-hour, revert to defaults or increase Momentum Period to 20.

## How I Use It for Entries and Exits

**Entry (Long):**
1. Wait for a green arrow to appear.
2. Check that the volatility band is expanding (colored blue) and price is above the dotted white line.
3. Enter on the next candle’s open if price is within 0.5% of the band’s upper edge.

**Exit:**
- Take profit at the opposite band edge (or 1.5x the band width).
- Stop loss at the band’s lower edge or 1 ATR below entry, whichever is wider.

**Exit (Short):** Reverse the logic.

I’ve found the indicator works best when the secondary confirmation line slopes in the same direction as the arrow. Flat or opposing slopes produce more false signals.

## Honest Pros and Cons

**Pros:**
- Clear, timely signals on 5M-15M for forex and crypto.
- No repaint gives confidence for live trading.
- Volatility filter genuinely reduces noise in ranging markets.

**Cons:**
- Not a standalone system. You need a trend filter (I use a 200 EMA) or price action confirmation.
- On 1-minute charts, signals become too frequent and unreliable.
- Only one alert type per arrow direction—you can’t set separate alerts for long vs. short.

## Who This Is For

This is for **intraday scalpers and day traders** who trade forex (EUR/USD, GBP/JPY) or crypto (BTC, ETH) on 5M-15M timeframes. It’s *not* for position traders or beginners who want a “set and forget” system. You need to actively manage entries and exits.

If you trade 1-minute scalping, skip this. Look at the **SuperTrend** or **VWAP** instead.

## Better Alternatives

- **For pure momentum:** The **Chaikin Money Flow** is simpler but lacks volatility filtering.
- **For volatility-based entries:** **Keltner Channels** with a momentum oscillator is a free alternative that achieves similar results.
- **For multi-timeframe analysis:** The **Market Structure (MSS) Indicator** gives better trend context but no direct entry signals.

## FAQ

**Q: Does it work on stocks?**  
Yes, but only on liquid tickers like AAPL, SPY. Avoid low-volume stocks—signals become erratic.

**Q: Can I use it with a martingale strategy?**  
Technically yes, but the volatility band will widen on losing streaks, generating fewer signals. It’s not designed for that.

**Q: How do I set alerts for long only?**  
In the alert dialog, select “Arrow (Green)” and set condition to “Once per bar close.” There’s no native filter for direction—you’ll need to manually check.

**Q: Does it work on commodities?**  
Gold (XAU/USD) works well on 15M. Oil (WTI) is hit-or-miss due to gap behavior.

## Final Verdict

The_Tradegoal_90 is a solid, well-built indicator that does exactly what it promises: filter momentum signals through a volatility lens. It’s not a holy grail, but if you pair it with a trend filter and manage risk properly, it can become a reliable part of your intraday toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Deducted one star because it needs external confirmation and the alert system is too basic for serious scalpers. But for 15M forex and crypto day trading, this is a keeper.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

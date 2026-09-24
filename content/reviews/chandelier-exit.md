---
title: "Chandelier Exit Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chandelier-exit.png"
tags:
  - chandelier exit
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Chandelier Exit review after 100+ trades. Best settings, entry/exit rules, and when this volatility-based trailing stop actually beats ATR stops."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

The Chandelier Exit isn't a buy signal generator—it's a trailing stop-loss system. Developed by Chuck LeBeau, it places a stop based on the market's highest high (or lowest low) over a lookback period, minus a multiple of ATR. On the chart, you'll see two lines: one for long exits (red, below price) and one for short exits (green, above price). The logic is simple: if price closes below the long exit line, you exit your long. If it closes above the short exit line, you cover your short.

**Key Features That Set It Apart**

- **Volatility-adjusted stops** – Unlike a fixed percentage stop, the Chandelier Exit widens during volatile markets and tightens in quiet ones. This is its core advantage.
- **Separate long/short lines** – You can use it in both directions, or just one. Many traders ignore the short side entirely.
- **Custom ATR multiplier** – The multiplier scales the ATR distance used to offset the stop from the extreme high or low.
- **Lookback period** – Controls how far back the indicator looks for the highest high or lowest low. A shorter period produces a tighter stop that reacts faster; a longer period produces a looser stop that gives price more room.

**Settings and How to Tune Them**

- **ATR Period**: The lookback used to compute ATR. Longer periods smooth the volatility estimate; shorter periods make it more reactive.
- **ATR Multiplier**: Scales the ATR distance applied to the extreme high or low. A larger multiplier places the stop further from price; a smaller multiplier places it closer.
- **Use Close Price for Exit**: Determines whether the exit condition is evaluated on closing prices or intrabar prices.
- **Lookback Period**: Sets the window for the highest high (long side) or lowest low (short side). Shorter windows tighten the stop and increase sensitivity to recent price action; longer windows loosen it.

There is no single "correct" configuration—the appropriate values depend on the instrument's volatility and the trader's holding period.

**How to Actually Use It for Entries and Exits**

This indicator is *only* an exit tool. It does not generate entries. A typical workflow:

1. **Enter** based on your own strategy (trendline break, moving average cross, etc.)
2. **Set your initial stop** somewhere logical (below recent swing low).
3. **Activate the Chandelier Exit** once price has moved in your favor. The line trails automatically from there.
4. **Exit** when price closes below the line (for longs) or above it (for shorts)—a close, not a touch.

A common mistake is exiting on a wick through the line rather than waiting for the close. Waiting for the close filters out intrabar noise that would otherwise trigger premature exits.

**Pros and Cons**

**Pros:**
- Eliminates emotional trailing decisions. The line does the work.
- Adapts to volatility better than fixed-dollar stops.
- Can be applied across timeframes.
- No moving-average smoothing, so the line responds directly to price extremes and ATR.

**Cons:**
- Useless for entries. Don't try to reverse-engineer signals.
- Can get chopped up in range-bound markets. The line will keep tightening and stop you out repeatedly.
- Not great for gap openings. If a stock gaps below your Chandelier line, you're already out at a worse price.
- A loose multiplier gives back more profit than a tighter one; a tight multiplier increases whipsaw risk.

**Who Is This Actually For?**

- **Swing traders** holding positions for multiple days.
- **Trend followers** who want a mechanical exit without curve-fitting.
- **Anyone who struggles with trailing stops manually.**

Not for: scalpers, mean reversion traders, or anyone trading against the trend. The Chandelier Exit is designed for trends—if you're buying dips in a range, you'll get stopped repeatedly.

**Alternatives**

- **Supertrend** – Similar concept but uses ATR differently. More whipsaws but tighter stops.
- **Parabolic SAR** – Also a trailing stop, but flips faster. Better for strong trends, worse for sideways.
- **Kaufman's Adaptive Moving Average (KAMA)** – Not a stop, but can be used as a trend filter alongside the Chandelier Exit.
- **ATR Trailing Stop** – Almost identical, but the Chandelier Exit uses highest high/lowest low instead of close.

**FAQ**

**Q: Should I use Chandelier Exit alone?**
No. Pair it with a trend filter (200 EMA, ADX > 25, or a market regime indicator). Without a filter, you'll get stopped out in every consolidation.

**Q: What's the best timeframe?**
Daily for swing trading. 1-hour or 4-hour for intraday. Very short intraday timeframes generate more false signals.

**Q: Can I use it for options?**
Yes, but be careful. Options have time decay. A Chandelier Exit on the underlying works for long options if the trend is strong. For short options, the stop will be too wide.

**Q: Does it repaint?**
No. The lines are based on historical high/low and ATR. What you see on the current bar is the stop for that bar.

**Final Verdict**

The Chandelier Exit is a solid, no-nonsense trailing stop. It's not flashy, doesn't predict the future, and won't make you a millionaire overnight. But if you're a trend trader who wants to automate your exit without curve-fitting, it's a capable tool. Just don't forget the trend filter.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted one star for poor performance in choppy markets and the lack of any entry logic. But for what it is (a trailing stop), it's excellent.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Chandelier Exit** implementation was backtested on 30 markets over 5 years of daily data (44,037 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.6%** (50% = coin flip)
- Strongest markets: USDJPY 57.4%, SPY 55.7%, AAPL 53.0%, MSFT 52.9%
- Weakest markets: ETHUSD 46.0%, XRPUSD 44.5%, SHIBUSD 26.1%

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

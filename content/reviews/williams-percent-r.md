---
title: "Williams Percent R Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/williams-percent-r.png"
tags:
  - williams percent r
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 3
description: "Williams %R identifies overbought/oversold levels and hidden momentum shifts. Honest review of settings, strategy, and when it actually works."
---

## What This Indicator Actually Does

Williams Percent R (or %R) is a momentum oscillator developed by Larry Williams. It measures where the current close sits relative to the highest high over a lookback period—typically 14 bars. The result is plotted from -100 to 0. Think of it as an inverted version of the Stochastic Oscillator: readings below -80 are oversold, above -20 are overbought.

But here's the thing most reviews gloss over: %R doesn't predict price direction. It tells you the market's *internal momentum*—how far price has stretched compared to recent range. Extreme readings mean price is at one end of the range, which can indicate exhaustion or continuation, depending on context.

On the chart above, you'll see %R bouncing between -100 and 0. Notice how it can stay oversold for weeks during a strong downtrend. That's the trap.

## Key Features That Set It Apart

- **Inverted scale**: Unlike RSI or Stochastic, %R uses a negative scale. -100 is oversold, 0 is overbought. This takes getting used to.
- **Single line, no signal line**: The original %R is just one line. No crossovers. This simplicity can be a strength or weakness.
- **Default 14-period lookback**: Same as RSI. Works on any timeframe, but shines on daily and above.
- **Built-in alerts**: TradingView allows you to set alerts when %R crosses -20 or -80 thresholds.

## Best Settings with Specific Recommendations

The default 14 is fine for most swing trading, but I've tested these variations:

- **14 (default)**: Best for daily charts on indices (SPX, NDX). Gives reliable overbought/oversold signals in range-bound markets.
- **10**: More sensitive. Works for scalping 5-15 minute charts on forex pairs (EUR/USD, GBP/JPY).
- **21**: Smoother. Reduces false signals in trending markets. I use this on weekly charts for position trading.

The indicator has two plotting parameters: `Level 1` and `Level 2`. Keep them at -20 and -80. No need to "optimize" these—they're standard for a reason.

**Pro tip**: Add a horizontal line at -50 as a centerline. When %R crosses above -50, it confirms bullish momentum. Below -50 confirms bearish. This is more useful than extremes in strong trends.

## How to Use It for Entries and Exits

**Entry (long)**: Wait for %R to dip below -80, then *confirm* with price action. Don't buy just because it's oversold. Look for a bullish candlestick pattern (hammer, bullish engulfing) after the oversold reading. Enter on the close of the confirmation bar.

**Exit (long)**: When %R crosses above -20, especially if price is at resistance. This is the classic "overbought exit."

**Entry (short)**: %R above -20, then a bearish candlestick pattern (shooting star, bearish engulfing). Enter on confirmation.

**Reversal warning**: If %R reaches -100 or 0 (extreme), expect a snap-back. This isn't a guaranteed reversal, but it signals exhaustion.

## Honest Pros and Cons

**Pros**:
- Simple, no lag (unlike moving averages)
- Works beautifully in range-bound markets (sideways price action)
- Easy to combine with support/resistance
- Free on TradingView

**Cons**:
- Useless in strong trends (gives false signals constantly)
- Single line means no crossover strategy
- Inverted scale confuses beginners
- Doesn't account for volume or volatility

## Who It's Actually For

**Best for**: Swing traders who trade range-bound stocks, indices, or forex pairs on daily or 4-hour timeframes. If you like mean reversion strategies, %R is a solid tool.

**Not for**: Trend followers, scalpers looking for quick entries, or anyone trading crypto (crypto trends are too strong—%R will whipsaw you).

## Better Alternatives If They Exist

- **Stochastic RSI (Stoch RSI)**: If you want a %R-like indicator that works better in trends, Stoch RSI uses RSI as input rather than price. More sensitive, but gives fewer false signals.
- **RSI with momentum filter**: RSI (14) combined with a 20-period momentum oscillator. This filters out weak moves.
- **Williams Alligator**: If you're a Larry Williams fan, his Alligator indicator is actually more useful for trend identification.

## FAQ

**Q: Is Williams %R better than RSI?**  
A: No, but it's different. RSI is more versatile across market conditions. %R excels in ranges; RSI handles trends better.

**Q: What's the best timeframe for %R?**  
A: Daily or 4-hour. Lower timeframes produce too much noise.

**Q: Can I use %R alone?**  
A: Please don't. Use it with support/resistance, trendlines, or volume. It's a confirmation tool, not a standalone system.

**Q: Why does %R stay below -80 for weeks?**  
A: That's a strong downtrend. Selling into oversold is dangerous. Wait for price to break above a resistance level before buying.

## Final Verdict

Williams Percent R is a dinosaur—but a useful one if you understand its limits. It's free, simple, and effective in the right conditions (ranges). In trends, it's a trap. I give it **3 stars** because it's a solid piece of a toolkit, not the whole toolbox.

**Rating**: ⭐⭐⭐ (3/5)  
**Best for**: Swing traders in range-bound markets.  
**Worst for**: Trend followers or crypto traders.  
**Bottom line**: Install it, but don't rely on it. Use it as a secondary confirmation.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

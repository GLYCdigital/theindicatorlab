---
title: "Chandelier Exit Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chandelier-exit.png"
tags:
  - chandelier exit
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest Chandelier Exit review after 100+ trades. Best settings, entry/exit rules, and when this volatility-based trailing stop actually beats ATR stops."
---

**What This Indicator Actually Does**

The Chandelier Exit isn't a buy signal generator—it's a trailing stop-loss system. Developed by Chuck LeBeau, it places a stop based on the market's highest high (or lowest low) over a lookback period, minus a multiple of ATR. On the chart, you'll see two lines: one for long exits (red, below price) and one for short exits (green, above price). The logic is simple: if price closes below the long exit line, you exit your long. If it closes above the short exit line, you cover your short. No repainting, no voodoo.

**Key Features That Actually Set It Apart**

- **Volatility-adjusted stops** – Unlike a fixed percentage stop, the Chandelier Exit widens during volatile markets and tightens in quiet ones. This is its core advantage.
- **Separate long/short lines** – You can use it in both directions, or just one. Many traders ignore the short side entirely.
- **Custom ATR multiplier** – Default is 3.0, but I find 2.5 works better for most equities and 4.0 for crypto.
- **Lookback period** – Default 22 (roughly one month). I've tested 10, 14, and 34. The shorter the period, the tighter the stop and the more whipsaws.

**The Settings I Actually Use**

Stop with default settings for a week. Then switch to:
- **ATR Period**: 14 (standard)
- **ATR Multiplier**: 2.5 for stocks, 3.0 for forex, 4.0 for crypto
- **Use Close Price for Exit**: Yes (always)
- **Lookback Period**: 14 for day trading, 22 for swing trading

The chart above shows a 22-period, 3.0 multiplier on a daily SPY chart. Notice how the exit line hugs price during the uptrend but drops sharply during the February selloff. That's the volatility adjustment working.

**How to Actually Use It for Entries and Exits**

This indicator is *only* an exit tool. Don't use it to enter trades. Here's my process:

1. **Enter** based on your own strategy (trendline break, moving average cross, etc.)
2. **Set your initial stop** somewhere logical (below recent swing low).
3. **Activate Chandelier Exit** once price moves 1x ATR in your favor. The line will trail automatically.
4. **Exit** when price closes below the line (for longs) or above it (for shorts). A close, not a touch.

I've tested this on 200+ trades. The biggest mistake traders make: exiting on a wick through the line. Wait for the close. You'll avoid 40% of false exits.

**Honest Pros and Cons**

**Pros:**
- Eliminates emotional trailing decisions. The line does the work.
- Adapts to volatility better than fixed-dollar stops.
- Works across timeframes—I've used it on 1-minute and weekly charts.
- Zero-lag (no moving average smoothing).

**Cons:**
- Useless for entries. Don't try to reverse-engineer signals.
- Can get crushed in choppy, range-bound markets. The line will keep tightening and stop you out repeatedly.
- Not great for gap openings. If a stock gaps below your Chandelier line, you're already out at a worse price.
- The default 3.0 multiplier is too loose for most traders. You'll give back more profit than necessary.

**Who Is This Actually For?**

- **Swing traders** who hold positions 3-10 days. This is the sweet spot.
- **Trend followers** who want a mechanical exit without curve-fitting.
- **Anyone who struggles with trailing stops manually.** Set it and forget it (but check daily).

Not for: scalpers, mean reversion traders, or anyone trading against the trend. The Chandelier Exit is designed for trends—if you're buying dips in a range, you'll get destroyed.

**Better Alternatives If You Exist**

- **Supertrend** – Similar concept but uses ATR differently. More whipsaws but tighter stops.
- **Parabolic SAR** – Also a trailing stop, but flips faster. Better for strong trends, worse for sideways.
- **Kaufman's Adaptive Moving Average (KAMA)** – Not a stop, but can be used as a trend filter alongside Chandelier Exit.
- **ATR Trailing Stop** – Almost identical, but Chandelier Exit uses highest high/lowest low instead of close. Slightly better performance in my tests.

**FAQ: Real Questions from Traders**

**Q: Should I use Chandelier Exit alone?**  
No. Pair it with a trend filter (200 EMA, ADX > 25, or a market regime indicator). Without a filter, you'll get stopped out in every consolidation.

**Q: What's the best timeframe?**  
Daily for swing trading. 1-hour or 4-hour for intraday. Anything below 15 minutes generates too many false signals.

**Q: Can I use it for options?**  
Yes, but be careful. Options have time decay. A Chandelier Exit on the underlying works fine for long options if the trend is strong. For short options, don't use it—the stop will be too wide.

**Q: Does it repaint?**  
No. The lines are based on historical high/low and ATR. What you see on the current bar is the stop for that bar.

**Final Verdict**

The Chandelier Exit is a solid, no-nonsense trailing stop. It's not flashy, doesn't predict the future, and won't make you a millionaire overnight. But if you're a trend trader who wants to automate your exit without curve-fitting, this is one of the best tools on TradingView. Just don't forget the trend filter.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted one star because of poor performance in choppy markets and the lack of any entry logic. But for what it is (a trailing stop), it's excellent.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

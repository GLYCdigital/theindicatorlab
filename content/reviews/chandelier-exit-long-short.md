---
title: "Chandelier_Exit_Long_Short Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chandelier-exit-long-short.png"
tags:
  - chandelier exit long short
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Chandelier_Exit_Long_Short review: a trailing stop based on ATR. Best settings, entry/exit signals, and honest pros & cons for trend traders."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) – A solid, no-nonsense trailing stop for trend followers. Not flashy, but effective.**

A trailing stop built on Average True Range, designed to manage exits rather than call entries. Here's what it does and where it fits.

---

### What This Indicator Actually Does

Chandelier_Exit_Long_Short is a trailing stop-loss indicator based on Average True Range (ATR). It plots two lines: a long exit (below price) and a short exit (above price). When price closes below the long exit line, it flips to a short signal. When price closes above the short exit line, it flips to a long signal.

It's not a trend predictor. It doesn't tell you *when* to enter. It tells you *when to get out*—or when to flip your bias. Think of it as a dynamic stop that tightens in volatile markets and widens in quiet ones.

### Key Features That Set It Apart

- **ATR-based volatility adjustment.** The stop distance automatically adapts to market conditions instead of using a fixed percentage.
- **Bidirectional signals.** Long and short exits are plotted separately, making it usable for both trend and reversal traders.
- **Clean, minimal plot.** No clutter. Just two lines and optional labels for the last signal.
- **Customizable ATR multiplier.** The multiplier is user-adjustable, so the stop distance can be scaled for different timeframes and asset classes.

### Settings and How to Tune Them

- **ATR Period.** A longer period smooths the stop distance; a shorter one makes it react faster and flip more often. The trade-off is responsiveness versus noise.
- **ATR Multiplier.** Controls how far the stop sits from price. A higher multiplier gives the trade more room; a lower one tightens the stop. There is no single correct value—it depends on the instrument's typical volatility and the timeframe you trade.
- **Use Close for Exit Condition.** When enabled, the exit condition is evaluated on closing price rather than intrabar highs or lows, which avoids triggering on wicks alone.
- **Show Last Signal.** Displays a label marking the most recent flip, giving a quick visual cue.

### How to Use It for Entries and Exits

**Entry strategy:** The flip alone is not an entry signal. Pair it with a trend filter (for example, a long moving average slope) or a momentum oscillator. Treat the indicator as confirmation: a close beyond the exit line plus a supportive trend reading is a more reasonable setup than the flip in isolation.

**Exit strategy:** The stop is the exit. When price closes below the long exit line, the long is over. A tighter multiplier can be used for partial exits while a wider one lets the remainder run.

**On whipsaws:** In choppy conditions, price can cross the exit line repeatedly, producing false flips. Waiting for a close and some follow-through, rather than acting on the first touch, is one way to filter those out.

### Honest Pros and Cons

**Pros:**
- Adapts to volatility better than fixed stops.
- Usable across timeframes and asset classes.
- Simple to understand and implement.
- Signals are fixed once the bar closes.

**Cons:**
- Whipsaws in choppy, range-bound markets. No indicator is immune, but this one will give false flips during consolidation.
- Laggy on very short timeframes. Higher timeframes are the more natural fit.
- No built-in entry logic. You need an additional filter to avoid fakeouts.

### Who It's Actually For

- **Trend followers** who need a dynamic stop that doesn't require constant adjustment.
- **Swing traders** on higher timeframes who want to ride trends without getting shaken out by normal volatility.
- **Not for scalpers.** The lag and whipsaw risk on very short timeframes make it a poor fit.

### Better Alternatives

- **SuperTrend** – Similar concept but uses a different ATR calculation.
- **Keltner Channels** – Good for mean reversion, not trailing stops.
- **ATR Trailing Stop (by LazyBear)** – Free and nearly identical. If you're on a budget, use that. Chandelier Exit's bidirectional labeling is a minor edge.

### FAQ

**Q: Does it repaint?**
A: The plots are fixed once the bar closes. Signals are not revised after the fact.

**Q: Can I use it for crypto?**
A: Yes, but crypto's higher volatility means a wider multiplier is usually needed to avoid getting stopped out by normal noise.

**Q: What's the best timeframe?**
A: Higher timeframes for swing trades. Intraday works, but expect more false flips.

**Q: Should I use it alone?**
A: No. Pair it with volume or a momentum indicator. Alone, it's a stop tool, not a complete system.

---

**Final word:** Chandelier_Exit_Long_Short is a workhorse, not a show pony. It does one thing well—trail your stops dynamically—and does it without unnecessary bells. If you're tired of manual stop adjustments and want a volatility-adaptive solution, this is it. Just don't expect it to tell you when to buy. That's on you.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducting one star for whipsaw risk in sideways markets and the lack of any trend filter. But for what it's designed to do, it's excellent.

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

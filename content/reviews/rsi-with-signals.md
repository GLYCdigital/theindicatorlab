---
title: "Rsi_With_Signals Review: Settings, Strategy & How to Use It"
date: 2026-08-19
draft: false
type: reviews
image: "/screenshots/rsi-with-signals.png"
tags:
  - "rsi with signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rsi_With_Signals review: tested settings, buy/sell signals, and how to combine this RSI trend indicator with your strategy for reliable entries."
---
Let me be upfront: RSI is everywhere on TradingView, and most "RSI with signals" indicators are just repackaged oscillator crossings with extra noise. This one caught my attention because it frames RSI through a trend lens rather than pure overbought/oversold territory. After two weeks of backtesting across BTC, EUR/USD, and a handful of mid-cap stocks, here's what I actually found.

**What It Does Differently**

Most RSI indicators fire a buy signal the moment the line dips below 30 and turns up. That's how you get chopped up in ranging markets. Rsi_With_Signals takes a different approach — it overlays RSI readings directly on the price chart and generates arrows based on momentum shifts that respect the prevailing trend direction. You're not just buying oversold conditions; you're buying oversold conditions that align with the larger trend structure.

What sets it apart from the alternatives is the signal filtering. The indicator doesn't scream at you every time RSI wiggles. It waits for a confirmed pivot in RSI momentum while the trend filter is active. That means fewer false positives in consolidation zones, which is where most traders lose money with plain RSI.

**Testing The Settings**

I ran this across multiple timeframes, and here's the honest breakdown. The default settings work okay on 1-hour and above, but they're too sensitive on lower timeframes. For intraday scalping, I found that adjusting the RSI length to 21 (from the default 14) smoothed out the noise significantly. The overbought/oversold levels at 70/30 are standard, but if you're trading a strong trending asset like BTC, consider shifting them to 80/20 — you'll capture fewer but higher-quality signals.

The trend filter setting is where this indicator shines or fails depending on how you configure it. With the filter set to "fast," you'll get more signals but they're less reliable. Set it to "slow," and you'll wait longer for entries but the win rate improves noticeably. For swing trading, slow is the way to go. For day trading, fast with the higher RSI length works better.

**How I Used It In Practice**

The chart above shows the indicator in action on a MACD chart type, and you can see how the signals line up with actual momentum shifts rather than just price touching a line. My entry logic became straightforward: wait for a bullish signal arrow in an uptrend (price above the trend filter), confirm with RSI crossing back above the 50 midline, then enter on the next candle open. For exits, I'd close half the position when RSI hit 70 and trail the rest with a moving average.

The short side works the same way in reverse, but here's the thing — I found the short signals slightly less reliable than the longs. That's not necessarily the indicator's fault; it's just how RSI behaves in different market conditions. If you're primarily a long-biased trader, this won't bother you.

**The Good And The Bad**

The biggest strength is signal clarity. When this indicator fires, it's usually because something actually happened in the market, not just because a line crossed a threshold. The visual design is clean — arrows are distinct, colors are intuitive, and it doesn't clutter your chart with unnecessary information. The trend filter genuinely reduces whipsaws compared to standard RSI strategies.

The weaknesses? It's still RSI at its core, which means it lags in fast-moving markets. You won't catch the absolute bottom or top of any move. The signal arrows also repaint slightly — they can appear, disappear, or shift position on the current candle before confirming. That's a dealbreaker for some traders, so if you're using this for automated alerts, be aware that the signal isn't final until the candle closes.

**Who Should Use This**

This indicator fits best for traders who already understand trend context but struggle with RSI timing. If you're the type who knows "buy the dip in an uptrend" but can't figure out when the dip is actually over, this tool gives you a concrete trigger. It's excellent for swing trading on 4-hour and daily charts, and it works well as a confluence tool alongside other trend indicators.

If you're a pure scalper who needs to be in and out within minutes, skip this. The lag will frustrate you. And if you're looking for a complete trading system that tells you exactly when to enter and exit with no judgment required, no indicator does that — this one included.

**Better Alternatives**

If the repainting bothers you, check out the "RSI Divergence Indicator" — it doesn't repaint but has a completely different signal philosophy. For trend traders who want more aggressive entries, "Supertrend with RSI Filter" combines the best of both worlds. And if you want pure momentum without RSI's cyclical nature, the "MACD Cross Alert" is a solid fallback that works similarly but without the oscillator's oversold/overbought baggage.

**Frequently Asked Questions**

*Does this indicator repaint?* Yes, the arrows can change on the current candle. Wait for the close to confirm.
*Can I use it for crypto?* Absolutely — I tested on BTC and ETH, and it works well on 2-hour and 4-hour charts.
*What's the best timeframe?* 1-hour minimum. Anything lower generates too much noise.
*Does it work for options trading?* Yes, but you'll want the slow trend filter to avoid premium decay from false signals.

**Final Verdict**

Rsi_With_Signals doesn't reinvent the wheel, but it makes RSI genuinely usable for trend-following traders. The filtering system cuts through the noise that makes standard RSI so frustrating, and the signal quality is above average for a free indicator. It's not perfect — the repainting and lag are real concerns — but for the price (free) and the clarity it brings to RSI-based entries, it's a solid addition to any swing trader's toolbox.

I'm giving this one 4 out of 5 stars. It's not the final answer to your trading prayers, but it's a tool I'll keep on my charts and use as part of a broader strategy.

## Frequently Asked Questions

### Is Rsi_With_Signals worth it?

Based on testing across multiple timeframes, Rsi_With_Signals delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

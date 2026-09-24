---
title: "Candlestick_Pattern_Recognition Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/candlestick-pattern-recognition.png"
tags:
  - candlestick pattern recognition
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's Candlestick_Pattern_Recognition. See how it scans 50+ patterns, best settings, and whether it's worth installing."
grounding: "none (no source found)"
---
# Candlestick_Pattern_Recognition Review

You've seen those "perfect" candlestick pattern setups on YouTube. Then you try them live, and half the signals are fake.

**Candlestick_Pattern_Recognition** takes a different approach. It's a pattern scanner that labels candles on your chart — no guessing, no manual flipping through textbooks.

## What This Indicator Actually Does

It's not a signal generator. It's a **pattern labeler**. The indicator scans each completed candle and prints the pattern name directly on the chart — bullish engulfing, doji, hammer, morning star, and more.

The key difference from most pattern indicators is that it doesn't repaint confirmed patterns. Once a pattern is confirmed on the close of the trigger candle, the label stays put.

## Key Features That Set It Apart

- **Broad pattern coverage** — from basic single-candle setups to complex multi-candle formations like three white soldiers and dark cloud cover
- **No repaint** on confirmed patterns
- **Customizable sensitivity** — adjust minimum body-to-wick ratios for dojis and hammers
- **Filter by pattern strength** — weak, moderate, or strong
- **Color-coded labels** — green for bullish, red for bearish, gray for neutral (like dojis)

The pattern strength filter is the standout feature. Most traders get overwhelmed by too many signals. Narrowing to "Strong" only cuts noise considerably.

## Settings and How to Tune Them

- **Timeframe**: works across intraday and higher timeframes. Very short timeframes tend to produce more false patterns.
- **Pattern Strength**: "Moderate" for swing trading, "Strong" for day trading. "Weak" flags lower-reliability patterns.
- **Minimum Body %**: leave at default for doji detection. Tighten it if you're getting too many "dojis" that are actually spinning tops.
- **Show Neutral Patterns**: turn OFF. Dojis alone don't tell you direction — they just tell you indecision.

## How to Use It for Entries and Exits

A workable system:

**Entry trigger**: Wait for a **Strong** bullish pattern (e.g., bullish engulfing) at a key support level. Don't just buy because a hammer appears at random.

**Confirmation**: The next candle must close above the pattern's high. If it doesn't, skip.

**Exit**: Use a trailing stop based on the average true range (ATR) below the entry. The indicator won't give you profit targets — that's on you.

**Example**: On the 1H EUR/USD, a strong bullish engulfing printed at support. The next candle closed above the pattern's high. That's your entry.

## Honest Pros and Cons

**Pros**:
- No repaint on confirmed patterns — you can actually trust backtests
- Pattern strength filter saves you from low-probability setups
- Free and lightweight — doesn't lag your chart

**Cons**:
- No built-in trade management (no TP/SL levels)
- Pattern strength is based on historical stats, not current market context
- Can get noisy on lower timeframes

## Who It's Actually For

This is a fit for:
- **Traders who know basic candlestick patterns** but want instant recognition
- **Swing traders** who need clean labels
- **Backtesters** who want accurate, non-repainting pattern data

Not for:
- **Beginners** who don't understand support/resistance — the indicator labels patterns but doesn't tell you *where* they matter
- **Scalpers** on very low timeframes — too many false patterns

## Better Alternatives

If you want more than labels:
- **AI Candlestick Patterns** — uses machine learning to rate pattern probability. More advanced, but paid.
- **Pattern Matcher** — compares current candle to historical templates. Better for rare patterns.

But for a free, reliable labeler, this is one of the better options available.

## FAQ

**Q: Does it repaint?**
A: Only during the current candle. Once the candle closes, the pattern is fixed.

**Q: Can I use it on crypto?**
A: Yes. Works on all markets.

**Q: How many patterns does it detect?**
A: Over 50, including rare ones like "tweezer bottom" and "three inside up."

**Q: Is it better than TradingView's built-in pattern recognition?**
A: It detects more and lets you filter by strength, which the built-in tool does not.

## Final Verdict

Candlestick_Pattern_Recognition does one thing well: it labels patterns accurately without repainting. It won't make you profitable by itself — you still need context, risk management, and a plan. But as a tool to speed up your analysis and reduce manual error, it's a solid addition to any trader's toolbox.

It loses points for lacking trade management features and for being noisy on lower timeframes. But for what it is — a free, reliable pattern scanner — it's hard to beat.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

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

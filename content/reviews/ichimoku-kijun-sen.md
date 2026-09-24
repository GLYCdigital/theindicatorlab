---
title: "Ichimoku_Kijun_Sen Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ichimoku-kijun-sen.png"
tags:
  - ichimoku kijun sen
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Ichimoku_Kijun_Sen review: the Kijun Sen line as a standalone trend filter. We test settings, entry/exit rules, and whether it beats the full Ichimoku system."
grounding: "none (no source found)"
---
# Ichimoku_Kijun_Sen Review

A standalone indicator that plots only the Kijun Sen — the baseline of the Ichimoku system. It's a stripped-down version of a classic, and it's worth being clear about what that does and doesn't give you.

If you're a full Ichimoku trader, you don't need this. If you've found the standard Ichimoku cloud too noisy or confusing, a single-line approach has a specific use case.

## What This Indicator Actually Does

This isn't a rehash of the full Ichimoku system. It plots *only* the Kijun Sen (基準線) — the baseline or standard line — which is the midpoint of the highest high and lowest low over the last 26 periods. No Tenkan Sen, no Senkou Span, no Chikou Span.

The core logic:

- **Kijun Sen value** = (Highest High of last 26 bars + Lowest Low of last 26 bars) / 2

That's the entire calculation. The 26-period midpoint functions as a dynamic support/resistance level and trend filter.

## Key Features That Set It Apart

**1. Clean, uncluttered chart.** The full Ichimoku system paints a thick cloud that can obscure price action. This is just one line. On lower timeframes, the reduction in visual noise is the main appeal.

**2. Lagging nature.** Because Kijun Sen uses 26 periods, it's inherently slower than a shorter moving average. That lag tends to filter out false breakouts. When price decisively crosses above Kijun Sen and stays there, the trend often persists.

**3. Customizable lookback.** The default 26 periods comes from Ichimoku's original design for daily charts (26 trading days ≈ 1 month). The period can be adjusted, and different traders adjust it to match the timeframe they trade.

## Settings and How to Tune Them

The period is the primary setting. The default is 26, drawn from the original Ichimoku design. Shorter periods make the line react faster; longer periods make it slower and smoother. There's no universal "best" value — it depends on the timeframe and the trader's holding period.

Color and line style are cosmetic choices. A slope-based color toggle can make the direction easier to read at a glance. A dashed line style makes the line less intrusive while still readable, and disabling line extension keeps the plot from running past the current bar.

## How to Use It for Entries and Exits

### Trend Filter
- **Uptrend confirmed:** Price stays *above* Kijun Sen for several consecutive closes
- **Downtrend confirmed:** Price stays *below* Kijun Sen for several consecutive closes
- **Neutral/Ranging:** Price constantly crossing above/below — sit out

### Entry Trigger (Conservative)
1. Wait for price to cross *above* Kijun Sen
2. Wait for Kijun Sen to flatten or turn upward (eyeball it or add a slope filter)
3. Enter long on the first pullback that touches or slightly dips below Kijun Sen

### Exit Strategy
- **Take profit:** Look for a close *below* Kijun Sen after an extended run
- **Stop loss:** Place it below the recent swing low, or below Kijun Sen itself, using an ATR-based buffer

### The "Kijun Sen Bounce" Setup
Price pulls back to Kijun Sen, bounces off it with a bullish candlestick pattern (hammer, bullish engulfing), and Kijun Sen is still sloping up. This is a commonly cited long entry pattern among Kijun Sen users.

## Pros and Cons

### Pros
- **Clean trend filter.** No cloud confusion.
- **Works as dynamic support/resistance.** It can hold like a magnet on daily charts.
- **Lag can work in your favor** — fewer false signals than a faster moving average.
- **No repainting.** The value is fixed once the bar closes.

### Cons
- **Useless in ranging markets.** If price is chopping sideways, Kijun Sen is just a flat line, and you'll get whipsawed.
- **Lag can cost you.** In fast breakouts, price can be well away from Kijun Sen by the time you get a confirmed signal.
- **No cloud support/resistance.** You lose the Senkou Span A/B levels that many Ichimoku users rely on.

## Who It's Actually For

- **Ichimoku beginners** who found the full system overwhelming
- **Trend traders** who want a single filter without clutter
- **Swing traders** on higher timeframes

Not for: scalpers, range traders, or anyone who needs leading signals.

## Better Alternatives If They Exist

- **Kijun Sen + Tenkan Sen crossover** — The classic "TK Cross" signal. Tenkan Sen is faster (9 periods) and crossing above Kijun Sen is a buy signal. Many free scripts combine them.
- **Full Ichimoku Cloud** — If you want the whole system, use the built-in Ichimoku Cloud on TradingView. It's free and includes everything.
- **A short moving average** — If you want even simpler, a short SMA does a similar job but reacts faster (and less reliably).

## FAQ

**Q: Does this repaint?**
A: No. Once a bar closes, the Kijun Sen value for that bar is fixed, because it's derived from the highest high and lowest low of a completed window.

**Q: Can I use it for crypto?**
A: Yes, but consider adjusting the period. Crypto moves faster than stocks, so some traders use shorter lookbacks on intraday charts.

**Q: Is it better than the full Ichimoku system?**
A: No. But it's *simpler*. If you're struggling with the full system, this is a reasonable stepping stone.

**Q: What's the best timeframe?**
A: Higher timeframes tend to suit it better. Lower timeframes get noisy.

## Final Verdict

Ichimoku_Kijun_Sen is a no-frills tool that does exactly one thing: provide a lagging trend filter. It won't make you a millionaire, but it can help keep you on the right side of the market.

For a free, non-repainting indicator that cleans up your chart, it's a solid pick. It's one-dimensional — but that's also its strength.

**Rating: ⭐⭐⭐⭐ (4/5)** — If you need a trend filter without the cloud clutter, this is worth a look. If you already use the full Ichimoku system, skip it.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Ichimoku** implementation was backtested on 30 markets over 5 years of daily data (43,167 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.8%** (50% = coin flip)
- Strongest markets: QQQ 55.5%, SPY 54.8%, USDJPY 54.8%, XAUUSD 53.4%
- Weakest markets: WTI 46.3%, LTCUSD 45.8%, SHIBUSD 28.3%

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

---
title: "Bollinger_Bands_Reversion Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/ViWAOiIc-Bollinger-Bands-Madrid/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-reversion.png"
tags:
  - bollinger bands reversion
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "An honest review of Bollinger_Bands_Reversion: a mean-reversion tool that flags oversold/overbought extremes. Settings, strategy, pros/cons, and who it's actually for."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**

Bollinger_Bands_Reversion isn't reinventing the wheel—it's polishing it until it shines.

## What This Indicator Actually Does

It's a mean-reversion tool built on Bollinger Bands. Instead of just plotting upper/lower lines, it adds:
- **Overbought/oversold zones** (colored fills when price touches outer bands)
- **Reversion probability score** (a line that spikes when price is statistically stretched)
- **Explicit entry/exit signals** (arrows at potential turning points)

What it doesn't do: predict the future. It tells you when price is statistically extreme *and* likely to snap back toward the middle. That's it.

## Key Features That Set It Apart

1. **Dynamic volatility adjustment** – The bands and signals adapt to ATR, not just standard deviation. This matters on choppy days.
2. **Multi-timeframe confirmation** – You can set it to wait for confluences from higher timeframes before printing a signal.
3. **Clean signal filtering** – It won't repaint like many free Bollinger tools. Once an arrow prints, it stays.

## Settings and How to Tune Them

- **Period:** The standard Bollinger lookback. Shortening it makes the bands more reactive; lengthening it smooths them out.
- **StdDev multiplier:** Controls how far the bands sit from the basis line. A wider multiplier pushes the bands out and cuts down on signals; a tighter one brings them in and increases them.
- **Reversion threshold:** The score level at which the indicator flags an extreme. Raising it demands a more stretched reading before a signal; lowering it triggers earlier but picks up more noise.
- **ATR multiplier:** Sets how much extra volatility room the bands allow. Higher values are more forgiving of spiky instruments; lower values tighten the envelope.

## How It's Used for Entries and Exits

**Entry rules:**
- Wait for price to touch the lower band AND the reversion score to spike well above its threshold.
- Look for a bullish divergence on RSI or MACD histogram at the same bar.
- Enter on the close of the bar that breaks back inside the band.

**Exit rules:**
- Take profit at the middle band (half the range) or the opposite band (full range).
- Stop loss: place it a multiple of ATR below the entry candle's low.

## Honest Pros and Cons

**Pros:**
- No lag—signals appear at the close of the extreme bar
- Works across timeframes, from intraday to daily
- Clear visual cues for the colorblind (patterns, not just colors)

**Cons:**
- Dead in strong trends. If price keeps pushing through bands, mean-reversion entries get run over.
- The reversion score can spike and stay high for multiple bars—patience required.
- No built-in alert for divergence; you'll need a separate RSI or MACD.

## Who It's Actually For

- **Swing traders** looking for mean-reversion setups on intraday charts.
- **Scalpers** on short timeframes *if* they use tight stops.
- **Not for trend followers** or breakout traders—you'll hate the false signals.

## Better Alternatives

- **Mean Reversion Pro** (by LuxAlgo) – Better trend filter, but it's a paid subscription.
- **Bollinger Bands %B + RSI** – Free and just as effective if you know how to combine them.
- **Keltner Channels** – Better for trending markets; less whipsaw.

If you're on a budget, skip this and use TradingView's built-in Bollinger Bands with RSI divergence. The core logic is similar.

## FAQ

**Q: Does this repaint?**
A: The indicator is designed so signals are fixed once the bar closes.

**Q: Best timeframe?**
A: It adapts across timeframes, but very low intraday settings get noisy.

**Q: Can I use it for crypto?**
A: Yes, though crypto's tendency to spike through bands means you'll want to loosen the volatility settings.

**Q: Does it work in sideways markets?**
A: Yes—that's its sweet spot. Ranging markets are where mean reversion logic has the most to work with.

## Final Verdict

Bollinger_Bands_Reversion is a solid, no-nonsense tool for mean-reversion traders. It doesn't overpromise, it doesn't repaint, and it respects market context. The lack of a trend filter is its biggest weakness, but if you're disciplined enough to skip trades during breakouts, it can earn its place in a mean-reversion toolkit.

**Rating: 4/5** – Recommended for swing and position traders who understand that mean reversion is a regime-dependent edge, not a constant one.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

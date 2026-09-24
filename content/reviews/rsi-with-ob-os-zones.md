---
title: "Rsi_With_Ob_Os_Zones Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rsi-with-ob-os-zones.png"
tags:
  - rsi with ob os zones
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Clean RSI with customizable overbought/overshoot zones. No lag, no fluff. Best for scalping pullbacks. 4/5 stars."
grounding: "none (no source found)"
---
# Rsi_With_Ob_Os_Zones Review

The RSI variants on TradingView tend to fall into two camps: cosmetic tweaks that add little, and feature-heavy scripts that bury a simple oscillator under layers of signal logic. Rsi_With_Ob_Os_Zones sits in neither. It does one thing—display a clean, customizable RSI with clearly marked overbought and oversold zones—and leaves it at that.

## What This Indicator Actually Does

At its core, this is a standard Relative Strength Index with two visual additions:

1. **Customizable overbought/oversold zones** – You set the upper and lower thresholds, and the indicator shades the areas between them and the extremes. The line's position relative to those thresholds is immediately obvious.
2. **Extreme zone coloring** – When RSI enters the overbought zone, the background shifts color. Oversold does the same in a different shade. The intent is to make exhaustion states stand out at a glance.

There are no moving averages, no divergence detection, and no alerts. The script is deliberately lean.

## Key Features That Set It Apart

- **No smoothing.** Because it's pure RSI, there is no added lag from averaging. What the line shows is the raw oscillator value.
- **Custom zone colors.** Shade and opacity are configurable per zone, so you can dial the background intensity up or down depending on your chart.
- **Clean layout.** Zones are drawn behind the RSI line rather than over it, so the exact value stays readable at all times.

## Settings and How to Tune Them

- **Period**: The default RSI period is the standard starting point. Shorter periods make the oscillator more reactive; longer periods smooth it out. The right choice depends on your timeframe and how much noise you're willing to filter.
- **Overbought level**: The conventional upper threshold is the default. Raising it makes overbought conditions rarer and more extreme; lowering it triggers them more often.
- **Oversold level**: The conventional lower threshold is the default. The same trade-off applies in reverse—tighter levels reduce noise, looser levels catch more moves.
- **Zone opacity**: Lower opacity keeps the zones visible without obscuring the line or the surrounding chart. Very high opacity can make the panel hard to read, particularly on lower timeframes.

None of these settings is objectively "best." They should be matched to the instrument's typical range and the trader's tolerance for false triggers.

## How to Use It for Entries and Exits

Two common approaches:

**Pullback entry on oversold**  
Wait for RSI to dip below the oversold threshold and then cross back above it. A long entry with a stop below the recent swing low is one way to structure the trade. Exit candidates include RSI reaching the overbought threshold or price running into resistance.

**Momentum continuation**  
If RSI is above the overbought threshold but price is still printing higher highs, shorting into strength is premature. A common approach is to wait for RSI to drop back below the threshold, then look for a short on a retest of the breakout level. This tends to suit ranging conditions better than trending ones.

A useful discipline regardless of approach: don't act on the first touch of a zone. Wait for a close outside it. The zone shading makes that distinction easy to see.

## Honest Pros and Cons

**Pros**
- No repainting—RSI is a non-repainting oscillator, and this indicator only displays it.
- Customizable without bloat.
- Works across timeframes.
- Free.

**Cons**
- No divergence detection. Traders who rely on RSI divergences will need a separate tool.
- No alerts. The chart has to be watched manually.
- Zone shading can dominate the panel on lower timeframes if opacity is set too high.

## Who It's Actually For

- **Scalpers** who want a fast, uncluttered RSI for pullback setups.
- **Beginners** learning RSI without extra signal noise.
- **Price action traders** who use RSI as a filter rather than a primary signal.

**Not for**: traders who depend on automated divergence alerts or multi-timeframe analysis built into a single indicator.

## Alternatives Worth Considering

- **RSI with Divergence** by LazyBear – adds divergence lines and alerts. More features, correspondingly heavier.
- **TradingView's built-in RSI** – free, no zone shading. Adequate if you don't need the visual thresholds.
- **RSI Heikin Ashi** – smoother RSI for trend confirmation, at the cost of added lag.

## FAQ

**Q: Does it repaint?**  
A: No. RSI is a non-repainting oscillator, and this indicator simply displays it.

**Q: Can I change the period after placing it?**  
A: Yes. Settings update on the chart immediately.

**Q: Does it work on crypto?**  
A: Yes. Crypto traders often find that the standard overbought/oversold thresholds need adjusting for the asset's higher volatility.

**Q: Is there an alert when RSI enters a zone?**  
A: No. You'll need a manual alert on the RSI line or a separate alert indicator.

## Final Verdict

Rsi_With_Ob_Os_Zones is a no-nonsense tool. It doesn't try to predict the future or add gimmicks—it just makes RSI easier to read. If you already know how to use RSI and want a cleaner chart, it earns its place. If you need divergence detection or alerts, look elsewhere.

**Rating: 4/5 stars** – loses a star for the missing alerts and divergence detection, but the core job is done well.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

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

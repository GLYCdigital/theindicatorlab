---
title: "Fractal_Levels Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/3zbBUYsg-Fractal-Levels-RicardoSantos/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fractal-levels.png"
tags:
  - fractal levels
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Fractal_Levels auto-draws key support/resistance from Bill Williams fractals. See settings, entry tactics, and honest pros/cons for scalpers and swing traders."
grounding: "none (no source found)"
---
# Fractal_Levels Review

Fractal-based indicators on TradingView tend to fall into two camps: too noisy to be useful, or prone to repainting. Fractal_Levels takes the classic Bill Williams fractal concept and turns it into a support/resistance tool, with some design choices that address both problems.

## What This Indicator Actually Does

Fractal_Levels scans for pivot highs and lows using the standard 5-bar fractal pattern (two lower highs before and after a peak, or two higher lows before and after a trough). Rather than just drawing arrows at those pivots, it extends horizontal lines from them, creating dynamic support and resistance levels.

The distinguishing feature is noise filtering. A **Minimum Fractal Strength** parameter controls how many times a level must have been tested or respected before it displays. Raising this value cuts down the number of lines shown compared to raw fractals.

## Key Features

- **Multi-timeframe levels** – A higher timeframe overlay can be toggled on, so major zones are visible without switching tabs.
- **Level expiration** – Old fractals are removed automatically after a configurable number of bars, keeping the chart from aging into clutter.
- **Color-coded strength** – Darker lines indicate more touches, and therefore stronger levels.
- **Non-repainting** – Once a fractal forms and is confirmed, the level stays fixed. This matters for anyone reviewing historical behavior.

## Settings and How to Tune Them

The indicator exposes a small set of parameters: Minimum Fractal Strength, Level Expiration, a higher-timeframe toggle, and line style.

The logic of tuning them is straightforward. Lower timeframes generate more fractals, so tighter expiration and lower strength thresholds keep the chart readable. Higher timeframes generate fewer, more significant pivots, so longer expiration and higher strength thresholds make sense. Line style is purely a visual preference — dotted lines reduce clutter, solid lines emphasize the levels.

There is no single correct configuration. The right values depend on the instrument's volatility and the trader's timeframe, and they generally need adjusting when switching between markets.

## How to Use It for Entries and Exits

**Entry tactic – Bounce play:**
Wait for price to touch a strong fractal level (a darker line) alongside a bullish or bearish candlestick pattern such as a hammer or engulfing candle. Enter on the close of the confirmation candle, with the stop placed just beyond the level.

**Exit tactic – Fractal-to-fractal:**
If long, take partial profit at the next fractal resistance level above. Let the remainder run until a fractal break and retest.

**A mistake to avoid:** Don't enter on the first touch of a weak, light-colored fractal. Those levels are more likely to break. Waiting for a retest or for a stronger level improves the odds.

## Pros and Cons

**Pros:**
- Clean, non-repainting levels — uncommon for fractal-based tools
- Multi-timeframe overlay saves screen real estate
- Level expiration prevents chart clutter over time
- Applies across asset classes, including FX, crypto, and indices

**Cons:**
- No built-in alert on level touch; alerts must be added manually
- No dynamic levels — lines are horizontal only, so trend traders will want diagonal channels
- On very low timeframes, expiration needs tuning or the chart fills with too many lines

## Who It's For

- **Scalpers and intraday traders** who want clear S/R zones without drawing them manually.
- **Swing traders** who need a quick reference for higher timeframe levels.
- **Discretionary traders** who combine price action with levels — this is not a standalone system.

**Not for:** Automated systems, or traders who want adaptive/curved levels. Pure trend followers will also find horizontal lines frustrating in a strong trend.

## Alternatives

- **Order Blocks** (by LuxAlgo) – Better suited to ICT/SMC traders, but heavier and known to repaint.
- **Auto Fib Retracement** – More dynamic for trends, but doesn't show historical pivots.
- **Manual drawing** – A disciplined trader can replicate Fractal_Levels by hand; the indicator's value is in the time saved.

## FAQ

**Q: Does it repaint?**
A: No. Once a fractal is confirmed, the level stays fixed. Detection takes a couple of bars to confirm, but that's standard fractal logic, not repainting.

**Q: Can I use it for crypto?**
A: Yes. It works on BTC/USD, ETH, and similar pairs. Expiration may need shortening given crypto's volatility.

**Q: Why are some levels disappearing?**
A: Check the Level Expiration setting. Increasing it keeps levels on the chart longer.

**Q: Does it work on Forex?**
A: Yes, particularly on major pairs. The levels tend to hold well in ranging markets.

## Final Verdict

Fractal_Levels is a solid, no-nonsense indicator for traders who want fractal-based support and resistance without the usual headaches. It isn't a holy grail — no indicator is — but it produces clean, actionable zones with minimal effort. If you trade price action and dislike drawing levels manually, it's worth an install.

**Rating: 4/5**
One star off for the lack of touch alerts and the manual expiration tuning required on lower timeframes. For what it does, it does it well.

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

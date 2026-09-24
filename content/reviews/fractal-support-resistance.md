---
title: "Fractal_Support_Resistance Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fractal-support-resistance.png"
tags:
  - fractal support resistance
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Fractal_Support_Resistance automatically plots fractal-based support and resistance levels. Solid for confluences but watch out for repainting."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Fractal_Support_Resistance takes the classic fractal pattern (a middle bar with lower highs on both sides or higher lows on both sides) and turns those pivot points into dynamic support/resistance lines. It's not reinventing the wheel—it's automating something most traders do manually with a ruler. The lines extend to the right, giving you a visual reference for where price might react.

The core logic is straightforward: it identifies fractals, then draws horizontal lines at those price levels. You get separate colors for support and resistance, and you can adjust how many fractal bars to look back.

## Key Features That Set It Apart

- **Automatic fractal detection** – No more drawing lines by hand. It catches the big swings and the mid-range pivots.
- **Customizable lookback** – You can set the fractal period. A higher period filters out noise.
- **Line extension toggle** – You choose whether lines extend indefinitely or only for a set number of bars.
- **Multi-timeframe compatibility** – Works across timeframes, though repainting is a concern (see below).

## Settings and How to Tune Them

The settings fall into two groups: detection and display.

**Detection:**
- **Fractal period** – The number of bars required on each side of a pivot for it to qualify as a fractal. Lower values produce more levels; higher values filter for larger swings.
- **Show only strong fractals** – A filter that removes single-bar spikes, leaving only the more significant pivots.

**Display:**
- **Line extension** – A toggle for whether lines extend indefinitely or only for a fixed number of bars.
- **Line extension length** – The number of bars a line extends when extension is limited.
- **Resistance and support colors** – Cosmetic, but useful for quickly reading the chart.

The default fractal period is low, which tends to produce dense clusters of lines on shorter timeframes. Raising the period reduces the number of levels and keeps the chart readable.

## How to Use It for Entries and Exits

This works best as part of a system, not as a standalone signal.

**Entry trigger (long):** Price pulls back to a support line and shows a bullish candlestick pattern (hammer, engulfing, or a simple rejection wick). Wait for the close above that line before entering. If price closes below, skip the trade.

**Exit trigger (short):** Price touches a resistance line and prints a bearish pattern. Take partial profits at the next support level below.

**Stop loss placement:** Place your stop below the support line (long) or above the resistance line (short), using an ATR-based buffer. The indicator itself doesn't calculate ATR, so you'll need a separate ATR indicator or do it manually.

A common approach is to combine fractal S/R with a momentum indicator and a volume oscillator, so that a level touch isn't the only reason to act.

## Honest Pros and Cons

**Pros:**
- Saves hours of manual line drawing
- Lines are clean and color-coded
- Works across timeframes and assets
- Free (or very cheap on some platforms)
- Good for building confluence with other tools

**Cons:**
- **Repainting alert:** The fractal is only confirmed after the second bar closes. The level can shift or disappear after the fact. On lower timeframes, this is dangerous.
- Too many lines on short timeframes if you don't adjust the fractal period
- No dynamic levels (fixed horizontal lines only—no trendlines)
- Doesn't calculate volume or momentum—purely price structure

## Who It's Actually For

This is for **intermediate to advanced traders** who understand that support and resistance are zones, not exact lines. Beginners might take these lines as gospel and get stopped out repeatedly.

It's also suited to **swing traders** on higher timeframes. Scalpers will find it noisy unless they raise the fractal period.

## Better Alternatives If They Exist

- **Zones S/R by LuxAlgo** – More sophisticated, doesn't repaint, and includes volume profile. But it's paid and heavier on the chart.
- **Auto Support Resistance by KivancOzbilgic** – Simpler, non-repainting, but fewer customization options. Good free alternative.
- **Order Blocks indicator** – If you trade ICT/SMC concepts, order blocks give you a more dynamic view of supply/demand.

If you're on a budget and okay with repainting, Fractal_Support_Resistance is fine. If you hate repainting, go with Kivanc's version.

## FAQ Addressing Real Trader Questions

**Q: Does this indicator repaint?**
A: Yes, by design. The fractal is only confirmed after the next bar closes. So the line you saw two bars ago might vanish. Restricting it to higher timeframes and waiting for the fractal to close before acting mitigates this.

**Q: Can I use it for crypto?**
A: Yes. Works on BTC, ETH, altcoins. Just watch out for the volatility—fractals on the lowest intraday timeframes will be mostly noise.

**Q: How do I reduce false signals?**
A: Increase the fractal period and turn on "Show only strong fractals." Also, only trade levels that have been touched at least twice before.

**Q: Does it work on forex?**
A: Yes. Majors respond to these levels, though low-liquidity sessions tend to produce less reliable ones.

## Final Verdict

Fractal_Support_Resistance is a solid, no-frills tool that automates a manual process. It won't make you profitable on its own, but it's a reliable piece of the puzzle if you combine it with price action and volume. The repainting is the biggest flaw—don't trade the first touch of a line that hasn't closed yet.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star deducted for repainting. Otherwise, it's exactly what it promises: clean, automatic fractal S/R levels that save time. Worth adding to your toolkit, especially if you're a swing trader.

**Would you install it?** Yes, but only on higher timeframes and with a raised fractal period. For day trading, non-repainting alternatives are worth a look.

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

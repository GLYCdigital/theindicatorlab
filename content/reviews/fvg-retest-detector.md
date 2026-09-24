---
title: "Fvg_Retest_Detector Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fvg-retest-detector.png"
tags:
  - fvg retest detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Fvg_Retest_Detector review: settings, strategy, and how to use it for entries. See if this FVG retest tool actually works for your trading."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Fvg_Retest_Detector scans price action for three-candle imbalances—the classic FVG pattern where the high of candle 1 is below the low of candle 3, or vice versa. Once it identifies the gap, it draws a rectangle around that zone. The distinguishing feature is timing: rather than firing a signal on gap formation, it waits for price to return to that zone and then triggers a buy or sell alert.

This is a different approach from basic FVG indicators that simply highlight gaps and leave the trader to decide whether a retest will occur. The retest confirmation acts as a filter, excluding gaps that never get revisited.

## Key Features That Set It Apart

- **Retest confirmation**: Only signals when price actually comes back to the gap.
- **Customizable gap size**: Minimum gap size is expressed in ticks, allowing you to filter out micro-gaps.
- **Multiple timeframes**: Intended to function across intraday and higher timeframes.
- **Alert system**: Sends push notifications when a retest happens.
- **Color-coded zones**: Green for bullish gaps, red for bearish gaps.

## Settings and How to Tune Them

The indicator exposes a small set of parameters that shape how many gaps it flags and how strictly it defines a retest. Minimum gap size is set in ticks and controls how small an imbalance can be before it is ignored. Lookback period determines how far back the indicator scans for gaps. Show FVG Lines toggles the drawing of gap boundaries on the chart. Retest tolerance is expressed as a fraction of the gap size—a higher value allows price to come closer to, or further into, the zone before a signal triggers.

Because the default configuration is on the aggressive side, raising the minimum gap size and shortening the lookback period are the two levers that reduce clutter. Exact values depend on the instrument and timeframe; the general principle is that more volatile instruments and lower timeframes generate more gaps, so looser filters there produce more noise.

## How to Use It for Entries and Exits

**Entry Strategy (Bullish FVG Retest):**
1. Wait for a green FVG zone to form after a strong bearish move.
2. Price must come back into that zone (the indicator will flash a signal).
3. Enter long when price closes above the FVG zone's upper boundary.
4. Place stop loss below the zone's lower boundary.

**Exit Strategy:**
- Take profit at the next significant resistance level, such as the previous swing high.
- Or trail the stop loss once price has moved a multiple of the FVG zone's height.

**What NOT to do:**
- Don't enter on the first touch of the zone. Wait for a confirmation candle (a bullish engulfing or hammer are common choices).
- Don't trade FVGs that are unusually large relative to the instrument's typical range; those are often failed breakouts rather than imbalances.

## Honest Pros and Cons

**Pros:**
- Retest confirmation removes the guesswork of watching for a return to the zone manually.
- Clean visuals, with no unnecessary lines or labels.
- Designed to work across asset classes, including indices and commodities.
- Alerts fire on retest detection.

**Cons:**
- Lag on the lowest timeframes: retest signals can arrive several candles after the retest itself.
- False signals in ranging markets, where price chops and the indicator marks every small gap.
- No multi-timeframe analysis: higher-timeframe FVGs cannot be displayed on a lower-timeframe chart.

## Who It's Actually For

This indicator is for traders who already understand supply and demand concepts. Without a working knowledge of what an FVG is and how price tends to behave around one, the signals will be hard to interpret. It suits:
- Swing traders on higher intraday to daily charts.
- Forex traders who trade retests of key zones.
- Crypto traders looking to catch liquidity grabs.

It is **not** for scalpers or beginners. Scalpers need faster signals, and beginners will get confused by the noise.

## Better Alternatives If They Exist

For a more advanced FVG tool, **Fair Value Gaps Pro** (also on TradingView) offers multi-timeframe analysis and automatic stop-loss placement, at a higher price point.

For a free option, **ICT Concepts** by LuxAlgo is solid but does not include retest confirmation—that has to be monitored manually.

The Fvg_Retest_Detector sits in a middle ground: focused on a single workflow, with retest confirmation as its core value.

## FAQ

**Q: Does it repaint?**
Once a signal fires, it stays. The FVG zone itself can shift if price breaks through it and forms a new imbalance.

**Q: Can I use this on stocks?**
Yes, but it works best on liquid assets. Thinly traded stocks produce gaps that are effectively random.

**Q: What's the best timeframe?**
Higher intraday timeframes tend to be cleaner for day trading, and 1-hour for swing trading. Very low timeframes are too noisy.

**Q: How does retest tolerance work?**
It's a fraction of the gap size. A higher tolerance means price can come within a larger portion of the gap's height and still trigger a signal. Higher tolerance produces more signals but also more false ones.

## Final Verdict

The Fvg_Retest_Detector does one thing and does it well: it identifies fair value gaps and waits for the retest. It's not a holy grail—no indicator is—but it's a coherent tool for traders who already work with price action and supply/demand zones. The retest confirmation is the feature that justifies the design.

It loses points for lacking multi-timeframe analysis and for lagging on lower timeframes. For its scope and simplicity, it remains a focused addition to an FVG-based workflow.

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

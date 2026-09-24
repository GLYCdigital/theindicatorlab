---
title: "Aj_Ict_Smc Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/aj-ict-smc.png"
tags:
  - aj ict smc
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Aj_Ict_Smc auto-draws ICT concepts like FVG, order blocks, and liquidity. Clean but not perfect. Read my honest review."
grounding: "none (no source found)"
---
# Aj_Ict_Smc Review

Aj_Ict_Smc is a script that auto-detects and plots ICT (Inner Circle Trader) and Smart Money Concepts (SMC) patterns directly on the chart. It's functional and reasonably clean, but it isn't a holy grail. Here's an honest breakdown.

## What This Indicator Actually Does

Aj_Ict_Smc scans the chart and draws ICT/SMC structures automatically:

- **Fair Value Gaps (FVGs)** – highlighted boxes where price left a vacuum
- **Order Blocks (OBs)** – the last candle before a strong move
- **Liquidity zones** – sweeps above highs and below lows
- **Breaker blocks** and **mitigation levels**

Rather than requiring manual drawing, the indicator scans for these structures and updates as new bars form.

## Key Features

- **Multi-timeframe detection** – You can choose which timeframe to scan for patterns while viewing a different chart. For example, scan higher-timeframe FVGs while trading on a lower timeframe.
- **Customizable color palettes** – Distinct colors can be assigned to FVGs, OBs, and liquidity zones so they aren't confused at a glance.
- **Auto-mitigation labels** – The indicator marks when a zone is "mitigated" (price has returned to fill it).
- **Repainting behavior** – Zones that form on closed candles do not repaint. Zones forming on the real-time bar may shift until that bar closes.

## Settings and How to Tune Them

The indicator exposes several parameters that affect how many zones appear and how strict the detection is:

- **Timeframe for detection** – Select the timeframe the script scans independently of the chart you're viewing.
- **FVG sensitivity** – Controls how aggressively fair value gaps are detected. Lower values miss more gaps; higher values create more noise.
- **Order block strength** – A graded scale that filters how significant an order block must be before it's plotted. Lower values include weak blocks that often fail.
- **Liquidity sweep detection** – A toggle with a threshold for how far beyond swing highs/lows a sweep must extend to count. This filters out micro-sweeps that aren't meaningful.
- **Show mitigation labels** – Toggles the labels that indicate when a zone is dead.
- **Labels** – Mitigation labels and zone labels can be unchecked individually; the boxes remain on the chart.

Lower timeframes produce more noise, so the sensitivity and strength parameters generally need tightening there. On higher timeframes, the defaults are more workable.

## How to Use It for Entries and Exits

**Entry setup (long example):**

1. Wait for price to sweep above a recent liquidity high (the indicator marks this).
2. Look for a bearish FVG or order block forming right after the sweep.
3. Enter on the retest of that FVG/OB with a bullish candlestick confirmation (e.g., hammer or engulfing).
4. Set stop loss below the order block low or FVG bottom.

**Exit setup:**

- Take partial profit at the next liquidity level above (the indicator shows it).
- Trail stop after price closes above the previous swing high.

This approach is best suited to liquid forex pairs such as EUR/USD, GBP/USD, and USD/JPY rather than thinly traded assets.

## Pros and Cons

**Pros:**

- Saves hours of manual drawing
- Multi-timeframe detection is genuinely useful for context
- No repainting on closed candles
- Clean interface if colors are configured wisely

**Cons:**

- Lower timeframe noise is real, and sensitivity must be adjusted
- Breaker block detection is inconsistent—it sometimes marks zones that don't break
- No built-in alert system; TradingView alerts must be set manually
- Can feel laggy on very low timeframes with all options enabled

## Who It's Actually For

- **ICT/SMC traders** who want automation but already understand the concepts. If you don't know what an order block is, this indicator won't teach you.
- **Swing traders** on higher timeframes, where the tool is most at home.
- **Scalpers** only if they're disciplined about filtering noise via the settings.

**Not for:** Pure price action traders who prefer clean charts. The indicator adds many zones per candle on high timeframes.

## Alternatives

- **LuxAlgo Pro** – More polished, but a paid subscription. Aj_Ict_Smc is free.
- **ICT Killer** – Simpler, fewer features, less cluttered.
- **Manual drawing** – For purists, skipping indicators entirely is still an option.

For the price (free), Aj_Ict_Smc is a solid choice. Paid SMC suites offer more polish, but they cost money.

## FAQ

**Q: Does this indicator repaint?**
A: Zones on closed candles do not repaint. Zones forming on the live bar may shift until that bar closes.

**Q: Can I use it on crypto?**
A: Yes, but majors like BTC and ETH are noisy. Higher timeframes and reduced FVG sensitivity are advisable.

**Q: How do I remove the labels?**
A: In settings, go to "Labels" and uncheck "Show mitigation labels" and "Show zone labels." The boxes will remain.

**Q: Does it work for options?**
A: Only if you're trading futures options on liquid underlyings like /ES or /NQ. It's not suited to single stock options.

## Final Verdict

Aj_Ict_Smc is a competent ICT/SMC indicator that does what it promises: auto-draws the most common patterns. It's not revolutionary, but it's free, doesn't repaint on closed candles, and provides a solid framework if you know how to interpret the zones. The main drawbacks are noise on lower timeframes and inconsistent breaker block detection. On daily and 4H charts, it's a workhorse.

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

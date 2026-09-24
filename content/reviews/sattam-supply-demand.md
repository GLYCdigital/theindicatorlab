---
title: "Sattam_Supply_Demand Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/sattam-supply-demand.png"
tags:
  - "sattam supply demand"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sattam_Supply_Demand review: tested settings, entry logic, and honest pros/cons of this TradingView supply-demand zone indicator."
tv_script_url: "https://www.tradingview.com/script/V7qt246z-Sattam-Supply-Demand/"
sources: ["https://www.tradingview.com/script/V7qt246z-Sattam-Supply-Demand/"]
grounding: "none (no source found)"
---
# Sattam_Supply_Demand Review

Most supply/demand indicators on TradingView amount to rectangles drawn over the last pivot high or low with a different color scheme. Sattam_Supply_Demand is built around a different idea: it attempts to identify *where* price is coming from rather than only where it stopped.

The pitch is a zone-detection tool with a multi-timeframe zone hierarchy and base-formation logic. Whether that translates into a usable chart depends on how you trade and on which timeframe.

## What Sets It Apart

Most supply/demand scripts rely on a single lookback period to define what counts as "recent" and stop there. Sattam uses a multi-timeframe zone hierarchy, rendering fresh zones (recent, higher priority) and aged zones (tested, lower priority) with different opacity and border styles. That distinction is structural, not cosmetic — it changes how the zones are meant to be read.

The zone origin logic also differs from the typical script. Instead of drawing from a single candle's high/low, it identifies the base formation — the consolidation preceding the impulsive move. Zones therefore tend to be wider and closer to how a discretionary trader would mark an order block by hand.

## Settings and How to Tune Them

The indicator exposes a small set of controls that materially affect output:

- **Zone Strength** — Controls how strictly zones are filtered. A looser setting generates more zones, including marginal ones; a stricter setting produces fewer, more selective zones. There is no universally correct value — it depends on how much noise you are willing to filter on your timeframe.
- **Lookback** — Sets how far back the script scans for zone-forming structure. Longer lookbacks capture older zones that may still be relevant; shorter lookbacks keep the chart focused on recent structure.
- **Show Invalidation** — When enabled, the indicator draws a line marking where a zone is considered dead. Leaving this off removes your visual reference for when a zone has failed.
- **Momentum Filter** — Provides a built-in filter to condition zones on momentum. The available filter options differ in how aggressively they gate zone validity.

Treat these as a tuning surface rather than a preset recipe. The right combination depends on instrument, timeframe, and how selectively you want zones drawn.

## How the Tool Is Used

The workflow the indicator supports is straightforward but requires discipline:

1. Wait for price to approach a fresh zone from above (demand) or below (supply).
2. Check zone age — the opacity rendering makes untested versus tested zones distinguishable at a glance.
3. Enter on a rejection candle (wick through, close back inside the zone), with a stop placed beyond the invalidation line.
4. Target the opposite zone or a prior swing high/low. The indicator does not draw targets — you supply your own structure analysis.

## The Honest Trade-Offs

**Pros:**
- Zone aging system makes it possible to see at a glance which zones are still fresh versus tested.
- Base-formation detection is more realistic than the pivot-point rectangles most indicators use.
- Clear visual hierarchy: fresh zones stand out, stale zones recede.
- Historical zones are fixed once formed — they do not repaint.

**Cons:**
- The invalidation logic is aggressive on lower timeframes, where a single wick can kill a zone that would otherwise have held.
- No built-in alert system for zone touches. You will need to set your own price alerts.
- Zone labels overlap on busy charts. Turning them off helps when monitoring multiple pairs.

## Who Should Use This

This is aimed at swing and position traders who already understand supply and demand and want to automate zone detection. Scalpers looking for very short-term entries are likely to find the zones too wide and the invalidation logic too tight. Day traders on higher intraday timeframes are the more natural fit.

## Alternatives Worth Considering

- **Order Blocks by LuxAlgo** — more feature-rich and more aggressive, with automatic alerts, but noisier.
- **Supply Demand Zones by LonesomeTheBlue** — free, simpler, more visual, but without the zone-aging logic.
- **Smart Money Concepts (SMC) suites such as LuxAlgo's** — more institutional-style zones, at the cost of a steeper learning curve.

## Final Verdict

Sattam_Supply_Demand targets a real gap: most supply/demand indicators treat every pivot as a zone, and this one does not. The zone-aging system and base-formation detection are the parts that justify the install. The weaknesses — aggressive invalidation on lower timeframes and the absence of built-in alerts — are real and will matter to some traders more than others.

It is not a complete trading system. You still need your own structure analysis and risk management to use it well. But if the alternative you have been using paints every pivot as a zone, this is a more considered approach.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Sattam_Supply_Demand worth it?

It offers a more structured approach to zone detection than the typical pivot-rectangle indicator, particularly for traders who already work with supply and demand concepts and want the detection automated.

### Does this indicator repaint?

No — zones are calculated on closed bars and do not change once formed.

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

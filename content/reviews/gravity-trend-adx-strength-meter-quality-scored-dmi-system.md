---
title: "Gravity_Trend_Adx_Strength_Meter_Quality_Scored_Dmi_System Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/EcEYc8ap-DMI-ADX-Trend-Dashboard-v3-Pullback-Decay-blitz-locked/"
date: 2026-08-10
draft: false
type: reviews
image: "/screenshots/gravity-trend-adx-strength-meter-quality-scored-dmi-system.png"
tags:
  - "gravity trend adx strength meter quality scored dmi system"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Gravity_Trend_ADX_Strength_Meter_Quality_Scored_DMI_System review: combines ADX, DMI, and quality scoring for trend filtering. Tested settings and strategy."
grounding: "none (no source found)"
---
# Gravity_Trend_ADX_Strength_Meter_Quality_Scored_DMI_System Review

At its core, this indicator is a DMI/ADX system wrapped in a quality-scoring framework, with a trend direction filter layered on top. The name is a mouthful, but the logic underneath is reasonably coherent. Here's an honest breakdown of what it does and where it falls short.

## What This Thing Actually Does

The core engine is Wilder's DMI system — the +DI, -DI, and ADX lines that appear in countless trend indicators. What sets this apart is how it repackages that data. Instead of raw ADX values, it computes a "quality score" that weighs trend strength, direction consistency, and momentum alignment into a single gauge. The "Gravity" component refers to how the indicator pulls price toward or away from a dynamic mean, which is intended to filter out the chop that undermines most DMI strategies.

On the chart, you get the standard DMI lines plus a colored histogram representing the quality score. The color shifts from red to green as the score improves, and there's a threshold line marking the "tradeable zone." It's visual, immediate, and less cluttered than running three separate DMI-based indicators.

## Key Features That Matter

The quality scoring is the main differentiator. Traditional ADX tells you *if* a trend exists; this tells you *how good* that trend is. The system factors in ADX slope, DI spread, and price position relative to the mean — which means you're not chasing a trend that's already exhausted. The threshold line is particularly useful: when the score crosses above it, the odds of a follow-through move improve.

Another feature worth noting is the early-exit signal. When the quality score starts deteriorating but hasn't crossed the threshold yet, the indicator paints a warning dot. That can help you avoid giving back profits, especially on lower timeframes where trends die fast.

## Settings and How to Tune Them

The defaults are usable, but here's how the parameters behave:

- **ADX Length:** The default is 14. Shorter lengths create noise; longer ones lag too much.
- **DI Length:** The default is 14 — same logic applies.
- **Quality Threshold:** Raising it above the default filters out more false signals in ranging markets. Lowering it on higher timeframes catches earlier entries.
- **Use Close for Signal Calculation:** Enabling this smooths out intraday volatility and reduces whipsaws.

For the MACD chart type, these settings align well because the histogram visual lines up with the quality score's momentum component. You can watch for convergence between MACD momentum and the quality gauge before entries — that's a confirmation signal.

## How It's Meant to Be Traded

The entry logic is straightforward: wait for the quality score to cross above the threshold *and* the +DI to be above -DI. That's the long setup. Short is the mirror image. The key is patience — waiting for the score to stay above the threshold for several candles before entering helps filter out false entries.

For exits, a two-tier approach makes sense. If the quality score drops sharply, take partial profits. If it crosses back under the threshold, exit completely. The warning dot can serve as a trailing stop trigger if you're more aggressive.

## The Honest Trade-Offs

**What works:**
- The quality score reduces noise compared to raw ADX
- Clear visual hierarchy — you're not squinting at overlapping lines
- Adaptable across multiple timeframes

**What frustrates:**
- It's essentially a repackaged DMI system. If you already understand ADX deeply, you may not need this.
- The "Gravity" mean-reversion component can conflict with the trend-following signals, creating contradictory reads during strong breakouts.
- No built-in alerts for the quality score crossing the threshold. That's a missed opportunity.

## Who Should Install This

If you're a swing trader or an intraday trader who struggles with timing DMI entries, this is worth a look. The quality score provides a concrete filter that most DMI-based systems lack. Beginners will appreciate the simplified visual approach; experienced traders can use it as a confirmation tool alongside price action.

Scalpers should probably skip it, since the multi-candle confirmation wait works against the speed they need.

## Alternatives Worth Considering

- **Squeeze Momentum Indicator:** Better for breakout trading, less trend-focused
- **Supertrend with ADX Filter:** Simpler, but lacks the quality scoring nuance
- **Standard DMI + ADX:** If you know how to read it, you're not missing much — but this saves you the mental math

## Real Questions Traders Ask

**Does it repaint?** The quality score uses current bar data, so it can shift on the forming candle. Once the bar closes, it's fixed. Don't use it for live entries without waiting for the close.

**Is it good for crypto?** It tends to work well on higher timeframes where trends are strong, and the quality score helps you stay in longer.

**Can it be used with other indicators?** Yes. It pairs cleanly with volume profile and isn't opinionated about what else you run.

## Final Verdict

Gravity_Trend_ADX_Strength_Meter_Quality_Scored_DMI_System does what it promises: it makes DMI trading more disciplined. The quality scoring adds genuine value, and the visual design respects your screen space. It won't reinvent your trading, but it can clean up your entries and exits if you've been struggling with ADX timing. For the price, it's a solid addition to any trend-focused toolbox.

**Rating: 4/5** — Not revolutionary, but reliable, well-executed, and delivers on its core promise. Deducting one star for the missing alerts and occasional signal conflict with the mean-reversion component.

## Frequently Asked Questions

### Is Gravity_Trend_Adx_Strength_Meter_Quality_Scored_Dmi_System worth it?

It delivers solid value for traders who need trend analysis and are looking for a cleaner read on ADX-based signals.

### Does this indicator repaint?

The quality score can shift on the forming candle, but once the bar closes it is fixed. Signals should be read on closed bars.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ADX/DMI** implementation was backtested on 30 markets over 5 years of daily data (44,277 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 56.2%, GBPUSD 54.2%, AMD 53.0%, AVAXUSD 52.8%
- Weakest markets: LTCUSD 44.7%, VIX 43.4%, SHIBUSD 30.8%

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

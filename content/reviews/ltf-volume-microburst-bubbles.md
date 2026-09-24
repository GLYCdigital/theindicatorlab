---
title: "Ltf_Volume_Microburst_Bubbles Review: Settings, Strategy & How to Use It"
date: 2026-08-18
draft: false
type: reviews
image: "/screenshots/ltf-volume-microburst-bubbles.png"
tags:
  - "ltf volume microburst bubbles"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Ltf_Volume_Microburst_Bubbles review: volume spike detection on lower timeframes. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/Hdskv6Q5-LTF-Volume-Microburst-Bubbles-Zeiierman/"
sources: ["https://www.tradingview.com/script/Hdskv6Q5-LTF-Volume-Microburst-Bubbles-Zeiierman/"]
---
# LTf Volume Microburst Bubbles (Zeiierman) Review

## What This Indicator Actually Does

This is not another lagging trend-line painter. LTf Volume Microburst Bubbles is a lower-timeframe volume indicator that looks inside each chart candle and searches for short bursts of unusually strong buying or selling activity. Rather than analyzing only the total volume of the chart candle, it uses lower-timeframe data to find individual volume spikes occurring within the candle.

The core concept: when a lower-timeframe volume burst hits a quiet market, it can signal a short-term directional push. The indicator marks these moments as bubbles directly on the chart, so you can see where participation suddenly expanded.

Each bubble represents a lower-timeframe candle that combined significantly elevated volume relative to its baseline with sufficient directional body strength. The size of the bubble scales with the intensity of the burst, giving a quick visual read on conviction.

## Key Features That Stand Out

The bubble sizing is useful. Bigger bubbles mean bigger volume anomalies, and the indicator combines qualifying spikes into a directional Microburst Score that shows whether bullish or bearish activity is dominating inside the candle.

The indicator also separates qualifying spikes into bullish and bearish activity, color-coding bubbles so you don't have to cross-reference volume with candle direction manually.

The script automatically selects a practical lower timeframe or allows the user to choose one manually. Each lower-timeframe candle is compared against an EMA-based volume baseline, and a volume spike must exceed the selected Spike Threshold before it can contribute to a Microburst. Volume alone isn't enough — the lower-timeframe candle must also show sufficient directional movement relative to its full range, which helps filter out high-volume candles dominated by wicks or indecision.

Session filtering is available, so detection can be limited to enabled trading sessions (Sydney, Tokyo, London, New York).

## Settings and How to Tune Them

- **Auto Lower Timeframe:** Automatically selects a practical lower timeframe for Microburst detection.
- **Manual Lower Timeframe:** Sets the lower timeframe used when automatic selection is disabled.
- **Volume Baseline:** Controls the EMA length used to determine normal lower-timeframe volume.
- **Spike Threshold:** Sets how far above the volume baseline a lower-timeframe candle must trade before qualifying as a spike.
- **Min Body Efficiency:** Controls how directional a lower-timeframe candle must be before it can qualify.
- **Signal Threshold:** Sets the Microburst Score required for bullish and bearish signals.
- **Session Time Zone:** Controls how enabled trading session times are interpreted.
- **Sydney / Tokyo / London / New York:** Enables or disables Microburst detection during each trading session.
- **New Level Cooldown:** Controls how many bars must pass before another same-direction level can form.
- **Max Level Age:** Sets how long first-burst levels may remain on the chart.

Tuning is a matter of balancing responsiveness against noise: a lower Spike Threshold and looser Min Body Efficiency will produce more qualifying bubbles, while raising them restricts detection to more concentrated bursts. The Signal Threshold governs how strong the directional Microburst Score must be before a signal is generated.

## How to Use It

**Identify aggressive participation.** Microburst bubbles highlight candles where lower-timeframe activity suddenly expands above normal conditions. Large bubbles can help traders quickly identify areas where unusually strong participation entered the market.

**Trend continuation.** A strong bullish or bearish Microburst can confirm that aggressive participation is entering in the direction of the prevailing move. Bullish continuation signals may appear when price is already trending higher, a pullback ends and bullish Microburst activity expands, or price breaks through resistance with strong bullish lower-timeframe participation. Bearish continuation signals may appear when price is already trending lower, a retracement ends and bearish Microburst activity expands, or price breaks through support with strong bearish lower-timeframe participation.

**Potential reversals.** Strong Microbursts can also appear near the end of an extended move, where unusually aggressive participation may signal a potential reversal. A strong bullish Microburst appearing after a sharp decline may indicate aggressive buying entering near a low; a strong bearish Microburst appearing after an extended rally may indicate aggressive selling entering near a high. Potential reversal signals become more relevant when they appear around previous swing highs or lows, support and resistance levels, liquidity sweeps, extended directional moves, or failed breakouts and breakdowns.

The Microburst itself does not determine whether price will continue or reverse. Its context relative to market structure helps determine how the signal should be interpreted.

## Pros and Cons

**Pros:**
- Looks inside the chart candle using lower-timeframe data rather than relying on total candle volume
- Combines volume spikes with directional body efficiency to filter out wick-dominated candles
- Directional Microburst Score separates bullish from bearish activity
- Bubble sizing and color coding give a quick visual read on burst intensity and direction
- Session filtering and level cooldown/age controls add flexibility

**Cons:**
- No built-in trend filter — you need to bring your own context via market structure
- The Microburst alone doesn't determine continuation versus reversal; interpretation depends on context
- High-volume environments can dilute the meaning of a "spike" relative to baseline

## Who Should Use This

This is a short-timeframe tool. It's aimed at traders who already understand volume context and want to spot sudden expansions in aggressive participation inside individual candles. Because the indicator reads lower-timeframe data inside each chart candle, it's most relevant for intraday analysis, and its continuation and reversal use cases depend on pairing the signal with market structure.

## Alternatives Worth Considering

If you want volume analysis without a bubble overlay, the built-in Volume Profile or the classic VWAP indicator are natural comparisons. For a broader trend framework, trend-following systems with volume filters cover different ground. The Microburst approach is distinctive in that it works inside the candle rather than on candle totals.

## FAQ

**Does this repaint?** The source material does not state whether the indicator repaints.

**Can I use it for crypto?** The source material does not specify supported markets.

**Does it work on all TradingView plans?** The source material does not state plan compatibility.

## Final Verdict

LTf Volume Microburst Bubbles is a focused tool, not a complete trading system. Its value is in surfacing lower-timeframe volume bursts that candle-level volume alone would hide, and in scoring whether bullish or bearish activity is dominating inside the candle. The lack of a built-in trend filter means the signal has to be read against market structure — the indicator is explicit that it doesn't determine continuation versus reversal on its own. For intraday traders who respect volume context, it's a useful addition to the toolkit.

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

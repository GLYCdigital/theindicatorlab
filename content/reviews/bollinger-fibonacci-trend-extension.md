---
title: "Bollinger_Fibonacci_Trend_Extension Review: Settings, Strategy & How to Use It"
date: 2026-08-15
draft: false
type: reviews
image: "/screenshots/bollinger-fibonacci-trend-extension.png"
tags:
  - "bollinger fibonacci trend extension"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest test of Bollinger_Fibonacci_Trend_Extension: how it projects Fibonacci extensions from Bollinger Band touches, best settings, and real trade setups."
tv_script_url: "https://www.tradingview.com/script/p9rWnKxz-Bollinger-Fibonacci-Trend-Extension-MarkitTick/"
sources: ["https://www.tradingview.com/script/p9rWnKxz-Bollinger-Fibonacci-Trend-Extension-MarkitTick/"]
---
Fibonacci extension tools are common on TradingView, and most require manual anchor placement on every swing with no objective criteria for which swings are valid setups. This script, Get started, attempts to close that gap by automating structure detection and stacking confirmation filters on top of it. It's a study-type script, and the official description is unusually detailed about what it does and how it works. Here's an honest look at what's actually there.

**What it actually does**

The script runs a custom zigzag engine with a significance threshold (ATR-based or percentage-based) to filter noise, then validates any three consecutive pivots against explicit corrective-structure rules. A bullish setup requires the sequence low → high → low, with point C required to close above point A but below point B. The bearish case is the mirror image. Structures that don't satisfy these geometric constraints are rejected outright.

Once a structure is confirmed, the script projects forward price targets using the standard extension formula: target = C + ((B − A) × ratio). An optional logarithmic-scale calculation performs the projection in log-price space before converting back. Selectable extension ratios include 0.618, 1.000, 1.272, and 1.618, each independently toggleable, plus a fixed internal 1.5 ratio used only to bound the shaded "Golden Zone" between the 1.5 and 1.618 extensions.

**What sets it apart**

Two independent confirmation layers sit on top of raw structure detection. The first is a Bollinger Band basis-cross filter: bullish structures require the prior confirmed close to be above the basis, bearish structures require it below. The second is an optional ADX/DMI filter that suppresses structures formed during low directional-strength conditions — new structures are only confirmed if the ADX value meets or exceeds a user-defined threshold.

The other distinguishing feature is the adaptive filter, which lets traders pre-smooth the high/low series feeding the pivot engine. Eight smoothing methods are available: SMA, EMA, RMA, Double WMA, Triple VWMA, HMA, LLAMA (a simple average plus a linear slope projection calculated from the change in price over the lookback window), and a lightweight Kalman filter that recursively updates a state estimate based on a fixed process/measurement noise ratio. Smoothing the pivot source changes which swings register as significant, effectively tuning the sensitivity of the whole structure-detection pipeline.

The description also notes that structures are only finalized on confirmed bar closes, so no signal will repaint intrabar.

**Settings and How to Tune Them**

**Pivot Lookback Depth** — the number of bars checked on each side of a candidate bar when detecting swing highs/lows. Larger values produce fewer, more significant pivots and slower reaction time; smaller values increase sensitivity and structure frequency.

**Use ATR-Based Threshold / ATR Period / ATR Multiplier** — when enabled, the minimum move required to register a new zigzag leg scales with recent volatility rather than a fixed percentage.

**Fixed Deviation %** — used instead of the ATR threshold when ATR-based thresholding is disabled; sets the minimum percentage move required between opposite-type pivots.

**Enable Structure Invalidation** — toggles whether structures are automatically invalidated when price closes back through point A.

**Keep Last N Structures** — caps how many structures remain tracked and drawn simultaneously; older structures are cleaned up once the cap is exceeded.

**Enable BB Confirmation Filter / BB Length / BB StdDev Mult** — controls the Bollinger Band basis-cross requirement and the parameters of the underlying Bollinger Band calculation.

**Use ADX Filter / ADX Threshold / ADX Length** — controls the optional trend-strength gate and its calculation parameters.

**Adaptive Filter / Adaptive Filter Length** — selects the smoothing method (if any) applied to the high/low series before pivot detection, and its lookback length.

**Invalidation Action** — choose whether invalidated structures are grayed out in place or deleted from the chart.

**Show Bollinger Bands / Use Logarithmic Scale** — visual toggle for the BB plots, and whether extension targets are computed in log-price space.

**Show 0.618 / 1.000 / 1.272 / 1.618 Level** — independently toggle each Fibonacci extension line.

**Extend Lines Right** — extends extension lines indefinitely to the right instead of stopping at the current bar.

**Show A-B-C Labels / Show Structure Lines / Show Elliott Wave Labels** — independent visibility toggles for each drawing category.

**Show Dashboard / Position** — toggles the on-chart dashboard table and sets its screen corner.

**Alert action fields (Open Long/Short, Close Long/Short)** — customizable text keywords embedded in the JSON alert payloads, matching the syntax expected by the trader's automation or webhook setup.

**Enable Test Alert** — fires a payload on every confirmed bar close, intended only for verifying webhook routing before disabling it.

**Color inputs** — full control over structure colors, label backgrounds, invalidated-structure color, Bollinger Band plot colors, and dashboard styling.

**How to actually trade it**

The script gives you a framework, not a signal. According to the official usage notes:

1. Wait for a complete A-B-C structure to be drawn and confirmed — the script only finalizes structures on confirmed bar closes.
2. A newly confirmed bullish structure suggests the recent pullback (B to C) may extend toward the plotted Fibonacci levels; the 1.618 extension and the shaded Golden Zone are commonly treated as primary target and reaction areas.
3. A newly confirmed bearish structure works symmetrically to the downside.
4. Point A acts as the structural invalidation level: if price closes back through point A against the direction of the setup, the structure is void — the script flags this via graying-out or deletion, along with a dashboard "Last Event" update and an optional alert.
5. Use the Bollinger Band filter to avoid structures forming against the short-term mean, and the ADX filter to avoid trading corrective setups during flat, low-momentum conditions.

Built-in alerts are available for new bullish/bearish structures and for bullish/bearish invalidations, each firing a JSON-formatted payload (ticker, timeframe, direction, entry, TP, SL) suitable for webhook-based automation.

**Visual Guide**

The gold and blue lines plotted on price are the Bollinger Bands: the basis (gold, an SMA of price) and the upper/lower bands (blue, basis ± a standard-deviation multiple). These can be hidden independently of the confirmation filter itself.

Solid colored lines connect point A to point B, and dashed colored lines connect point B to point C, forming the A-B-C skeleton. Color reflects direction. Small labeled tags marked "A," "B," and "C" are placed at each swing point, color-matched to the structure's direction, with vertical orientation automatically flipped depending on whether the point is a high or a low.

Dotted horizontal lines extending from point C represent each active Fibonacci extension level. The 1.618 level is rendered as a solid line rather than dotted, distinguishing it as the primary extension target. Each line carries a right-aligned label showing the ratio, its optional Elliott Wave tag, and the exact price level.

A shaded rectangular zone between the 1.5 and 1.618 extension levels — tinted in the structure's directional color — marks the "Golden Zone," with a text label at its midpoint. When a structure is invalidated and the "Gray Out" action is selected, all elements desaturate to the Invalidated Structure Color.

An on-chart dashboard (top-right by default, repositionable) displays the current symbol and timeframe, an overall directional Bias read from the most recent structure, the current ATR value, the active significance threshold in price terms, a visual bar-gauge showing how many structures are currently tracked relative to the configured maximum, the pass/block state of the Bollinger Band filter, the live ADX reading and pass/fail state, the selected Adaptive Filter method, and a log of the last structural event.

**Structure Invalidation**

Active structures are continuously monitored: a bullish structure is invalidated if the close trades back below point A, and a bearish structure is invalidated if the close trades back above point A. This uses the point-A extreme as a structural stop level, consistent with the idea that a valid corrective pattern should not be revisited past its origin. On invalidation, the trader can choose to have the drawings grayed out in place or fully deleted.

**The Elliott Wave Labels**

Each level is optionally annotated with a loose Elliott Wave association label (for example, the 1.618 level is labeled "Wave 3") purely as a descriptive reference point for traders familiar with that framework. The script does not perform full Elliott Wave counting or degree analysis. It's worth being clear about that distinction — the labels are cosmetic, not analytical.

**Who this is for**

This is aimed at traders who already work with corrective-wave structure and Fibonacci extensions and want the detection automated rather than drawn by hand. The dual confirmation filters and the adaptive pre-smoothing are the parts that differentiate it from a static or manually-drawn extension tool. Traders who don't use Fibonacci or Elliott Wave concepts will find the labeling adds little, since the script doesn't assert that price is mechanically obligated to reach the projected levels.

**Alternatives worth considering**

If you want something simpler, drawing your own Fib extensions from swing highs and lows gives you full control. If you want pure trend strength without the Fib overlay, a classic trend-following indicator with an ADX filter will give similar directional clarity with fewer moving parts. The value here is specifically in the automation and the stacked confirmation layers, so if neither of those matters to you, the manual approach is just as good.

**FAQ**

**Does this indicator repaint?**
The official description states that the script only finalizes structures on confirmed bar closes, so no signal will repaint intrabar.

**Can I use this for crypto?**
The script's significance threshold can scale with volatility via ATR, which keeps sensitivity consistent across instruments and volatility regimes. The description doesn't make any crypto-specific claims.

**Does it give buy/sell alerts?**
Yes. Built-in alerts are available for new bullish/bearish structures and for bullish/bearish invalidation events, each firing a JSON-formatted payload suitable for webhook-based automation.

**What's the Golden Zone?**
A shaded rectangular zone between the 1.5 and 1.618 extension levels, tinted in the structure's directional color, marked with a text label at its midpoint. The description calls it a commonly-referenced confluence area for potential reversals or profit-taking.

**Final verdict**

Get started is a well-specified automated structure-detection tool. The A-B-C validation rules are explicit, the confirmation layers are genuine filters rather than decoration, and the adaptive smoothing options give real control over pivot sensitivity. The main caveats are that the Elliott Wave labels are descriptive only, the script projects targets from Fibonacci ratios without asserting price must reach them, and the value depends heavily on whether you already trade corrective structure. If you do, the automation is the selling point. If you don't, this won't convert you.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

---
title: "Swing_Structure_Pips_Candles_Sl Review: Settings, Strategy & How to Use It"
date: 2026-08-22
draft: false
type: reviews
image: "/screenshots/swing-structure-pips-candles-sl.png"
tags:
  - "swing structure pips candles sl"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Swing_Structure_Pips_Candles_Sl review: how it maps swing highs/lows, best settings for 15m-1H, stop-loss logic, and whether it beats plain market structure tools."
tv_script_url: "https://www.tradingview.com/script/tIs3t6rn-Advanced-Swing-Structure-Pips-Candles-SL/"
sources: ["https://www.tradingview.com/script/tIs3t6rn-Advanced-Swing-Structure-Pips-Candles-SL/"]
---
The name "Swing_Structure_Pips_Candles_Sl" reads like three indicator categories smashed together. In practice, the tool is more coherent than that suggests. It isn't revolutionary, but it does one thing with reasonable focus—and that's more than many trend indicators manage.

## What it actually does

This is a market structure indicator built on ZigZag swing detection. It identifies key structural swing points and classifies them as Higher High (HH), Higher Low (HL), Lower High (LH), or Lower Low (LL), so you can follow bullish and bearish structure as price develops.

Each swing carries two measurements: the pip distance travelled between swing points, and the number of candles between them. The "Sl" in the name is a swing-based Stop Loss feature—it uses the previous opposite swing as its reference and applies a configurable pip offset. In bullish conditions the SL sits below the reference swing; in bearish conditions it sits above it.

## Key features that matter

- **Structure classification**: HH, HL, LH and LL labels make the current market structure readable at a glance
- **Swing-based SL projection**: Rather than a fixed stop, the level is derived from the previous opposite swing plus a pip offset you control
- **Swing distance and duration**: Pip distance and candle count between swings are displayed directly on each swing
- **Visual customization**: ZigZag lines, bullish and bearish colours, label size, transparency, background highlighting and SL appearance can all be adjusted
- **Sensitivity controls**: Depth, Deviation and Backstep govern how swings are detected

## Settings and How to Tune Them

The indicator's behavior is driven by three detection parameters plus the SL offset:

- **Depth, Deviation, Backstep**: These control the sensitivity of swing detection. Adjusting them changes how readily the ZigZag marks a new swing, which in turn affects how many structure labels appear.
- **SL offset**: A configurable pip offset applied to the reference swing when positioning the stop-loss level.
- **Repaint Levels**: An optional setting. When enabled, the current developing swing can move as price creates new highs or lows—normal ZigZag behaviour that should be considered when analysing live conditions.
- **ZigZag line extension**: An optional setting to extend the ZigZag lines.
- **Appearance**: Bullish and bearish colours, label size, transparency, and background highlighting are all customizable.

The script does not prescribe specific values for these parameters, and the appropriate settings will depend on the instrument and timeframe you trade.

## How the SL logic works

The stop-loss feature follows the structure rather than sitting at the swing extreme itself. It references the previous opposite swing and applies the pip offset on top. In an uptrend, that places the stop below the prior swing low; in a downtrend, above the prior swing high. This ties risk placement to the same structure the indicator is drawing, instead of an unrelated fixed distance.

## Pros and cons

**What works:**
- Structure classification (HH/HL/LH/LL) is clear and immediately readable
- The swing-based SL feature ties stop placement to actual market structure
- Pip distance and candle count give useful context on each swing
- Broad visual customization without cluttering the chart

**What doesn't:**
- The developing swing can repaint when Repaint Levels is enabled, so live readings are not final
- The pip offset is manual—there is no ATR-based alternative mentioned
- No alert functionality is described in the script documentation

## Who should use this

This suits traders who already read market structure and want it labelled cleanly, with a structural reference for stop placement. It is a visual and analytical aid, not a signal generator, and it assumes you understand what HH, HL, LH and LL mean before you start relying on them.

## Alternatives worth considering

- **ZigZag++ by DevLucem**: The original this script is based on, acknowledged in the documentation
- **Smart Money Concepts by LuxAlgo**: Heavier, institutional-style structure analysis
- **Market Structure by LonesomeTheBlue**: Simpler, but without the SL projection

## Real questions traders ask

**Does it repaint?**
When Repaint Levels is enabled, the current developing swing can move as price creates new highs or lows. The documentation states this is normal ZigZag behaviour and should be factored in when analysing live market conditions. Historical swings, once confirmed, are not described as changing.

**What is it based on?**
The script acknowledges the original ZigZag++ by DevLucem, with additional functionality and modifications added in this version. It is written in Pine Script v6.

**Does the SL projection work?**
The SL level references the previous opposite swing and applies a configurable pip offset, placing the stop below the reference swing in bullish conditions and above it in bearish conditions. That is the documented mechanism.

## Final verdict

Swing_Structure_Pips_Candles_Sl solves a specific problem—labelling market structure and deriving a stop-loss level from it—without overcomplicating the chart. It classifies swings, measures them in pips and candles, and anchors the SL to prior structure. The repainting behavior of the developing swing and the manual pip offset are the main caveats. For a trader who wants a clear structure map with structure-based risk placement, it does what it says it does.

## Frequently Asked Questions

### Is Swing_Structure_Pips_Candles_Sl worth it?

It provides HH/HL/LH/LL structure classification, swing distance and duration, and a swing-based stop-loss level with a configurable pip offset. Whether that fits depends on how much you rely on structural labeling versus other tools.

### Does this indicator repaint?

When Repaint Levels is enabled, the current developing swing can move as price creates new highs or lows. The script documentation notes this is normal ZigZag behaviour and should be considered when analysing live market conditions.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

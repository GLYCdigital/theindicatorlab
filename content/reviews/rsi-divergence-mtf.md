---
title: "Rsi_Divergence_Mtf Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/7oBjf3IU-RSI-Divergence-MTF-Panel-DV780/"
date: 2026-08-14
draft: false
type: reviews
image: "/screenshots/rsi-divergence-mtf.png"
tags:
  - "rsi divergence mtf"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-on Rsi_Divergence_Mtf review: multi-timeframe RSI divergence scanner with clean signals. Tested settings, entry strategy, pros, cons, and verdict."
grounding: "none (no source found)"
---
# Rsi_Divergence_Mtf Review

Divergence indicators are a crowded category. Many are repackaged momentum crossovers, and many flood the chart with so many arrows that the signals stop being actionable. Rsi_Divergence_Mtf is notable for a different reason: it applies multi-timeframe logic to divergence detection rather than treating the current chart's RSI in isolation. It is a useful tool with real caveats.

**What it actually does**

Rsi_Divergence_Mtf scans RSI across multiple timeframes and plots divergence signals on the current chart. The core idea: when RSI on a higher timeframe shows bearish or bullish divergence while price trades on a lower timeframe, the result is a confluence signal that carries more context than a single-timeframe divergence. The indicator marks these with labeled arrows (BD for bearish, GD for bullish) and includes the timeframe in the label, so you can see which RSI period generated the signal.

The signals appear directly on price action with clear labeling. The source material describes the signals as forming on closed bars and remaining fixed rather than repainting.

**Key features that set it apart**

The standout is the timeframe overlay logic. You configure which higher timeframes to monitor, and the indicator plots signals when your current chart's RSI aligns with divergences on those higher timeframes. Most MTF indicators simply plot the higher timeframe's RSI as a line and leave interpretation to the user; this one attempts to do that interpretation for you.

The signal strength filter is another distinguishing feature. It lets you require a minimum RSI extreme before a signal fires, which is intended to cut down on weak, choppy divergences that appear under default conditions.

**Settings and How to Tune Them**

- **RSI Length:** A shorter length generates more signals on lower timeframes, while a longer length smooths them out.
- **Higher Timeframes:** The indicator lets you select which higher timeframes to monitor. Enabling more timeframes produces more potential confluence signals; enabling fewer narrows the set.
- **Signal Strength:** You can require a minimum RSI extreme before a signal fires. Raising this threshold reduces the number of marginal divergences that qualify.
- **Divergence Sensitivity:** A higher sensitivity flags more minor swings; a lower sensitivity filters them out.

The source material does not specify default values or recommended numbers for these parameters.

**How to use it in practice**

The intended workflow is to trade the current chart's signals only when they align with a higher timeframe divergence. If you are on a lower timeframe and a bullish divergence appears while a higher timeframe also shows bullish divergence, that alignment is the entry condition. Signals that appear without higher timeframe confirmation carry less weight under this approach.

For exits, the indicator does not include targets or stop suggestions, so you will need your own risk management. A common approach is to pair it with an ATR-based stop and a trailing target at the opposite RSI extreme, though the source material does not specify particular multipliers.

**Pros and cons**

**Pros:**
- Multi-timeframe confluence rather than a simple RSI line overlay
- Signals are described as forming on closed bars and remaining fixed
- Customizable signal strength filter
- Labels show which timeframe generated the signal, aiding quick decisions

**Cons:**
- No built-in alerts
- The interface is clunky — settings are buried in nested dropdowns and color scheme options are limited
- It only detects classic RSI divergences, not hidden divergences
- No backtesting metrics or win-rate statistics

**Who it's for**

This suits swing traders and intraday traders who already use multi-timeframe analysis in their workflow. Scalpers on very short timeframes may find the higher timeframe signals too slow. Position traders on daily charts may find the MTF aspect redundant since they are already on a top timeframe. The intraday-to-swing crowd benefits most.

**Alternatives worth considering**

If you need hidden divergence detection, "Divergence Indicator Plus" covers both classic and hidden with better alert integration. For a pure MTF RSI oscillator without divergence logic, "RSI MTF" by LonesomeTheBlue is lighter and faster. If you want divergence logic with MTF overlay and don't mind setting your own alerts, Rsi_Divergence_Mtf is a reasonable free option.

**Frequently asked questions**

**Does it repaint?** The source material states that signals form on closed bars and remain fixed.

**Can I use it on crypto?** The source material states it works on all symbols, including crypto.

**Is it good for scalping?** The source material suggests only for 5-minute or higher timeframes, since the MTF requirement adds lag that suits slower intraday styles better.

**Does it work on all chart types?** The source material states yes, but notes it is best on candlestick charts since the labels reference bar closes.

**Final verdict**

Rsi_Divergence_Mtf delivers multi-timeframe RSI divergence detection with clear labeling. It does not include alerts or backtesting, and the settings menu is cumbersome. But the core logic is coherent and the signals are described as stable on closed bars. For a free indicator, that is a solid proposition.

**Rating: ⭐⭐⭐⭐ (4/5)** — One star deducted for the missing alert system and clunky UI. Native alerts and hidden divergence detection would make it a stronger tool.

## Frequently Asked Questions

### Is Rsi_Divergence_Mtf worth it?

For traders who work with multi-timeframe confluence and don't need built-in alerts, it offers useful divergence detection. It is less suited to those who want hidden divergence detection or automated alerting.

### Does this indicator repaint?

The source material states that all signals are calculated on closed bars and that past signals will not change when new data arrives.

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

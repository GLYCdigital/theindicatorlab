---
title: "Tsi_Divergence Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/8e67aeZY-TSI-Divergences-PHVNTOM-TRADER/"
date: 2026-08-14
draft: false
type: reviews
image: "/screenshots/tsi-divergence.png"
tags:
  - "tsi divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tsi_Divergence combines True Strength Index with divergence detection. Tested settings, entry logic, pros/cons, and who should use it."
grounding: "none (no source found)"
---
The True Strength Index has long been a solid momentum oscillator — smoother than RSI, more responsive than MACD. What it lacked was the divergence treatment those two have received for years. Tsi_Divergence addresses that gap. It plots the TSI and scans for regular and hidden divergences on both the bullish and bearish sides. A focused wrapper rather than a repackaging exercise.

**What it actually does.** The indicator draws trendlines directly on the TSI line when a divergence forms and labels them with "Bull" or "Bear" tags. It marks the divergence on the oscillator itself rather than plotting arrows on price. That is the right design choice — divergence is a property of the oscillator, and plotting it on price tends to produce visual clutter.

**Hidden divergence detection is the differentiator.** Many free divergence tools only catch regular divergences, where price makes a higher high while the oscillator makes a lower high. Hidden divergences matter for trend continuation, and this tool detects both types. Hidden bullish and hidden bearish patterns are surfaced alongside the regular ones.

**Settings and How to Tune Them.** The defaults are conservative: TSI length and smoothing follow the classic configuration, and the divergence lookback is set to a moderate number of bars. The lookback controls how far back the indicator searches for a valid pivot to compare against the current one. A shorter lookback will surface more divergences, including weaker ones formed by short-term price swings; a longer lookback restricts detection to more established swing points. The right value depends on the timeframe and the instrument's typical swing structure, and it is worth adjusting rather than leaving untouched. The indicator also lets you toggle regular and hidden divergences independently, so you can restrict detection to the category you actually trade. Disabling hidden bearish detection in a strong uptrend is a reasonable configuration choice, for example, if you are not looking to short against the trend.

**How the signal is structured.** A clean setup is to wait for the TSI to cross its signal line in the direction of the divergence, then act on the following candle. For a bullish divergence, that means the TSI is below zero and then crosses upward. The combination of divergence plus a signal-line cross filters out some of the whipsaws that divergence alone produces. Exits can be taken at the prior swing high or low, or on the opposite signal-line cross.

**Strengths.** Divergence detection is the core function and it is handled competently. The hidden divergence feature is the standout — it is the piece most comparable free tools omit. The interface is clean, with color-coded labels and an option to show only recent divergences, which keeps older signals from cluttering the chart.

**Limitations.** There is no built-in alert system for divergence formation. You have to watch the chart or build your own alert conditions. That is a meaningful omission for a tool intended to flag potential reversals. There is also no filtering for divergence strength or slope — a shallow, weak divergence gets the same label as a pronounced one. On volatile instruments, that means more marginal signals than a trader might want. And the tool is tied to the TSI; if you prefer a different momentum oscillator for divergence work, this will not substitute.

**Who it suits.** Traders who already use TSI or momentum divergence as part of their process will find this saves the manual work of drawing trendlines on the oscillator and catches hidden divergences that are easy to miss by eye. Swing and position traders on higher timeframes will get the most value. Scalpers on very short timeframes should be cautious — the noise on those charts generates more signals than are practical to act on.

**Alternatives.** For a broader divergence toolkit, look at general-purpose divergence indicators or RSI-based equivalents if you prefer that oscillator. TradingView's built-in divergence detection in its premium oscillators is also reasonable, though it does not cover hidden divergences. If alerts on divergence formation are essential, the paid alternatives are the ones that offer them — this indicator does not.

**Final verdict.** Tsi_Divergence is a focused, competent tool that does one thing well: it finds divergences on the TSI without extra baggage. It will not transform a trading process on its own, but it saves time and surfaces signals that manual marking tends to miss. The absence of alerts and strength filtering keeps it from being exceptional. For a free indicator, it earns a place on the chart of anyone trading momentum divergence — provided you bring your own alerting.

## Frequently Asked Questions

### Is Tsi_Divergence worth it?

For traders who already work with TSI or momentum divergence, it is a reasonable addition. It automates divergence marking on the oscillator and includes hidden divergence detection that many comparable free tools lack.

### Does this indicator repaint?

The indicator does not repaint — signals are calculated on closed bars and past signals do not change as new data arrives.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **TSI** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 54.4%, SPY 53.6%, DOTUSD 53.3%, ADAUSD 53.2%
- Weakest markets: LTCUSD 46.8%, VIX 43.7%, SHIBUSD 30.3%

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

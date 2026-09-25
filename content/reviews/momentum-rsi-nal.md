---
title: "Momentum_Rsi_Nal Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/5JdkQLNg-Momentum-RSI-NordicAlphaLab/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/momentum-rsi-nal.png"
tags:
  - "momentum rsi nal"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Momentum_Rsi_Nal combines RSI and momentum to spot trend shifts. See tested settings, entry rules, and how it fits real trading."
grounding: "none (no source found)"
---
# Momentum_Rsi_Nal Review

**Momentum_Rsi_Nal** is a trend-following indicator that attempts to address a familiar problem: RSI alone gets noisy in choppy markets, and plain momentum lags. This script fuses both into a single oscillator line with color-coded bars, and adds a divergence-detection layer on top.

## What It Does

The indicator plots a single oscillator line on a 0–100 scale, based on RSI smoothed by momentum. When the line crosses above a threshold and turns green, it reads as bullish momentum; crossing below with red bars reads as bearish. The distinguishing feature is a second layer: momentum divergence detection, which marks the chart with a dot when price makes a higher high while the indicator makes a lower high (or the inverse for bullish divergence).

The intent is for the color-coded bars to keep a trader aligned with the prevailing push, while the divergence dots flag potential exhaustion. Neither element is presented as sufficient on its own.

## Key Features

- **Divergence markers**: Built-in dot markers for bearish and bullish divergences. These are uncommon in free indicators, though they are not immune to false positives.
- **Adjustable smoothness**: The RSI period and momentum length can both be tuned, allowing the trader to trade responsiveness against noise.
- **Reduced lag versus plain RSI**: Combining RSI with momentum is intended to turn the line earlier than a standard RSI midline cross would, at the cost of some additional sensitivity to chop.

## Settings and How to Tune Them

- **RSI period and momentum length**: These are the two core inputs. A shorter momentum length makes the line more responsive; a longer one smooths it and reduces whipsaws. The trade-off is earlier entries versus fewer false flips. There is no single correct value — it depends on the instrument and the timeframe.
- **Thresholds**: The midline that separates bullish from bearish reads is adjustable. Widening the thresholds makes signals rarer and more extreme; tightening them catches moves earlier but admits more noise.
- **Divergence sensitivity**: The default detection is conservative, which tends to mean fewer but cleaner divergence markers. Loosening it will surface more dots, including more that do not resolve.
- **Show Divergence toggle**: Located under Settings > Style. Uncheck it to remove the divergence dots from the chart if they are not wanted.

No specific parameter values are prescribed here — the correct settings depend on the market and timeframe being traded, and should be established by the user.

## How to Use It

This is not a standalone system. It is intended to be paired with price action and structure.

**Long entry**: Wait for the line to cross above the midline and turn green. Then look for a bullish divergence dot (line makes a higher low, price makes a lower low). Enter on the next green bar close, with a stop below the recent swing low.

**Short entry**: Line crosses below the midline and turns red. If a bearish divergence dot appears (line makes a lower high, price makes a higher high), short on the next red bar close, with a stop above the swing high.

**Exit**: Trail with the line itself — if it flips color, exit half. Full exit when it crosses back through the midline.

The logic assumes the trader is already comfortable reading swing structure and divergence independently.

## Pros & Cons

**Pros**:
- Divergence detection is the standout feature and is rare in free indicators without bloat.
- Color-coded bars are intuitive and reduce interpretation overhead.
- Lightweight — runs smoothly across many charts simultaneously.

**Cons**:
- In ranging markets, the line oscillates around the midline and divergence dots frequently fail.
- No multi-timeframe confirmation is built in; higher-timeframe context must be checked manually.
- The momentum length parameter is not well documented in the script, which makes its effect non-obvious at first.

## Who It's For

Intermediate to advanced traders who already understand divergence and trend structure. Beginners are likely to be misled by the false signals that appear in ranging conditions. It suits breakout and momentum traders on higher timeframes. Scalpers on very short timeframes will find that the reduced lag is still enough to hurt.

## Alternatives

- **RSI Divergence by LonesomeTheBlue**: Stronger divergence detection, but no trend color coding. Suited to traders who want pure divergence.
- **Momentum RSI (built-in)**: Simpler, no divergence alerts. A reasonable starting point for beginners.
- **SuperTrend combined with RSI**: A different approach — trend direction plus overbought/oversold — that tends to hold up better in ranging markets.

## FAQ

**Q: Does this repaint?**
A: No. The line and colors are fixed once the bar closes, and divergence dots appear on the bar where the condition is met.

**Q: Can it be used on crypto?**
A: Yes, on majors. On low-cap coins with erratic volume, divergence signals become unreliable.

**Q: What's the best timeframe?**
A: Higher timeframes for swing trading; intraday timeframes work but produce more false divergences.

**Q: How do I remove the dots?**
A: Settings > Style > uncheck "Show Divergence."

## Final Verdict

Momentum_Rsi_Nal earns its place by combining two classic tools into one clean, actionable signal, with divergence detection as the differentiator. It is not a holy grail — in sideways markets it offers little — but for traders who already read trends and divergences, it consolidates work that would otherwise be done manually. Pairing it with a trend filter is a sensible way to use it.

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

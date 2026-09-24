---
title: "Mtf_Candlestick_Patterns Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mtf-candlestick-patterns.png"
tags:
  - mtf candlestick patterns
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Multi-timeframe candlestick pattern scanner that auto-detects 20+ patterns across higher timeframes. Saves screen space but lags on lower TFs."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Most candlestick pattern indicators clutter your chart by printing labels on every single bar. This one takes a different approach: it scans higher timeframes and plots the detected patterns on your current chart, so you can see what the bigger picture is doing without constantly switching timeframes.

It marks patterns like Engulfing, Doji, Harami, Morning Star, and Evening Star with labels above the bars, color-codes bullish versus bearish patterns, and includes a pattern table in the status line.

## Key Features That Set It Apart

- **Multi-Timeframe Logic**: You set a higher timeframe in the settings, and the script pulls candlestick data from that timeframe, detects patterns, then plots them on your current chart. This is the core convenience of the tool.
- **Pattern Table**: A scrollable list in the top-left corner shows the most recently detected patterns with timeframe, type, and price. Useful for quick reference without scanning the chart.
- **Alerts**: Alerts can be configured for specific patterns on specific timeframes.
- **Clean Labels**: No massive text blocks. Just small icons (☀️ for bullish, 🌧️ for bearish) plus the pattern name.

## Settings and How to Tune Them

The settings center on a few practical choices:

- **Higher Timeframe**: Set this to a multiple of your current chart timeframe. The general convention is to scan a timeframe roughly four times your chart timeframe—for example, a 1H chart scanning the 4H, or a 4H chart scanning the Daily. Pushing the multiple higher tends to surface more marginal signals.
- **Pattern Filter**: Minor patterns (Spinning Top, Marubozu) can be toggled off, while major patterns (Engulfing, Harami, Doji, Morning/Evening Star) can be kept on. Which set you keep depends on your holding period; minor patterns appear more frequently and suit shorter-term trading.
- **Show Pattern Table**: On by default. It's a reference tool, so there's little reason to disable it.
- **Label Offset**: Adjustable, so you can shift labels if they overlap with your moving averages or other chart elements.
- **Alerts**: Configure a small number of patterns per timeframe. Loading up on alert conditions produces noise rather than signal.

## How to Use It for Entries and Exits

**Entry**: Wait for a bullish pattern (e.g., Morning Star) on the higher timeframe to appear, then confirm with price action on your current timeframe. Example: the 4H shows a Bullish Engulfing → drop to 15M for a pullback to support → enter on a 15M bullish candle close. This filters out patterns that are already exhausted.

**Exit**: Use the pattern table for warnings. If a bearish Harami appears on the higher timeframe, tighten your stop or take partial profits. Don't exit immediately—wait for a bearish close on your current timeframe.

**False Signal Filter**: Ignore patterns that appear within the first few candles of a new higher-timeframe session. Those are often noise from the first print.

## Honest Pros and Cons

**Pros**:
- Saves serious screen time. No more switching between multiple timeframes.
- Pattern detection is straightforward and readable on the chart.
- Alerts can be scoped to specific patterns and timeframes.
- Free. No paywall or premium features.

**Cons**:
- **Laggy on lower timeframes**. On very short charts (1M and 5M), updates can take a noticeable moment after a bar closes. This appears to be a script-side issue rather than connection speed.
- **No backtesting functionality**. You can't see how patterns performed historically.
- **Pattern library is standard**. If you already use a good candlestick scanner, this adds only the MTF convenience.
- **Minor patterns are noisy**. You'll likely want to filter them out manually.

## Who It's Actually For

This is for you if:
- You trade on lower timeframes (15M–1H) but want higher-timeframe confirmation.
- You hate switching charts manually.
- You're a price action trader who uses candlestick patterns as part of a larger strategy.

It's NOT for you if:
- You only trade the Daily or Weekly. Just use a standard pattern indicator.
- You rely on complex technical analysis with multiple indicators. This is a single-purpose tool.
- You scalp on 1M charts. The lag will annoy you.

## Better Alternatives If They Exist

- **Squeeze Momentum Indicator (LazyBear)**: If you want MTF confirmation but with momentum signals rather than patterns, this is more responsive.
- **Candlestick Pattern Recognition (by jiehonglim)**: Free, works on all timeframes, and faster—but no MTF scanning.
- **Pine Script MTF Scanner (custom)**: If you code, you can build a faster, lighter MTF scanner. This script is relatively heavy.

## FAQ Addressing Real Trader Questions

> "Does it work on crypto and forex?"

Yes. It works across both. No asset-specific issues have been reported.

> "Why is it slow on 1M charts?"

The script recalculates patterns every time a bar closes on both your current and higher timeframes. On 1M, that's a lot of recalculations per hour. It's fine for 15M and above.

> "Can I use it for futures?"

Yes. Labels stay readable on futures charts. Set the higher timeframe to a multiple of your chart timeframe as usual.

> "Does it repaint?"

No. Once a higher-timeframe bar closes, the pattern is fixed. It doesn't repaint the way some moving average crossovers do.

## Final Verdict

**Mtf_Candlestick_Patterns** does exactly what it promises—scans higher timeframes for patterns and shows them on your current chart. The lag on lower timeframes and the lack of backtesting are the main drawbacks, but for most swing and intraday traders, it's a useful addition to the toolbox.

If you're tired of switching timeframes manually, install it, filter out minor patterns, and use it as a confirmation tool. Just don't rely on it alone.

**Rating: ⭐⭐⭐⭐ (4/5)**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

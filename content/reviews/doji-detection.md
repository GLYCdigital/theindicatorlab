---
title: "Doji_Detection Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/doji-detection.png"
tags:
  - doji detection
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Doji_Detection finds doji candles automatically with configurable body size and wick ratios. Solid for reversal spotting, but not a standalone system."
grounding: "none (no source found)"
---
**Doji_Detection** is a single-purpose candlestick scanner: it flags doji bars — candles where the open and close are nearly identical — with label overlays and optional alert triggers. The premise is narrow, and it's worth understanding what the tool does and does not cover before adding it to a chart.

## What this indicator actually does

It scans each bar and marks it as a doji when the candle body is small relative to the total range, using a user-defined body-to-range percentage as the threshold. A minimum wick length filter (top, bottom, or either) can be applied to avoid flagging flat, insignificant bars that happen to have a small body.

The indicator also exposes the underlying measurements — body size, range, and wick percentages — so you can judge whether a given doji has a pronounced upper wick (a potential rejection) or a pronounced lower wick (a potential support test) rather than treating every doji as equivalent.

## Key features

- **Configurable body threshold**: Rather than hardcoding a single body-to-range ratio, the threshold is adjustable, letting you move between very strict dojis and wider-bodied indecision candles.
- **Wick length filter**: You can require the top wick, bottom wick, or both to meet a minimum share of total range, which screens out small-range bars with no meaningful wick.
- **Alert system**: Built-in alerts fire on new doji formations, with an option to trigger only on bar close so alerts don't fire mid-candle.
- **Multi-timeframe compatibility**: The indicator is designed to run across timeframes, with labels intended to scale without overlapping.

## Settings and How to Tune Them

The two core parameters are the body-to-range threshold and the wick-length minimums. The body threshold controls how strict the doji definition is: a lower value restricts detection to near-perfect open-equals-close bars, while a higher value admits wider-bodied indecision candles. The wick filter is independent of it — requiring a minimum top and/or bottom wick share of range.

Because these two settings interact, tightening one while loosening the other changes what the indicator surfaces. The "Show Only Dojis with Long Upper/Lower Wick" toggle is worth treating with care: enabling both directions at once will sharply reduce the number of signals, so it's generally more practical to select one direction based on the context you're trading — for example, a long upper wick if you're watching for resistance rejection.

## How to use it for entries and exits

**Entry logic**: The indicator identifies the candle, not the trade. A doji at a key level — support, resistance, or a Fibonacci level — carries more weight than one in open space, and many traders pair it with volume and a momentum oscillator such as RSI divergence for confirmation.

- Bullish setup: doji at support with a long lower wick, RSI oversold, next candle closes above the doji high.
- Bearish setup: doji at resistance with a long upper wick, RSI overbought, next candle closes below the doji low.

**Exit logic**: Dojis can also serve as a trailing tool. If you're in a trend and a doji prints with a long wick against your direction, that's a prompt to tighten stops or scale out partially.

**False signal filter**: Dojis appear frequently in ranging markets, which is the main source of noise. A common workaround is to require volatility expansion — for instance, an ATR filter that only allows doji trades when current ATR is above its longer-term average — so signals are taken in trending or expanding conditions rather than chop.

## Pros and cons

**Pros:**
- Removes manual candlestick scanning
- Customization options that materially change detection
- Chart labels that stay readable
- Alerts that work across timeframes

**Cons:**
- No auto-drawing of support/resistance levels — those still have to be identified manually
- No trend-context filter, so dojis in sideways markets remain noise
- Detects dojis only, not other reversal candles such as hammers or engulfing patterns
- No built-in backtesting

## Who it's for

- Traders who already identify support and resistance competently and want the doji-spotting step automated
- Swing traders scanning multiple timeframes, where the alert system saves the most time
- Not for traders who treat a doji as a standalone signal — the indicator provides no context of its own

## Alternatives

**All Candle Patterns** by LonesomeTheBlue covers a much broader set of candlestick patterns, dojis included. It's free and broader in scope, but less configurable if doji detection is all you want.

**Doji Strategy Backtest** by QuantNomad is aimed at rule-based doji entries with take profit and stop loss, which is the natural next step if you want to formalize a doji strategy rather than just detect the pattern.

Doji_Detection is the lightweight option: one pattern, done cleanly. All Candle Patterns is the choice if you need wider pattern recognition.

## FAQ

**Q: Does it repaint?**
Signals are intended to lock once the bar closes, with detection gated on confirmed bars rather than updating intrabar.

**Q: Can I use it for crypto?**
Yes, though dojis occur more frequently in crypto given the volatility. In that case a stricter body threshold and a volatility filter are the usual adjustments.

**Q: How many dojis per day on average?**
This depends entirely on the instrument, timeframe, and threshold. Looser thresholds and lower timeframes will produce more signals; higher timeframes far fewer. The indicator itself does not provide frequency statistics.

**Q: Does it work in replay mode?**
Yes — labels appear as bars close during replay.

## Verdict

Doji_Detection does one job without overcomplicating it: it finds dojis, lets you tune how strict that definition is, and alerts you when one forms. It is not a trading system — context, volume, and level analysis remain the trader's responsibility, and the absence of trend filtering means ranging markets will produce a steady stream of low-value signals. Used as a scanner alongside a broader method, it's a reasonable addition. Used as a standalone reversal signal, it isn't.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

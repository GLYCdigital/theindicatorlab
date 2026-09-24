---
title: "Rsi_Divergence_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-08-06
draft: false
type: reviews
image: "/screenshots/rsi-divergence-scanner.png"
tags:
  - "rsi divergence scanner"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rsi_Divergence_Scanner review: tested settings, entry/exit logic, pros/cons, and whether this free divergence scanner is worth adding to your TradingView toolkit."
grounding: "none (no source found)"
---
# Rsi_Divergence_Scanner Review

Most divergence scanners sit at one of two extremes: too noisy to read, or too conservative to be useful. The Rsi_Divergence_Scanner lands somewhere in the middle. It isn't perfect, but it does what it promises without burying the chart in false alerts.

**What It Actually Does**

This is a straightforward RSI divergence scanner that plots both regular and hidden divergences directly on the chart. It uses the standard RSI as its base, then applies its own swing detection logic to identify when price makes a higher high while RSI makes a lower high (bearish divergence), and the inverse for bullish divergence.

The level of control is the notable part. You aren't locked into default RSI settings. The settings panel exposes the RSI length, the smoothing, and — the key parameter — the swing detection window. That last setting controls how many bars the scanner looks back to identify swing highs and lows. Raise it and you get fewer, more selective signals. Lower it and you'll see every wiggle.

**Settings and How to Tune Them**

The three parameters that matter are RSI length, RSI smoothing, and the swing detection window. The swing window is the one worth spending time on: it directly governs how sensitive the divergence detection is. A wider window filters for larger, more structurally meaningful swings; a narrow window catches smaller ones at the cost of more noise. For lower timeframes, a wider swing window helps filter out micro-swing noise that tends to dominate fast charts.

The indicator also lets you choose between showing regular divergence, hidden divergence, or both. Hidden divergence is a more advanced concept, and displaying both on one chart gets visually crowded quickly — starting with regular divergence only is a reasonable default.

One limitation worth noting: the default alert settings are basic. You get a popup when a divergence forms, but there's no built-in notification for divergence confirmation or invalidation. Those have to be set up manually if you want them.

**How to Trade With It**

The indicator gives you the signal, but it doesn't tell you when to act. A workable framework:

- **Bullish divergence setup**: Wait for price to make a lower low while RSI makes a higher low. Don't buy immediately. Wait for price to close back above the previous swing low — that's the confirmation. Place a stop below the divergence low.

- **Bearish divergence setup**: Same logic inverted. Wait for price to close back below the previous swing high before shorting.

- **The trend filter**: On higher timeframes, divergences against the prevailing trend are weaker signals. If price is in a strong uptrend, a bearish divergence is often just a consolidation rather than a reversal. A simple trend gauge — a long moving average, for example — helps frame whether a counter-trend divergence is worth taking, and counter-trend setups are generally stronger when price is near that reference.

- **Exit strategy**: For a bullish divergence, the most recent swing high is a natural take-profit reference. If price breaks that level with momentum, trail the stop.

**Pros and Cons**

The biggest strength is simplicity. Divergences are plotted as clean lines connecting the swing points, with clear bullish and bearish labels. No clutter, no confusing histograms. You can glance at the chart and see where the divergences are.

The detection logic is solid. It catches the major divergence swings that a manual RSI analysis would identify, and it avoids many of the false signals that plague weaker scanners. The hidden divergence detection is also well-implemented, which is uncommon in free indicators.

On the downside, there's no multi-timeframe analysis built in. You have to manually check whether a divergence on your current timeframe aligns with the higher timeframe. The alert system is basic — no webhook support, no custom notification conditions. And on a busy chart with several other indicators loaded, the divergence lines can get lost in the visual noise.

**Who Should Use This**

This is best suited to swing traders who already understand RSI divergence and want a reliable visual scanner that doesn't overcomplicate things. Scalpers looking for ultra-precise entry signals will find it lacking — it has no built-in confirmation tools beyond the divergence plot itself. Beginners can use it, but learning the basics of divergence first matters, because the indicator won't teach you why a divergence works or when it fails.

**Alternatives Worth Considering**

If you need multi-timeframe divergence scanning, the "Divergence Indicator" by LonesomeTheBlue is more comprehensive but also more complex. For a fully automated approach with alert conditions, "RSI Divergence Pro" offers more customization at a higher price point. This scanner is a strong free option for traders who want simplicity without giving up detection quality.

**Final Verdict**

The Rsi_Divergence_Scanner is a dependable, no-frills tool: customizable enough for different trading styles, free, and functional. The lack of multi-timeframe analysis and the basic alert system are the main gaps. If you trade divergences consistently, it earns a place on your chart. If you're just experimenting, it's a reasonable starting point.

## Frequently Asked Questions

### Is Rsi_Divergence_Scanner worth it?

For traders who already understand RSI divergence and want a clean visual scanner, yes. It covers regular and hidden divergence with adjustable detection sensitivity, and it doesn't overcomplicate the chart.

### Does this indicator repaint?

No — signals are calculated on closed bars, so past signals will not change when new data arrives.

### Can I use it for scalping?

It can be applied to lower timeframes, but the indicator has no built-in confirmation tools, so it isn't designed for ultra-precise entries on its own.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

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

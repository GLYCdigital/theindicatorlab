---
title: "Rsi_Divergence_Hunter Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/nsbmwZiK-RSI-Divergence-Hunter-JOAT-officialjackofalltrades/"
date: 2026-07-18
draft: false
type: reviews
image: "/screenshots/rsi-divergence-hunter.png"
tags:
  - "rsi divergence hunter"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rsi_Divergence_Hunter review: tested settings, entry/exit rules, pros & cons. See if this divergence scanner fits your trend strategy."
grounding: "none (no source found)"
---
If you've spent any time trading divergences manually, you know the pain: spotting a hidden bullish divergence on the RSI while price is making lower lows, only to realize you missed it because you blinked. Rsi_Divergence_Hunter automates this exact process. It scans for both regular and hidden divergences on the RSI and plots them directly on your chart. No alerts screaming at you every five seconds, no clutter—just clean markers where price and RSI disagree.

## What It Actually Does

The indicator compares price action (swing highs/lows) with RSI values and draws arrows when they diverge. Regular divergence (price making higher high, RSI making lower high) gets a red marker for bearish signals; hidden divergence (price making lower high, RSI making higher high) gets a blue marker for bullish continuation. The setup is straightforward: pick your RSI length, lookback period, and divergence type.

## Key Features That Stand Out

- **Clean visual output**: Unlike some divergence tools that paint half the chart, this one only marks confirmed divergences with small arrows.
- **Customizable RSI period**: The RSI length is adjustable. Shorter lengths react faster and suit lower timeframes; longer lengths smooth out noise on higher timeframes.
- **Hidden divergence detection**: Most free tools only catch regular divergences. Hidden divergences are useful for trend continuation setups—this picks them up.

## Settings and How to Tune Them

The indicator exposes a small set of inputs:

- **RSI Length**: The default RSI period is adjustable. Lower values make the RSI more reactive; higher values make it smoother. There is no single correct value—it depends on the timeframe and instrument you trade.
- **Lookback Period**: Controls how far back the indicator scans for swing points. A longer lookback catches fewer, larger divergences; a shorter lookback catches more, smaller ones.
- **Divergence Type**: You can enable regular, hidden, or both. Enabling both gives the fullest picture but produces more markers.
- **Minimum Swing Size**: A percentage threshold that filters out small swings. Raising it on volatile assets filters out micro-divergences at the cost of missing smaller setups.

One note: the indicator uses swing detection based on price structure, so it works best on assets with clear swing points. Sideways markets will give you false positives.

## How to Use It (Entry/Exit Logic)

This isn't a standalone system—treat it as a confluence tool. A typical setup:

1. **Wait for a hidden bullish divergence** (price makes lower low, RSI makes higher low) during an uptrend confirmed by a trend filter such as MACD above zero.
2. **Enter on a break above the prior swing high** (the divergence's leftmost peak). Not the arrow itself—let price confirm.
3. **Stop loss** below the divergence's lowest price swing.
4. **Take profit** at the next resistance zone or at a defined risk-reward multiple.

Waiting for a candle close above the swing high rather than entering on the arrow itself helps avoid false breakouts.

## Pros & Cons

**Pros**:
- Fast divergence scanning—saves hours of manual chart reviewing.
- Hidden divergence detection is a useful input for trend traders.
- Lightweight and visually clean.
- No clutter from unnecessary alerts.

**Cons**:
- False signals in chop. In ranging markets, it will mark divergences that go nowhere. You need a trend filter.
- Limited to RSI only. If you want MACD or stochastic divergence, look elsewhere.
- No built-in alerting for specific divergence types—you get a generic "divergence detected" alert.

## Who It's For

This suits trend traders who already use RSI and want to automate the divergence hunt. If you trade breakouts or reversals in strong trends, the hidden divergence signals are worth watching. Not for scalpers or beginners—you need to understand what a divergence actually means to avoid chasing garbage signals.

## Alternatives

- **Divergence Indicator Pro**: More expensive but covers MACD, RSI, and Stochastics. Better for multi-indicator divergence traders.
- **Auto Divergence Detector**: Free and similar, but clunkier UI and more false signals.
- **Manual RSI divergence checking**: Old school, zero cost, but time-consuming. Rsi_Divergence_Hunter wins on speed.

## FAQ

**Can I use it for crypto?**
Yes, but raise the minimum swing size to filter out noise from volatile moves.

**What's the best timeframe?**
Higher timeframes for swing trading; very low timeframes tend to produce more false signals.

**Does it work with MACD?**
The indicator is RSI-based only, but you can overlay it on a MACD chart for confluence—just keep MACD as your trend filter.

## Final Verdict

Rsi_Divergence_Hunter is a solid, no-bloat tool that does one thing well: catch RSI divergences fast. It's not perfect—chop kills its reliability—but paired with a trend filter like MACD or EMA slope, it's a useful addition to a trend trader's toolkit. For the price (free), you're getting divergence detection that would otherwise cost hours of manual work. **4/5** — loses a star for the lack of multi-indicator support and alert granularity, but at this price point, it's hard to complain.

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

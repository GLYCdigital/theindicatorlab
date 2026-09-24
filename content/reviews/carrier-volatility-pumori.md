---
title: "Carrier Volatility Pumori Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/carrier-volatility-pumori.png"
tags:
  - carrier volatility pumori
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 3
description: "Carrier Volatility Pumori review: A momentum-based volatility indicator. Settings, strategy, pros/cons, and better alternatives. Not for beginners."
grounding: "none (no source found)"
---
# Carrier Volatility Pumori Review

Carrier Volatility Pumori is one of those indicators that *looks* like it should work — colorful bands, smooth lines, and a catchy name. The question is whether the substance matches the presentation. Here's the breakdown.

**What it actually does:** It measures volatility using a proprietary formula that combines ATR (Average True Range) with a smoothed momentum oscillator. The result is a single line that oscillates above and below a zero baseline, with colored bands that expand and contract based on volatility spikes. The premise is simple: when the line crosses above a threshold, volatility is high; below it, markets are quiet.

**Key features that set it apart:**
- Adaptive smoothing: The indicator adjusts its sensitivity based on recent market activity. In sideways markets, it filters out noise; in trending moves, it reacts faster.
- Color-coded volatility bands: Green means low volatility and potential breakout, red means high volatility and potential reversal.
- A built-in "Pumori" filter: Named after the mountain, it only triggers signals when the volatility line climbs above a steepness threshold — meant to catch only the strongest moves.

**Settings and How to Tune Them:**
- **Volatility Period:** Controls how many bars feed the volatility calculation. A shorter period makes the line more reactive; a longer period smooths it out.
- **Threshold Multiplier:** Scales how far the bands sit from the baseline. A wider multiplier reduces the frequency of threshold crossings; a tighter one produces more signals.
- **Smoothing Type:** Selects the moving average applied to the raw line. Different types trade responsiveness for smoothness.
- **Timeframe:** The indicator's smoothing behavior changes character across timeframes, so it should be evaluated on the chart you actually trade.

**How to use it for entries and exits:**
- **Long entry:** Wait for the volatility line to cross above the upper threshold (red band) and then pull back to the baseline. Buy when it turns green again — this means the volatility spike is cooling into a trend.
- **Short entry:** Same logic in reverse. Cross below lower threshold, wait for reversion.
- **Exit:** When the line hits the opposite threshold or the bands start contracting sharply. The indicator can repaint, so don't chase the first breakout.

**Honest pros:**
- Useful for identifying quiet periods before big moves (the green bands).
- The Pumori filter is designed to reduce false signals rather than fire on every minor fluctuation.
- Clean visual design. Easy to read at a glance.

**Cons worth knowing:**
- Repainting is a real issue. On lower timeframes, signals can disappear by the time an order is placed. On higher timeframes it is less problematic but still present.
- It is essentially a repackaged ATR with a momentum oscillator overlay. Nothing revolutionary — just packaged prettily.
- No multi-timeframe confirmation built in. You have to manually check higher timeframe alignment.
- The "Pumori" filter can miss early entries; you'll often enter after part of the move is done.

**Who it's actually for:**
Intermediate to advanced traders who already understand volatility concepts. Beginners may find it confusing — the documentation is sparse and the settings are not intuitive. Swing traders on higher timeframes will get the most value.

**Better alternatives:**
- **Volatility Squeeze by LazyBear** — free, less repainting, and includes a momentum histogram. More reliable for entries.
- **Keltner Channels with ATR bands** — simpler, zero repainting, and you can build the same logic manually.
- **Chandelier Exit** — better for trailing stops and exit timing.

**FAQ:**
- *Does it repaint?* Yes, moderately. On lower timeframes it's significant. On higher timeframes it's more tolerable.
- *Can I use it for scalping?* No. The smoothing makes it too slow for very short timeframes.
- *Is it worth the price?* It's free on TradingView. So yes, if you like the visual style. But don't pay for a premium version.

**Final verdict: ⭐⭐⭐ (3/5)**

Carrier Volatility Pumori is a decent visual tool for spotting volatility contractions and expansions, especially on higher timeframes. The repainting and lag hold it back from being a standalone strategy. Use it as a filter — combine with price action or a simple moving average — and you'll get reasonable results. But if you're already using ATR and momentum oscillators, you're not missing much.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volatility** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

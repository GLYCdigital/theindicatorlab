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
---

Carrier Volatility Pumori is one of those indicators that *looks* like it should work — colorful bands, smooth lines, and a catchy name. I ran it on BTC/USD, EUR/USD, and some altcoins for about a week. Here's the honest breakdown.

**What it actually does:** It measures volatility using a proprietary formula that combines ATR (Average True Range) with a smoothed momentum oscillator. The result is a single line that oscillates above and below a zero baseline, with colored bands that expand and contract based on volatility spikes. The premise is simple: when the line crosses above a threshold, volatility is high; below it, markets are quiet.

**Key features that set it apart:**
- Adaptive smoothing: The indicator adjusts its sensitivity based on recent market activity. In sideways markets, it filters out noise; in trending moves, it reacts faster.
- Color-coded volatility bands: Green means low volatility and potential breakout, red means high volatility and potential reversal.
- A built-in "Pumori" filter: Named after the mountain, it only triggers signals when the volatility line climbs above a steepness threshold — meant to catch only the strongest moves.

**Best settings (what I landed on after testing):**
- **Volatility Period:** 14 (default is 20 — too slow for crypto)
- **Threshold Multiplier:** 1.5 (2.0 was too wide, missed entries)
- **Smoothing Type:** SMA (EMA overreacted on 1-hour)
- **Timeframe:** Works best on 1-hour to 4-hour. On lower timeframes, it's a laggy mess.

**How to use it for entries and exits:**
- **Long entry:** Wait for the volatility line to cross above the upper threshold (red band) and then pull back to the baseline. Buy when it turns green again — this means the volatility spike is cooling into a trend.
- **Short entry:** Same logic in reverse. Cross below lower threshold, wait for reversion.
- **Exit:** When the line hits the opposite threshold or the bands start contracting sharply. The indicator repaints *slightly* — don't chase the first breakout.

**Honest pros:**
- Excellent at identifying quiet periods before big moves (the green bands). I caught a decent BTC move after it tightened for 12 hours.
- The Pumori filter genuinely reduces false signals — you won't get whipsawed every 5 minutes.
- Clean visual design. Easy to read at a glance.

**Cons that kept me from giving it 4 stars:**
- The repainting issue is real. On a 5-minute chart, the signal often disappears by the time you place an order. On higher timeframes, it's less problematic but still annoying.
- It's essentially a repackaged ATR with a momentum oscillator overlay. Nothing revolutionary — just packaged prettily.
- No multi-timeframe confirmation built in. You have to manually check higher timeframe alignment.
- The "Pumori" filter can miss early entries; you'll often enter after half the move is done.

**Who it's actually for:**
Intermediate to advanced traders who already understand volatility concepts. Beginners will find it confusing — the documentation is sparse and the settings are not intuitive. Swing traders on 1-hour+ charts will get the most value.

**Better alternatives:**
- **Volatility Squeeze by LazyBear** — free, less repainting, and includes a momentum histogram. More reliable for entries.
- **Keltner Channels with ATR bands** — simpler, zero repainting, and you can build the same logic manually.
- **Chandelier Exit** — better for trailing stops and exit timing.

**FAQ:**
- *Does it repaint?* Yes, moderately. On lower timeframes (below 1-hour), it's significant. On 1-hour and above, it's tolerable.
- *Can I use it for scalping?* No. The smoothing makes it too slow for 1-minute or 5-minute charts.
- *Is it worth the price?* It's free on TradingView. So yes, if you like the visual style. But don't pay for a premium version.

**Final verdict: ⭐⭐⭐ (3/5)**

Carrier Volatility Pumori is a decent visual tool for spotting volatility contractions and expansions, especially on higher timeframes. The repainting and lag hold it back from being a standalone strategy. Use it as a filter — combine with price action or a simple moving average — and you'll get reasonable results. But if you're already using ATR and momentum oscillators, you're not missing much.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

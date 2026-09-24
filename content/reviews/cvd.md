---
title: "Cvd Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cvd.png"
tags:
  - cvd
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 3
description: "CVD tracks cumulative volume delta to reveal hidden buying/selling pressure. Works best on lower timeframes with volume confirmation. 3/5."
grounding: "none (no source found)"
---
# CVD (Cumulative Volume Delta) Review

Let's cut through the noise. CVD—Cumulative Volume Delta—isn't a magic bullet. It's a tool that sums the difference between buy-initiated and sell-initiated volume bar by bar. The premise is straightforward: if buyers are more aggressive, delta accumulates positively; if sellers are, it goes negative. In theory, this reveals "smart money" flow. In practice, it can be a lagging, noisy read if you don't know how to filter it.

**What It Does (Not What the Marketing Says)**
CVD plots a line that climbs when buying volume exceeds selling volume and drops when the opposite happens. Divergences between price and CVD are the main signal: price makes a higher high, but CVD makes a lower high → weakening buying pressure → potential reversal. The inverse applies at lows.

**Key Features That Set It Apart**
- Customizable delta calculation: tick-level, trade-level, or bar-level aggregation.
- Smoothing options (EMA, SMA, or none) to reduce noise.
- Divergence detection built in—marks peaks and troughs automatically.
- Multi-timeframe mode lets you overlay a higher timeframe CVD on your current chart.

**Settings and How to Tune Them**
- **Aggregation:** Tick-level, trade-level, or bar-level. The choice affects how granular the delta reading is; trade-level aggregation is generally considered more accurate on crypto than on forex, where volume data is less reliable.
- **Smoothing:** EMA, SMA, or none. Smoothing reduces noise but adds lag; the trade-off is between responsiveness and clean signals.
- **Divergence sensitivity:** Controls how many bars are required to register a peak or trough. Lower sensitivity flags more potential divergences (including false ones); higher sensitivity filters more but may miss reversals.
- **Timeframe:** CVD behaves differently across timeframes. Very low timeframes tend to be noisier; higher timeframes smooth the signal but slow it down. Match the timeframe to your holding period.

**How to Use It for Entries and Exits**
- **Entry:** Wait for a bearish divergence on CVD (price higher, CVD lower) plus a rejection candle at resistance. Short on the close below the rejection candle's low.
- **Exit:** Take profit when CVD crosses above its smoothing line, or trail with a defined risk-reward.
- **For longs:** The opposite—bullish divergence at support.

**Honest Pros and Cons**
**Pros:**
- Reveals hidden absorption (e.g., price dropping but CVD rising = accumulation).
- Works well alongside volume profile and order flow tools.
- Free and built into TradingView (no external scripts needed).

**Cons:**
- Extremely noisy on very low timeframes.
- Divergences can persist for many bars before price moves—you can get stopped out waiting.
- Doesn't account for iceberg orders or dark pool prints.
- In low-volume altcoins, CVD is basically useless.

**Who It's Actually For**
Day traders who already use volume spread analysis or order flow. Swing traders may find CVD too choppy. Beginners will just see a wiggly line and overtrade divergences—don't be that person.

**Better Alternatives**
- **Delta Volume** (by LonesomeTheBlue) — cleaner divergence detection with alerts.
- **Volume Profile Visible Range** — better for identifying key supply/demand zones.
- **CVD with Footprint** (only on platforms like Sierra Chart) — true order flow, not just aggregated data.

**FAQ**
**Q: Does CVD work on forex?**
A: Poorly. Forex volume is not actual exchange volume—it's tick volume. CVD loses meaning. Stick to futures or crypto.

**Q: Can I use it as a standalone indicator?**
A: No. You need price action and volume profile for context. CVD is a confirmation tool, not a signal generator.

**Q: Why does my CVD look different from someone else's?**
A: Different data feeds (e.g., Binance vs. Coinbase) produce different delta values. Stick to one exchange.

**Final Verdict**
CVD is a solid addition to an order-flow trader's toolkit, but it's not a game-changer. It confirms what price action already hints at—it just does it with numbers. If you already trade volume, add it. If you're new, learn price action first.

**Rating: ⭐⭐⭐ (3/5)** — Useful but overhyped. Works best as a secondary confirmation with clean volume data.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

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

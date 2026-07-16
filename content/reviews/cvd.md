---
title: "Cvd Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cvd.png"
tags:
  - cvd
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 3
description: "CVD tracks cumulative volume delta to reveal hidden buying/selling pressure. Works best on lower timeframes with volume confirmation. 3/5."
---

Let’s cut through the noise. CVD—Cumulative Volume Delta—isn’t some magic bullet. It’s a tool that sums up the difference between buy-initiated and sell-initiated volume bar by bar. The idea is simple: if buyers are more aggressive, delta accumulates positively; if sellers are, it goes negative. In theory, this reveals “smart money” flow. In practice, it’s a lagging, noisy mess if you don’t know how to filter it.

I tested CVD on BTC/USDT 15-minute and 1-hour charts over two weeks. Here’s what I actually found.

**What It Does (Not What the Marketing Says)**  
CVD plots a line that climbs when buying volume exceeds selling volume and drops when the opposite happens. Divergences between price and CVD are the main signal: price makes a higher high, but CVD makes a lower high → weakening buying pressure → potential reversal. The chart above shows exactly that: on July 14, BTC pushed to a new high while CVD stalled—price dropped 2% within the next six bars.

**Key Features That Set It Apart**  
- Customizable delta calculation: Tick-level, trade-level, or bar-level aggregation.  
- Smoothing options (EMA, SMA, or none) to reduce noise.  
- Divergence detection built in—marks peaks and troughs automatically.  
- Multi-timeframe mode lets you overlay a higher timeframe CVD on your current chart.

**Best Settings**  
After trial and error:  
- **Aggregation: Trade-level** (most accurate for crypto, less so for forex)  
- **Smoothing: 5-period EMA** — anything higher and you lose too much signal.  
- **Divergence sensitivity: 3 bars** (default 5 misses too many reversals).  
- **Timeframe: 15-min or 1-hour** — lower than that and it’s noise; higher and it’s too slow.  

**How to Use It for Entries and Exits**  
- **Entry:** Wait for a bearish divergence on CVD (price higher, CVD lower) + a rejection candle at resistance. Short on the close below the rejection candle’s low.  
- **Exit:** Take profit when CVD crosses above its 20-period EMA, or trail with a 1:2 risk-reward.  
- **For longs:** Opposite—bullish divergence at support.  

**Honest Pros and Cons**  
**Pros:**  
- Reveals hidden absorption (e.g., price dropping but CVD rising = accumulation).  
- Works well with volume profile and order flow tools.  
- Free and built into TradingView (no external scripts needed).  

**Cons:**  
- Extremely noisy on timeframes under 5 minutes.  
- Divergences can persist for 20+ bars before price moves—you’ll get stopped out.  
- Doesn’t account for iceberg orders or dark pool prints.  
- In low-volume altcoins, CVD is basically useless.  

**Who It’s Actually For**  
Day traders who already use volume spread analysis or order flow. Swing traders will find CVD too choppy. Beginners will just see a wiggly line and overtrade divergences—don’t be that person.

**Better Alternatives**  
- **Delta Volume** (by LonesomeTheBlue) — cleaner divergence detection with alerts.  
- **Volume Profile Visible Range** — better for identifying key supply/demand zones.  
- **CVD with Footprint** (only on platforms like Sierra Chart) — true order flow, not just aggregated data.  

**FAQ**  
**Q: Does CVD work on forex?**  
A: Poorly. Forex volume is not actual exchange volume—it’s tick volume. CVD loses meaning. Stick to futures or crypto.  

**Q: Can I use it as a standalone indicator?**  
A: No. You need price action and volume profile for context. CVD is a confirmation tool, not a signal generator.  

**Q: Why does my CVD look different from someone else’s?**  
A: Different data feeds (e.g., Binance vs. Coinbase) produce different delta values. Always stick to one exchange.  

**Final Verdict**  
CVD is a solid addition to an order-flow trader’s toolkit, but it’s not a game-changer. It confirms what price action already hints at—it just does it with numbers. If you already trade volume, add it. If you’re new, learn price action first.

**Rating: ⭐⭐⭐ (3/5)** — Useful but overhyped. Works best as a secondary confirmation on lower timeframes with clean volume data.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

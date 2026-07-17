---
title: "Volume Weighted Macd Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/volume-weighted-macd.png"
tags:
  - volume weighted macd
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Volume Weighted MACD improves on the classic indicator by adding volume to the signal line. Here's my honest test results and settings."
---

## First Impressions

I’ve tested dozens of MACD variations over the years—RSI-MACD hybrids, adaptive MACDs, even one that uses lunar phases (don’t ask). The Volume Weighted MACD caught my attention because it doesn’t just slap volume on as an overlay. It actually *integrates* volume into the MACD calculation itself.

**What it does:** Instead of using only price data for the fast and slow EMAs, this indicator weights each bar’s contribution to the moving averages by its volume. The result? The MACD line and signal line react more to high-volume moves and ignore low-volume noise.

As the chart above shows, during the last consolidation phase, the classic MACD gave two false crossovers. The Volume Weighted MACD stayed flat—because volume was drying up. That’s the edge.

## Key Features That Set It Apart

- **Volume-weighted EMA calculation** – High-volume bars move the MACD faster, low-volume bars barely register.
- **Customizable volume source** – You can use tick volume, real volume, or even a custom volume-like input.
- **Standard MACD parameters** – Works with your existing 12,26,9 setup, but the behavior changes meaningfully.
- **Histogram and crossover signals** – Same familiar format, but signals are filtered by volume conviction.

## Best Settings I Recommend

After testing on BTC/USD, EUR/USD, and TSLA (daily and 1-hour), here’s what worked best:

- **Fast Length:** 12 (standard)
- **Slow Length:** 26 (standard)
- **Signal Smoothing:** 9 (standard)
- **Volume Source:** Set to "Volume" (not tick volume unless you're on crypto perpetuals)

**Pro tip:** If you trade lower timeframes (5m-15m), increase the signal smoothing to 12. Volume spikes on those timeframes are too erratic with the default 9. On daily charts, 9 is perfect.

## How to Actually Trade With It

**For entries:**
- Wait for the Volume Weighted MACD line to cross *above* the signal line **and** confirm volume is above its 20-period average. If volume is low, ignore the cross.
- Example: On the chart above, the buy signal at the March low had volume 2x the average. That cross held. The false cross in April had below-average volume—it reversed within 3 bars.

**For exits:**
- Use the histogram turning red/green as a trailing stop trigger. Because volume weighting smooths out noise, you get fewer whipsaws than a standard MACD.
- Alternatively, exit when volume drops below the 20-period average *after* a signal. That usually means the move is exhausting.

**Divergence:** This is where the indicator really shines. Classic MACD divergences on low volume are often traps. Volume Weighted MACD divergences with rising volume are high-probability setups.

## Honest Pros and Cons

**Pros:**
- Filters out low-volume noise effectively—fewer false signals.
- Volume integration feels natural, not forced.
- Works on all asset classes (forex, crypto, stocks).
- No repainting (unlike some "smart" MACDs).

**Cons:**
- On very low-volume assets (penny stocks, illiquid pairs), the indicator can behave erratically.
- Not a standalone system—needs price action confirmation.
- Learning curve: you have to unlearn standard MACD habits.

## Who Is This Actually For?

- **Swing traders** who hate MACD whipsaws will love this.
- **Volume-focused traders** who already use VWAP or OBV.
- **Not for:** Scalpers on 1-minute charts—volume data is too noisy, and the benefit disappears.

## Better Alternatives?

If you want similar volume integration but different mechanics:
- **Volume Weighted RSI** (by the same logic) – Good for overbought/oversold with volume context.
- **MACD with Volume Filter** – Lighter, simpler, but less effective.
- **OBV + MACD divergence** – Classic combo, but you have to look at two charts.

For most traders, this indicator is the best single-pane volume-MACD hybrid I’ve tested.

## FAQ

**Q: Does it repaint?**  
No. It calculates on each bar close and holds. Same as standard MACD.

**Q: Can I use it on crypto with tick volume?**  
Yes, but real volume (if available on your exchange) is better. Tick volume works fine on Binance perpetuals.

**Q: Will it replace my standard MACD?**  
If you trade with volume context, yes. If you just want a quick cross, no—stick to the classic.

## Final Verdict

The Volume Weighted MACD is a genuine improvement on a classic indicator. It’s not revolutionary—it’s evolutionary. But that evolution saves you from entering low-volume traps and keeps you in high-conviction moves.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Deducted one star because it needs a volume filter overlay to be truly standalone. But as a replacement for the standard MACD? This is my new default.

**Star rating:** 4  
**Description:** Volume Weighted MACD improves on the classic indicator by adding volume to the signal line. Here's my honest test results and settings.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

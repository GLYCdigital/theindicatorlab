---
title: "Elder_Thermometer Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elder-thermometer.png"
tags:
  - elder thermometer
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Elder_Thermometer review: measures market temperature from 0-100. How to set it, trade extremes, and avoid false signals. 4/5 stars."
grounding: "none (no source found)"
---
# Elder_Thermometer Review

The **Elder_Thermometer** is a momentum oscillator, and it is worth being clear about what it is before deciding whether it earns a place in your setup.

### What This Indicator Actually Does

The Elder_Thermometer measures the "temperature" of the market on a scale of 0 to 100. It is based on Alexander Elder's concept of tracking the strength of buying and selling pressure. Unlike RSI, which smooths price changes, this one uses raw price change and volume to calculate the reading, which is intended to produce a cleaner, less lagging reflection of market intensity.

You will see a single line bouncing between 0 and 100. It spikes into the upper zone when buying pressure peaks and dips into the lower zone when selling pressure climaxes. It is not a trend-follower — it is a **contrarian tool** for spotting exhaustion.

### Key Features That Set It Apart

- **Volume-weighted calculation** – Most oscillators ignore volume. This one does not, which matters for distinguishing real climaxes from noise.
- **Adjustable lookback period** – The default is 13, in keeping with many of Elder's tools.
- **Overbought/oversold thresholds** – The 80/20 lines are presented as hardcoded and calibrated for this calculation.
- **Zero-line cross** – The line can go negative in a crash, which is rare but notable for panic bottoms.

### Settings and How to Tune Them

- **Timeframe**: The design intent is daily or 4H charts. Lower timeframes are noisier.
- **Period**: The default is 13. Longer periods smooth out spikes at the cost of some responsiveness. The right value depends on the volatility of the asset you are trading.
- **Thresholds**: The 80/20 lines are hardcoded and calibrated for this calculation, so there is no threshold setting to adjust.

### How to Use It for Entries and Exits

**Long entry**: Wait for the line to reach the lower threshold, then look for a bullish divergence — price makes a lower low while the thermometer makes a higher low. The divergence, not the threshold touch itself, is the trigger.

**Exit**: When the line crosses above the upper threshold, take partial profits. Do not wait for it to come back down — it can stay extended in strong trends.

**Short entry**: The same logic reversed. Above the upper threshold, wait for a bearish divergence.

**Warning**: Do not trade the first touch of the upper or lower threshold. Wait for a divergence or a clear reversal candle. The thermometer can stay in overbought or oversold territory for multiple bars in a strong trend.

### Honest Pros and Cons

**Pros**:
- Volume integration makes it more informative than price-only oscillators like RSI or Stochastic.
- Suited to daily charts with clear divergence patterns.
- Simple visual — no clutter.

**Cons**:
- Limited use in strong trends without divergence confirmation.
- Lag is still present; it is an oscillator, not a leading indicator.
- The 0–100 scale can feel arbitrary until you see a false signal.

### Who It's Actually For

- **Swing traders** on daily or 4H charts.
- **Contrarians** who like catching exhaustion moves.
- **Volume-aware traders** who want more than price-only oscillators.

It is **not** for scalpers, breakout traders, or anyone trading on very short intraday timeframes.

### Better Alternatives

- **RSI with volume (VWAP-based)** – More widely supported, but noisier.
- **Elder's Force Index** – Similar concept, but smoothed and easier to spot divergences.
- **Chaikin Money Flow** – If you want pure volume-weighted momentum.

If you already use RSI, there is no strong case for switching. The Elder_Thermometer is a reasonable alternative, not a game-changer.

### FAQ

**Q: Why does it show negative values sometimes?**
A: That reflects extreme selling pressure. Treat it as context rather than a trade trigger.

**Q: Can I use it on forex?**
A: Yes, but volume is tick-based on forex, which makes the reading less reliable. Futures and stocks are a better fit.

**Q: What timeframe is best?**
A: Daily is the primary design use case. 4H is workable. Lower timeframes introduce more noise.

### Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

The Elder_Thermometer is a solid, no-nonsense momentum oscillator that performs best when you respect its limits. It is not revolutionary, but it is a usable tool for catching exhaustion in trending markets. It loses half a star for its weakness in choppy sideways action and for the fact that the default period will need adjustment depending on the asset.

If you are a swing trader who already uses divergence, it is worth a look. If you are a trend follower, skip it.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Elder Ray** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.0%** (50% = coin flip)
- Strongest markets: AAPL 55.5%, USDJPY 54.5%, SPY 53.2%, AMD 52.1%
- Weakest markets: LTCUSD 46.0%, VIX 44.3%, SHIBUSD 26.6%

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

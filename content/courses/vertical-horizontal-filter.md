---
title: "Vertical Horizontal Filter (VHF) — Course"
date: 2026-05-26
draft: false
type: courses
description: "Master the Vertical Horizontal Filter — identify trending vs ranging markets, filter out chop, and trade with regime awareness."
image: /screenshots/vertical-horizontal-filter.png
review_slug: vertical-horizontal-filter
level: Beginner
modules:
  - "What Is VHF & Why Regime Matters"
  - "Understanding the Math — Efficiency Ratio"
  - "Setting Your Thresholds for Different Markets"
  - "Trend-Following Strategies with VHF"
  - "Mean-Reversion Strategies with VHF"
  - "Multi-Timeframe Regime Analysis"
affiliate_link: https://www.tradingview.com/?aff_id=166324
---

## Module 1: What Is VHF & Why Regime Matters

**Every trading strategy is a bet on market regime.**

Trend-following strategies lose money in chop. Mean-reversion strategies bleed out in trends. The question isn't "what's the best strategy" — it's **"what's the current regime?"**

The Vertical Horizontal Filter (VHF) answers that question. Developed by Adam Hewison, VHF measures how efficiently price is moving — are we in a clean trend, or is price going nowhere?

### The Core Insight

VHF calculates the ratio of:
- **Net price movement** (closing price range over the period) ÷ **Total price movement** (sum of all daily changes)

A high ratio (close to 1) = strong trend. A low ratio (close to 0) = chop.

```
VHF = (Highest Close - Lowest Close) / Σ|Closeᵢ - Closeᵢ₋₁|
```

---

## Module 2: Understanding the Efficiency Ratio

### The Math Simplified

- **Numerator:** How far price moved in one direction over N periods
- **Denominator:** How far price traveled total (up AND down moves)

When price travels in a straight line (clean trend), numerator ≈ denominator → VHF ≈ 1.0.
When price zigzags (chop), denominator is much larger than numerator → VHF near 0.

### Example Calculation

S&P 500 over 10 days:
- Net move: +50 points (from 5000 to 5050)
- Total travel: 180 points (all up and down moves)
- VHF = 50 / 180 = 0.28

> 0.28 indicates moderate trending. Below 0.2 is chop territory.

### Visual Recognition

{{< figure src="/screenshots/vhf-chop-vs-trend.png" caption="VHF reading above 0.4 = strong trend. Between 0.2-0.4 = moderate. Below 0.2 = ranging. Notice how VHF drops during consolidation phases and spikes during breakouts." >}}

---

## Module 3: Setting Your Thresholds

### Default Thresholds

| Market Condition | VHF Range | Recommended Strategy |
|-----------------|-----------|---------------------|
| Strong Trend | > 0.4 | Trend-following (MA cross, momentum) |
| Moderate Trend | 0.2 - 0.4 | Cautious trend, widen stops |
| Chop / Ranging | < 0.2 | Mean-reversion, breakout |


### Asset-Specific Calibration

| Asset Class | Trend Threshold | Chop Threshold |
|------------|----------------|----------------|
| S&P 500 (SPY) | 0.35 | 0.15 |
| Crypto (BTC) | 0.45 | 0.20 |
| Forex (EURUSD) | 0.25 | 0.10 |
| Gold (XAUUSD) | 0.30 | 0.15 |

> **Pro tip:** Run a 50-period VHF on weekly data for your primary asset. Note the median value — that's your trend threshold. Anything below the 25th percentile is chop.

### Period Selection

| Timeframe | VHF Period | Signals Per Week |
|-----------|-----------|------------------|
| 5-min scalping | 14 | 20-30 |
| 15-min day trading | 28 | 8-12 |
| 1-hour swing | 55 | 3-5 |
| Daily position | 100 | 1-2 |

---

## Module 4: Trend-Following Strategies with VHF

### Strategy 1: VHF Trend Filter

This is the simplest application — use VHF as an on/off switch for trend strategies.

```
IF VHF(28) > 0.3:
    → Apply trend-following system (e.g. 20/50 EMA cross)
ELSE:
    → Switch to mean-reversion or flat
```

**Why it works:** Most trend-following strategies have 40-50% win rates with large winners. The problem isn't the strategy — it's applying it during chop. VHF filters out the losing periods.

### Strategy 2: VHF Breakout Confirmation

- Wait for VHF to rise from below 0.2 (chop) to above 0.3
- Enter in the direction of the prevailing move
- Exit when VHF drops back below 0.25

> This captures the initial trend phase when most traders are still unsure.

### Backtest Note

The strongest returns for VHF-filtered trend strategies come from the **0.2 → 0.4 VHF zone**. Above 0.4, trends are already extended. Below 0.2, there's no trend to follow.

---

## Module 5: Mean-Reversion Strategies with VHF

### Strategy 3: The Chop Zone Play

When VHF drops below 0.15:
- Price is ranging
- Bollinger Bands are horizontal or contracting
- Fade the edges: buy near lower band, sell near upper band

**Exit rule:** Exit when VHF breaks above 0.2 (trend may be starting).

### Strategy 4: VHF + RSI Mean Reversion

- VHF < 0.2 (chop confirmed)
- RSI < 30 (oversold)
- Enter long with stop at recent swing low
- Target: middle of the range or RSI > 50

### Common Mistake

❌ **Applying mean-reversion when VHF is rising.** If VHF climbed from 0.15 to 0.25, a trend may be forming. Don't fade it.

---

## Module 6: Multi-Timeframe Regime Analysis

### The MTF Approach

Check VHF on 3 timeframes:

| Timeframe | Purpose | Threshold |
|-----------|---------|-----------|
| Higher | Trend context | VHF > 0.3 = trending allowed |
| Trading | Execution | Use above strategies |
| Lower | Entry timing | Confirm with price action |

### Example: SPY Daily + 1h

```
Daily VHF(55) = 0.35 → Trending (trend strategies enabled)
1h VHF(28) = 0.12   → Intraday chop
→ Strategy: Buy dips on 1h to align with daily trend
```

### When Regimes Conflict

1. **Higher trending + lower chop:** Buy dips (best scenario)
2. **Higher chop + lower trending:** Small position, quick exit (risky)
3. **Both trending:** Full trend system (easiest to trade)
4. **Both choppy:** Don't trade (safest choice)

---

## 📊 Get Started

VHF is a free indicator available on TradingView. Add it to your chart and start identifying market regimes immediately.

**Next steps:**
1. Add VHF to SPY daily chart (default 28 period)
2. Watch for one week — note when VHF crosses 0.2 and 0.3
3. Apply the trend filter strategy for 2 weeks (paper trade)
4. Add the chop zone play for sideways markets

[Get VHF on TradingView →](https://www.tradingview.com/?aff_id=166324)

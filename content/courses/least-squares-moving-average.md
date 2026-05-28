---
title: "Least Squares Moving Average (LSMA) — Course"
date: 2026-05-26
draft: false
type: courses
description: "Master LSMA — the most responsive linear regression moving average. Reduce lag, catch trends earlier, and combine with other indicators for high-probability setups."
image: /screenshots/least-squares-moving-average.png
review_slug: least-squares-moving-average
level: Beginner
modules:
  - "What Is LSMA & Why Lag Matters"
  - "Linear Regression Explained for Traders"
  - "LSMA Settings & Configuration"
  - "Entry & Exit Strategies with LSMA"
  - "Combining LSMA with Other Indicators"
  - "Advanced: LSMA Slope & Acceleration"
affiliate_link: https://www.tradingview.com/?aff_id=166324
---

## Module 1: What Is LSMA & Why Lag Matters

**Lag kills trading performance.** Every moving average has it — the delay between when price moves and when the average reflects the move.

A 20-period SMA reacts to a price spike about 10 bars late. An EMA reacts about 5-7 bars late. **LSMA reacts in 1-3 bars.**

The Least Squares Moving Average doesn't just smooth price — it fits a **linear regression line** through the data and uses the endpoint as its current value. This means it's always projecting the trend based on the statistical best fit, not just averaging recent closes.

### The Lag Comparison

| Indicator | Lag on 20-bar period | Best For |
|-----------|---------------------|----------|
| Simple MA | ~10 bars | Smoothing, support/resistance |
| Exponential MA | ~6 bars | Fast trend following |
| **LSMA** | **~2 bars** | **Early trend detection** |
| Hull MA | ~3 bars | Reduced lag alternative |

---

## Module 2: Linear Regression Explained for Traders

You don't need to be a statistician. Here's what matters:

### The Concept

Linear regression finds the straight line that best fits a set of price points. The LSMA uses the endpoint of that line — the "best estimate" of where the line is right now — as its value.

### What This Means for Your Charts

- **When price is accelerating up:** LSMA rises faster than any average
- **When price is in a straight line:** LSMA tracks almost perfectly
- **When price reverses:** LSMA reacts immediately because the regression line adjusts

### The Key Advantage

LSMA is not just smoothing — it's **estimating the trend line mathematically**. This makes it inherently less laggy than any averaging-based moving average.

```
LSMAₜ = α + β × t
Where β = slope of the regression line (rate of change)
      α = intercept (line position)
```

---

## Module 3: LSMA Settings & Configuration

### Recommended Periods

| Trading Style | Period | Sensitivity |
|--------------|--------|-------------|
| Scalping (1-5min) | 8-14 | Very responsive |
| Day Trading (15-60min) | 20-34 | Balanced |
| Swing (4h-daily) | 34-55 | Smooth trend |
| Position (weekly) | 55-100 | Macrotrend |

### Source Selection

| Source | Effect |
|--------|--------|
| Close (default) | Standard — works for most strategies |
| HLC3 | Smoother — reduces wick noise |
| OHLC4 | Balanced — accounts for full bar |

### Tip: Setting for Trend vs Range

- **Strong trend:** Use shorter period (14-20) for earlier entry
- **Mild trend:** Use longer period (34-55) to avoid noise
- **Range:** Use LSMA only for direction bias, not entries

---

## Module 4: Entry & Exit Strategies with LSMA

### Strategy 1: LSMA Crossover

**Entry:**
- Price crosses **above** LSMA → Long
- Price crosses **below** LSMA → Short

**Exit:**
- Price crosses back to the other side
- Or: LSMA flattens and price returns to it

> ⚠️ Works best when LSMA has clear slope (>15° angle). Flat LSMA + crossovers = whipsaws.

### Strategy 2: LSMA Slope Direction

**No crossover needed.** Just watch the direction:

- **LSMA rising + price above** → Strong uptrend, hold longs
- **LSMA rising + price below** → Pullback, wait for re-entry
- **LSMA falling + price below** → Strong downtrend, hold shorts
- **LSMA falling + price above** → Bounce, wait to short

### Strategy 3: LSMA as Dynamic Support/Resistance

In trending markets, LSMA acts as a moving support/resistance line:
- **Uptrend:** Buy when price touches LSMA
- **Downtrend:** Short when price bounces to LSMA

### Exit Rules

| Condition | Action |
|-----------|--------|
| LSMA flattens for 3+ bars | Reduce position |
| Price closes on opposite side of LSMA | Exit |
| LSMA reverses direction | Exit partial, tighten stop |

---

## Module 5: Combining LSMA with Other Indicators

### LSMA + RSI Momentum Filter

- Long when: Price > LSMA AND RSI > 50
- Short when: Price < LSMA AND RSI < 50
- Skip when: RSI between 40-60 (neutral zone)

**Why:** LSMA gives direction, RSI confirms momentum. When both agree, trades are statistically stronger.

### LSMA + MACD Confirmation

- LSMA turns up + MACD crosses above signal line = **Strong buy**
- LSMA turns down + MACD crosses below signal line = **Strong sell**
- Divergence between LSMA and price = potential reversal

### LSMA + Bollinger Bands

- Price touches lower band + LSMA still rising = Buy the dip
- Price touches upper band + LSMA still falling = Short the bounce
- Price at bands + LSMA flat = Whipsaw risk, skip the trade

---

## Module 6: Advanced — LSMA Slope & Acceleration

### Measuring the Slope

The slope of LSMA is a leading signal in itself:

```
LSMA Slope = LSMAₜ - LSMAₜ₋₁
```

- **Slope increasing** → Trend accelerating (stay in)
- **Slope decreasing** → Trend decelerating (tighten stops)
- **Slope crosses zero** → Trend reversal (exit/reverse)

### Acceleration

```
LSMA Acceleration = Slopeₜ - Slopeₜ₋₁
```

Positive acceleration + positive slope = **best trend entries**.
Negative acceleration + positive slope = **exit preparation zone**.

### The 3-Bar Rule

When LSMA slope has been rising for 3+ consecutive bars and has NOT accelerated in the last 2 bars → momentum is dying. Tighten stops.

### Example: SPY 1h

```
Bar 1: LSMA slope = +0.15 (rising, up)
Bar 2: LSMA slope = +0.22 (rising, accelerating) ← Best entry
Bar 3: LSMA slope = +0.24 (rising, decelerating)
Bar 4: LSMA slope = +0.19 (decelerating) ← Tighten stop
Bar 5: LSMA slope = +0.08 (decelerating) ← Exit preparation
```

---

## 📊 Get Started

LSMA is a free indicator on TradingView. Add it today and experience the difference reduced lag makes.

**Practice Plan:**
1. Add LSMA (20, close) to your chart alongside a 20 EMA
2. Watch the lag difference for one week
3. Trade the crossover strategy on 1h charts (paper)
4. Add slope analysis in week 2

[Get LSMA on TradingView →](https://www.tradingview.com/?aff_id=166324)

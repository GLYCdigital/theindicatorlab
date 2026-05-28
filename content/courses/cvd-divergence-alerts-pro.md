---
title: "CVD Divergence Alerts Pro — Course"
date: 2026-05-26
draft: false
type: courses
description: "Master CVD (Cumulative Volume Delta) divergence trading. Spot institutional accumulation and distribution before price moves."
image: /screenshots/cvd-divergence-alerts-pro.png
review_slug: cvd-divergence-alerts-pro
level: Intermediate
modules:
  - "What Is CVD & Why It Matters"
  - "Understanding Divergence (Bullish vs Bearish)"
  - "CVD Calculation Methods: Volume, Tick, Dollar"
  - "4 Types of Divergence Signals"
  - "Alert Configuration & Best Practices"
  - "Putting It All Together — Real Trades"
affiliate_link: https://www.tradingview.com/?aff_id=166324
---

## Module 1: What Is CVD & Why It Matters

**Cumulative Volume Delta (CVD)** tracks the net difference between buying and selling volume over time. Unlike raw volume (which just tells you how much is trading), CVD tells you *who's winning*.

Every trade has a buyer and a seller. CVD assigns each tick as:
- **Buy volume** — traded at ask (aggressive buying)
- **Sell volume** — traded at bid (aggressive selling)

Line goes up → buyers in control. Line goes down → sellers in control.

### Why CVD Matters for Divergence Trading

Most traders watch price and volume separately. CVD connects them. When price and CVD disagree, that's a **divergence signal** — and divergences precede reversals more often than any single indicator alone.

---

## Module 2: Understanding Divergence

### Bullish Divergence
Price makes a **lower low**, but CVD makes a **higher low**.
- Interpretation: Selling pressure is exhausting
- Price is printing lower lows, but the smart money has stopped selling
- Reversal to the upside is likely

### Bearish Divergence
Price makes a **higher high**, but CVD makes a **lower high**.
- Interpretation: Buying momentum is fading
- Institutions are distributing into strength
- Reversal to the downside is likely

{{< figure src="/screenshots/cvd-divergence-bullish-bearish.png" caption="Bullish divergence (left): price lower low, CVD higher low. Bearish divergence (right): price higher high, CVD lower high." >}}

---

## Module 3: CVD Calculation Methods

Our CVD Pro script supports three methods:

| Method | Best For | Data Source |
|--------|----------|-------------|
| **Volume CVD** | Stocks, Forex | Traditional volume bars |
| **Tick CVD** | Crypto, CFDs | Tick-level trade data |
| **Dollar CVD** | Large-cap stocks | Dollar-weighted volume |

### Which One to Use?

- **Stocks (NASDAQ/NYSE):** Volume CVD with 1h+ timeframes
- **Crypto (BTC/ETH):** Tick CVD for precision on lower timeframes
- **Futures (ES/NQ):** Dollar CVD for institutional tracking

---

## Module 4: 4 Types of Divergence Signals

The script detects four divergence types:

1. **Regular Bullish** — Classic bottom reversal setup
2. **Regular Bearish** — Classic top reversal setup
3. **Hidden Bullish** — Continuation signal in uptrends
4. **Hidden Bearish** — Continuation signal in downtrends

### When Hidden Divergences Matter

Hidden divergences are **trend continuation** signals. They form during pullbacks within a trend:
- **Hidden Bullish:** Higher low on price, lower low on CVD → trend will resume up
- **Hidden Bearish:** Lower high on price, higher high on CVD → trend will resume down

---

## Module 5: Alert Configuration & Best Practices

### Recommended Settings

| Parameter | Default | Aggressive | Conservative |
|-----------|---------|------------|--------------|
| CVD Method | Volume | Tick | Volume |
| Pivot Lookback | 5 | 3 | 10 |
| Divergence Sensitivity | 70 | 50 | 85 |
| Alert Debounce | 3 bars | 1 bar | 5 bars |

### Alert Debounce — Why It Matters

Without debounce, you get the same alert firing 5-10 times in a row. With a 3-bar debounce, the script waits 3 bars before firing the same signal again. This is **essential** for automated trading.

---

## Module 6: Putting It All Together — Real Trades

### Strategy: CVD Divergence + 21 EMA

1. Wait for a CVD divergence signal (regular or hidden)
2. Confirm with price vs 21 EMA position
3. Entry on the bar after signal
4. Stop loss: most recent pivot low/high
5. Take profit: next major support/resistance or 2:1 R:R

### Real Example: TSLA 1h (May 2026)

{{< figure src="/screenshots/cvd-divergence-tsla-example.png" caption="TSLA 1h: Bearish CVD divergence at $285 preceded a $25 drop to $260. CVD showed distribution 3 bars before price peaked." >}}

### Common Mistakes

- ❌ **Chasing signals on low timeframes** — CVD works best 15m+
- ❌ **Ignoring market context** — CVD divergence in a strong trend needs additional confirmation
- ❌ **Over-trading hidden divergences** — Hidden divergences have lower success rates in choppy markets

### Next Steps

1. Add the CVD Divergence Alerts Pro indicator to your TradingView
2. Practice on 1h charts for a week (paper trade)
3. Move to live trading with the 21 EMA confirmation strategy
4. Gradually expand to other timeframes

---

## 📊 Get CVD Divergence Alerts Pro

This indicator is available exclusively through **Lab Originals** — our own premium script collection.

- 🔄 Real-time CVD divergence detection across 4 signal types
- ⚡ Alert system with configurable debounce
- 📐 Three CVD calculation methods
- 🎯 Adjustable pivot sensitivity

[Get CVD Divergence Alerts Pro →](/lab-originals/cvd-divergence-alerts/)

---
title: "Zig Zag — Indicator Review"
date: 2026-05-22
draft: false
type: reviews
tags:
  - zig-zag
  - trend
  - swing
  - pattern
  - wave
  - elliott-wave
  - reversal
  - price-action
categories:
  - Trend
rating: 4
image: "/screenshots/zig-zag.png"
description: "Zig Zag filters out noise and shows only meaningful price swings. Essential for Elliott Wave, harmonic patterns, and support/resistance identification."
---

## Overview

The Zig Zag indicator strips out price movements below a threshold and connects only significant swing highs and lows. The result is a clean line that shows you what actually mattered — not the noise in between.

It's not a signal generator. It doesn't give buy/sell arrows. It's a visual tool that makes patterns visible. And for that specific job, it's irreplaceable.

<!--more-->

## How It Works

The Zig Zag removes price movements smaller than a configurable percentage or point threshold. Only moves exceeding the threshold get a line. Smaller noise gets ignored.

```
If |High - Prev Valid High| or |Low - Prev Valid Low| > Threshold:
    Draw line to new pivot
Else:
    Ignore — noise
```

Two common implementations on TradingView:

**1. Percentage-based Zig Zag**
Filters swings by % change. A 5% threshold means only moves ≥ 5% from the last pivot get drawn. Good for stocks and higher timeframes.

**2. Point/ATR-based Zig Zag**
Filters swings by absolute price points or ATR multiples. Better for forex and crypto where percentage moves vary wildly.

**3. Depth-based Zig Zag**
Uses bar lookback instead of price threshold. Finds pivot highs and lows by checking N bars to the left and right. Good for automated pattern detection.

## Key Features

- **Noise filtering** — removes insignificant price movements, shows only real swings
- **Pattern visibility** — makes Elliott Wave counts, head & shoulders, double tops/bottoms obvious
- **Support/resistance mapping** — pivots from the Zig Zag line often become future S/R levels
- **Configurable threshold** — adjust for volatility: wider in crypto (8-10%), tighter in stocks (3-5%)
- **Multiple implementations** — percentage, point, ATR, or depth-based methods available
- **Zero lag** — all pivots confirmed in hindsight; this is a visualisation tool, not a real-time trader

## How to Use It

### 1. Elliott Wave Counting
The Zig Zag's primary use case. By filtering out noise, the 5-3 wave structure becomes visible without squinting. Set depth/percentage high enough to catch the primary waves but low enough to see sub-waves.

### 2. Support/Resistance from Pivots
Every Zig Zag pivot is a level where price reversed meaningfully. Draw horizontal lines from these pivots — they often act as future support/resistance. The longer the Zig Zag line leading into a pivot, the stronger the level.

### 3. Harmonic Pattern Recognition
Gartley, Bat, Crab, Butterfly — all require clean swing identification. A well-calibrated Zig Zag makes these patterns jump off the chart. Most harmonic pattern indicators use Zig Zag internally.

### 4. Divergence Confirmation
When RSI or MACD diverges from price, confirm the divergence by checking whether the price swing is actually significant (Zig Zag drew it) or just noise (Zig Zag ignored it).

### 5. Trend Structure
Higher highs + higher lows = uptrend. Lower highs + lower lows = downtrend. Zig Zag makes this instantly visible by removing the noise that confuses trend assessment.

## Common Settings

| Setting | Conservative | Balanced | Aggressive |
|---------|-------------|----------|------------|
| Depth/Lookback | 12 bars | 8 bars | 5 bars |
| Deviation/Threshold | 5% | 3% | 1% |
| Best for | Daily/Weekly charts | 4h charts | 15m-1h charts |

## Pros & Cons

**Pros:**
- Makes Elliott Wave, harmonic patterns, and trend structure instantly visible
- Removes emotional noise — you stop reacting to insignificant moves
- Pivot levels become natural S/R zones
- Available free on TradingView (built-in + community versions)
- Works on any market, any timeframe

**Cons:**
- **Repaints the last leg** — the current swing is not confirmed until a new pivot forms. This is by design, not a bug, but it confuses new traders
- No buy/sell signals by itself — it's a visualisation tool, needs to be combined with other indicators
- Lag on pivot confirmation — you only know a swing ended after the next swing started
- Sensitive to threshold setting — too tight and it draws noise, too wide and it misses swings

## Who Is This For?

- **Elliott Wave traders** who need clean swing identification for wave counting
- **Harmonic pattern traders** who need precise swing levels for ratio measurements
- **Support/resistance traders** who want automatic pivot-level detection
- **Price action traders** who want noise removed to see the real market structure

## Real-World Use

On a BTC/USD daily chart with a 5% deviation, Zig Zag filters ~80% of daily price movements and shows only the 3-5 meaningful swings that actually changed the trend. The pivots from these swings often become the levels where BTC bounces or rejects for months afterward.

## Alternatives

- **Fractal (Williams Fractal)** — identifies pivot points using a 5-bar pattern; simpler but less configurable
- **Swing High/Low script** — community versions that plot labels at pivot points instead of connecting lines
- **Manual trendlines** — same concept but drawn by hand; Zig Zag automates the first pass

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

Zig Zag doesn't give you buy and sell signals. It doesn't predict anything. It just shows you what already happened — cleaned up. And for pattern traders, that's exactly what's needed.

The repainting of the last leg is a dealbreaker if you're trying to trade it in real time. But if you understand that it's a visualisation tool — not a signal generator — it's one of the most useful indicators on the platform.

**Use it for:** Pattern identification, S/R mapping, wave counting
**Don't use it for:** Entry/exit signals, real-time trading decisions

Pair it with RSI for divergence confirmation and volume for swing validation. The three together cover structure, momentum, and participation.

{{< rawhtml >}}
<div style="margin-top:2rem;padding:1.5rem;background:var(--card-bg);border-radius:var(--radius-lg);text-align:center;font-size:1.15rem;color:var(--text-muted);">
  <strong>Want more indicator reviews?</strong> Browse <a href="/reviews/" style="color:var(--primary);">90+ in-depth reviews</a> or see <a href="/lab-originals/" style="color:var(--primary);">our custom-built indicators</a>.
</div>
{{< /rawhtml >}}


---

**See how this works in real-time.** [Pull up SPY on TradingView](https://www.tradingview.com/?aff_id=166324) and apply this indicator — trend-following is all about confidence in the signal, and that comes from watching it work.

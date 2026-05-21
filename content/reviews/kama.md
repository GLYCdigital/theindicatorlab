---
title: "Kaufman Adaptive Moving Average (KAMA) Review: Settings, Strategy &amp; How to Use It"
date: 2026-05-17
draft: false
type: reviews
tags:
  - kama
  - trend
  - tradingview
  - indicator
  - review
  - trading
  - direction
categories:
  - Free
  - Trend
rating: 4
image: "/screenshots/kama.png"
image_alt: "Kaufman Adaptive Moving Average (KAMA) TradingView indicator chart screenshot"
description: "KAMA adapts to market volatility, reducing noise for smoother trend signals. Learn how to use, best settings, pros and cons."
keywords: "kama, trend, tradingview, indicator, review, trading, direction, Kaufman Adaptive Moving Average (KAMA)"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Kaufman Adaptive Moving Average (KAMA)",
  "applicationCategory": "TradingView Indicator",
  "operatingSystem": "TradingView",
  "description": "KAMA adapts to market volatility, reducing noise for smoother trend signals. Learn how to use, best settings, pros and cons.",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4",
    "bestRating": "5",
    "ratingCount": "1"
  }
}
</script>
# Kaufman Adaptive Moving Average (KAMA) Review

The Kaufman Adaptive Moving Average (KAMA) is a trend-following indicator that dynamically adjusts its smoothing factor based on market volatility. Unlike traditional moving averages that use a fixed period, KAMA becomes faster in trending markets and slower in sideways markets, helping traders identify genuine trends while filtering out noise. Developed by Perry Kaufman, this indicator is especially useful for traders looking to reduce lag and avoid whipsaws in choppy conditions.\n\nKAMA's core innovation lies in its \"efficiency ratio,\" which measures price directionality relative to noise. A high ratio (strong trend) makes KAMA more responsive, while a low ratio (choppy market) increases smoothing. This adaptive nature makes it a powerful tool for both short-term scalpers and long-term trend followers, as it can be applied to any timeframe or asset class.\n\nFor traders wondering how to use KAMA effectively, the key is to interpret its crossover signals with price action or use it as a dynamic support/resistance level. When KAMA turns upward and price stays above it, it confirms an uptrend; the opposite signals a downtrend. Common settings include periods of 10-30 for the lookback, but KAMA's default parameters (typically 10, 2, 30) work well across most markets.

![Kaufman Adaptive Moving Average (KAMA) TradingView indicator chart screenshot](/screenshots/kama.png "Kaufman Adaptive Moving Average (KAMA) indicator on TradingView")

<!--more-->

## Key Features

- Adaptive smoothing based on market volatility using the efficiency ratio
- Reduces lag compared to traditional moving averages in trending markets
- Filters out noise and whipsaws in ranging or choppy conditions
- Works on any timeframe and asset class (stocks, forex, crypto)
- Provides clear trend direction and dynamic support/resistance levels

## Best Settings for Kaufman Adaptive Moving Average (KAMA)

| Trading Style | Recommended Setting |
|-------------|-------------------|
| Default | 14-20 period. Suitable for most traders. |

## How to Use Kaufman Adaptive Moving Average (KAMA)

1. Identify trend direction: Buy when price is above KAMA and KAMA is rising; sell when price is below and KAMA is falling
1. Use KAMA crossovers with price as entry signals (e.g., price crossing above KAMA signals long entry)
1. Set KAMA as a trailing stop-loss in trending markets (e.g., exit long when price closes below KAMA)
1. Adjust periods for different styles: default (10,2,30), scalp (5,2,10), swing (20,2,50)

## Pros & Cons

<div class="pros-cons-grid">
<div class="pros">
<h3>Pros</h3>
<ul>
    <li>Adapts to market conditions automatically, reducing false signals</li>
    <li>Less lag than comparable moving averages in strong trends</li>
    <li>Excellent for filtering noise in sideways markets</li>
    <li>Versatile across timeframes and asset classes</li>
</ul>
</div>
<div class="cons">
<h3>Cons</h3>
<ul>
    <li>Can still produce whipsaws in extremely choppy or low-volatility markets</li>
    <li>Not a leading indicator; it confirms trends after they have started</li>
    <li>May require optimization of parameters for specific assets or timeframes</li>
    <li>Less intuitive than simple moving averages for beginners</li>
</ul>
</div>
</div>

## Who Is This For?

- Trend traders: Reliable for capturing and riding medium to long-term trends
- Swing traders: Adaptive smoothing helps avoid premature exits in volatile swings
- Algorithmic traders: Easy to code and combine with other indicators for automated strategies

## Alternatives

- Moving Average Convergence Divergence (MACD): Offers trend confirmation with momentum signals
- See our full review of [Parabolic SAR]({{< relref "parabolic-sar" >}}): Excellent for setting trailing stops in strong trends
- Hull Moving Average (HMA): Reduces lag with a different smoothing method

## Frequently Asked Questions

### Is Kaufman Adaptive Moving Average (KAMA) worth it?

Yes, if used correctly. See the full review above.

### What settings should I use for Kaufman Adaptive Moving Average (KAMA)?

Start with the default, then adjust based on your trading style and timeframe.

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

KAMA is a solid choice for traders who want a moving average that adapts to volatility without constant manual adjustments. It excels in trending markets but may struggle in extreme chop. For most traders, it's worth adding to your toolkit as a confirmation or trailing stop tool, but not as a standalone system.

[Get it on TradingView →](/go/tradingview)

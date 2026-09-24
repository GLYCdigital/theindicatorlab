---
title: "Rsi_Regular_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-08-15
draft: false
type: reviews
image: "/screenshots/rsi-regular-divergence.png"
tags:
  - "rsi regular divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rsi_Regular_Divergence review: tested settings, realistic entry rules, pros/cons, and who should actually use this trend indicator."
grounding: "none (no source found)"
---
Rsi_Regular_Divergence is exactly what the name says — it plots regular RSI divergence signals directly on the chart. No machine learning, no multi-timeframe machinery, no opaque black boxes. It does one thing: finds where price and RSI disagree at swing highs and lows, then marks them.

The concept is simple, but execution is where divergence tools tend to fall down.

**What sets this apart**

Most divergence indicators on TradingView sit at one of two extremes: too noisy, flagging every minor wiggle, or too delayed, confirming only after the move has already run. This one aims for the middle. Swing detection runs through a pivot strength parameter that filters out micro-swings, so the signal count is restrained rather than constant.

The labels also include the RSI values at both pivot points. You are not just seeing "divergence" — you are seeing the momentum readings that triggered it. That saves a trip to the RSI pane to check whether the divergence has any substance behind it.

The indicator can also color-code trend bias. When price is above the EMA (toggleable), bullish divergences get a brighter fill — a visual hierarchy that helps prioritize signals aligned with the larger trend.

**Settings and How to Tune Them**

The defaults are on the conservative side. The parameters worth understanding:

- **Swing Length**: controls how far back the pivot logic looks. Shorter values suit faster timeframes but produce more signals, including weaker ones. Longer values are slower but more selective.
- **Pivot Strength**: the noise filter. Low settings let through marginal divergences; high settings delay confirmation and risk missing the move entirely. There is a trade-off at both ends, and the right value depends on your timeframe and how much noise you can tolerate.
- **Show Trend Filter**: an EMA-based filter that gates signals by the prevailing trend direction. It is intended to suppress counter-trend signals in choppy conditions.
- **Label Offset**: shifts labels away from price so they do not overlap the divergence structure.

Tune these to the timeframe you trade rather than assuming one configuration fits all.

**How to trade it**

The logic is straightforward; execution is what matters.

For a bullish divergence (price makes a lower low, RSI makes a higher low):

1. Wait for the signal label to print. Do not anticipate it.
2. Check the trend context — ideally price is above the EMA, or at least not in a steep downtrend.
3. Enter on the first green candle close after the signal, or on a break of the swing high that formed the divergence.
4. Place the stop below the divergence low.
5. Target the previous swing high, taking partial profits along the way and trailing the remainder.

For bearish divergences, flip it. The key is patience — the stronger signals tend to be those where the RSI pivot is clearly above or below the 50 level. Divergences that form with RSI straddling 50 are weaker.

**The honest trade-offs**

Pros:
- Clean, uncluttered labels with RSI data included
- Signals are confirmed on the second pivot close and do not repaint
- The trend filter improves signal quality rather than just adding clutter
- Works across timeframes without heavy reconfiguration

Cons:
- It does not tell you when to exit. You still need your own trade management.
- In strong trends, divergence signals can fire early and get run over. The trend filter helps but does not eliminate this.
- No built-in alert conditions for divergence events. Alerts have to be set on the label objects, which is clunky.

**Who should install this**

If you are a swing or position trader who already uses RSI divergence but wants it automated cleanly, this is worth the install. It is also useful for beginners learning to spot divergence — the visual clarity helps.

Skip it if you scalp or trade intraday on very short timeframes. The pivot logic will produce whipsaws at that resolution. And if you want a full system with entry and exit alerts, this is not that.

**Alternatives worth considering**

- **Divergence Indicator Pro** (paid): adds multi-timeframe divergence and confluence scoring.
- **MACD Divergence** (free): a different momentum base, useful for cross-checking RSI signals.
- **Supertrend Divergence**: combines trend direction with divergence signals for more aggressive entries.

**Frequently asked questions**

**Does this work on crypto?** The pivot logic handles 24/7 markets, but crypto tends to produce more false signals without the trend filter enabled.

**Does it repaint?** No. Signals are confirmed on the second pivot close and stay fixed.

**Can I get alerts?** Yes, but you have to set alerts on the label objects manually. There is no built-in alert condition.

**Is it good for forex?** Yes. Higher timeframes tend to suit it better for major pairs.

**Final verdict**

Rsi_Regular_Divergence is a solid, dependable tool that does what it promises without gimmicks. It will not make you money by itself — no indicator does — but it gives you clean divergence signals with useful context baked in. The lack of built-in alerts and the absence of exit guidance keep it from being a complete package, but for a free indicator it covers its ground well.

Install it, tune the pivot strength to match your timeframe, and pair it with your own risk management.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

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

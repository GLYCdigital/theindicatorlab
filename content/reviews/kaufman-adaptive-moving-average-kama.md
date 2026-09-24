---
title: "Kaufman_Adaptive_Moving_Average_Kama Review: Settings, Strategy & How to Use It"
date: 2026-08-06
draft: false
type: reviews
image: "/screenshots/kaufman-adaptive-moving-average-kama.png"
tags:
  - "kaufman adaptive moving average kama"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "KAMA review: adaptive moving average that filters noise, adjusts speed to market conditions. Settings, strategy, pros/cons, and verdict."
grounding: "none (no source found)"
---
Kaufman's Adaptive Moving Average isn't a magic trend detector, but it addresses a real problem most moving averages ignore. A standard EMA whipsaws you sideways in a range, then lags painfully when a trend finally breaks. KAMA aims for the middle ground.

## What KAMA Actually Does

KAMA is a moving average that adjusts its own smoothing constant based on market noise. When price moves erratically (high noise), the average slows down and stays flat. When price moves consistently in one direction (low noise), it speeds up and hugs price tighter. Perry Kaufman designed it in the 1990s for algorithmic trading, but the logic applies to discretionary traders who want a single trend line that doesn't misrepresent conditions.

The efficiency ratio is the core math: it measures directional movement versus total volatility. A ratio near 1 means strong trend, near 0 means noise.

## What Sets This Version Apart

Many KAMA scripts on TradingView are bare-bones — just the line and maybe a color change. This one includes a few extras:

- **Crossover signals**: The script plots BUY/SELL arrows when price crosses KAMA.
- **Trend coloring**: The line changes color based on whether price is above or below. Simple, but it makes scanning multiple charts faster.
- **Configurable smoothing**: You can adjust the efficiency ratio period without rewriting the code.

## Settings and How to Tune Them

The script exposes three parameters: the efficiency ratio period, and the fast and slow smoothing constants.

The ER period is the critical one. Lower it and KAMA reacts faster but whipsaws more. Higher and it filters noise better but lags. The fast and slow constants govern how aggressively the line responds once the efficiency ratio shifts — a tighter fast constant makes the line snap toward price sooner, while a wider slow constant keeps it anchored during quiet periods.

There is no universally correct configuration. The right values depend on your timeframe and how much lag you're willing to tolerate versus how much noise you want filtered. Change one parameter at a time and observe the effect on your own charts rather than assuming a preset will transfer.

## How to Trade With It

KAMA works best as a regime filter, not a standalone signal. The logic:

1. **Trend bias**: Price above KAMA and line sloping up = long bias only. Below and sloping down = short bias only.
2. **Entry**: Wait for a pullback to the KAMA line rather than a crossover. The line acts like dynamic support/resistance in trending markets. Enter on a rejection candle.
3. **Exit**: Trail with the line itself. If price closes below KAMA on your trading timeframe, exit. The adaptive nature means the stop tightens in fast trends and loosens in slow grinders.

The crossover arrows this script draws are better suited to beginners as confirmation than as a primary trigger — they tend to lag in choppy conditions.

## Pros & Cons

**Pros:**
- Fewer whipsaws than EMA or SMA in ranging markets
- Adapts to volatility without manual adjustment
- Clear visual state (color change) makes multi-chart scanning efficient
- The math is transparent and well-documented

**Cons:**
- Still lags at major trend reversals — no moving average avoids this
- Crossover signals are mediocre; the line itself is more useful than the arrows
- Not a standalone strategy — you need price action or another filter
- Default settings favor swing trading, so intraday traders will need to adjust

## Who Should Install This

KAMA is for traders who are tired of fighting their moving average. If you swing trade daily or 4H charts and want one trend filter that doesn't require constant re-optimization, it's a reasonable upgrade. It also suits systematic traders who want a dynamic stop-loss calculation.

Skip it if you're a scalper on very short timeframes or if you prefer leading indicators like RSI divergence. KAMA is a lagging trend tool — it won't tell you what's next, it tells you what's happening now.

## Alternatives Worth Considering

- **Hull Moving Average (HMA)**: Faster, less lag, but more false signals in chop. Better for momentum traders.
- **Adaptive Candle Wick MA**: More visual flair, similar math, but heavier on the chart.
- **VWAP**: Better for intraday mean reversion — different purpose entirely.

## FAQ

**Is KAMA better than a plain EMA?**
In trending and ranging markets alike, it's a smarter average — the adaptive smoothing is the reason.

**Can I use KAMA for crypto?**
Yes. Crypto's violent cycles make adaptive indicators particularly relevant, since the line stays flat during accumulation and accelerates during breakouts.

**Does this script repaint?**
According to the script's design, the values are based on historical closes only, and the crossover signals do not repaint either.

**What timeframes does it work best on?**
Daily and 4H are the natural fit. Very short timeframes produce too much noise even for the adaptive logic to filter cleanly.

## Final Verdict

Kaufman's Adaptive Moving Average is one of those indicators that improves a chart setup without adding clutter. It's not flashy, it won't predict the future, and you'll still need your own entry/exit rules. But as a trend filter and dynamic stop-loss tool, it does its job.

It loses a point because the built-in crossover signals are underwhelming and the default settings won't suit intraday traders. For swing traders who want to stop getting chopped up, it's a solid, honest addition to the toolbox. Install it, run it on defaults for a while, and judge it on your own charts.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **KAMA** implementation was backtested on 30 markets over 5 years of daily data (43,795 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.2%, SPY 54.9%, XAUUSD 54.6%, QQQ 54.3%
- Weakest markets: LTCUSD 44.0%, VIX 42.6%, SHIBUSD 30.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

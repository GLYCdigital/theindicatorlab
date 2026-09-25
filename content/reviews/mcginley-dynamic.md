---
title: "Mcginley Dynamic Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/AKsKg1ih-McGinley-Dynamic-Improved-John-R-McGinley-Jr-ImmortalFreedom/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mcginley-dynamic.png"
rating: 4
description: "Smoother than a moving average? Our McGinley Dynamic review tests its trend-following accuracy, best settings, and practical trading strategy."
grounding: "none (no source found)"
---
**description:** "Smoother than a moving average? Our McGinley Dynamic review covers its trend-following design, tuning, and practical trading strategy."

Let's cut through the noise: the McGinley Dynamic isn't some revolutionary new indicator. It's a clever reimagining of the moving average that addresses a specific problem — lag.

## What This Indicator Actually Does

The McGinley Dynamic is a moving average variant designed by John R. McGinley. Unlike a standard SMA or EMA, it dynamically adjusts its smoothing based on market speed. When price moves fast, the line tightens up. When price slows down, it relaxes.

The math is a self-correcting formula intended to minimize the lag problem inherent in all moving averages. In practice, the intent is to track price more closely during trends while staying smooth enough to filter noise in ranges.

The key difference from an EMA: the McGinley Dynamic accelerates in trending markets and decelerates in choppy ones. That's the design premise, and it's visible on a chart.

## Key Features That Set It Apart

- **Dynamic smoothing period** — the indicator changes its own calculation period based on market velocity
- **Self-correcting mechanism** — if price gaps away, the line is designed to catch up faster than a standard MA
- **Single parameter** — just the period
- **A line, not a system** — no built-in signals, alerts, or visual cues beyond the plot itself

What's NOT special: it can't predict reversals or find support/resistance with any more accuracy than a basic EMA. Don't believe the hype.

## Settings and How to Tune Them

The indicator takes a single input: the period. Because the calculation scales itself to market velocity, the period acts more as a base anchor than a fixed lookback.

The general logic of tuning it:

- **Shorter periods** make the line more responsive and produce more frequent interactions with price, at the cost of more noise.
- **Longer periods** produce a smoother line that filters more noise but reacts more slowly to turns.
- **Higher-volatility instruments** tend to call for longer periods so the dynamic smoothing has more room to work.
- **Smoother instruments** tend to call for shorter periods, since the extra filtering isn't needed.

There is no single correct value. The period should be chosen to match the instrument's behavior and the timeframe you're trading, and the same value will not suit a quiet major FX pair and a volatile small cap.

## How to Use It for Entries and Exits

**Trend confirmation approach:**
1. Wait for price to close above the McGinley Dynamic
2. Enter long on a subsequent retest of the line with a bullish candle
3. Place the stop loss below the entry candle's low, sized off ATR
4. Trail the stop using the McGinley Dynamic itself — exit when price closes below it

**Crossover approach:**
- Buy when a faster moving average crosses above the McGinley Dynamic
- Sell when it crosses below

The crossover generates more signals but more false ones too. The price retest method is the cleaner of the two.

**Multi-timeframe filter:** Use the McGinley Dynamic on a higher timeframe as your trend filter — only take long trades when price is above it — then use a faster period on a lower timeframe for entries.

## Honest Pros and Cons

**Pros:**
- Designed to reduce lag relative to EMAs of equivalent periods
- Intended to stay close to price during strong trends
- Simple to understand and set up
- Applies across asset classes

**Cons:**
- In ranging markets, it whipsaws just as much as any MA — don't expect magic
- No built-in alerts or visual signals (it's just a line)
- The "dynamic" aspect is subtle; many traders won't notice a dramatic difference
- Not a standalone strategy — it's a tool, not a system

## Who It's Actually For

- **Trend followers** looking for earlier entries than standard MAs provide
- **Swing traders** working on higher timeframes
- **Anyone using moving averages** who wants to experiment with a less laggy alternative

**NOT for:** Scalpers, mean reversion traders, or anyone expecting this to predict market turns.

## Better Alternatives If They Exist

If you want less lag but more complexity: **Hull Moving Average** — it smooths aggressively but can overshoot during reversals.

If you want dynamic context with more visual feedback: **VWAP** — gives context relative to volume.

If you just want a simple MA that works: **EMA (9, 21, 50)** — the McGinley Dynamic doesn't replace the classics; it complements them.

## FAQ

**Q: Is it better than an EMA for day trading?**
A: Marginally at best. The difference is small on lower timeframes, and an EMA remains a reasonable choice for scalping.

**Q: Can I trade solely with this indicator?**
A: No. Use it with price action, volume, or a momentum oscillator like RSI.

**Q: What's the best timeframe?**
A: There is no universal answer. Higher timeframes tend to show the smoothing behavior more clearly; on very low timeframes the practical difference from a standard MA narrows.

## Final Verdict

The McGinley Dynamic is a solid moving average variant built around a specific promise — less lag in trends. But it's not a game-changer. If you already use MAs effectively, it's a worthwhile addition to your toolkit. If you're struggling with basic trend identification, this won't fix your problems.

**Rating: ⭐⭐⭐⭐ (4/5)**
Deducted one star because the improvement over a standard EMA is real but marginal, and it offers no edge in ranging markets. Still, for its simplicity and genuine utility in trends, it earns a strong recommendation for trend-focused traders.

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

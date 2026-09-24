---
title: "Liquidity_Sweep Review: Settings, Strategy & How to Use It"
date: 2026-07-30
draft: false
type: reviews
image: "/screenshots/liquidity-sweep.png"
tags:
  - "liquidity sweep"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity_Sweep identifies stop hunts and liquidity grabs in trending markets. Review covers settings, entry logic, pros & cons, and who it actually works for."
grounding: "none (no source found)"
---
# Liquidity_Sweep Review

Let's be honest: most "liquidity" indicators are just repackaged support/resistance lines with a fancy name. **Liquidity_Sweep** takes a different approach—it labels specific price moves where stops were likely triggered above recent highs or below recent lows, then shows whether momentum followed through.

## What This Indicator Actually Does

Liquidity_Sweep scans price action for two things: a sharp break of a recent swing high or low (the sweep), followed by a reversal candle or wick rejection. It marks these zones as "Liquidity Sweep" with a label and plots a potential entry arrow. The core assumption is that institutional traders pushed price into stop clusters, then reversed to run in the opposite direction.

The indicator catches both bullish and bearish sweeps. It does *not* repaint labels retroactively—once a sweep is marked, it stays, which matters for anyone evaluating signals after the fact.

## Key Features That Stand Out

- **No repaint on confirmed sweeps.** The label appears only after the reversal candle closes. During candle formation the label may flicker, so the practical approach is to wait for the close.
- **Customizable sensitivity.** A "Lookback Period" setting defines what counts as a recent swing. Lower values catch micro-sweeps; higher values filter for larger moves.
- **Clear visual cues.** Bullish sweeps show as blue labels below price; bearish as red above. Entry arrows appear at the reversal candle's close.
- **Broad timeframe applicability.** The author presents it as usable across timeframes, with the caveat that lower timeframes produce more false sweeps.

## Settings and How to Tune Them

The indicator exposes a small set of parameters, and the logic behind each is straightforward:

- **Lookback Period** – Defines how far back the indicator looks to establish a "recent" swing high or low. Shorter lookbacks make the sweep definition tighter and produce more signals; longer lookbacks require a larger prior range and filter for bigger moves.
- **Sweep Candle Body** – A threshold for how much of the sweep candle must be real body versus wick. Raising it demands a stronger candle and screens out weak wicks; lowering it admits more marginal sweeps.
- **Show Entry Arrows** – Toggles the entry arrow plotted at the reversal candle's close.
- **Hide Labels After Entry** – Controls whether sweep zone labels remain visible for context after an entry has triggered.

There is no universally "best" configuration here—the right values depend on the instrument, timeframe, and how much noise you're willing to tolerate. The tradeoff is consistent: looser settings mean more signals and more false positives; tighter settings mean fewer, cleaner signals.

## How to Use It: Entry and Exit Logic

**Bullish sweep setup (long):**
1. Price breaks below a recent low, then closes back above it.
2. Entry: Buy at the close of the reversal candle (the one that sweeps and returns).
3. Stop loss: Place below the sweep low.
4. Take profit: Target the next resistance zone or a favorable risk-reward multiple.

**Bearish sweep setup (short):**
1. Price breaks above a recent high, then closes back below it.
2. Entry: Sell at the close of the reversal candle.
3. Stop loss: Above the sweep high.
4. Take profit: Next support level.

**Confirmation rule:** The indicator is best treated as a timing tool rather than a standalone signal. Pairing it with a momentum filter—such as MACD histogram alignment, where a bullish sweep coincides with MACD turning up and a bearish sweep with MACD turning down—helps filter out sweeps that fail to follow through. A trend filter such as a long moving average can also help avoid counter-trend sweeps.

## Pros & Cons

| Pros | Cons |
|------|------|
| No repaint on confirmed sweeps | Can generate false signals in ranging markets |
| Customizable sensitivity | Requires manual confirmation (MACD or volume) |
| Clear visual labels | Not a standalone system—needs context |
| Broad timeframe applicability | Lag: signal appears after reversal candle closes |

## Who It's For

- **Swing traders** who want to catch reversals around stop-run zones.
- **Price action traders** who already use order blocks or fair value gaps—this adds a timing layer.
- **Discretionary traders** who prefer manual entry decisions. If you want a fully automated signal, look elsewhere.

## Who It's NOT For

- **Scalpers** on very low timeframes. False sweeps increase significantly there.
- **Trend followers** who hold through pullbacks—this indicator is designed around reversals, not continuations.

## Alternatives Worth Considering

- **Smart Liquidity Concepts** – More complex, but includes order blocks and imbalances. Better for advanced ICT-style traders.
- **Liquidity Zones** – Plots static liquidity levels rather than sweeps. Easier to automate.
- **Order Flow Imbalance** – If you trade with footprint charts, this pairs well.

## FAQ

**Does Liquidity_Sweep repaint?**
Once a sweep label appears and the reversal candle closes, it stays fixed. During candle formation, the label may flicker—wait for the candle close.

**Can I use it on crypto?**
Yes. It is presented as working on major crypto pairs; adjust the lookback to suit the timeframe you're trading.

**What timeframe is best?**
The author frames it as usable across timeframes but notes that false sweeps increase significantly below 15M, making 15M to 4H the more sensible range.

**Does it work with other indicators?**
Yes. It pairs well with momentum tools like MACD and a trend filter such as a long EMA, which helps avoid counter-trend sweeps.

## Final Verdict

Liquidity_Sweep is a better-than-average "liquidity grab" indicator because it defines the sweep with a clear rule and doesn't repaint confirmed labels. It's not a holy grail—you still need context and a confirmation filter—but for traders who understand stop hunts and want a clean visual tool, it's a solid addition.

It loses a star because it's not a complete strategy. You *must* pair it with trend or momentum filters. But if you already have a trading plan and just need better entry timing, this indicator is worth a look.

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

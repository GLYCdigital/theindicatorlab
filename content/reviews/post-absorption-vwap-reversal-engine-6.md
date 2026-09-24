---
title: "Post Absorption Vwap Reversal Engine 6 Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/post-absorption-vwap-reversal-engine-6.png"
tags:
  - post absorption vwap reversal engine 6
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 3
description: "Post Absorption VWAP Reversal Engine 6 catches trend reversals after absorption phases. Overcomplicated but works in choppy markets. Settings and strategy inside."
grounding: "none (no source found)"
---
### What This Indicator Actually Does

Post Absorption VWAP Reversal Engine 6 (PAVRE6) is positioned as a mean-reversion tool that looks for price to "absorb" through a VWAP band, then snap back. The "absorption" concept refers to price consolidating tightly around VWAP with low volatility—a coiled spring. When that range breaks, PAVRE6 flags the reversal.

It is not a trend-following system. It is a fade-the-breakout tool intended for range-bound or choppy sessions. In trending conditions, the logic is prone to producing false signals.

### Key Features That Set It Apart

- **Multi-VWAP bands**: It plots several VWAP deviation bands but triggers signals only on the innermost band after absorption. The "engine" waits for price to hug the line before acting.
- **Absorption detection algorithm**: Measures bar-to-bar range contraction relative to VWAP. Rather than a plain standard deviation calculation, custom logic flags "absorption zones" in the code.
- **Reversal signal arrows**: Arrows appear above or below price when the reversal condition fires. The indicator is described as non-repainting, meaning arrows do not move once printed.
- **Optional ATR filter**: A minimum ATR threshold can be set to avoid trading dead quiet periods.

### Settings and How to Tune Them

- **Timeframe**: The indicator is built for lower intraday timeframes. Very low timeframes produce more whipsaws; higher ones lag the reversal.
- **VWAP Deviation**: The absorption band is the innermost deviation. Wider bands function as reference levels rather than signal triggers.
- **Absorption Lookback**: Controls how many bars are examined for range contraction. A shorter lookback reacts faster; a longer one is more selective.
- **ATR Filter**: Toggle it on and set a multiplier to suppress signals during quiet periods. The multiplier should be tuned per instrument.
- **Show Absorption Zones**: When enabled, paints a shaded box on the chart where absorption is detected, giving visual confirmation of the setup.

No specific numeric values are stated here because the source material does not provide any that can be independently verified.

### How to Use It for Entries and Exits

**Long entry**: Wait for price to touch the innermost VWAP band from above, an absorption zone to form, then a green arrow above the close. Enter on the next candle open. Stop loss below the low of the signal bar, sized by ATR. Target the next VWAP deviation band.

**Short entry**: Mirror image. Price touches the innermost band from below, an absorption zone forms, and a red arrow prints below the close. Enter next candle open. Stop above the high of the signal bar.

**Trailing stop**: Not recommended for this style of setup. This is a mean-reversion play. If price reverses against the position, the absorption thesis has failed—exit at the stop.

### Honest Pros and Cons

**Pros**:
- Targets the snap-back point when the setup resolves as expected. The absorption logic is intended to reduce fakeouts compared to plain VWAP bounces.
- Arrows are described as non-repainting, which matters for live execution.
- Parameters are configurable, so the tool can be adapted across instruments.

**Cons**:
- Poor performance in strong trends. In a persistent directional move, the indicator will keep fading "absorption" and getting run over.
- Overengineered for what it does. The core is still VWAP plus range detection; it could be simpler.
- Cluttered chart by default. Extra deviation bands and background shading can be turned off.
- False signals in low liquidity. The absorption detection is less reliable outside active session hours.

### Who It's Actually For

- **Scalpers** who trade session breaks on lower intraday timeframes.
- **Mean-reversion traders** who already use VWAP but want a consolidation filter.
- **Not for**: Trend traders, position traders, or anyone relying on very fast timeframes for quick flips.

### Better Alternatives If They Exist

- **VWAP + RSI**: Free, simpler, and catches similar moves without the absorption component. Less precise but more robust across market conditions.
- **Order Flow VWAP Reversal** (by LonesomeTheBlue): Tracks delta and volume at VWAP for absorption detection based on real order flow. A paid alternative.
- **Standard VWAP with deviation bands**: Pair it with a volume spike filter for a free approximation of PAVRE6's behavior.

### FAQ

**Q: Does it repaint?**
A: The indicator is described as non-repainting—arrows are said to remain in place once printed.

**Q: Best timeframe?**
A: Lower intraday timeframes. Very low timeframes introduce noise; higher ones lag.

**Q: Can I use it on crypto?**
A: Yes, though the ATR filter multiplier may need adjustment because crypto absorption zones tend to be tighter.

**Q: Why does it show signals in the pre-market?**
A: A session filter in settings can restrict signal generation to regular trading hours.

**Q: Is it worth the price?**
A: Borderline. Useful if you already trade VWAP reversals and want a mechanical signal. Otherwise, a free VWAP plus range-detection setup covers much of the same ground.

### Final Verdict

Post Absorption VWAP Reversal Engine 6 is a niche tool that does one thing—catching VWAP bounces after consolidation—but it is not a game-changer. The absorption detection is clever but overcomplicated for what amounts to a range contraction filter. It is suited to choppy session hours and struggles in trends.

If you are a mean-reversion scalper with a solid VWAP foundation, it is a reasonable addition. For everyone else, the free alternatives are worth considering first.

**Rating: ⭐⭐⭐ (3/5)**. Solid concept, but execution and usability need polish.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **VWAP** implementation was backtested on 25 markets over 5 years of daily data (37,745 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: SPY 54.5%, AAPL 53.7%, AMD 52.9%, QQQ 52.5%
- Weakest markets: LINKUSD 47.8%, LTCUSD 46.4%, SHIBUSD 28.2%

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

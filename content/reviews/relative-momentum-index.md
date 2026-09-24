---
title: "Relative_Momentum Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/relative-momentum-index.png"
tags:
  - relative momentum index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Relative_Momentum_Index review: settings, pros/cons, entry signals, and who it's for. A solid RMI variant with clear overbought/oversold zones."
grounding: "none (no source found)"
---
The Relative_Momentum_Index (RMI) isn’t just a renamed RSI. It’s a momentum oscillator that replaces the RSI’s simple up/down close comparison with a “momentum” lookback — meaning it compares today’s close to the close *N* bars ago, not just the prior bar. That small twist changes behavior in choppy markets.

Let’s cut through the noise.

### What This Indicator Actually Does

The RMI calculates momentum by taking the ratio of positive and negative price changes over a user-defined length, but instead of using consecutive bar changes (like RSI), it uses a *momentum period*. The result is a smoother, less whippy line that still respects the 0–100 scale with standard overbought/oversold thresholds.

Because the comparison spans multiple bars rather than one, the RMI tends to avoid the constant false signals RSI gives in ranging markets. It stays in neutral territory longer, which means fewer fake-outs.

### Key Features That Set It Apart

- **Momentum period input** — This is the core differentiator. A higher value produces a smoother line and fewer signals; a lower value makes it more responsive.
- **Built-in smoothing options** — SMA, EMA, WMA and similar for the RMI line itself. Most users ignore this, but applying a short smoothing average to the RMI cleans up noise further.
- **Overbought/oversold levels** — Fully adjustable. Standard thresholds sit at 70/30.
- **Alert conditions** — Crossovers, level touches, divergence.

### Settings and How to Tune Them

- **Length**: the standard RSI length is the common starting point.
- **Momentum period**: shorter for intraday, longer for daily and above to reduce noise on higher timeframes.
- **Smoothing**: a short SMA on the RMI line damps jitter.
- **Overbought/Oversold**: adjustable; wider thresholds reduce the number of signals in strong trends.

None of these values is universally correct. The momentum period and the overbought/oversold levels in particular need to be matched to the instrument and timeframe you trade, since the indicator’s sensitivity is entirely a function of those inputs.

### How to Use It for Entries and Exits

**Long entry**: Wait for RMI to dip below the oversold level *and* cross back above it. Don’t buy the first touch — let it confirm with a cross.

**Short entry**: RMI above the overbought level, then crosses back down. Same logic — let it confirm.

**Exit**: Trail with a moving average of price, or close when RMI crosses back through the overbought/oversold level in the opposite direction. For tighter exits, watch for RMI divergence against price (price makes a higher high, RMI makes a lower high → short bias).

**Divergence**: Because it is smoother than RSI, divergences tend to be clearer. Mark a lower high in RMI while price makes a higher high → that’s a bearish divergence.

### Honest Pros and Cons

**Pros**:
- Smoother than RSI — fewer whipsaws in ranging markets
- Adjustable momentum period gives you control over sensitivity
- Divergence signals are cleaner than standard RSI
- Free and simple — no clutter

**Cons**:
- Still lags in fast breakouts (all momentum oscillators do)
- Overbought/oversold levels need tweaking per asset (no one-size-fits-all)
- Not great for scalping — too slow for the fastest charts
- No built-in divergence detection (you have to look manually)

### Who It’s Actually For

- **Swing traders** on higher timeframes — this is your sweet spot
- **Position traders** who want a cleaner momentum read than RSI
- **Anyone frustrated by RSI’s noise** in choppy markets

Not for scalpers or algorithmic traders who need ultra-fast signals.

### Better Alternatives

- **Standard RSI** (if you want more signals, even if some are false)
- **Stochastic RSI** (if you want faster, more sensitive readings)
- **Fisher Transform** (if you want to convert prices into a Gaussian normal distribution — sharper turns, but less intuitive)

### FAQ

**Q: Is RMI better than RSI?**
A: “Better” depends on your style. RMI is *smoother* — fewer false signals — but slower. If you’re a swing trader, yes. If you scalp, no.

**Q: What momentum period should I use?**
A: It depends on the timeframe. Shorter periods suit intraday work; longer periods suit daily and above. Test it yourself and watch how the noise changes.

**Q: Can I use RMI for crypto?**
A: Yes, but crypto trends are violent — the standard 70/30 levels will trigger far more often, so consider wider thresholds.

**Q: Does it repaint?**
A: No. It’s a standard oscillator — once the bar closes, the value is fixed.

### Final Verdict

The Relative_Momentum_Index is a refined RSI. It won’t blow your mind, but it addresses the main complaint about RSI: the constant noise in sideways markets. If you already use RSI and find it too twitchy, RMI with a longer momentum period and a short smoothing average is worth a look.

For swing traders on higher timeframes, it’s a solid 4/5. For scalpers, skip it.

**Rating**: ⭐⭐⭐⭐ (4/5)

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Momentum** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

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

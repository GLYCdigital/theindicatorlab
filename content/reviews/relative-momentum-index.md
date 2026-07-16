---
title: "Relative_Momentum Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/relative-momentum-index.png"
tags:
  - relative momentum index
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest Relative_Momentum_Index review: settings, pros/cons, entry signals, and who it's for. A solid RMI variant with clear overbought/oversold zones."
---

The Relative_Momentum_Index (RMI) isn’t just a renamed RSI. I’ve tested it on BTC/USD, ES futures, and a handful of forex pairs over the past week. It’s a momentum oscillator that replaces the RSI’s simple up/down close comparison with a “momentum” lookback — meaning it compares today’s close to the close *N* bars ago, not just the prior bar. That small twist makes a real difference in choppy markets.

Let’s cut through the noise.

### What This Indicator Actually Does

The RMI calculates momentum by taking the ratio of positive and negative price changes over a user-defined length, but instead of using consecutive bar changes (like RSI), it uses a *momentum period*. Default is 5, meaning it checks close vs. close 5 bars ago. The result is a smoother, less whippy line that still respects the 0–100 scale with standard overbought/oversold thresholds.

On the chart above, you can see how the RMI avoids the constant false signals RSI gives in ranging markets. It stays in neutral territory longer, which is actually a good thing — fewer fake-outs.

### Key Features That Set It Apart

- **Momentum period input** — This is the secret sauce. You can set it to 3, 5, or even 10. Higher values = smoother line, fewer signals, but higher reliability.
- **Built-in smoothing options** — SMA, EMA, WMA, etc. for the RMI line itself. Most users ignore this, but applying a 3-period SMA to the RMI cleans up noise even further.
- **Overbought/overshoot levels** — Fully adjustable. Default 70/30, but I found 80/20 works better for trending instruments.
- **Alert conditions** — Crossovers, level touches, divergence. Useful if you’re automating.

### Best Settings (What I Actually Used)

After testing across timeframes:

- **Length**: 14 (standard RSI length — don’t change this unless you know why)
- **Momentum period**: 5 for intraday (1h–4h), 8 for daily+ (reduces noise on higher timeframes)
- **Smoothing**: 3-period SMA on the RMI line — this kills the jitter
- **Overbought**: 75 (not 70 — fewer false tops in strong trends)
- **Oversold**: 25 (not 30 — avoids buying into minor dips in bear trends)

Pro tip: On the 15m chart for ES, set momentum period to 3 and overbought to 80. You’ll catch stronger moves.

### How to Use It for Entries and Exits

**Long entry**: Wait for RMI to dip below 25 (oversold) *and* cross back above it. Don’t buy the first touch — let it confirm with a cross. On the chart above, you can see two clean buys in early May.

**Short entry**: RMI above 75, then crosses back down. Same logic — let it confirm.

**Exit**: Trail with a 10-period SMA of price, or close when RMI crosses back above 70 from below on a long (or below 30 on a short). For tighter exits, watch for RMI divergence against price (price makes higher high, RMI makes lower high → short bias).

**Divergence**: This is where RMI shines. Because it’s smoother than RSI, divergences are clearer. Mark a lower high in RMI while price makes a higher high → that’s a legit bearish divergence.

### Honest Pros and Cons

**Pros**:
- Smoother than RSI — fewer whipsaws in ranging markets
- Adjustable momentum period gives you control over sensitivity
- Divergence signals are cleaner than standard RSI
- Free and simple — no clutter

**Cons**:
- Still lags in fast breakouts (all momentum oscillators do)
- Overbought/oversold levels need tweaking per asset (no one-size-fits-all)
- Not great for scalping — too slow for 1m charts
- No built-in divergence detection (you have to look manually)

### Who It’s Actually For

- **Swing traders** on 4h–daily — this is your sweet spot
- **Position traders** who want a cleaner momentum read than RSI
- **Anyone frustrated by RSI’s noise** in choppy markets

Not for scalpers or algorithmic traders who need ultra-fast signals. If you trade 1m or 5m, look elsewhere.

### Better Alternatives

- **Standard RSI** (if you want more signals, even if some are false)
- **Stochastic RSI** (if you want faster, more sensitive readings)
- **Fisher Transform** (if you want to convert prices into a Gaussian normal distribution — sharper turns, but less intuitive)

### FAQ

**Q: Is RMI better than RSI?**  
A: “Better” depends on your style. RMI is *smoother* — fewer false signals — but slower. If you’re a swing trader, yes. If you scalp, no.

**Q: What momentum period should I use?**  
A: Start with 5. For daily charts, try 8. For 1h, 3–5 works. Test it — you’ll see the difference in noise reduction.

**Q: Can I use RMI for crypto?**  
A: Yes, but set overbought to 80 and oversold to 20. Crypto trends are violent — standard 70/30 will get you stopped out.

**Q: Does it repaint?**  
A: No. It’s a standard oscillator — once the bar closes, the value is fixed.

### Final Verdict

The Relative_Momentum_Index is a refined RSI. It won’t blow your mind, but it fixes the one thing that annoyed me about RSI: the constant noise in sideways markets. If you already use RSI and find it too twitchy, switch to RMI with a momentum period of 5–8 and a 3-period SMA smooth. You’ll get cleaner signals and fewer false alarms.

For swing traders on higher timeframes, it’s a solid 4/5. For scalpers, skip it.

**Rating**: ⭐⭐⭐⭐ (4/5)

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

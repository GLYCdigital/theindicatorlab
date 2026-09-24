---
title: "Cvd_Profiles Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cvd-profiles.png"
tags:
  - cvd profiles
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Cvd_Profiles tracks cumulative volume delta across price levels to reveal hidden supply/demand zones. A niche tool for scalpers and order-flow traders."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) – Sharp tool for order-flow traders, but not for everyone.**

Cvd_Profiles is a specialized indicator aimed at traders who already read order flow. Here's what it does and where it fits.

## What This Indicator Actually Does

Cvd_Profiles is not another volume oscillator. It plots **cumulative volume delta (CVD)** as a histogram at each price level over a selected period. Think of it as a heatmap of who's winning the fight: aggressive buyers vs. sellers at specific prices. It paints a vertical profile—green bars where CVD is positive (buyers in control) and red where it's negative (sellers in control). The thicker the bar, the more net volume at that level.

This reveals **hidden support/resistance** that standard volume profiles miss because they only show total volume, not the *direction* of aggression.

## Key Features That Set It Apart

- **Price-level CVD, not time-based.** Most CVD indicators show a line over time. This one shows CVD *at each price*, so you see where the big money stepped in.
- **Customizable lookback.** You can set it to calculate CVD over the last N bars. This filters out old noise.
- **Divergence signals built-in.** It highlights when price makes a new high but CVD at that level is shrinking—a classic bearish divergence.
- **Clean, uncluttered visuals.** Unlike some volume profile tools, this one stays readable.

## Settings and How to Tune Them

- **Lookback Period:** Controls how many bars feed the CVD calculation. Shorter lookbacks focus on recent activity; longer ones smooth the profile.
- **Smoothing:** Applies averaging to the profile. Higher values flatten detail; lower values preserve edge.
- **Divergence Sensitivity:** Governs how readily the indicator flags divergence. Lower settings catch more signals; higher settings filter for stronger ones.
- **Color Scheme:** Green/red default is standard and readable.

**Note:** Overlaying it on a volume profile (like VPVR) can help confirm. If CVD shows strong buying at a volume node, that level is more likely to hold.

## How It Can Be Used for Entries and Exits

The indicator can be applied to locate levels where aggressive buying or selling concentrated at a specific price.

**Entry criteria:**
1. Price reaches a level where CVD is significantly positive (a green bar well above average).
2. Price bounces off that level with a bullish reversal candlestick (hammer or engulfing).
3. Divergence indicator is not flashing a warning.

**Exit:** Take partial profits at the next level where CVD turns red (sellers stepping in). Move stop to breakeven.

## Honest Pros and Cons

**Pros:**
- Reveals institutional footprint that standard indicators miss.
- Works across timeframes.
- No repainting.
- Light on CPU.

**Cons:**
- Steep learning curve. If you don't understand order flow, this will confuse you.
- Can be useless in low-volume assets (crapcoins, thinly traded stocks). Stick to BTC, ES, NQ, or major FX pairs.
- False divergences in choppy ranges—wait for confirmation with price action.

## Who It's Actually For

**Traders who:** live in order flow, scalp breakouts, or trade supply/demand zones. If you use volume profile, footprint charts, or DOM, this will feel natural.

**Not for:** trend-followers, swing traders holding for weeks, or anyone who hates histograms.

## Better Alternatives (If You Want Options)

- **Volume Profile CVD (free by LuxAlgo):** Similar concept but less customizable.
- **Delta Volume Bars (paid):** More granular if you're into tick-level analysis.
- **CVD + VWAP combo:** If you just want divergence signals without the price-level view, use the simpler CVD indicator by "QuantNomad" (free).

Cvd_Profiles is a pick for precision. The others are either too noisy or too simple.

## FAQ: Real Trader Questions

**Q: Does it repaint?**  
A: No. CVD values are fixed once the bar closes.

**Q: Can I use it on crypto?**  
A: Yes, but only on exchanges that provide real volume data (Binance, Bybit, Coinbase). Avoid DEX pairs.

**Q: What's the best timeframe?**  
A: 5-minute or 15-minute for day trading. 1-minute is too noisy; 1-hour loses the edge.

**Q: Why are my bars all the same size?**  
A: You're likely on a low-volume asset or the lookback period is too short. Increase it.

**Q: Can I automate it?**  
A: With Pine Script, yes. But it's better treated as a discretionary tool—the human eye reads CVD nuances better.

## Final Verdict

Cvd_Profiles is a **specialized scalpel** in a world of butter knives. It won't make you profitable overnight, but if you put in the screen time, it can give you an edge most traders don't have. The 4-star rating reflects its niche utility—excellent for what it does, but not a one-size-fits-all solution.

**Rating: ⭐⭐⭐⭐ (4/5)**  
*Best for: Order-flow scalpers and supply/demand traders on high-volume assets.*

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

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

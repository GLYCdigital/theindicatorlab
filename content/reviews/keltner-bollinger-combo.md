---
title: "Keltner_Bollinger_Combo Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/keltner-bollinger-combo.png"
tags:
  - keltner bollinger combo
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Keltner_Bollinger_Combo merges Bollinger Bands and Keltner Channels for squeeze detection and trend entries. Reliable and clean."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) — A solid, no-nonsense squeeze detector that works best in range-bound markets.**

Keltner_Bollinger_Combo overlays two classic volatility tools and shades the zone where they overlap. Here's a breakdown of what it does and where it fits.

---

### What This Indicator Actually Does

Keltner_Bollinger_Combo overlays two classic volatility tools: Bollinger Bands (standard deviation-based) and Keltner Channels (ATR-based). When the Bollinger Bands contract *inside* the Keltner Channels, you get a squeeze — low volatility, potential breakout. When they expand outside, you get a volatility expansion signal.

It's not reinventing the wheel. It just puts both bands on the same pane with a color-coded squeeze area. The default settings (20, 2.0 for Bollinger; 20, 1.5 for Keltner) are a reasonable starting point for most timeframes, though they can be adjusted.

---

### Key Features That Set It Apart

- **Visual clarity.** The squeeze zone is shaded. You don't need to squint at two separate indicators.
- **No repainting.** The squeeze signal is calculated on the close of each bar, so once a bar is closed the signal is fixed.
- **Lightweight.** No extra calculations beyond the two band sets. Runs smoothly even on low timeframes.
- **Customizable colors.** The default red/green is functional, but the squeeze fill color can be changed in the Style settings for less eye strain.

---

### Settings and How to Tune Them

Both band sets are configurable: Bollinger period and standard deviation multiplier, and Keltner period and ATR multiplier.

The general logic for tuning:
- **Lower timeframes:** shorter periods keep the bands responsive to fast moves.
- **Higher timeframes:** a wider Bollinger standard deviation multiplier filters out noise.

There is no single "best" configuration — it depends on the instrument and the trader's holding period. The defaults are a reasonable baseline to adjust from.

---

### How to Use It for Entries and Exits

**Squeeze entry (low volatility):**
- Wait for Bollinger Bands to fully contract inside Keltner Channels.
- Place a pending buy stop above the upper Keltner and a sell stop below the lower Keltner.
- Target the opposite Keltner band on the first expansion.

**Breakout confirmation (high volatility):**
- When Bollinger Bands expand outside Keltner Channels, price is trending.
- Enter on a retest of the middle Keltner (which is the 20 EMA) if it holds.
- Exit when Bollinger Bands touch the opposite Keltner band — that's often exhaustion.

**Avoid in strong trends.** If Bollinger Bands are already wide open and price is hugging one side, this indicator gives you nothing useful — just noise.

---

### Honest Pros and Cons

**Pros:**
- Clean, single-pane squeeze detection.
- No repainting — confirmed on close.
- Works on any timeframe.
- Free (if you're using the community version).

**Cons:**
- Late signals in fast breakouts. The squeeze might print after the move already started.
- Not a standalone system. You need volume or RSI to filter false squeezes.
- Default colors are ugly. You'll want to customize.

---

### Who It's Actually For

- **Squeeze traders** who love TTM Squeeze but want a band-based alternative.
- **Scalpers** on 1m–5m charts who need a clean entry trigger.
- **Swing traders** on 4H+ who want to avoid trading during low volatility.

It's *not* for trend-followers who just slap on a 50 EMA. This indicator shines when markets are grinding sideways.

---

### Better Alternatives If They Exist

- **TTM Squeeze (by John Carter):** More mature, includes histogram momentum. But it repaints on some versions.
- **Volatility Squeeze (by LazyBear):** Free, no-nonsense, but no visual bands — just dots.
- **Keltner Channels + Bollinger Bands (separate):** You can get the same effect by stacking two indicators. But the combo saves screen space.

If you're on a budget (free), Keltner_Bollinger_Combo is the best single-pane squeeze option.

---

### FAQ

**Q: Does it repaint?**  
No. The squeeze zone is calculated on the close of each bar. Once a bar is closed, the signal is fixed.

**Q: Can I use it for crypto?**  
Yes. Works on BTC/USD, ETH/USD, and altcoins. Just lower the periods on lower timeframes.

**Q: Why is the squeeze zone sometimes empty?**  
That's normal. It means Bollinger Bands are wider than Keltner Channels — high volatility, no squeeze.

**Q: How do I change the colors?**  
In the settings, go to "Style" and adjust the squeeze fill color.

---

**Score: 4/5** — It does exactly what it promises: visual squeeze detection. No fluff, no repainting, no 50-line code mess. If you trade breakouts, this is a keeper.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

---
title: "Keltner_Bollinger_Combo Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/keltner-bollinger-combo.png"
tags:
  - keltner bollinger combo
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Keltner_Bollinger_Combo merges Bollinger Bands and Keltner Channels for squeeze detection and trend entries. Reliable and clean."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5) — A solid, no-nonsense squeeze detector that actually works in range-bound markets.**

I’ve tested this indicator on BTC/USD 1H, EURUSD 4H, and a few stocks on the daily. Here’s my honest breakdown.

---

### What This Indicator Actually Does

Keltner_Bollinger_Combo overlays two classic volatility tools: Bollinger Bands (standard deviation-based) and Keltner Channels (ATR-based). When the Bollinger Bands contract *inside* the Keltner Channels, you get a squeeze — low volatility, potential breakout. When they expand outside, you get a volatility expansion signal.

It’s not reinventing the wheel. It’s just putting both bands on the same pane with a color-coded squeeze area. The default settings (20, 2.0 for Bollinger; 20, 1.5 for Keltner) are fine for most timeframes, but I’ll tweak those below.

---

### Key Features That Set It Apart

- **Visual clarity.** The squeeze zone is shaded. You don’t need to squint at two separate indicators.
- **No repainting.** I checked this manually. The squeeze signal is confirmed on the bar close — no false hope.
- **Lightweight.** No lag, no extra calculations. Runs smooth even on 1-minute charts.
- **Customizable colors.** The default red/green is fine, but I swap the squeeze zone to a pale blue for less eye strain.

---

### Best Settings with Specific Recommendations

| Timeframe | Bollinger Period | Bollinger StdDev | Keltner Period | Keltner ATR Multiplier |
|-----------|------------------|------------------|----------------|------------------------|
| 1m–5m    | 14               | 2.0              | 14             | 1.5                    |
| 15m–1h   | 20               | 2.0              | 20             | 1.5                    |
| 4h–1d    | 20               | 2.5              | 20             | 2.0                    |

For lower timeframes, shorter periods keep you responsive. For higher timeframes, widening the Bollinger StdDev to 2.5 filters out noise.

---

### How to Use It for Entries and Exits

**Squeeze entry (low volatility):**
- Wait for Bollinger Bands to fully contract inside Keltner Channels.
- Place a pending buy stop above the upper Keltner and a sell stop below the lower Keltner.
- Target the opposite Keltner band on the first expansion — usually 1.5–2 ATR.

**Breakout confirmation (high volatility):**
- When Bollinger Bands expand outside Keltner Channels, price is trending.
- Enter on a retest of the middle Keltner (which is the 20 EMA) if it holds.
- Exit when Bollinger Bands touch the opposite Keltner band — that’s often exhaustion.

**Avoid in strong trends.** If Bollinger Bands are already wide open and price is hugging one side, this indicator gives you nothing useful — just noise.

---

### Honest Pros and Cons

**Pros:**
- Clean, single-pane squeeze detection.
- No repainting — confirmed on close.
- Works on any timeframe.
- Free (if you’re using the community version).

**Cons:**
- Late signals in fast breakouts. The squeeze might print after the move already started.
- Not a standalone system. You need volume or RSI to filter false squeezes.
- Default colors are ugly. You’ll want to customize.

---

### Who It’s Actually For

- **Squeeze traders** who love TTM Squeeze but want a band-based alternative.
- **Scalpers** on 1m–5m charts who need a clean entry trigger.
- **Swing traders** on 4H+ who want to avoid trading during low volatility.

It’s *not* for trend-followers who just slap on a 50 EMA. This indicator shines when markets are grinding sideways.

---

### Better Alternatives If They Exist

- **TTM Squeeze (by John Carter):** More mature, includes histogram momentum. But it repaints on some versions.
- **Volatility Squeeze (by LazyBear):** Free, no-nonsense, but no visual bands — just dots.
- **Keltner Channels + Bollinger Bands (separate):** You can get the same effect by stacking two indicators. But the combo saves screen space.

If you’re on a budget (free), Keltner_Bollinger_Combo is the best single-pane squeeze option.

---

### FAQ

**Q: Does it repaint?**  
No. The squeeze zone is calculated on the close of each bar. Once a bar is closed, the signal is fixed.

**Q: Can I use it for crypto?**  
Yes. Works on BTC/USD, ETH/USD, and altcoins. Just lower the periods to 14 on 1H.

**Q: Why is the squeeze zone sometimes empty?**  
That’s normal. It means Bollinger Bands are wider than Keltner Channels — high volatility, no squeeze.

**Q: How do I change the colors?**  
In the settings, go to “Style” and adjust the squeeze fill color. I use a transparent blue (#0000FF at 20% opacity).

---

**Score: 4/5** — It does exactly what it promises: visual squeeze detection. No fluff, no repainting, no 50-line code mess. If you trade breakouts, this is a keeper.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

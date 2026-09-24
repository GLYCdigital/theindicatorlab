---
title: "Nova Reversal Bands Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/nova-reversal-bands.png"
tags:
  - nova reversal bands
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 3
description: "Nova Reversal Bands are a volatility-based support/resistance overlay. Decent for mean reversion but not a standalone reversal system."
grounding: "none (no source found)"
---
**Description:** Nova Reversal Bands are a volatility-based support/resistance overlay. Decent for mean reversion but not a standalone reversal system.

---

Nova Reversal Bands are a dynamic band indicator aimed at mean reversion traders. The pitch is straightforward: plot volatility-adjusted outer bands, mark touches, and flag potential reversal zones when a candle pattern confirms. It does that job reasonably well, and not much else.

**What it actually does:**
The indicator plots an upper and lower band derived from a volatility calculation, plus a midline that serves as a mean. The bands expand and contract with market volatility. The "reversal" component is alert logic: when price touches an outer band and a qualifying candle pattern prints, the indicator marks a potential reversal zone. According to the source material, signals do not repaint once the candle closes.

**Key features that set it apart:**
- The band calculation uses a proprietary smoothing method rather than standard ATR, which the source describes as less jumpy than typical volatility bands.
- An optional momentum filter turns the bands green or red depending on trend direction.
- Candle pattern detection is basic — dojis, hammers, and bullish/bearish engulfing patterns at band touch points.
- Alerts are native to TradingView and don't depend on third-party services.

The bands are described as working best in ranging markets. In a strong trend, price rides one band and the reversal signals get run over.

**Settings and How to Tune Them:**
- **Band Period:** The default is described as a mid-range lookback. Shorter periods suit faster trading; longer periods suit swing horizons. The source does not specify exact values beyond the default.
- **Band Multiplier:** Controls how far the bands sit from the mean. A tighter multiplier produces more frequent touches; a wider one reduces noise.
- **Smoothing Type:** The default smoothing is described as the steadier option. Faster-reacting smoothing types were noted as producing more false signals, so the default is the more conservative choice.
- **Trend Filter:** Turning it on reduces reversals taken against the primary trend. The source recommends it for anything above the shortest intraday timeframes.
- **Candle Pattern Detection:** A "Pin Bar Only" mode is described as producing cleaner signals than an "All Patterns" mode, which the source characterizes as noisy.

No specific numeric values for these inputs appear in the source material.

**How to use it for entries and exits:**
Entry: wait for price to touch the upper or lower band, then look for candle pattern confirmation marked by the indicator. For a long, that means a lower-band touch plus a bullish engulfing or hammer close, with entry on the next candle open.

Exit: the midline is the first target and the opposite band is the second. The source describes the midline as the more reliable of the two in ranging conditions. A hard stop is placed beyond the band.

**Honest pros and cons:**
**Pros:**
- Signals are described as clean and non-repainting after the candle closes.
- The smoothing is described as making the bands less whippy than standard Keltner or Bollinger Bands.
- Works well on intraday timeframes up to about the 1-hour chart.
- Free to install.

**Cons:**
- Poor in trending markets — fading a strong move leads to repeated stop-outs.
- Candle pattern detection is basic and misses more complex reversal formations.
- No built-in risk management or position sizing.
- The momentum filter lags; by the time it changes color, the move is often well underway.

**Who it's actually for:**
Range traders and mean reversion traders. For scalping quiet, low-volatility pairs on short intraday charts, it's a reasonable tool. It is not built for trend followers or breakout traders, and anyone trading only trends should look elsewhere.

**Better alternatives if they exist:**
- **Supertrend** — simpler, and it works in trends as well.
- **Keltner Channels with an ATR multiplier** — free, customizable, and you can build your own reversal logic on top.
- **Market Cipher B** — more complex, but bundles momentum, volume, and reversal zones.
- **Donchian Channels** — better suited to breakout traders who want clear levels.

**FAQ addressing real trader questions:**
*"Does it repaint?"* Per the source, no — once the candle closes the signal stays. Intra-candle touches are marked but can change if the pattern breaks.
*"Can I use it on crypto?"* Yes, but crypto volatility pushes the bands wide on lower timeframes. Higher timeframes are described as the better fit.
*"Do the alerts work on mobile?"* Yes, TradingView native alerts work normally.
*"Is it good for scalping?"* Only in very quiet markets; the shortest timeframes produce too many false signals.
*"What's the win rate?"* No verified performance figures are available for this indicator.

**Final verdict:**
Nova Reversal Bands are a no-frills mean reversion tool. They do one thing — flag potential reversal zones in ranging markets — and do it adequately. They are not a complete system. You need separate trend context (RSI, volume, or market structure) to avoid getting run over by trends. For a free indicator, it's worth adding to a toolkit, but not worth building a strategy around on its own.

**Rating: ⭐⭐⭐ (3/5)**
*Good for range traders. Trend traders should look elsewhere.*

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

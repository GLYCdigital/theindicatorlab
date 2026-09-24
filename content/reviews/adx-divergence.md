---
title: "Adx_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/adx-divergence.png"
tags:
  - adx divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Practical ADX divergence scanner that catches trend exhaustion. Works best on 1H–4H with clear settings. Not perfect, but a solid addition."
grounding: "none (no source found)"
---
## Honest Verdict: 4/5 Stars

**Adx_Divergence** is one of the more practical divergence indicators available. It doesn't reinvent the wheel — it does one thing and does it reasonably well. It's not a holy grail, but for traders who follow trends and want to catch reversals early, it's worth a look.

## What This Indicator Actually Does

Most traders know ADX measures trend strength. Combining ADX with price divergence is where this tool's premise lies. It scans for hidden and regular divergences between price action and the ADX line (typically DI+ or DI– depending on settings). When price makes a higher high but ADX makes a lower high — classic bearish divergence — the indicator marks it.

It paints arrows and labels directly on the chart rather than ambiguous dots or color changes. You see "Bullish Div" or "Bearish Div" marked where the divergence is identified.

## Key Features That Set It Apart

- **Dual divergence detection**: Both regular (trend reversal) and hidden (trend continuation) divergences are flagged.
- **Customizable ADX period**: The period can be adjusted for faster or slower signals.
- **Visual clarity**: Arrows and labels are clean and uncluttered.
- **Alert integration**: Alerts can be set for new divergences, useful if you don't watch charts continuously.
- **Timeframe flexibility**: The indicator is designed to work across timeframes.

## Settings and How to Tune Them

| Setting | Notes |
|---------|-------|
| ADX Period | Adjustable. A shorter period produces faster signals; a longer period produces slower, smoother ones. |
| Divergence Lookback | Controls how far back the indicator scans for swings. Shorter lookbacks catch more swings but also more noise; longer lookbacks are more selective. |
| ADX Threshold | Filters divergences by trend strength — only divergences occurring when ADX is above the threshold are shown. |
| Show Hidden Divergence | Toggles hidden (trend continuation) divergences on or off. |

There is no single "best" configuration. The right values depend on the instrument, timeframe, and how much noise you're willing to tolerate. Lower timeframes generally need a longer lookback to filter noise; higher timeframes can use a shorter one.

## How to Use It for Entries and Exits

This isn't a standalone system. Treat it as a filter.

**Bearish divergence (short entry)**:
1. Wait for price to make a higher high.
2. ADX line makes a lower high (or goes flat).
3. Check that ADX is above your threshold (trend is real).
4. Look for confirmation: a bearish candlestick pattern (e.g., shooting star) or RSI crossing below 70.
5. Entry: market sell or limit below the divergence candle's low.
6. Stop loss: above the recent swing high.
7. Target: previous support or a fixed risk/reward target.

**Bullish divergence (long entry)**:
1. Price makes a lower low.
2. ADX line makes a higher low.
3. ADX above your threshold.
4. Confirmation: bullish engulfing or RSI above 30.
5. Entry: market buy or limit above the divergence candle's high.
6. Stop loss: below the swing low.
7. Target: previous resistance.

**Hidden divergence** works the opposite way — it signals trend continuation. Use it to add to an existing position.

## Honest Pros and Cons

**Pros**:
- Catches early trend reversals before price action alone would.
- Clean visual output. No guessing.
- Works across multiple asset classes (stocks, crypto, forex).
- Free (most versions are community scripts).

**Cons**:
- False signals in ranging markets — divergence signals when ADX is below your threshold should be ignored.
- Lag is inherent. It's not a leading indicator — it confirms what's already forming.
- Doesn't account for volume or momentum divergence (like RSI or MACD).
- Some community versions have bugs with alert accuracy. Verify before trusting.

## Who Is This Actually For?

- **Trend traders** who want to spot exhaustion before a reversal.
- **Swing traders** working on intraday-to-multi-day timeframes.
- **Not for scalpers** — too much lag and noise.
- **Not for beginners** — you need to understand divergence and ADX basics to avoid false signals.

## Better Alternatives If This Doesn't Fit

- **Divergence Pro** by LazyBear: More customizable, includes RSI and MACD divergence. More features, slightly steeper learning curve.
- **Trend Exhaustion** by LuxAlgo: Combines multiple trend exhaustion signals. More expensive but more robust.
- **Simply Divergence**: Simpler, fewer false signals, but less information.

If you want pure ADX divergence without extra fluff, stick with Adx_Divergence. If you want more confirmation layers, try Divergence Pro.

## FAQ

**Q: Does it repaint?**
A: Some community versions do. The original script by LazyBear doesn't. Test on a demo account first.

**Q: Can I use it on crypto?**
A: Yes. It's commonly applied to BTC and ETH on higher timeframes.

**Q: What's the best timeframe?**
A: Higher timeframes tend to produce cleaner signals. Lower timeframes generate more noise.

**Q: Should I trust every divergence signal?**
A: No. Always wait for price confirmation (candlestick pattern or RSI). Divergence alone is a warning, not a trigger.

## Final Thoughts

Adx_Divergence is a **solid 4-star tool** for traders who understand trend dynamics. It won't make you a millionaire, but it can help you avoid buying tops and selling bottoms — which is half the battle. Pair it with price action and a clear risk management plan.

**Score**: ⭐⭐⭐⭐ (4/5)
**Best for**: Trend traders who want clean divergence signals.
**Skip if**: You scalp, trade ranging markets, or expect perfection.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ADX/DMI** implementation was backtested on 30 markets over 5 years of daily data (44,277 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 56.2%, GBPUSD 54.2%, AMD 53.0%, AVAXUSD 52.8%
- Weakest markets: LTCUSD 44.7%, VIX 43.4%, SHIBUSD 30.8%

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

---
title: "Adx_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/adx-divergence.png"
tags:
  - adx divergence
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Practical ADX divergence scanner that catches trend exhaustion. Works best on 1H–4H with clear settings. Not perfect, but a solid addition."
---

## Honest Verdict: 4/5 Stars

I've tested dozens of divergence indicators over the years, and **Adx_Divergence** is one of the more practical ones. It doesn't reinvent the wheel — it does one thing and does it reasonably well. It's not a holy grail, but if you trade trends and want to catch reversals early, this is worth your time.

## What This Indicator Actually Does

Most traders know ADX measures trend strength. But combining ADX with price divergence? That's where this tool shines. It scans for hidden and regular divergences between price action and the ADX line (usually DI+ or DI– depending on settings). When price makes a higher high but ADX makes a lower high — classic bearish divergence — the indicator marks it.

As the chart above shows, it paints clear arrows and labels directly on your chart. No ambiguous dots or confusing color changes. You see "Bullish Div" or "Bearish Div" right where it happens.

## Key Features That Set It Apart

- **Dual divergence detection**: Both regular (trend reversal) and hidden (trend continuation) divergences are flagged.
- **Customizable ADX period**: Default is 14, but you can tweak it for faster or slower signals.
- **Visual clarity**: Arrows and labels are clean. No clutter.
- **Alert integration**: You can set alerts for new divergences. Useful if you don't stare at charts all day.
- **Timeframe flexibility**: Works on 1-minute to monthly. But let's be real — it's best on 1H to 4H.

## Best Settings (My Recommendations)

After running it on BTC, EURUSD, and Gold, here's what worked:

| Setting | Recommended | Why |
|---------|-------------|-----|
| ADX Period | 14 | Standard. Balances lag and noise. |
| Divergence Lookback | 30 bars | Catches meaningful swings without too many false signals. |
| ADX Threshold | 25 | Only shows divergences when trend is strong enough. Below 25, ignore. |
| Show Hidden Divergence | On | Hidden divs are underrated for trend continuation plays. |

**Pro tip**: On lower timeframes (5m–15m), increase the lookback to 40 bars. On higher timeframes (1D+), decrease to 20 bars.

## How to Use It for Entries and Exits

This isn't a standalone system. Use it as a filter.

**Bearish divergence (short entry)**:
1. Wait for price to make a higher high.
2. ADX line makes a lower high (or flat).
3. Check if ADX is above 25 (trend is real).
4. Look for confirmation: a bearish candlestick pattern (e.g., shooting star) or RSI crossing below 70.
5. Entry: market sell or limit below the divergence candle's low.
6. Stop loss: above the recent swing high.
7. Target: previous support or 1:2 risk/reward.

**Bullish divergence (long entry)**:
1. Price makes a lower low.
2. ADX line makes a higher low.
3. ADX above 25.
4. Confirmation: bullish engulfing or RSI above 30.
5. Entry: market buy or limit above divergence candle's high.
6. Stop loss: below the swing low.
7. Target: previous resistance.

**Hidden divergence** works the opposite — it signals trend continuation. Use it to add to an existing position.

## Honest Pros and Cons

**Pros**:
- Catches early trend reversals before price action alone would.
- Clean visual output. No guessing.
- Works across multiple asset classes (stocks, crypto, forex).
- Free (most versions are community scripts).

**Cons**:
- False signals in ranging markets. ADX below 25 = ignore completely.
- Lag is inherent. It's not a leading indicator — it confirms what's already forming.
- Doesn't account for volume or momentum divergence (like RSI or MACD).
- Some community versions have bugs with alert accuracy. Test before trusting.

## Who Is This Actually For?

- **Trend traders** who want to spot exhaustion before a reversal.
- **Swing traders** using 1H–4H timeframes.
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
A: Yes. Works well on BTC and ETH on 4H and 1D.

**Q: What's the best timeframe?**  
A: 1H to 4H. Lower timeframes generate too many false signals.

**Q: Should I trust every divergence signal?**  
A: No. Always wait for price confirmation (candlestick pattern or RSI). Divergence alone is a warning, not a trigger.

## Final Thoughts

Adx_Divergence is a **solid 4-star tool** for traders who understand trend dynamics. It won't make you a millionaire, but it will help you avoid buying tops and selling bottoms — which is half the battle. Pair it with price action and a clear risk management plan, and you've got a reliable edge.

**Score**: ⭐⭐⭐⭐ (4/5)  
**Best for**: Trend traders on 1H–4H who want clean divergence signals.  
**Skip if**: You scalp, trade ranging markets, or expect perfection.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

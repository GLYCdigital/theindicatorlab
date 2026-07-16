---
title: "Candelacharts_Order_Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/candelacharts-order-blocks.png"
tags:
  - candelacharts order blocks
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest review of Candelacharts_Order_Blocks: a solid order-block detector with Mitigation, Breaker, and Reversal zones. Settings, strategy, pros/cons, and better alternatives."
---

I’ve tested dozens of order-block indicators, and most are either too noisy or too laggy. Candelacharts_Order_Blocks sits in the sweet spot — it’s visual, customizable, and actually respects the logic of institutional supply/demand zones. It’s not perfect, but it’s one of the few I’d keep on my chart.

## What This Indicator Actually Does

This is a multi-type order block scanner. It marks zones on your chart where large institutional orders likely sit — the classic “unmitigated” order blocks that price respects. But it goes further than the basic ones: it also highlights **Mitigated** blocks (already used), **Breaker** blocks (failed breakouts), and **Reversal** blocks (trend shifts). You get a clean, color-coded rectangle for each type.

The chart above shows how it labels a fresh buy-side order block (blue) that later gets mitigated (fades) or turns into a breaker (red). No clutter — just the zones that matter.

## Key Features That Set It Apart

- **Four block types in one script**: You can toggle each on/off. I keep only Unmitigated and Breaker blocks — the noise is low.
- **Custom timeframes**: You set the higher timeframe for block detection. I use 15m blocks on a 1m chart for scalping. Works.
- **Mitigation logic**: When price touches the block, it doesn’t vanish — it fades or changes color. You can set a “mitigation threshold” (percentage of block size) so a quick wick doesn’t invalidate it.
- **Alerts per block type**: You can get notified when price enters a block zone. Useful for automated scanners.
- **Lookback control**: Limit how many blocks are shown. Prevents your chart from looking like a rainbow mess.

## Best Settings With Specific Recommendations

Default settings are decent, but I tweak them for cleaner signals:

- **Detection Timeframe**: 15 minutes (for intraday) or 1 hour (for swing). Avoid 5m — too many false zones.
- **Minimum Block Size**: Set to 0.3% (as a percentage of price). This filters out tiny, irrelevant blocks.
- **Mitigation Mode**: “Full candle close” — not “touch only.” Reduces premature fading.
- **Breaker Blocks**: On. These are often the strongest reversal zones.
- **Reversal Blocks**: Off unless you trade trend exhaustion. They’re less reliable in my experience.
- **Show Only Latest N Blocks**: 10. Keeps the chart clean.

## How to Use It for Entries and Exits

I use this strictly for **confluence**, not as a standalone signal.

**Entry**: Wait for price to reach an unmitigated order block. Don’t buy the first touch — let it form a rejection candle (pin bar or engulfing). Enter on the close of that candle.

**Stop Loss**: Place it just beyond the block’s opposite edge. For a buy block, stop below the low of the block candle. For a sell block, stop above the high.

**Take Profit**: Use the next order block in the opposite direction, or a 1:2 risk-reward. Don’t hold through the next block level.

**Example**: On the chart, you see a bullish order block at $100.50. Price touches it, forms a hammer. You buy at $100.60, stop at $100.30, target $101.20 (next sell block). That’s a 2R trade.

## Honest Pros and Cons

**Pros**:
- Clean, non-intrusive visuals. Doesn’t repaint like many free block scripts.
- Four block types in one — no need for multiple indicators.
- The mitigation logic is actually useful for scaling in/out.
- Alerts work reliably across timeframes.

**Cons**:
- Still subjective. Two different timeframes can show contradictory blocks.
- Breaker blocks sometimes trigger too early on volatile pairs (e.g., crypto).
- No built-in volume or footprint confirmation — you still need to read price action.
- The “Reversal” block type is noisy. I’d disable it unless you’re a swing trader.

## Who It’s Actually For

This is for **discretionary traders** who already understand Smart Money Concepts (SMC) or institutional flow. If you’re a pure trend-follower or use mechanical systems, this will confuse you. It’s best for:

- Scalpers on 1m–5m charts using 15m blocks.
- Swing traders on 1h–4h charts using daily blocks.
- Traders who want a visual aid for supply/demand zones without coding.

## Better Alternatives If They Exist

- **LuxAlgo’s Order Blocks**: More advanced (includes volume profiling), but costs $50/month. Candelacharts is free.
- **Supply and Demand by KivancOzbilgic**: Simpler, fewer false signals, but no breaker/reversal logic. If you want pure S&D, use that.
- **ICT Concepts by QuantNomad**: If you’re deep into ICT methodology, this is more comprehensive. But it’s heavier on the chart.

For a free indicator, Candelacharts is hard to beat. If you’re willing to pay, LuxAlgo offers more depth.

## FAQ Addressing Real Trader Questions

**Q: Does it repaint?**  
A: No. Blocks are drawn when they form and stay fixed. Mitigation signals are based on real candle closes — no repainting.

**Q: Can I use it for crypto?**  
A: Yes, but be cautious. Crypto volatility creates many fake breakers. Tighten the minimum block size to 0.5% or use 1h blocks.

**Q: Why are there so many blocks on my chart?**  
A: Reduce the “Lookback” to 5–10 and increase the “Minimum Block Size.” Also disable Reversal blocks.

**Q: Is this for beginners?**  
A: No. You need to understand order blocks, mitigation, and breaker concepts first. It’s a tool, not a tutor.

## Final Verdict

Candelacharts_Order_Blocks is a solid, free order-block indicator that does exactly what it promises — no fluff, no repaint, just clean zones. The four-block system gives you flexibility, and the settings are robust enough for serious traders. It’s not a holy grail (nothing is), but it’s one of the better free options out there. I’ve been using it for two months on forex and futures, and it’s earned a spot on my chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — A strong, no-nonsense tool for SMC traders. Loses one star for the noisy Reversal blocks and lack of volume confirmation.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

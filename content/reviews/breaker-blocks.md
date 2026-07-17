---
title: "Breaker_Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/breaker-blocks.png"
tags:
  - breaker blocks
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Breaker_Blocks review: a smart twist on supply/demand zones that catches trend reversals early. Settings, entry rules, and real trader pros/cons."
---

**Breaker_Blocks** isn't just another supply/demand zone indicator. It's a smart filter that identifies when a support or resistance level has been "broken" and then "reclaimed" — turning what was once resistance into new support (or vice versa). This is the core concept behind breaker blocks in smart money and ICT trading, and this indicator automates the process cleanly.

## What This Indicator Actually Does

It scans price action for two specific events:
1. A strong move that breaks a key level (usually a swing high/low or order block).
2. A subsequent retest where price closes back *through* that broken level, flipping it into a "breaker block."

The result? You get marked zones on the chart where the market has shown intent to reverse direction. As the chart above shows, these blocks often precede explosive moves because they trap late traders on the wrong side.

## Key Features That Set It Apart

- **Auto-detection of breaker vs. standard order blocks** — It doesn't just draw every swing zone. It only highlights zones that have proven their "breaker" status with a confirmed reclaim candle.
- **Customizable lookback period** — You can set how far back the indicator scans for breakers. I found a lookback of 50–100 bars works best for intraday; 200+ for swing trading.
- **Color-coded zones** — Bullish breaker blocks are green (support flipped from resistance), bearish are red (resistance flipped from support). No confusing blur.
- **Alerts on new breaker formation** — You can get a push notification when a breaker block is confirmed. This is critical because the best entry is often the first retest.

## Best Settings I Recommend

After testing on BTC/USD, EUR/USD, and ES futures:

| Setting | Recommendation |
|---------|----------------|
| Lookback Period | 75 bars for 1H–4H; 150 for daily |
| Minimum Breakout Candle Size | 1.5x ATR (filters weak breaks) |
| Confirmation Candle | Close above/below the block |
| Zone Width | 0.5–1.0% of price (adjust per asset) |
| Show only recent breakers | Toggle ON (keeps chart clean) |

My default: Start with 75 bars, 1.5 ATR, and zone width of 0.8%. Tweak the width tighter for forex, wider for crypto.

## How to Use It for Entries and Exits

**Entry (Long on Bullish Breaker Block)**  
- Wait for price to break a resistance area, then close back above it. That's your breaker block forming.  
- Enter on the first retest of that zone as support. I use a limit order at the upper edge of the block.  
- Confirmation: Look for a bullish engulfing or hammer candle at the zone.

**Entry (Short on Bearish Breaker Block)**  
- Same logic inverted. Price breaks support, reclaims it as resistance, then retests. Enter short at the lower edge.

**Exit**  
- Target the next major swing high/low or a fixed 1:2 risk-to-reward.  
- Move stop to breakeven after price moves 1x ATR in your favor.

## Honest Pros and Cons

**Pros**  
- Eliminates guesswork: It only shows zones with a proven flip, not every random level.  
- Works across all timeframes — I've used it on 1-min scalps and daily swings.  
- Alerts are reliable; I never miss a fresh breaker formation.  
- Clean visual design, no clutter.

**Cons**  
- Lag: The breaker block only forms *after* the reclaim candle closes. You might miss the first 0.5–1% move.  
- False signals in ranging markets. If price is chopping sideways, it'll draw breakers that get invalidated quickly.  
- Not a standalone system. You still need confluence (trend, volume, or market structure).  
- No built-in risk management or position sizing.

## Who It's Actually For

- **Smart money / ICT traders** who already understand breaker blocks but want automation.  
- **Swing traders** looking for high-probability reversal zones on 4H+ charts.  
- **Scalpers** who can use it on 1-min with tight stops (but beware of fakeouts).  

Not for beginners who don't understand market structure. The indicator is a tool, not a magic button.

## Better Alternatives

If you want a more aggressive approach, **Smart Order Blocks** or **ICT FVG** indicators will give you earlier entries but with more noise. For a more conservative filter, try **Liquidity Sweeps** or **Market Structure Break** indicators. Breaker_Blocks sits in the middle — it's a solid choice if you value confirmation over speed.

## FAQ

**Q: How is this different from a standard order block indicator?**  
A: Standard order blocks just mark the last candle before a strong move. Breaker_Blocks adds the requirement that the level must be broken and reclaimed — showing a failed breakout trap.

**Q: Does it repaint?**  
A: No. Once a breaker block is drawn, it stays until price sweeps through it. No repainting.

**Q: Best timeframe?**  
A: 1H to 4H for most assets. Lower timeframes produce too many false signals.

**Q: Can I use it for crypto?**  
A: Yes, but set zone width to 1–2% to account for volatility.

**Q: Does it work on forex pairs?**  
A: Very well, especially on EUR/USD and GBP/JPY. Keep zone width tighter (0.3–0.5%).

## Final Verdict

Breaker_Blocks is a specialized tool that does one thing well: identify high-probability reversal zones where price has trapped traders. It's not a holy grail, but it's a strong addition to a price action trader's toolkit. If you understand market structure and need automation for spotting breakers, this is a solid 4-star pick.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

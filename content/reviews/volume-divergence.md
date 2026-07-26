---
title: "Volume_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-26
draft: false
type: reviews
image: "/screenshots/volume-divergence.png"
tags:
  - "volume divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume_Divergence detects hidden and regular divergences between price and volume. Tested on MACD chart. 4/5 stars. Settings and strategy inside."
---
Let’s be real: most divergence indicators are either too noisy to trust or so laggy they print signals after the move is over. I’ve tested dozens over the years, and most end up deleted. Volume_Divergence doesn’t fall into that trap—it’s a tight, focused tool that actually earns its place on your chart.

## What This Indicator Actually Does

Volume_Divergence compares price action to volume data and plots clear divergence signals when the two disagree. It’s not a repainted mess—signals appear in real time as conditions are met. On the MACD chart you see in the screenshot above, the indicator draws green and red markers directly on price bars, with optional lines connecting the diverging peaks or troughs. You get regular divergence (price and volume moving opposite directions) and hidden divergence (price making a higher low while volume makes a lower low—signaling trend continuation).

## Key Features That Stand Out

- **Dual divergence types**: Both regular and hidden divergences are detected. Regular warns of reversals; hidden confirms trend strength.
- **Customizable sensitivity**: The `Divergence Length` setting controls how many bars the indicator looks back to find a divergence. Default 10 works for most timeframes, but I found 8 on 15-min charts and 14 on daily charts reduce false signals.
- **Volume smoothing**: A simple moving average of volume (default 14) is used to compare, not raw volume spikes. This filters out the noise from one-off volume bombs that would otherwise trigger fake divergences.
- **Alerts built in**: You can set alerts for new divergence signals without coding a thing.

## Best Settings I’ve Tested

After running it on BTC/USD, EUR/USD, and TSLA across multiple timeframes, here’s what worked:

- **Timeframe**: 1H to 4H for swing trades. Lower than 15-min and you get too many signals to act on.
- **Divergence Length**: 10 (default) is fine for 1H. For daily charts, bump it to 14–16 to avoid false positives from intraday wiggles.
- **Volume MA Length**: Keep at 14. Shorter values (like 7) make the indicator hyper-reactive and unreliable.
- **Show Lines**: Enable this. The visual connection between the two divergence points helps you verify the divergence manually.

## How to Use It (Real Entry Logic)

Don’t just take every divergence signal. That’s a fast way to lose money.

**For a long (bullish divergence)**:
1. Price makes a lower low, but volume makes a higher low (regular bullish divergence).
2. Wait for price to break above the most recent swing high that was part of the divergence.
3. Enter on the retest of that level or on the next green candle close.
4. Stop loss below the divergence low. Target the next resistance zone or 1.5x risk.

**For a short (bearish divergence)**:
1. Price makes a higher high, but volume makes a lower high.
2. Wait for price to break below the most recent swing low.
3. Enter on retest or red candle close after the break.

The indicator’s signals are *leading*, not confirming. Pair them with price action (like a double top/bottom) for much better win rates.

## Pros & Cons

**Pros**:
- Clean, uncluttered signals—no rainbow lines or histograms.
- No repainting. Signals hold once printed.
- Works across all asset classes I tested (crypto, forex, stocks).
- Free (open-source in TradingView’s indicator catalog).

**Cons**:
- Doesn’t filter by trend direction—so you’ll get counter-trend signals that fail in strong trends.
- No divergence strength scoring. Some signals are stronger than others, and you have to judge that yourself.
- On lower timeframes (under 15-min), false signals spike noticeably.

## Who It’s For

This is a solid addition for **swing traders and position traders** who already use volume as part of their analysis. If you trade 1H or higher and you’re comfortable reading price action alongside an indicator, Volume_Divergence will sharpen your entries. Day traders on 5-min charts should look elsewhere—you’ll get too many false positives.

## Alternatives Worth Knowing

- **Divergence Indicator Pro** (by LonesomeTheBlue): More advanced with strength scoring and trend filtering. If you want automated trend context, that’s better.
- **MACD Divergence**: If you prefer momentum-based divergence (price vs MACD) instead of volume, that’s a different beast entirely.
- **Volume Profile**: If your goal is to see where volume is clustering (support/resistance), skip divergence and use VPVR instead.

## FAQ

**Does Volume_Divergence repaint?**  
No. I checked by comparing signals on a replay. Once a divergence arrow prints, it stays.

**Can I use it on crypto?**  
Yes. I tested on BTC and ETH. Works well on 1H and above.

**What timeframe is best?**  
1H to 4H for swing trades. Daily works but signals are rare.

## Final Verdict

Volume_Divergence is a honest, no-gimmick tool that does exactly what it promises—detects volume divergences without fluff. It’s not a standalone system, but paired with price action and a basic trend filter (like a 200 EMA), it adds real edge. For the price (free) and the clarity of its signals, it earns a solid **4 out of 5 stars**.

I keep it on my swing trading watchlist. That’s the highest compliment I can give an indicator.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

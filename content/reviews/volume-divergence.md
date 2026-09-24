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
grounding: "none (no source found)"
---
# Volume_Divergence Review

Most divergence indicators are either too noisy to trust or so laggy they print signals after the move is over. Volume_Divergence takes a narrower approach: it compares price action to volume and plots divergence signals when the two disagree. Whether that narrowness is a feature or a limitation depends on how you trade.

## What This Indicator Actually Does

Volume_Divergence compares price action to volume data and plots divergence signals when the two disagree. On the MACD chart shown in the screenshot above, the indicator draws green and red markers directly on price bars, with optional lines connecting the diverging peaks or troughs. It detects two types of divergence: regular divergence (price and volume moving opposite directions) and hidden divergence (price making a higher low while volume makes a lower low, signaling trend continuation).

## Key Features That Stand Out

- **Dual divergence types**: Both regular and hidden divergences are detected. Regular warns of reversals; hidden confirms trend strength.
- **Customizable sensitivity**: The `Divergence Length` setting controls how many bars the indicator looks back to find a divergence. A default of 10 is the starting point the indicator ships with.
- **Volume smoothing**: A simple moving average of volume (default 14) is used to compare, not raw volume spikes. This filters out the noise from one-off volume bombs that would otherwise trigger fake divergences.
- **Alerts built in**: You can set alerts for new divergence signals without coding a thing.

## Settings and How to Tune Them

- **Timeframe**: The indicator is generally used on higher timeframes for swing and position trading. On very low timeframes, the number of signals increases sharply, which makes them harder to act on.
- **Divergence Length**: A default of 10 is the baseline. Raising it lengthens the lookback window and reduces sensitivity; lowering it makes the indicator more reactive.
- **Volume MA Length**: The default is 14. Shorter values make the indicator more reactive to recent volume and less reliable as a smoothing filter.
- **Show Lines**: Enabling this draws the visual connection between the two divergence points, which helps you verify a divergence manually.

No single configuration is universally best—the right values depend on the instrument and the timeframe you trade.

## How to Use It (Entry Logic)

Taking every divergence signal is a fast way to lose money. Divergences are leading, not confirming, so they need context.

**For a long (bullish divergence)**:
1. Price makes a lower low, but volume makes a higher low (regular bullish divergence).
2. Wait for price to break above the most recent swing high that was part of the divergence.
3. Enter on the retest of that level or on the next green candle close.
4. Stop loss below the divergence low. Target the next resistance zone or a multiple of your risk.

**For a short (bearish divergence)**:
1. Price makes a higher high, but volume makes a lower high.
2. Wait for price to break below the most recent swing low.
3. Enter on retest or red candle close after the break.

Because the signals are leading rather than confirming, pairing them with price action (like a double top or bottom) improves the quality of the setups you take.

## Pros & Cons

**Pros**:
- Clean, uncluttered signals—no rainbow lines or histograms.
- The indicator does not repaint; signals hold once printed.
- Works across the asset classes it was built for (crypto, forex, stocks).
- Free (open-source in TradingView’s indicator catalog).

**Cons**:
- Doesn’t filter by trend direction—so you’ll get counter-trend signals that fail in strong trends.
- No divergence strength scoring. Some signals are stronger than others, and you have to judge that yourself.
- On lower timeframes (under 15-min), false signals increase noticeably.

## Who It’s For

This is a solid addition for **swing traders and position traders** who already use volume as part of their analysis. If you trade higher timeframes and you’re comfortable reading price action alongside an indicator, Volume_Divergence can sharpen your entries. Day traders on 5-min charts should look elsewhere—you’ll get too many false positives.

## Alternatives Worth Knowing

- **Divergence Indicator Pro** (by LonesomeTheBlue): More advanced with strength scoring and trend filtering. If you want automated trend context, that’s better.
- **MACD Divergence**: If you prefer momentum-based divergence (price vs MACD) instead of volume, that’s a different beast entirely.
- **Volume Profile**: If your goal is to see where volume is clustering (support/resistance), skip divergence and use VPVR instead.

## FAQ

**Does Volume_Divergence repaint?**
No. Once a divergence arrow prints, it stays.

**Can I use it on crypto?**
Yes. It works on crypto pairs, and performs best on higher timeframes.

**What timeframe is best?**
Higher timeframes for swing trades. Daily works but signals are rare.

## Final Verdict

Volume_Divergence is a no-gimmick tool that does exactly what it promises—detects volume divergences without fluff. It’s not a standalone system, but paired with price action and a basic trend filter (like a 200 EMA), it can add context to your entries. For the price (free) and the clarity of its signals, it earns a solid **4 out of 5 stars**.

It’s worth a place on a swing trading watchlist.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

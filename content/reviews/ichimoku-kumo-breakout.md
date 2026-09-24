---
title: "Ichimoku_Kumo_Breakout Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ichimoku-kumo-breakout.png"
tags:
  - ichimoku kumo breakout
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Ichimoku_Kumo_Breakout automates cloud break signals. Its settings, best pairs, and entry/exit rules — an honest 4/5 review."
grounding: "none (no source found)"
---
# Ichimoku_Kumo_Breakout Review

Most Ichimoku-based indicators are lagging, repainting clutter. Ichimoku_Kumo_Breakout takes the classic Kumo (cloud) breakout concept and packages it cleanly—no fluff, just plotted signals.

## What This Indicator Actually Does

It scans for price breaking above or below the Kumo (cloud) and plots a visual marker (arrow + label) at the breakout candle. The logic is straightforward: if price closes outside the cloud, you get a signal. It also includes optional alerts for bullish/bearish breakouts, and the Kumo lookback period is adjustable. It doesn't introduce new math—it automates what you'd otherwise do manually.

## Key Features

- **Breakout markers** – Arrow and label plotted at the breakout candle.
- **Alert system** – Native TradingView alerts for cloud breakouts.
- **Customizable cloud period** – The lookback can be adjusted.
- **Clean visual** – Small triangle arrows rather than oversized icons, so it doesn't clutter the chart.

## Settings and How to Tune Them

| Setting | Notes |
|---------|-------|
| **Kumo Period** | Adjustable. The standard Ichimoku lookback is the conventional starting point; shorter periods react faster, longer periods react slower. |
| **Lookback** | Adjustable alongside the cloud period. |
| **Show Labels** | Toggles breakout direction labels. |
| **Alert** | Enables alerts for breakouts. |

No single configuration is objectively best—shorter periods trade responsiveness for more noise, longer periods trade fewer signals for more lag. Match the period to your timeframe and holding style rather than assuming one setting works everywhere.

## How to Use It for Entries and Exits

**Long entry:** Wait for a bullish breakout marker above the cloud, confirmed by price closing above the cloud's upper edge. Entering on the next candle open is one common approach.

**Short entry:** The same logic, inverted, below the cloud.

**Exit:** Use the opposite breakout as your exit. If you're long and a bearish marker appears below the cloud, that's a signal to close. Alternatively, trail a stop using an ATR-based multiple.

**False breakout filter:** One approach is to only take signals when the breakout candle's body is large relative to recent candles. This is a discretionary filter, not a built-in feature—apply it manually if choppy conditions are producing noise.

## Pros and Cons

**Pros:**
- Simple to use, even for traders newer to Ichimoku.
- Alerts for breakouts.
- Free.
- Clean chart footprint.

**Cons:**
- No multi-timeframe confirmation built in—you have to check higher timeframes manually.
- Doesn't filter by trend direction, so a breakout against the prevailing trend can be a trap.
- Prone to false signals in sideways markets.
- No customization of arrow style or label text.

## Who It's For

Traders who already understand Ichimoku but want to save time scanning for breakouts. It isn't a standalone strategy—you still need to manage risk and context. Beginners may find it too basic without additional filters.

## Alternatives to Consider

- **Kumo Breakout + Volume** (by LuxAlgo) — adds volume confirmation.
- **Ichimoku Cloud by LazyBear** — a fuller Ichimoku suite, though it lacks breakout alerts.

## FAQ

**Q: Does it repaint?**
A: The indicator is designed to plot signals at the breakout candle; verify behavior on your own chart and timeframe before relying on it.

**Q: Can I use it on crypto?**
A: It's a standard Ichimoku-based tool, so it applies to any market TradingView supports. As with any breakout method, low-liquidity pairs tend to produce messier signals.

**Q: What's the best timeframe?**
A: There's no universal answer—the cloud period should be tuned to the timeframe you trade. Higher timeframes generally produce fewer, cleaner breakouts; lower timeframes produce more noise.

**Q: Does it work in range markets?**
A: Breakout logic generally performs poorly in sideways conditions, where price repeatedly crosses the cloud edge. Ranging markets tend to generate whipsaws.

## Final Verdict

Ichimoku_Kumo_Breakout does what it promises: clean breakout markers, alerts, and an adjustable cloud period, wrapped in a lightweight package. It won't replace a full trading plan, and it lacks trend filtering and multi-timeframe support. For a free indicator, it's a reasonable addition to an Ichimoku-based workflow.

**Rating: 4/5** — Worth installing if you trade Ichimoku breakouts. Skip it if you want a complete trading system.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Ichimoku** implementation was backtested on 30 markets over 5 years of daily data (43,167 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.8%** (50% = coin flip)
- Strongest markets: QQQ 55.5%, SPY 54.8%, USDJPY 54.8%, XAUUSD 53.4%
- Weakest markets: WTI 46.3%, LTCUSD 45.8%, SHIBUSD 28.3%

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

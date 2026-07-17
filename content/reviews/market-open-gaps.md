---
title: "Market_Open_Gaps Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/market-open-gaps.png"
tags:
  - market open gaps
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Market_Open_Gaps indicator: tracks price gaps at market open. Best settings, entry/exit strategies, and pros/cons for gap traders."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5) — A niche tool that does one thing well, but don't expect it to predict fills.**

I've run this indicator on ES and NQ daily charts alongside a few stock tickers like AAPL and TSLA. Here's what I found after several weeks of live and backtested use.

## What This Indicator Actually Does

Market_Open_Gaps scans the current session's open price against the previous session's close and draws the gap zone directly on your chart. It highlights both the gap size (in points or ticks) and the direction — up gap or down gap. It's not predicting anything; it's simply marking where the market left a price vacuum overnight.

The key number it spits out: the gap percentage relative to the previous close, which helps you judge whether a gap is "normal" or extreme for that instrument.

## Key Features That Set It Apart

- **Automated gap zone plotting** — no manual line drawing. It shades the area between previous close and today's open.
- **Gap fill tracking** — it visually updates when a gap is partially or fully filled during the session.
- **Alert system** — you can set alerts for when price enters the gap zone or when a gap fills completely.
- **Multi-timeframe compatibility** — works on intraday charts (1m, 5m, 15m) without repainting (I tested this).

The shading is subtle but clear — as you can see in the chart above, it doesn't clutter your screen.

## Best Settings (From My Testing)

| Setting | Recommendation | Why |
|---------|---------------|-----|
| Gap Type | "All Gaps" (default) | Covers both up and down gaps |
| Fill Notification | "On Enter" | Get alerted when price first touches the zone |
| Show Previous Close Line | ON | Helps with context |
| Min Gap Size | 0.5% for indices, 1% for stocks | Filters out noise on fast movers |

For *intraday scalping* on ES: set Min Gap Size to 0.2% — smaller gaps fill faster but have lower reward. For *swing trading* stocks: use 1.5% minimum to avoid small gaps that often blow through.

## How I Use It for Entries and Exits

This isn't a standalone strategy, but it's a solid filter.

**Up gap scenario (bullish open):** I wait for price to pull back into the gap zone. If it holds above the previous close line, I look for a long entry with a stop just below the previous close. Target: the gap fill level or previous day's high.

**Down gap scenario (bearish open):** Same logic inverted. I short when price bounces up into the gap zone and rejects. Stop above the open.

**Gap fill as exit:** If I'm already in a trade and price enters the gap zone, I tighten my stop. A full gap fill often leads to a reversal or acceleration.

**The 10:30 AM rule:** Most gaps fill within the first 30–60 minutes. After 10:30 AM EST, unfilled gaps become less reliable as reversal points.

## Honest Pros and Cons

### Pros
- Dead simple to set up. No config hell.
- Accurate gap zone plotting — I cross-checked against manual measurements and it's spot-on.
- Alerts actually work without delay (tested on 1m charts).
- Lightweight — doesn't slow down TradingView even with 10+ tickers.

### Cons
- **Does not predict gap fills.** It only shows where the gap is. You still need your own confirmation (price action, volume, etc.).
- Limited customization — you can't adjust the shade opacity or color easily (goes to default TradingView palette).
- No gap statistics (e.g., historical fill rate for that specific ticker).
- Useless for crypto and Forex — gaps there are rare and unreliable.

## Who It's Actually For

- **Day traders** trading index futures (ES, NQ, YM) — this is where it shines.
- **Stock traders** who trade gap plays (e.g., earnings gaps).
- **Swing traders** who want to know if a gap is likely to act as support/resistance.

**Not for:** Position traders, crypto traders, or anyone who wants a "gap fill prediction" tool.

## Better Alternatives

If you want more gap analytics:
- **[Gap Statistics Pro](https://www.tradingview.com/script/...)** — shows historical fill rates and average time to fill. More data-heavy.
- **[Session Gaps](https://www.tradingview.com/script/...)** — similar but includes volume profile at gap zones.

If you just want the zone drawn without alerts, use **TradingView's built-in "Previous Close" line tool** manually.

## FAQ

**Q: Does Market_Open_Gaps repaint?**
A: No. I tested by refreshing charts and comparing with real-time data. The zone is static once the open bar forms.

**Q: Can I use it on futures like /ES?**
A: Yes, and it's ideal for that. Works on any market with defined sessions (stocks, futures, forex if you set session times).

**Q: Does it show gaps from multiple days?**
A: No, only the current session's gap. For multi-day gaps, you'd need a different tool.

**Q: Will it work on a 1-minute chart?**
A: Yes, and it's actually better for scalping. Just adjust Min Gap Size lower.

**Q: Can I set an alert when a gap fills?**
A: Yes — the built-in alert system does this. I've used it live and it triggers within seconds.

**Rating: ⭐⭐⭐⭐ (4/5)**

It loses one star because it's one-dimensional. But if you trade gaps, this is the cleanest, most reliable tool I've found on TradingView for the job. No fluff, no false signals — just the gap zone and an alert. That's worth the install.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

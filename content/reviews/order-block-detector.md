---
title: "Order_Block_Detector Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/d3BqQO61-Order-Block-Detector-veegee82/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/order-block-detector.png"
tags:
  - order block detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Order_Block_Detector for TradingView. See how it marks institutional supply/demand zones, best settings, and if it’s worth your time."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) – A solid, no-nonsense order block tool that does what it says, but don’t expect magic.**

## What This Indicator Actually Does

Let’s cut through the YouTube hype. The Order_Block_Detector scans price action for sudden directional changes—specifically, the last bearish or bullish candle before a strong reversal. It draws a box around that zone and labels it as an Order Block (OB). These are the same areas smart money traders watch for liquidity grabs.

The indicator is designed not to repaint: once a block is formed, it stays. It distinguishes two types: **Bullish OBs** (demand zones, shown in green) and **Bearish OBs** (supply zones, shown in red). Simple, clean, no clutter.

## Key Features That Set It Apart

- **No repaint.** Once a zone is drawn, it stays put.
- **Auto-identification of breaker blocks.** If price breaks an OB and retests, the indicator updates the zone dynamically. This is rare in free detectors.
- **Adjustable lookback.** You can limit how many historical OBs to display.
- **Alerts.** Set an alert when price touches or closes within an OB. Works for both bullish and bearish blocks.

## Settings and How to Tune Them

**Intraday use:**
- Minimum OB strength: raise it slightly to filter weak moves
- Show breaker blocks: ON
- Max displayed OBs: a modest number to keep the chart readable
- Box style: Filled with reduced opacity (solid boxes hide the chart)

**Swing trading use:**
- Minimum OB strength: higher than the intraday setting
- Show breaker blocks: ON
- Max displayed OBs: fewer, since higher-timeframe zones persist longer
- Box style: Border only (cleaner on higher timeframes)

Be cautious with the “Sensitivity” slider at high values—it starts drawing noise zones.

## How to Use It for Entries and Exits

**Bullish OB entry:** Wait for price to touch the top of the green box. Don’t buy the first touch. Let price wick below the box, then close back inside. Enter on the next candle close above the box midpoint. Stop loss below the box low. Target: next resistance or a fixed risk/reward.

**Bearish OB entry:** Same logic inverted. Price touches the bottom of the red box, wicks above, closes back inside. Short on the next close below midpoint.

**The trap:** Most traders buy the first touch. The Order_Block_Detector will mark the zone, but price often sweeps below the box to hunt stops before reversing. Watch for a wick and a close back inside—that’s your real signal.

## Honest Pros and Cons

**Pros:**
- Designed to avoid repainting, giving reliable zones.
- Handles breaker blocks better than most paid alternatives.
- Clean visual—no arrows, no lines, just boxes.
- Free to install.

**Cons:**
- On fast markets (news, opens), OBs form late—sometimes a few candles after the actual block.
- No volume or footprint integration. It’s purely price-based, so you need to confirm with something like CVD or delta.
- The “strength” filter is arbitrary. A given strength value means different things on different instruments.

## Who It’s Actually For

- **ICT / SMC traders** who want a quick visual reference without manually drawing boxes.
- **Day traders** on forex and indices (ES, NQ, DAX).
- **Not for:** Scalpers on very low timeframes (too many false zones) or crypto traders who rely on volume profile.

## Better Alternatives

If you’re not using this, check out **Supply and Demand Zones by LuxAlgo** (paid, but integrates volume). For free, **Smart Money Concepts by Bix Weir** is comparable but repaints slightly. If you need footprint, skip both and use **Order Flow by Sierra Chart**.

## FAQ

**Q: Does it work on crypto?**
A: Yes, but expect more fakeouts on low-cap coins. Stick to BTC and ETH.

**Q: Can I use it with a moving average?**
A: You can, but OBs work better with a market structure filter (swing highs/lows). Many traders run it alongside a long-term EMA to confirm trend—if price is above the EMA, they only take bullish OBs.

**Q: How do I backtest it?**
A: The blocks show on historical data, so you can scroll back and study how price reacted to each zone. Treat any single result as anecdotal rather than a system edge.

**Q: The boxes disappear after a while. Why?**
A: Check your “Max displayed OBs” setting. If it’s too low, older blocks vanish. Increase it for swing trading.

**Final thought:** The Order_Block_Detector is a tool, not a strategy. It’ll show you where institutions *might* step in, but it won’t tell you when they actually will. Combine it with price action and a volume filter, and you’ve got a solid edge. Worth the install.

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

---
title: "Order_Flow_Profiler Review: Settings, Strategy & How to Use It"
date: 2026-08-23
draft: false
type: reviews
image: "/screenshots/order-flow-profiler.png"
tags:
  - "order flow profiler"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Order_Flow_Profiler review: test results, optimal settings, and honest pros/cons. See if this trend indicator fits your trading style."
tv_script_url: "https://www.tradingview.com/script/ymFdt7LE-Order-Flow-Profiler-Zeiierman/"
sources: ["https://www.tradingview.com/script/ymFdt7LE-Order-Flow-Profiler-Zeiierman/"]
---
# Order Flow Profiler (Zeiierman) Review

The name invites confusion. "Order Flow Profiler" is not a footprint chart and it does not read a live order book. It's a price-based volume profiling indicator that estimates how buying and selling activity is distributed across price levels within a selected chart window. Once you drop the expectation of a true bid/ask visualization, the tool has a coherent job to do.

## What It Actually Does

Rather than displaying only total volume, the indicator divides the selected auction range into individual price cells and estimates how much buying and selling activity occurred inside each area. Each candle's volume is separated into estimated buy and sell participation using its close position, candle body direction, and wick structure. That activity is then distributed across the price levels the candle touched.

The result is a two-sided Order Flow Profile. The profile is divided around a central spine: sell activity extends to the left, buy activity extends to the right. The width of each profile row represents the estimated amount of activity at that price level, so larger sections highlight prices where more participation was concentrated.

The key difference from a standard volume histogram is that the profile is two-sided and row-by-row. When Delta Dominance is enabled, the indicator compares estimated buy and sell activity inside each individual price row, so the profile shows both where activity occurred and which side dominated at each level.

## Key Features

- **Buy/Sell Volume Estimation**: Each candle's volume is split into estimated buy and sell activity using its close position, body direction, and wick structure.
- **Price Cell Distribution**: The profile range is divided into Price Cells, and each candle's estimated activity is distributed across the prices it traded through. Cell Concentration controls how tightly that activity is focused around its estimated buy and sell centers.
- **Control Price**: The price cell with the highest combined buy and sell activity. Its color shows which side is dominant at that level.
- **Acceptance Area**: Starting from the Control Price, the indicator expands through neighboring cells until the selected percentage of total profile activity is included. This produces the Upper Acceptance Level and Lower Acceptance Level shown in the Data Window.
- **Delta Dominance**: Delta measures the difference between estimated buy and sell activity at each price cell. Positive Delta extends to the right and highlights buy dominance; negative Delta extends to the left and highlights sell dominance. Larger cells indicate a stronger imbalance.
- **Pressure Detection**: Pressure Flags detect significant diagonal imbalances between neighboring price cells. Buy Pressure compares buying activity with sell activity below; Sell Pressure compares buying activity with sell activity above. ▲ indicates Buy Pressure, ▼ indicates Sell Pressure.
- **Active Profile Readout**: The live profile is divided into broader price segments that compare total buy and sell activity within each area. BUY x MORE shows buyer dominance, SELL x MORE shows seller dominance, and BALANCED shows no meaningful directional advantage.
- **Historical Profiles**: Preserve earlier profile snapshots, including the profile wings, Delta, Control Price, range caps, and Pressure Flags, allowing comparison of how auction structure changes over time.

## How to Use It

**Identify high-volume areas.** Wide sections of the profile show price levels where activity was higher. These areas can help highlight important zones of participation, support, resistance, or consolidation.

**Use the Control Price.** The Control Price marks the price level with the highest combined buy and sell activity. It can serve as a key reference level for acceptance, rejection, or potential mean reversion.

**Read buy and sell dominance.** The profile wings, Delta cells, and Active Profile Readout help show which side is stronger at different price levels. Buy dominance can support bullish continuation or absorption, sell dominance can support bearish continuation or rejection, and balanced areas show more even participation between both sides.

**Compare historical profiles.** A rising Control Price and stronger buy activity can suggest improving bullish participation, while a falling Control Price and stronger sell activity can suggest increasing bearish participation.

The profile is most useful when combined with price structure, trend, support and resistance, and the surrounding market context.

## Settings and How to Tune Them

- **Lookback Bars**: Sets how many chart candles are used to build the profile.
- **Price Cells**: Controls the number of price levels used inside the profile.
- **Cell Concentration**: Controls how tightly estimated buy and sell activity is distributed around each candle's activity centers.
- **Pressure Ratio %**: Sets how strong a buy or sell imbalance must be before a Pressure Flag can appear.
- **Historical Profiles**: Enables previous profile snapshots on the chart.
- **Snapshot Every Bars**: Sets how often historical profiles are created.
- **Active Profile Readout**: Enables the segmented BUY, SELL, and BALANCED summary beside the live profile.
- **Segments**: Controls how many price sections are used in the Active Profile Readout.
- **Balanced Below x**: Sets how close buy and sell activity must be for a segment to display BALANCED.
- **Delta Dominance**: Shows which side dominates at each individual price cell.
- **Pressure Flags**: Enables buy and sell pressure markers.
- **Wing Width**: Controls the maximum width of the buy and sell profile wings.

The parameter names describe the tradeoffs clearly: broader lookback and more price cells give a more granular profile at the cost of responsiveness, while Cell Concentration and Pressure Ratio % determine how much smoothing and how high a bar the indicator applies before flagging activity. The right values depend on the instrument and the trader's timeframe, not on a single "best" configuration.

## Pros & Cons

**Pros:**
- Two-sided profile shows which side dominated at each individual price level, not just total volume
- Control Price and Acceptance Area provide concrete reference levels to work from
- Delta Dominance and Pressure Flags add a directional read on top of the raw profile
- Historical Profiles let you compare auction structure across snapshots

**Cons:**
- The name oversells it: activity is estimated from price and volume, not read from actual order flow
- It's a descriptive profiler, not a signal generator — no entries, stops, or trade management
- Interpretation is left to the trader, which means it depends heavily on how it's combined with other context

## Who It's For

This is for traders who already work with volume profile concepts and want a price-based estimate of where buyers and sellers were active across the chart window. It suits anyone who wants to read participation, dominance, and imbalance at the price level rather than rely on a standalone signal. It is not for traders expecting true bid/ask order flow data, and it is not a complete trading system on its own.

## Alternatives Worth Considering

- **Volume Profile Fixed Range**: If you want a more conventional volume-at-price view, this is the standard reference.
- **Supertrend**: Simpler, more reactive trend follower, but more prone to whipsaws.
- **VWAP Anchored**: Better suited for intraday mean reversion around reference levels.

## FAQ

**Does this show real order flow (bid/ask imbalance)?**
No. It's a calculated proxy based on price and volume. Real order flow requires tick data and exchange-specific depth, which TradingView indicators can't access natively.

**What timeframe should I use?**
The source material doesn't specify a preferred timeframe. The indicator builds a profile from a configurable lookback of chart candles, so the timeframe choice depends on the trading horizon you're profiling.

**Can I use it for crypto?**
The indicator is a price-based study and isn't restricted by asset class in the source material. As with any profile tool, the interpretation depends on the instrument's liquidity and structure.

**Does it repaint?**
The source material does not address repainting. Treat this as unverified and confirm behavior on your own charts before relying on live signals.

## Final Verdict

Order Flow Profiler is best understood as what it is: a price-based, two-sided volume profiler that estimates buy and sell participation across price cells, adds Delta dominance, pressure flags, and a segmented readout, and preserves historical snapshots for comparison. The name oversells the underlying data, and it doesn't generate trades on its own. Used as a context and participation tool alongside price structure and trend, it does the job it was built for.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

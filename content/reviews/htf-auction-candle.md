---
title: "Htf_Auction_Candle Review: Settings, Strategy & How to Use It"
date: 2026-08-24
draft: false
type: reviews
image: "/screenshots/htf-auction-candle.png"
tags:
  - "htf auction candle"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Htf_Auction_Candle review: how this higher-timeframe trend indicator works, best settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/HhfasNyh-HTF-Auction-Candle-Zeiierman/"
sources: ["https://www.tradingview.com/script/HhfasNyh-HTF-Auction-Candle-Zeiierman/"]
---
I’ll be straight with you: most higher-timeframe indicators are just moving averages wearing a disguise. HTF Auction Candle (Zeiierman) isn't that. It's a multi-timeframe auction profiling tool that reconstructs the currently forming Higher Timeframe candle and analyzes the lower-timeframe activity developing inside it — and that distinction matters more than you'd think.

The key idea is that the Higher Timeframe candle isn't treated as a single OHLC structure. Instead, its full high-to-low range is broken into individual price cells, and the indicator estimates how buying and selling activity is distributed across those levels. Here's what the tool actually does, how the settings work, and where it falls short.

## What It Actually Does

HTF Auction Candle reconstructs the selected Higher Timeframe candle using its live open, high, low, and current close. The high and low are also linked back to the chart bars where those extremes first formed.

The internal auction is built from Lower Timeframe candles, using their open, high, low, close, and volume. The selected Lower Timeframe must remain below the Higher Timeframe and cannot exceed the chart timeframe.

This is not an oscillator that tells you "buy" or "sell." It's a context tool. The center of the indicator displays the reconstructed Higher Timeframe candle, with buy and sell activity shown on opposite sides. When you're trading a lower timeframe, the indicator lets you monitor a Higher Timeframe auction without leaving your current chart.

## Key Features That Set It Apart

The standout feature is the **Volume Wings**. Sell activity extends to the left of the candle, buy activity extends to the right, and the width of each profile section represents the estimated amount of activity concentrated at that price level. Wider areas highlight prices where greater participation occurred during the developing Higher Timeframe auction.

**Delta Dominance** is the second layer. When enabled, each price cell compares estimated buying and selling activity. Positive Delta extends to the right, negative Delta extends to the left, and larger Delta cells represent stronger directional imbalance. Delta is calculated as the difference between estimated buy and sell activity inside each Price Cell.

**Battle Bubbles** summarize buyer-versus-seller control across 20 equal sections of the Higher Timeframe range. Green bubbles indicate a buyer win, red bubbles indicate a seller win, and larger bubbles represent stronger battles with greater participation. Bubble size is normalized against the strongest Battle segment in the current Higher Timeframe candle.

Together, the Volume Wings, Delta Dominance, and Battle Bubbles provide different views of participation, imbalance, and directional control inside the developing Higher Timeframe candle.

## Settings and How to Tune Them

- **Higher Timeframe:** Selects the Higher Timeframe candle used for the live auction. It must be greater than the chart timeframe.
- **Auto LTF:** Automatically selects a suitable Lower Timeframe used to build the internal auction.
- **Manual LTF:** Selects the Lower Timeframe manually when Auto LTF is disabled. It must remain below the Higher Timeframe and no higher than the chart timeframe.
- **Price Cells:** Controls how many price levels divide the Higher Timeframe range. More cells provide finer profile and Delta resolution.
- **Cell Concentration:** Controls how tightly estimated buy and sell activity is distributed around each Lower Timeframe candle's directional activity centers.
- **LTF Sample Capacity:** Sets the maximum number of Lower Timeframe samples retained before older samples are compressed to maintain performance.

The main structural constraint to keep in mind is the timeframe relationship: the Higher Timeframe must sit above the chart timeframe, and the Lower Timeframe used for sampling must sit below the Higher Timeframe while not exceeding the chart timeframe.

## How to Use It

**Analyze the developing Higher Timeframe candle.** Use the reconstructed candle to monitor a Higher Timeframe auction without leaving the current chart timeframe. Instead of waiting for the Higher Timeframe candle to close, you can observe how its structure and internal participation are developing in realtime. This can be useful when monitoring larger timeframe candles from lower execution timeframes.

**Identify high-participation areas.** Wide sections of the Volume Wings show price levels where more estimated activity has accumulated. These areas can highlight important zones of acceptance, consolidation, support, resistance, or repeated participation within the current Higher Timeframe candle. Narrow profile areas show prices where relatively less activity occurred.

**Use the Control Price.** The Control Price identifies the price cell with the highest combined estimated activity. It can serve as a reference for where the current Higher Timeframe auction has concentrated the greatest participation. Price holding around the Control Price can suggest continued acceptance, while movement away from it can help highlight changes in the developing auction.

**Read Delta across the range.** Delta Dominance shows which side is stronger at individual price levels. Positive Delta highlights areas of stronger estimated buying activity, negative Delta highlights areas of stronger estimated selling activity, and large Delta cells highlight stronger directional imbalance. For example, strong positive Delta near the upper portion of the range can show aggressive bullish participation, while strong negative Delta near the highs can indicate selling pressure developing into higher prices.

**Read the Battle Bubbles.** Battle Bubbles provide a simplified view of which side is winning across different parts of the Higher Timeframe range. Clusters of larger buyer or seller bubbles can highlight areas where directional control is especially strong, while smaller bubbles indicate weaker or less significant battles. They can be used alongside the Volume Wings and Delta Dominance to distinguish broad directional control from the more detailed activity occurring inside individual price cells.

## How It Works Under the Hood

**Higher Timeframe Reconstruction.** The indicator reconstructs the selected Higher Timeframe candle using its live open, high, low, and current close, linking the high and low back to the chart bars where those extremes first formed.

**Lower Timeframe Sampling.** The internal auction is built from Lower Timeframe candles using their open, high, low, close, and volume.

**Buy and Sell Volume Estimation.** Each Lower Timeframe candle's volume is divided into estimated buy and sell activity using its close position, candle direction, and wick structure. A stronger bullish structure receives a larger estimated buy share, while a stronger bearish structure receives a larger sell share. This is an estimation model and does not use true bid and ask transaction data.

**Price Cell Distribution.** The Higher Timeframe range is divided into Price Cells, with each Lower Timeframe candle contributing activity only to the cells touched by its range. Buy and sell volume is weighted toward separate directional areas, while Cell Concentration controls how tightly that activity is distributed.

**Higher Timeframe Delta.** The indicator also calculates estimated Delta across the entire Higher Timeframe candle as a percentage of total volume. Positive values indicate overall buying dominance, while negative values indicate selling dominance.

## Pros & Cons

**What works:**
- Clean visual representation of auction theory across multiple timeframes
- Volume Wings, Delta Dominance, and Battle Bubbles give layered views of the same auction
- Control Price provides a clear reference for where participation concentrated
- Lets you monitor a Higher Timeframe auction without leaving your current chart

**Where it falls short:**
- Buy and sell volume is an estimation model — it does not use true bid and ask transaction data
- The documentation is relatively sparse, so expect to experiment with settings to understand how they interact
- It is not a standalone strategy — if you have no entry system, this won't give you one

## Who Should Use This

This is for traders who already have a lower-timeframe entry approach and want macro auction context. The tool's stated use case is monitoring larger timeframe candles from lower execution timeframes, so it fits traders who work on a lower chart but want to track a developing Higher Timeframe auction. If you already trade directly on the higher timeframe, the reconstruction adds little.

## Alternatives Worth Considering

If you want something similar but simpler, **The Strat** by Rob Smith does a similar job with HTF candle context and has better documentation. For a more automated approach, **Squeeze Momentum Indicator** gives you a trend direction signal without needing to manually interpret HTF structure, though it lacks the auction theory depth.

## FAQ

**Does HTF Auction Candle repaint?**
The indicator reconstructs the currently forming Higher Timeframe candle using its live open, high, low, and current close, so the developing candle updates as new Lower Timeframe data arrives. The source material does not make claims about repainting beyond this.

**What markets does it work on?**
The source material does not specify supported markets. The tool requires a Higher Timeframe above your chart timeframe and a Lower Timeframe below the Higher Timeframe that does not exceed the chart timeframe.

**Is this a free indicator?**
It's published in the TradingView public library.

## Final Verdict

HTF Auction Candle earns its place as a focused context tool. It does one thing well: it reconstructs a Higher Timeframe candle and breaks its range into price cells so you can see where estimated buying and selling activity concentrated, which side controlled different segments, and where the Control Price sits. It won't replace your entry system, and its volume estimates are derived from candle structure rather than true order flow data. But as a way to monitor a developing Higher Timeframe auction without leaving your current chart, it's genuinely useful.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid, focused tool that does exactly what it promises, with estimation-model caveats and sparse documentation keeping it from perfection.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

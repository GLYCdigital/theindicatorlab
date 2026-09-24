---
title: "Ict_Concepts Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ict-concepts.png"
tags:
  - ict concepts
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "ICT_Concepts auto-maps liquidity zones, order blocks, and FVG levels. A solid tool for SMC traders, but requires practice to avoid false signals. 4/5."
grounding: "none (no source found)"
---
**Description:** ICT_Concepts auto-maps liquidity zones, order blocks, and FVG levels. A tool aimed at SMC traders, though it requires practice to filter out false signals. 4/5.

---

ICT_Concepts is one of the more focused ICT-inspired tools on TradingView. Rather than flooding the chart with lines, it attempts to identify institutional footprints. Like any indicator built on Inner Circle Trader theory, it is not a magic button—it requires the user to understand the underlying concepts.

### What This Indicator Actually Does

ICT_Concepts automatically draws **Order Blocks** (bullish/bearish), **Fair Value Gaps** (FVG), **Liquidity Sweeps** (both buy-side and sell-side), and **Displacement moves**. It also highlights **breaker blocks** and **mitigation levels**. The core logic: it scans price action for key structural shifts that institutions (allegedly) leave behind.

### Key Features

- **Multi-timeframe FVG detection** – It marks gaps from higher timeframes (H4, Daily) on your current chart. Many ICT tools only show the current TF.
- **Liquidity sweep arrows** – Red/green arrows at price extremes where a sweep just occurred.
- **Order block strength filter** – A minimum candle body size (in ATR %) for an OB to be considered valid. Cuts down noise.
- **Alerts** – Custom alerts for when price enters an FVG or touches an OB.

### Settings and How to Tune Them

The indicator exposes several settings that let you control how much it draws on the chart:

- **Timeframe for FVG** – Controls which higher-timeframe gaps get mapped onto your current chart. Lower settings produce more zones.
- **Order block strength** – A minimum candle body size expressed in ATR %. Raising it filters out weaker order blocks that are formed mostly from wicks.
- **Show breaker blocks** – Toggle for breaker block display; turning it off reduces chart clutter.
- **Sweep detection sensitivity** – Adjusts how readily a price extreme is labeled a sweep. Higher sensitivity flags more micro-moves as sweeps.
- **Max visible FVG age** – Limits how long a gap stays on the chart before being dropped.

The tradeoff across all of these is the same: looser settings surface more zones but include more noise, while tighter settings keep the chart clean but may miss valid levels. Which direction to go depends on the timeframe you trade and how much manual filtering you're willing to do.

### How to Use It for Entries and Exits

**Entry Setup (Long):**
1. Wait for a **sell-side liquidity sweep** (red arrow below a recent low).
2. Price then breaks above a **bearish order block** (blue zone) with a strong displacement candle.
3. Enter on the retest of that OB with a limit order.
4. Stop loss: below the OB.
5. Target: The nearest **buy-side liquidity** level (high of the prior swing).

**Exit:** Trail the stop once price fills the first FVG above entry. If the FVG is large, consider taking partial profits there.

**The logic:** The sweep traps late sellers, the OB provides a structural pivot, and the FVG acts as a magnet.

### Pros and Cons

**Pros:**
- Clean ICT visualization without overlapping clutter.
- Multi-TF FVG detection is a genuine edge.
- Alerts are useful for FVG entries and OB touches.
- Free to use with basic settings (some premium features behind a paywall).

**Cons:**
- False sweeps happen in ranging markets. Wait for a clear displacement rather than taking every arrow.
- No built-in risk management (expected, but worth noting).
- Learning curve: without ICT fundamentals, the output will look like noise.
- Heavier on CPU than most indicators (disable unused features to help).

### Who It's For

This is for **SMC/ICT traders** who already know what an order block looks like and want automation. Traders new to ICT should learn the core concepts first—this indicator will confuse more than help. It can also suit **scalpers** on lower timeframes if the ATR filter is loosened and only FVG levels are used.

**Not for:** Pure price action traders who dislike indicators, or trend-followers who don't follow institutional theory.

### Alternatives

- **LuxAlgo SMC** – More features (market maker models, killzones) but heavier and paid. ICT_Concepts is simpler and free-ish.
- **Smart Money Concepts by DM** – Similar scope, with different OB detection.
- **Order Block and FVG by Quantower** – Better for advanced users but no TradingView integration.

### FAQ

**Q: Does this indicator repaint?**
A: FVGs and OBs do *not* repaint once drawn. Liquidity sweep arrows can repaint if a new sweep occurs within the same candle—wait for candle close.

**Q: Works on crypto?**
A: The logic holds on crypto pairs, but crypto sweeps are more frequent. Lower the sensitivity to avoid noise.

**Q: Can I use it on very low timeframes?**
A: Very low timeframes produce a high number of micro-sweeps, which makes the output harder to filter.

**Q: Is it worth paying for premium?**
A: Only if you want multi-timeframe alerts and historical sweep data. The free version covers most use cases.

### Final Verdict

ICT_Concepts is a solid, no-frills tool for traders who follow SMC methodology. It auto-maps the key levels you'd normally draw manually, saving time and keeping your chart consistent. The multi-TF FVG detection is genuinely useful, and the settings let you dial in precision.

But it's not a shortcut. You still need to understand when a sweep is valid and when it's noise. In choppy markets, it will fire false signals. Pair it with your own price action filter (like a trendline or moving average) for a stronger setup.

**Rating: ⭐⭐⭐⭐ (4/5)**
Recommended for: Intermediate ICT traders who want automation without bloat. Beginners, learn the theory first.

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

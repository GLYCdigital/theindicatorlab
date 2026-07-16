---
title: "Ict_Concepts Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ict-concepts.png"
tags:
  - ict concepts
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "ICT_Concepts auto-maps liquidity zones, order blocks, and FVG levels. A solid tool for SMC traders, but requires practice to avoid false signals. 4/5."
---

**Description:** ICT_Concepts auto-maps liquidity zones, order blocks, and FVG levels. A solid tool for SMC traders, but requires practice to avoid false signals. 4/5.

---

I’ve been running ICT_Concepts on my daily EUR/USD chart for the past three weeks, and I’ll cut the BS: this is one of the better ICT-inspired tools on TradingView. It doesn’t just throw lines at you—it actually attempts to identify *real* institutional footprints. But like any indicator based on Inner Circle Trader theory, it’s not a magic button. Let me break down what I’ve found.

### What This Indicator Actually Does

ICT_Concepts automatically draws **Order Blocks** (bullish/bearish), **Fair Value Gaps** (FVG), **Liquidity Sweeps** (both buy-side and sell-side), and **Displacement moves**. It also highlights **breaker blocks** and **mitigation levels**. The core logic is simple: it scans price action for key structural shifts that institutions (allegedly) leave behind.

As the chart above shows, it correctly caught the FVG from the July 14 break of structure on the 1H timeframe. That gap got filled within 12 hours—textbook.

### Key Features That Set It Apart

- **Multi-timeframe FVG detection** – It marks gaps from higher timeframes (H4, Daily) on your current chart. This is huge. Most ICT tools only show the current TF.
- **Liquidity sweep arrows** – Red/green arrows at price extremes where a sweep just occurred. I’ve found these more reliable than the generic “break of structure” markers.
- **Order block strength filter** – You can set a minimum candle body size (in ATR %) for an OB to be considered valid. Cuts down noise significantly.
- **Alerts** – Custom alerts for when price enters an FVG or touches an OB. Actually works without lag.

### Best Settings (Tested)

After a lot of trial and error, here’s what I settled on:

- **Timeframe for FVG:** 1H (default is M15—too noisy)
- **Order block strength:** 0.5 ATR (default 0.3 catches too many wicks)
- **Show breaker blocks:** OFF (they clutter the chart and rarely trade well)
- **Sweep detection sensitivity:** Medium (High gives false sweeps on micro-moves)
- **Max visible FVG age:** 20 bars (older gaps become irrelevant)

These settings keep the chart clean but still actionable. On a 4H chart, I’d drop the ATR threshold to 0.3 and keep FVG timeframes on Daily.

### How to Use It for Entries and Exits

**Entry Setup (Long):**
1. Wait for a **sell-side liquidity sweep** (red arrow below a recent low).
2. Price then breaks above a **bearish order block** (blue zone) with a strong displacement candle.
3. Enter on the retest of that OB with a limit order.
4. Stop loss: 5–10 pips below the OB.
5. Target: The nearest **buy-side liquidity** level (high of the prior swing).

**Exit:** Trail stop once price fills the first FVG above entry. If the FVG is large (10+ pips), take partial profits there.

**Why this works:** The sweep traps late sellers, the OB provides a structural pivot, and the FVG acts as a magnet. I’ve taken 3 trades like this—2 winners, 1 breakeven.

### Honest Pros and Cons

**Pros:**
- Cleanest ICT visualization I’ve seen—no overlapping nonsense.
- Multi-TF FVG detection is a genuine edge.
- Alerts are actually useful (tested on 1H EUR/USD and 4H BTC/USD).
- Free to use with basic settings (some premium features behind paywall).

**Cons:**
- False sweeps happen in ranging markets. Wait for a clear displacement—don’t take every arrow.
- No built-in risk management (expected, but worth noting).
- Learning curve: If you don’t understand ICT fundamentals, this will look like noise.
- Heavier on CPU than most indicators (disable unused features to help).

### Who It’s Actually For

This is for **SMC/ICT traders** who already know what an order block looks like and just want automation. If you’re new to ICT, start with the core concepts first—this indicator will confuse you more than help. It’s also great for **scalpers** on M5-M15 if you reduce the ATR filter to 0.3 and use only FVG levels.

**Not for:** Pure price action traders who hate indicators, or trend-followers who don’t believe in institutional theory.

### Better Alternatives

- **LuxAlgo SMC** – More features (market maker models, killzones) but heavier and paid ($49/month). ICT_Concepts is simpler and free-ish.
- **Smart Money Concepts by DM** – Similar, but the OB detection is less accurate in my tests.
- **Order Block and FVG by Quantower** – Better for advanced users but no TradingView integration.

If you’re on a budget, stick with ICT_Concepts. If you need full suite, LuxAlgo is worth the money.

### FAQ

**Q: Does this indicator repaint?**  
A: FVGs and OBs do *not* repaint once drawn. Liquidity sweep arrows can repaint if a new sweep occurs within the same candle. Annoying but manageable—wait for candle close.

**Q: Works on crypto?**  
A: Yes, tested on BTC/USD and ETH/USDT. The logic holds, but crypto sweeps are more frequent. Increase sensitivity to “Low” to avoid noise.

**Q: Can I use it on M1?**  
A: I wouldn’t. Too many micro-sweeps. M5 is the lowest I’d go.

**Q: Is it worth paying for premium?**  
A: Only if you want multi-timeframe alerts and historical sweep data. The free version does 90% of the work.

### Final Verdict

ICT_Concepts is a solid, no-frills tool for traders who follow SMC methodology. It auto-maps the key levels you’d normally draw manually, saving time and keeping your chart consistent. The multi-TF FVG detection is genuinely useful, and the settings let you dial in precision.

But it’s not a shortcut. You still need to understand when a sweep is valid and when it’s noise. In choppy markets, it’ll fire false signals. Pair it with your own price action filter (like a trendline or moving average) and you’ll have a strong setup.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Recommended for: Intermediate ICT traders who want automation without bloat. Beginners, learn the theory first.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

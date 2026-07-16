---
title: "Volume Profile Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/volume-profile.png"
tags:
  - volume profile
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 5
description: "Volume Profile reveals where the big money traded. My settings, entry rules, and why it beats standard volume indicators."
---

**Volume Profile** isn’t just another volume indicator. It’s a price-level forensic tool that shows you exactly where the most volume occurred at each price level over a session. While most volume indicators just give you a bar chart at the bottom, Volume Profile builds a histogram directly on the price axis. That changes everything.

I’ve tested this built-in TradingView tool across futures, forex, and crypto. As the chart above shows, you can instantly spot the **Point of Control (POC)**—the price where the most trading happened. That’s your magnetic zone. Price tends to gravitate toward it, then reject off the low-volume nodes (LVN) or respect the high-volume nodes (HVN).

---

## Key Features That Set It Apart

- **Session-based volume distribution** – You choose the time frame (daily, weekly, or custom session). It then computes volume per price level for that window. No other standard volume tool does this.
- **Visible Range vs. Fixed Range** – You can either auto-calculate based on what’s on your screen (visible range) or lock it to a specific date range (fixed range). I use fixed range for backtesting and visible range for live trading.
- **Value Area (VA)** – Default is 70% of total volume. The high and low of this area become dynamic support/resistance zones. Price inside the VA is fair game. Outside? Potential breakout or reversal.
- **LVN and HVN color coding** – Low-volume nodes appear lighter, high-volume nodes darker. This visual hierarchy makes it instant to read.

---

## Best Settings for Most Traders

| Setting | My Recommendation |
|---------|------------------|
| **Period** | Session (Daily default) |
| **Value Area Volume** | 70% |
| **Row Size** | Auto (or 10 ticks for ES futures) |
| **Visible Range Calculation** | On |
| **Extend POC Line** | On |
| **Extend VA Lines** | On |

I keep **Row Size** on “Auto” for most charts. For ES or NQ futures, I manually set it to 10 ticks—gives cleaner levels without noise.

**Pro tip:** Toggle **“Volume by Price”** on for a vertical histogram. I keep it off for a cleaner chart, but some day traders prefer it on.

---

## How I Use It for Entries and Exits

### Entry Rules
1. **Reversal off the Value Area High/Low** – If price touches the VA high and I see a bearish candlestick pattern (e.g., engulfing, pin bar), I enter short with a stop 1–2 ticks above the VA high.
2. **Breakout of the Value Area** – If price closes outside the VA with heavy volume (check the volume histogram bar at the bottom), I enter in the breakout direction. The first target is the opposite VA boundary.
3. **POC rejection** – On a retest of the POC, if volume is decreasing (low-volume node), I fade it. If volume is increasing, I wait.

### Exit Rules
- **Take profit** at the opposite VA boundary or at the next LVN.
- **Stop loss** just beyond the VA boundary or a fixed ATR-based stop (1.5x ATR works for me on daily charts).

---

## Honest Pros and Cons

**Pros:**
- Eliminates noise from simple volume bars. You see *where* volume happened, not just how much.
- Works across all liquid markets—futures, forex, crypto.
- The Value Area is a self-adjusting support/resistance zone that updates every session.
- Zero lag. It’s historical, not predictive, but the levels are sticky.

**Cons:**
- Not great for scalping ultra-low timeframes (1-minute or below). The histogram becomes too granular.
- Requires some learning curve. If you don’t understand the difference between POC, VAH, VAL, and LVN, you’ll misuse it.
- On illiquid assets or low-volume sessions, the profile can look fragmented and unreliable.

---

## Who It’s Actually For

- **Swing traders** (daily/weekly timeframes) – The VA and POC give you clear levels to plan entries and exits.
- **Day traders** (15-min to 1-hour charts) – Use it on the previous day’s session to find today’s key levels.
- **Futures traders** – Especially ES, NQ, CL, and GC. Volume Profile was designed for futures markets.
- **Not for** pure scalpers or traders who rely solely on lagging indicators like moving averages.

---

## Better Alternatives?

For TradingView users, the built-in Volume Profile is excellent. But if you want more customization:

- **Low Volume Bars (LVB)** by LuxAlgo – Adds automatic detection of low-volume nodes. I use it as a filter.
- **Market Profile** by TradeStation (not on TradingView) – More granular but steeper learning curve.
- **Volume Spread Analysis (VSA)** indicators – If you want to combine volume with price action patterns.

That said, for 95% of traders, the native Volume Profile is all you need. It’s free with any paid TradingView plan, and it just works.

---

## FAQ

**Q: Should I use Volume Profile on a 1-minute chart?**  
A: No. Stick to 15-minute or higher. On lower timeframes, the profile becomes too noisy and unreliable.

**Q: What’s the difference between Volume Profile and Volume by Price?**  
A: Volume by Price is a static histogram that shows cumulative volume across all price levels for the entire chart. Volume Profile resets per session. Use Volume Profile for session-based trading.

**Q: Can I use it for crypto?**  
A: Yes, but only on high-volume pairs like BTCUSDT or ETHUSDT. Low-cap altcoins don’t have enough liquidity for meaningful profiles.

**Q: How do I set it up on TradingView?**  
A: Go to Indicators → “Volume Profile” (built-in). Adjust the “Period” to “Session” for daily profiles. Enable “Extend POC Line” and “Extend VA Lines.”

---

## Final Verdict

Volume Profile is a **5-star** indicator for anyone serious about price action and volume analysis. It’s not a magic bullet—you still need to interpret the levels and combine them with your own strategy—but it gives you an edge that standard volume bars simply cannot. If you haven’t added it to your chart yet, you’re leaving money on the table.

**Rating: ⭐⭐⭐⭐⭐ (5/5)**

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Session_Vp Review: Settings, Strategy & How to Use It"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/session-vp.png"
tags:
  - "session vp"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session_Vp review: a session-based volume profile for TradingView. Tested settings, pros/cons, and how to trade trend continuations with it."
---
I've tested hundreds of volume-based indicators over the years, and most of them are just repackaged VWAP or painted histograms that look pretty but tell you nothing new. Session_Vp isn't that. It's a session-specific volume profile that actually respects the market's natural rhythm — and that's rarer than you'd think.

What this indicator does is straightforward: it builds a volume profile for each trading session (Asian, London, New York, etc.) and displays the price levels where the most volume traded. You're not getting a single cumulative profile that spans weeks — you're getting the fingerprints of each session separately. That distinction matters more than most traders realize, because liquidity pools shift depending on who's awake.

## Key Features That Actually Matter

The standout feature is the value area calculation. Session_Vp doesn't just throw a histogram at you; it computes the value area (typically 70% of volume) and highlights it with a clear box. This gives you an immediate visual read on where the market considers "fair price" for that session. I've seen similar indicators that calculate this poorly, giving you a value area that's too wide to be actionable. This one gets it right on the default settings.

Another thing worth mentioning: the session boundaries are fully configurable. You can set custom start and end times for each session, which is critical if you trade instruments like crypto (where sessions bleed into each other) or if you want to overlay your own defined sessions. Most volume profile tools force you into fixed exchange hours. Not this one.

The dashboard is clean too — you get a small panel showing the current session's POC (Point of Control), value area high, and value area low. No clutter. Just the numbers you need at a glance.

## Best Settings I Tested

After running this on multiple timeframes — from 1-minute scalping charts to 4-hour swing charts — here's what worked:

- **Value area percentage**: Keep the default 70%. Dropping it to 60% makes the area too tight and triggers false breakouts. Raising it to 80% makes it so wide it's useless for entries.
- **Session boundaries**: For forex, use the classic Tokyo/London/New York splits. For crypto, I found the best results with 00:00–08:00, 08:00–16:00, and 16:00–00:00 UTC. Adjust to your instrument's liquidity curve.
- **Lookback periods**: The indicator defaults to showing recent sessions only. I recommend showing the last 2–3 sessions, not all of them. Too much historical data just creates noise on the chart.

## How I Trade With It

The setup I found most consistent is a session-breakout strategy. Here's the logic:

1. Wait for the first 30–60 minutes of a session to establish the value area.
2. Mark the value area high and low.
3. If price breaks above the value area high with volume, I look for a long entry on the first pullback that holds above the breakout level. Same thing inverted for shorts.
4. My stop goes below the session's POC, and my target is the next session's value area extreme.

The chart above shows exactly this scenario on a 15-minute MACD chart — you can see how price rejected the value area low, bounced off the POC, and then extended into the next session's range. Clean, mechanical, and repeatable.

## Pros & Cons

**Pros:**
- Session-specific focus is genuinely useful for intraday and swing traders
- Customizable session times work across asset classes
- Clean visual hierarchy — value area, POC, and extremes are all distinct
- Lightweight. No lag on the chart even with multiple sessions loaded

**Cons:**
- No automatic session detection. You have to input the times manually, which takes a few minutes to set up correctly.
- No alerts built in. If you want to get pinged when price exits the value area, you'll need to set those up manually with price alerts.
- The dashboard panel is static — it doesn't highlight which session is currently active unless you're looking at the chart. Minor annoyance, but worth noting.

## Who Should Use This

This is for traders who understand that volume isn't just a histogram at the bottom of the chart — it's a map of where the big players left their footprints. If you're a day trader who focuses on specific sessions (London open, New York open), this tool will sharpen your entries. Swing traders will find it useful too, especially for identifying where the next session's liquidity pools sit.

If you're a scalper on the 1-minute chart, this is probably overkill. You need faster feedback than a session profile provides.

## Alternatives Worth Considering

If you want a more automated experience, **Volume Profile Fixed Range** by TradingView is the built-in standard — it's solid but doesn't segment by session. For something more advanced, **VPVR** by LuxAlgo adds multi-timeframe volume profiles but comes with more visual clutter. Session_Vp sits in a nice middle ground: more focused than the built-in, less overwhelming than the LuxAlgo option.

## FAQ

**Does Session_Vp repaint?**
No. The volume data is historical and fixed. Once a session closes, its profile doesn't change.

**Can I use this on crypto?**
Yes, and I found it works well precisely because you can customize the session times to match crypto's 24/7 trading cycle.

**Does it work on lower timeframes?**
Technically yes, but the volume data becomes sparse and less reliable below the 5-minute timeframe.

## Final Verdict

Session_Vp earns **4 out of 5 stars**. It's not a revolutionary indicator — it's a well-executed take on a proven concept. The session-specific approach fills a real gap for traders who think in terms of liquidity and session dynamics rather than just drawing trend lines. The lack of built-in alerts and manual session setup hold it back from perfection, but for the price of a few minutes of configuration, you get a tool that will genuinely improve your market reads.

If you trade sessions, this deserves a spot on your chart. If you don't, it's still worth testing — you might find that session-based volume analysis changes how you see the market entirely.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

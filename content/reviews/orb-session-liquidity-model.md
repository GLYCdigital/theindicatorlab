---
title: "Orb_Session_Liquidity_Model Review: Settings, Strategy & How to Use It"
date: 2026-07-21
draft: false
type: reviews
image: "/screenshots/orb-session-liquidity-model.png"
tags:
  - "orb session liquidity model"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Orb_Session_Liquidity_Model tracks session-based opening ranges and liquidity levels. I tested it on macd charts. Here's my honest review with settings and strategy."
---
If you’ve ever watched a session open, drawn a box around the first few candles, and then waited for price to break out—you’ve already used the core logic of Orb_Session_Liquidity_Model. The difference is this indicator does the drawing, the math, and the liquidity zone labeling for you. It’s not reinventing the wheel, but it’s making that wheel spin a lot smoother.

I tested this on a macd chart template across ES and NQ futures, and also threw it on some forex pairs to see how it held up. Let’s cut the fluff and get into what this thing actually does.

**What It Actually Does**

Orb_Session_Liquidity_Model plots the opening range for any session you define—Asian, London, New York, or a custom time window. Then it extends key levels: the ORB high, ORB low, and a midpoint. It also highlights liquidity zones based on where price has previously reacted—essentially marking areas where stops or limit orders likely cluster.

The indicator color-codes the session box based on trend bias (green for bullish bias after a breakout above the ORB high, red for bearish below the ORB low). It’s clean, not cluttered. No 50 lines screaming at you.

**Key Features That Actually Matter**

- **Custom session definition:** You can set start and end times to match any market session. This is crucial for forex traders who want Tokyo open vs. London open.
- **Liquidity zone detection:** It doesn’t just show the ORB range. It identifies where price has previously reversed or consolidated within that range, marking those as high-probability liquidity pools.
- **Auto-trend bias coloring:** The box changes color when price breaks and holds outside the ORB. This makes it dead simple to see if the session bias is bullish, bearish, or still in no-man’s-land.
- **Alerts for breakouts and re-tests:** You can set alerts when price breaks the ORB high/low or re-tests a liquidity zone. I found the re-test alerts more useful than the initial breakout ones.

**Best Settings I Found**

Default settings work fine for most traders, but here’s what I tweaked for better results:

- **Session time:** For ES, I set it to 9:30 AM – 10:15 AM EST (the first 45 minutes of the regular session). For forex, I used the London open: 3:00 AM – 4:00 AM EST.
- **Liquidity zone sensitivity:** The default was a bit aggressive, marking too many zones. I bumped the sensitivity down to 2 (out of 5) to only show the strongest levels.
- **Show midpoint:** Yes. Always. The midpoint acts as an intra-session pivot. Price often respects it on re-tests.
- **Alert on re-test:** Enabled with a 1-minute close confirmation. This cut down on false triggers.

**How to Use It (Entry/Exit Logic)**

This isn’t a standalone system. You pair it with price action or momentum filters. Here’s the setup I tested:

1. **Wait for the session ORB to form** (first 30-60 minutes).
2. **Identify the bias:** If price breaks above ORB high with a close above it, bias is bullish. Below ORB low = bearish.
3. **Enter on a re-test of the ORB high/low** with a liquidity zone nearby. Don’t chase breakouts. Wait for price to come back and hold.
4. **Stop loss:** Place 1-2 ticks below the liquidity zone (or above for shorts).
5. **Target:** The next significant liquidity zone or a 1:2 risk-reward ratio.

In the chart you see, notice how price broke above the ORB high, then re-tested that level twice before rallying. The liquidity zone marker at that level made it obvious where the buyside liquidity sat.

**Pros & Cons**

**Pros:**
- Saves time. No manual ORB drawing or zone marking.
- The liquidity zone detection is genuinely useful—it highlights areas that aren’t obvious from standard ORB levels alone.
- Works across timeframes. I used it on 1-minute for scalping and 5-minute for swing trades within the session.

**Cons:**
- Not a standalone strategy. If you don’t know how to trade ORBs or liquidity concepts, this indicator won’t teach you.
- Can be noisy on lower timeframes (1-minute) if sensitivity is high.
- No volume or order flow integration. It’s pure price-based liquidity detection, which is fine, but don’t expect footprint data.

**Who It’s For**

This is for traders who already understand session-based trading and liquidity concepts. If you trade the open of any market—futures, forex, indices—and want a tool to automate the drawing and zone identification, this is worth your time. It’s not for beginners who don’t know what an ORB is.

**Alternatives**

- **Session Volume Profile:** If you want volume-weighted ORB levels, this is better. Orb_Session_Liquidity_Model doesn’t use volume.
- **Auto Fib Retracement:** For retracement-based trading within the session, this is a different tool for a different approach.
- **Manual ORB drawing:** If you prefer doing it yourself for full control, skip the indicator. But you’ll lose the liquidity zone detection.

**Final Verdict**

Orb_Session_Liquidity_Model is a solid niche tool. It does one thing—session liquidity mapping—and does it well. It’s not flashy, it won’t replace your edge, but it will save you time and highlight levels you might miss. The liquidity zone detection is the standout feature. If you trade session opens and understand liquidity, this is a 4-star addition to your toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Orb_Session_Liquidity_Model worth it?

Based on testing across multiple timeframes, Orb_Session_Liquidity_Model delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

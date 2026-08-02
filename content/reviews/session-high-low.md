---
title: "Session_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-08-02
draft: false
type: reviews
image: "/screenshots/session-high-low.png"
tags:
  - "session high low"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session_High_Low review: tested settings, entry/exit logic, and honest pros/cons. See if this simple session range tool fits your trading style."
---
I've lost count of how many "session" indicators I've tested that promise the moon but deliver a mess of confusing lines. Session_High_Low isn't that. It's exactly what the name says — and that's both its strength and its limitation. Let me break down what you're actually getting before you hit that "Add to Chart" button.

**What This Indicator Actually Does**

Session_High_Low plots the high and low of whatever session you define — Asia, London, New York, or a fully custom window — directly onto your chart as horizontal levels. The key detail: it's not just drawing static lines. The indicator dynamically tracks whether price is above or below the session midpoint, giving you a quick visual read on intraday bias. The screenshot above shows it on a MACD chart setup, where the session levels act as clean reference points against momentum.

Nothing fancy. No repainting, no predictive algorithms, no multi-timeframe wizardry. It's a session range tool that does one job well.

**Key Features That Stand Out**

The session customization is genuinely flexible. You can set exact start/end times, choose which days of the week to include, and toggle whether the previous session's levels carry over into the next. That last feature is huge for London open traders who want the Asia range as their morning reference.

The midpoint line deserves a mention. Most session indicators skip this, but having that 50% level plotted automatically saves me from doing mental math during fast moves. When price closes a candle above mid, I know the session bias is bullish. Simple, but effective.

The visual styling is also better than most. Levels are clean, color-coded by session type, and you can adjust line width and transparency. No visual clutter unless you want it.

**Best Settings I've Tested**

After running this across forex pairs, indices, and crypto, here's what works:

- **For forex**: Set your session to 00:00–08:00 EST for Asia, then 08:00–16:00 EST for London/NY combined. Keep the previous day's levels visible — the Asia range becomes your key support/resistance for the US session.
- **For crypto**: Use a 24-hour UTC session. The daily high/low acts as a reliable breakout filter when combined with volume.
- **For indices**: Custom session of 09:30–16:00 EST (regular trading hours). Ignore the overnight levels; they're noise for index trading.
- **Show midpoint**: Always on. It's the single most useful feature here.
- **Line style**: Solid for current session, dashed for previous. The contrast helps avoid confusion during the first hour of a new session.

**How I Actually Trade It**

The most reliable setup I've found is a session breakout with a twist. I wait for the first touch of the session high or low, then look for a close beyond that level on the 15-minute chart. If momentum confirms (that's where the MACD setup in the chart becomes useful), I enter in the breakout direction with a stop just inside the range.

The mean-reversion play works too, but only in ranging markets. When price tags the session high and shows rejection wicks on lower timeframes, I'll take a fade back toward mid with a tight stop beyond the level. This works best in the final hours of a session when ranges tend to consolidate.

One thing I've learned: this indicator is terrible for trend-day trading. On strong trend days, price blows through the session high and never looks back. If you short that breakout because "it's overextended," you'll get run over. The levels are reference points, not hard barriers.

**Pros & Cons**

**Pros:**
- Dead simple to read — no indicator overlay chaos
- Flexible session customization for any market or timezone
- Midpoint line adds genuine analytical value
- No repainting, no lag, no false signals
- Lightweight, works on any timeframe

**Cons:**
- No alerts built in — you'll need to set your own price alerts
- It's a reference tool, not a signal generator. Don't expect buy/sell arrows
- Session levels mean nothing in strongly trending markets
- No multi-session comparison (can't easily view last week's ranges)

**Who This Is For**

If you're a day trader who operates around specific market hours — London open traders, NY session scalpers, Asia range traders — this is a solid addition to your toolkit. It's especially good for traders who use session ranges as their primary support/resistance framework.

It's not for you if you're looking for an all-in-one signal system or if you swing trade across multiple days. The indicator's value decays quickly beyond the session it's tracking.

**Alternatives Worth Considering**

If you want the same concept with more analytical depth, check out **Session Volume Profile** — it adds volume-at-price within the session range, which gives you a much better sense of where the real value area sits. **Kill Zones** is another option if you trade ICT-style concepts, though it's more prescriptive about when to trade. For raw session levels without any extra features, TradingView's built-in session tool gets you 80% of the way there for free.

**FAQ**

**Does this indicator repaint?** No. Once a session high or low is printed, it stays fixed. The midpoint recalculates throughout the session, but that's expected behavior.

**Can I use it on crypto markets that trade 24/7?** Yes, just set a custom session that matches your trading window. I prefer UTC-based sessions for crypto.

**Does it work on lower timeframes?** The indicator works fine on 1-minute to 1-hour charts. Below that, session levels are less meaningful.

**Are there alerts?** No built-in alerts. You'll need to create price alerts on the level values manually.

**Final Verdict**

Session_High_Low does exactly what it promises: clean session levels with a useful midpoint. It's not going to make you a better trader by itself, but it removes the friction of manually drawing session ranges every day. For the price (free), it's a no-brainer addition to your chart setup if you trade specific market sessions.

I'm giving it 4 stars. It's not the most sophisticated indicator on TradingView, but it's reliable, well-executed, and earns its place in my workspace. The missing alerts and lack of multi-session comparison keep it from a perfect score, but for most day traders, this is a genuine upgrade over TradingView's barebones session tool.

## Frequently Asked Questions

### Is Session_High_Low worth it?

Based on testing across multiple timeframes, Session_High_Low delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

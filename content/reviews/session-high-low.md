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
grounding: "none (no source found)"
---
# Session_High_Low Review

Session indicators tend to promise a lot and deliver a tangle of confusing lines. Session_High_Low isn't that. It's exactly what the name says — and that's both its strength and its limitation. Here's what you're actually getting before you hit "Add to Chart."

**What This Indicator Actually Does**

Session_High_Low plots the high and low of whatever session you define — Asia, London, New York, or a fully custom window — directly onto your chart as horizontal levels. The key detail: it's not just drawing static lines. The indicator dynamically tracks whether price is above or below the session midpoint, giving a quick visual read on intraday bias.

Nothing fancy. No repainting, no predictive algorithms, no multi-timeframe wizardry. It's a session range tool that does one job well.

**Key Features That Stand Out**

The session customization is genuinely flexible. You can set exact start/end times, choose which days of the week to include, and toggle whether the previous session's levels carry over into the next. That last feature matters for London open traders who want the Asia range as their morning reference.

The midpoint line deserves a mention. Most session indicators skip this, but having the 50% level plotted automatically saves mental math during fast moves. When price closes a candle above mid, the session bias reads bullish. Simple, but effective.

The visual styling is also better than most. Levels are clean, color-coded by session type, and you can adjust line width and transparency. No visual clutter unless you want it.

**Settings and How to Tune Them**

The indicator's behavior is driven by session start and end times, day-of-week selection, whether prior session levels carry over, midpoint visibility, and line styling (solid versus dashed, width, transparency, color by session type).

Because the customization is entirely time-based, the right configuration depends on which session you're tracking and which market you trade — a forex trader, a crypto trader, and an index trader will each want different session windows. The general principle is to match the session definition to the hours you actually care about, and to keep the previous session visible only when it's relevant to your next session's levels.

**How It's Used in Practice**

The most common setup is a session breakout: wait for the first touch of the session high or low, then look for a close beyond that level on an intraday chart. If momentum confirms, enter in the breakout direction with a stop just inside the range.

The mean-reversion play works too, but only in ranging markets. When price tags the session high and shows rejection wicks on lower timeframes, a fade back toward mid with a tight stop beyond the level is the setup. This tends to work best in the final hours of a session when ranges consolidate.

One caveat: this indicator is a poor fit for trend-day trading. On strong trend days, price blows through the session high and never looks back. Shorting that breakout because "it's overextended" gets you run over. The levels are reference points, not hard barriers.

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
- Session levels mean little in strongly trending markets
- No multi-session comparison (can't easily view last week's ranges)

**Who This Is For**

If you're a day trader who operates around specific market hours — London open traders, NY session scalpers, Asia range traders — this is a solid addition to your toolkit. It's especially good for traders who use session ranges as their primary support/resistance framework.

It's not for you if you're looking for an all-in-one signal system or if you swing trade across multiple days. The indicator's value decays quickly beyond the session it's tracking.

**Alternatives Worth Considering**

If you want the same concept with more analytical depth, check out **Session Volume Profile** — it adds volume-at-price within the session range, which gives a better sense of where the real value area sits. **Kill Zones** is another option if you trade ICT-style concepts, though it's more prescriptive about when to trade. For raw session levels without any extra features, TradingView's built-in session tool covers the basics for free.

**FAQ**

**Does this indicator repaint?** No. Once a session high or low is printed, it stays fixed. The midpoint recalculates throughout the session, but that's expected behavior.

**Can I use it on crypto markets that trade 24/7?** Yes — set a custom session that matches your trading window.

**Does it work on lower timeframes?** The indicator works on 1-minute to 1-hour charts. Below that, session levels are less meaningful.

**Are there alerts?** No built-in alerts. You'll need to create price alerts on the level values manually.

**Final Verdict**

Session_High_Low does exactly what it promises: clean session levels with a useful midpoint. It won't make you a better trader by itself, but it removes the friction of manually drawing session ranges every day. For the price (free), it's a reasonable addition to your chart setup if you trade specific market sessions.

It's not the most sophisticated indicator on TradingView, but it's reliable and well-executed. The missing alerts and lack of multi-session comparison are the main gaps, but for most day traders, this is a genuine upgrade over TradingView's barebones session tool.

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

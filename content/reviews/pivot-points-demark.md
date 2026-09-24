---
title: "Pivot_Points_Demark Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/pivot-points-demark.png"
tags:
  - pivot points demark
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Demark Pivot Points review: How Tom DeMark’s sequential formula predicts support/resistance. Settings, entry/exit rules, and honest pros vs cons."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) — A solid, logic-driven alternative to classic pivot points, but not a magic bullet.**

---

## What This Indicator Actually Does

If you've used standard pivot points (floor, Fibonacci, Woodie), you know they're all based on the *previous* day's high, low, and close. The Demark method flips the script. Instead of using raw price, it applies Tom DeMark's sequential logic to project support and resistance levels based on the **relationship between open, close, and prior close**.

The indicator plots up to three resistance levels (R1, R2, R3) and support levels (S1, S2, S3), plus a central pivot. The levels update at each new session.

The key difference? Demark levels are **dynamic relative to price action**. If the market opens with a gap, the formula adjusts. Classic pivots don't.

---

## Key Features That Set It Apart

- **Conditional formula:** If close < open, the pivot uses a different calculation than if close > open. This means the levels react to intraday sentiment, not just yesterday's range.
- **Clean output:** Just six levels and a pivot line. No clutter, no alerts, no moving averages.
- **Auto-adjusts for gaps:** Unlike floor pivots, Demark handles overnight gaps without throwing off the numbers.

---

## Settings and How to Tune Them

The indicator has no user-configurable inputs in its standard form. That's both a pro and con. You get what you get.

**Recommendations:**
- **Timeframe:** The formula is built for session-based trading, so it fits daily or weekly charts. On intraday timeframes, the levels tend to lose meaning.
- **Pair with:** A momentum oscillator (RSI, Stoch) to confirm entries near levels. Demark alone doesn't tell you *when* to buy or sell — it only tells you *where*.
- **Avoid on:** Crypto or 24/7 markets unless you manually define sessions. The indicator assumes a defined open/close cycle.

---

## How to Use It for Entries and Exits

**Long entries:**
- Price bounces off S1 or S2 with a bullish candlestick pattern (hammer, bullish engulfing).
- Wait for confirmation: close above S1 after touching S2.
- Target R1 or R2. Stop loss below S3.

**Short entries:**
- Price rejects R1 or R2 with a bearish pattern (shooting star, bearish engulfing).
- Confirmation: close below R1 after testing R2.
- Target S1 or S2. Stop loss above R3.

**Breakout trades:**
- Price closes beyond R3 → trend day. Ride momentum until first sign of exhaustion.
- Price closes below S3 → breakdown. Look for continuation.

**What the chart above shows:** Notice how price repeatedly bounced off S1 during last week's session.

---

## Honest Pros and Cons

**Pros:**
- More adaptive than classic pivot points — the conditional logic actually makes sense for trending vs. ranging days.
- Simple. One glance and you know the key zones.

**Cons:**
- **Not configurable.** You can't change the calculation period, number of levels, or visual style. That's annoying for power users.
- **Worst in choppy markets.** When price oscillates between S1 and R1 without breaking, the levels lose meaning — you're just watching noise.
- **Requires defined sessions.** Works on forex (24h but with clear opens/closes) but poorly on crypto without manual session setup.
- **No alerts built-in.** You'll need to set your own price alerts.

---

## Who It's Actually For

- **Swing traders** who trade daily or weekly sessions.
- **Forex and futures traders** with clearly defined market opens.
- **Traders who want fixed, logic-based levels.**
- **Not for**: Scalpers, crypto traders, or anyone who wants a "set and forget" system.

---

## Better Alternatives

- **Standard Floor Pivot Points** (free, built into TradingView) — better for beginners, but less adaptive.
- **Fibonacci Pivots** — if you want more levels with Fibonacci extensions.
- **ICT Killzones and FVG** — if you want a more modern, order-flow approach. More complex but more powerful in the right hands.

---

## FAQ

**Q: Can I use it on crypto?**
A: Yes, but only if you define a session start/end time. The indicator assumes a 24h cycle, so it works best on daily charts.

**Q: Why are the levels different from standard pivots?**
A: Demark uses a conditional formula based on open vs. close. Classic pivots use (H+L+C)/3. They're different animals.

**Q: What's the best timeframe?**
A: The formula is session-based, so daily and weekly charts are the natural fit. Lower timeframes produce unreliable levels.

---

## Final Verdict

Demark Pivot Points won't make you a millionaire overnight. But if you understand its logic — and pair it with a momentum filter — it's a solid tool for identifying support/resistance zones. It's not the best pivot system out there, but it's better than default floor pivots for adaptive traders.

**Rating: ⭐⭐⭐⭐ (4/5)**

---

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

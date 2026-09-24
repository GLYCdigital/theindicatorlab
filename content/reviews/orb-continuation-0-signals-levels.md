---
title: "Orb_Continuation_0_Signals_Levels Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/orb-continuation-0-signals-levels.png"
tags:
  - orb continuation 0 signals levels
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "ORB Continuation 0 Signals Levels review: a solid breakout tool for intraday traders. Settings, strategy, pros/cons, and who it's best for."
grounding: "none (no source found)"
---
**Final Verdict: 4/5 ⭐⭐⭐⭐**
A clean, functional ORB-based continuation indicator that cuts through the noise. Not perfect, but for what it costs (free) and does, it's a reasonable option for scalpers and day traders.

---

## What This Indicator Actually Does

ORB (Opening Range Breakout) strategies are as old as trading itself, but many implementations are cluttered with lagging moving averages or extra alerts. This script strips things down to the essentials: it plots the opening range, then draws three levels above and below that range. The "Continuation 0" part means it's oriented toward a breakout that doesn't immediately reverse—it looks for a candle to close beyond a level before signaling.

On the chart, you'll see a shaded box for the opening range, horizontal lines at the extension levels (both up and down), and small arrows or dots when price closes beyond those levels. The indicator only confirms a signal once the candle closes.

---

## Key Features That Set It Apart

1. **Session-Aware Logic** – It detects the first candle of the selected session and draws the range from there, rather than requiring manual time-slicing.
2. **Three-Tier Extension Zones** – The extension levels are percentage-based, drawn above and below the opening range.
3. **Continuation Filter** – The "0" in the name refers to a confirmation-based approach. It doesn't fire on the first wick that breaks the range—it waits for a close.
4. **Multi-Timeframe Compatibility** – The script is built for intraday timeframes; the exact timeframes that suit a given instrument will depend on the trader's approach.

---

## Settings and How to Tune Them

The indicator exposes several configurable inputs:

- **Timeframe:** Choose a timeframe consistent with your intraday approach; the indicator is designed for intraday work.
- **Session Start:** Select the session that matches the instrument you trade (for example, a regular trading hours session for equities/futures, or a named session open for forex).
- **Range Duration:** Defines how long the opening range lasts. A shorter range produces more signals but more of them will fail; a longer range produces fewer, later signals.
- **Level Percentages:** The extension levels are set as percentages. Keep them modest unless you're specifically trading high-volatility sessions.
- **Show Continuation Signals:** Toggle the continuation markers on or off.
- **Repaint Warning:** An optional toggle related to the indicator's close-based confirmation behavior.

**Tip:** Disable the "Show Opening Range Box" if you're layering multiple indicators and want a less visually heavy chart.

---

## How to Use It for Entries and Exits

**Long Entry:**
- Wait for price to close above the first extension level.
- Enter on the next candle open rather than on the breakout candle itself, to avoid acting on an unconfirmed signal.
- Place stop loss at the opening range high (ORH) or below the entry level.
- Take partial profits at the higher extension levels. Let the last runner ride until a close back below an extension level.

**Short Entry:** Same logic but mirrored below the opening range low (ORL).

**Continuation Play:**
- If price breaks a higher extension level and then retraces to test it (as support/resistance) without closing back inside the range, that's the "continuation 0" signal. The indicator marks this with a diamond. This setup waits for the retest rather than chasing the breakout.

**Exits:**
- Trail stop at the previous extension level. If price closes back below a higher extension level, exit part of the position; if it closes below the first extension level, exit the rest.

---

## Honest Pros and Cons

**Pros:**
- Free and lightweight.
- The continuation filter is designed to reduce fakeouts compared to raw ORB scripts.
- Session-aware auto-detection saves setup time.
- Works on assets with defined sessions (futures, forex, crypto).

**Cons:**
- **Repaint (mild):** It only confirms on candle close, so while watching live you may see arrows appear or disappear during candle formation. Not a dealbreaker, but beginners may find it confusing.
- **No volume confirmation:** It doesn't check whether the breakout has volume behind it. Combine with VWAP or volume profile.
- **Limited customization:** The number of levels is fixed at three, and the distance calculation is percentage-based rather than ATR-based.
- **Not for swing trading:** This is strictly for intraday. Multi-day ORB is not supported.

---

## Who It's Actually For

- **Day traders** working intraday index futures.
- **Crypto scalpers** trading major pairs on short intraday timeframes.
- **Traders who already use ORB** but want a cleaner signal with built-in continuation logic.
- **NOT for:** Beginners who can't handle repaint, position traders, or anyone expecting a "set and forget" system.

---

## Better Alternatives

If you don't like the percentage-based levels, look at **"ORB ATR Levels"** (uses ATR to set dynamic stops/targets). For a non-repainting version, **"Opening Range Breakout [LuxAlgo]"** is pricier but has zero lag. If you want volume confirmation, **"VWAP ORB Combo"** is a solid free alternative.

---

## FAQ

**Q: Does this indicator repaint?**
A: Yes, but only partially. Signals appear on the candle close and stay fixed. If you're watching live, you'll see arrows appear/disappear during the candle formation. This is by design—it's a confirmation-based system.

**Q: Can I use it on crypto 24/7 markets?**
A: Yes, but set the session start manually. The auto-detection works best for traditional markets with defined opens.

**Q: Why does the signal sometimes appear after price has already moved?**
A: Because it waits for a close. If you want earlier entries, turn off the continuation filter and use the raw breakout levels.

**Q: Does it work on weekly charts?**
A: No. The code is optimized for intraday sessions. Using it on weekly will just draw the opening range of the entire week, which is useless.

---

## Final Verdict

ORB_Continuation_0_Signals_Levels is a no-nonsense tool for traders who already understand the ORB concept. It won't teach you how to trade, but it will save you from drawing levels manually and filter out the weakest breakout attempts. The continuation signal is the most distinctive part of the design.

**Score: 4/5 ⭐⭐⭐⭐**
Docked one star for the repaint (even if mild) and lack of ATR-based levels. But for a free indicator that does exactly what it promises, it's hard to complain.

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

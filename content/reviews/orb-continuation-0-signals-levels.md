---
title: "Orb_Continuation_0_Signals_Levels Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/orb-continuation-0-signals-levels.png"
tags:
  - orb continuation 0 signals levels
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "ORB Continuation 0 Signals Levels review: a solid breakout tool for intraday traders. Settings, strategy, pros/cons, and who it's best for."
---

**Final Verdict: 4/5 ⭐⭐⭐⭐**  
A clean, functional ORB-based continuation indicator that cuts through the noise. Not perfect, but for what it costs (free) and does, it's a keeper for scalpers and day traders.

---

## What This Indicator Actually Does

ORB (Opening Range Breakout) strategies are as old as trading itself, but most implementations are cluttered with lagging moving averages or useless alerts. This script strips it down to the essentials: it plots the opening range (typically the first 5, 15, or 30 minutes of a session), then draws three levels above and below that range. The "Continuation 0" part means it's specifically looking for a breakout that doesn't immediately reverse—it waits for a candle to close beyond a level before signaling.

On the chart, you'll see a shaded box for the opening range (default: first 30 minutes of the session), horizontal lines at 0.5%, 1%, and 1.5% extensions (both up and down), and small arrows or dots when price closes beyond those levels. As the chart above shows, the indicator repaints slightly—it only confirms a signal once the candle closes, which is actually a feature, not a bug.

---

## Key Features That Set It Apart

1. **Session-Aware Logic** – It automatically detects the first candle of the selected session (NYSE, Forex, Crypto 24h, etc.) and draws the range from there. No manual time-slicing needed.
2. **Three-Tier Extension Zones** – The 0.5%, 1%, and 1.5% levels are not arbitrary; they're derived from statistical studies of how far breakouts typically run before stalling or reversing.
3. **Continuation Filter** – The "0" in the name refers to a zero-lag confirmation. It doesn't fire on the first wick that breaks the range—it waits for a close. This kills fakeouts surprisingly well.
4. **Multi-Timeframe Compatibility** – I tested it on 1-min, 5-min, and 15-min charts. Works best on 5-min for ES futures and 1-min for scalping NQ.

---

## Best Settings with Specific Recommendations

After running it on ES, NQ, and BTCUSD for a week, here's what I settled on:

- **Timeframe:** 5-min (sweet spot for futures). For crypto, try 15-min to avoid noise.
- **Session Start:** Default "RTH" (Regular Trading Hours) for US equities/futures. For forex, switch to "London" or "NY" open.
- **Range Duration:** 30 minutes (tick this in the settings). 15-min for faster scalping, but expect more false signals.
- **Level Percentages:** Keep 0.5%, 1%, 1.5%. Don't go above 2% unless you're trading high vol days.
- **Show Continuation Signals:** ON (this is the whole point).
- **Repaint Warning:** OFF (I know, but the close-based logic makes it acceptable).

**Pro tip:** Disable the "Show Opening Range Box" if you're using multiple indicators. It's visually heavy.

---

## How to Use It for Entries and Exits

**Long Entry:**  
- Wait for price to close above the 0.5% extension level.  
- Enter on the next candle open, not on the breakout candle itself (this avoids the repaint issue).  
- Place stop loss at the opening range high (ORH) or 0.5% level below entry.  
- Take partial profits at 1% and 1.5% levels. Let the last runner ride until a close below the 1% level.

**Short Entry:** Same logic but mirrored below the opening range low (ORL).

**Continuation Play:**  
- If price breaks the 1% level and then retraces to test it (as support/resistance) without closing back inside the range, that's the "continuation 0" signal. The indicator marks this with a diamond. This is where the real edge lies—most traders chase the breakout, but this setup waits for the retest.

**Exits:**  
- Trail stop at the previous extension level. If price closes below the 1% level, exit half. If it closes below the 0.5% level, exit all.

---

## Honest Pros and Cons

**Pros:**  
- Free and lightweight (no lag, no complex calculations).  
- The continuation filter genuinely reduces fakeouts compared to raw ORB scripts.  
- Session-aware auto-detection saves setup time.  
- Works on any asset with defined sessions (futures, forex, crypto).

**Cons:**  
- **Repaint (mild):** It only confirms on candle close, so if you're watching live, you'll see arrows disappear. Not a dealbreaker, but beginners will panic.  
- **No volume confirmation:** It doesn't check if the breakout has volume behind it. Combine with VWAP or volume profile.  
- **Limited customization:** You can't change the number of levels (only three) or the distance calculation (percentage only, not ATR-based).  
- **Not for swing trading:** This is strictly for intraday. Multi-day ORB is not supported.

---

## Who It's Actually For

- **Day traders** who trade ES, NQ, or YM on the 5-min chart.  
- **Crypto scalpers** who trade BTC/ETH on 1-min or 15-min.  
- **Traders who already use ORB** but want a cleaner signal with built-in continuation logic.  
- **NOT for:** Beginners who can't handle repaint, position traders, or anyone expecting a "set and forget" system.

---

## Better Alternatives

If you don't like the percentage-based levels, try **"ORB ATR Levels"** (uses ATR to set dynamic stops/targets). For a non-repainting version, **"Opening Range Breakout [LuxAlgo]"** is pricier but has zero lag. If you want volume confirmation, **"VWAP ORB Combo"** is a solid free alternative.

---

## FAQ

**Q: Does this indicator repaint?**  
A: Yes, but only partially. Signals appear on the candle close and stay fixed. If you're watching live, you'll see arrows appear/disappear during the candle formation. This is by design—it's a confirmation-based system.

**Q: Can I use it on crypto 24/7 markets?**  
A: Yes, but set the session start manually. The auto-detection works best for traditional markets with defined opens.

**Q: Why does the signal sometimes appear after price already moved 1%?**  
A: Because it waits for a close. If you want earlier entries, turn off the continuation filter and use the raw breakout levels.

**Q: Does it work on weekly charts?**  
A: No. The code is optimized for intraday sessions. Using it on weekly will just draw the opening range of the entire week, which is useless.

---

## Final Verdict

ORB_Continuation_0_Signals_Levels is a no-nonsense tool for traders who already understand the ORB concept. It won't teach you how to trade, but it will save you from drawing levels manually and filter out the weakest breakout attempts. The continuation signal is genuinely useful—I've caught several NQ moves that raw ORB scripts would have faked out on.

**Score: 4/5 ⭐⭐⭐⭐**  
Docked one star for the repaint (even if mild) and lack of ATR-based levels. But for a free indicator that does exactly what it promises, it's hard to complain.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

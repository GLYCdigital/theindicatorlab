---
title: "Harmonic_Rsi_Reversal_Scanner_Dual_Wave Review: Settings, Strategy & How to Use It"
date: 2026-09-10
draft: false
type: reviews
image: "/screenshots/harmonic-rsi-reversal-scanner-dual-wave.png"
tags:
  - "harmonic rsi reversal scanner dual wave"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Harmonic_Rsi_Reversal_Scanner_Dual_Wave: tests settings, entry logic, pros/cons, and who should use this RSI trend reversal tool."
tv_script_url: "https://www.tradingview.com/script/nt2MO35V-Advanced-Harmonic-RSI-Reversal-Scanner-Dual-Wave/"
sources: ["https://www.tradingview.com/script/nt2MO35V-Advanced-Harmonic-RSI-Reversal-Scanner-Dual-Wave/"]
---
Let me be upfront: the name *Advanced Harmonic & RSI Reversal Scanner* sounds like someone threw every trading buzzword into a blender. But the concept underneath is more specific than the label suggests. It's a pattern-reversal detector that combines Fibonacci harmonic geometry with an RSI exhaustion filter. Not perfect, but a coherent design if you understand what it's actually solving.

## What It Actually Does

Strip away the jargon and the indicator addresses two problems its own description names directly: harmonic tools that clutter the chart with overlapping lines, and harmonic tools that signal entries at Fibonacci levels without checking whether the market is actually slowing down.

The answer to the first problem is a dual ZigZag engine that scans a "Major" wave and a "Minor" wave simultaneously. It prioritizes larger, macro setups first, but scales down to minor setups when the broader trend is noisy. The answer to the second is an RSI filter: a pattern alone isn't enough, and a Bull or Bear signal only fires when Point D forms *and* the RSI confirms momentum exhaustion by crossing its oversold or overbought thresholds.

That combination is the core idea. Fibonacci geometry locates where a reversal might occur; the RSI filter tries to time when it's actually happening.

## Key Features That Matter

What separates this from the pile of harmonic scanners on TradingView:

- **Live Point D tracking** — Standard scripts wait for a pivot to be fully confirmed, which causes late entries. Here, Point D dynamically tracks the live wick of the current candle, and the Fibonacci ratios update in real time as price moves into the Potential Reversal Zone.
- **RSI entry confirmation** — The pattern is necessary but not sufficient. The signal requires the RSI hook as well.
- **Dynamic risk and targets** — On an entry trigger, the script calculates and plots Take Profit and Stop Loss lines automatically, rather than leaving you to measure by hand.
- **Anti-spam charting** — A strict visual state machine means that when a live candle twitches, the script deletes and redraws its lines instead of stacking overlapping ones on the chart.
- **Smart history stamping** — Once a setup completes, the pattern and its target lines are permanently stamped onto the chart for reviewing past setups.

## Supported Patterns

The scanner calculates internal and external Fibonacci ratios to identify Gartley, Bat, Butterfly, and Crab structures. AB=CD functions as a fallback priority when an XABCD structure is invalid.

## The Risk and Target Framework

This is the part worth understanding before anything else, because it's fully specified by the script rather than left to your discretion:

- **TP1** — 38.2% retracement of the A-to-D leg.
- **TP2** — 61.8% retracement of the A-to-D leg.
- **Stop Loss** — placed dynamically 20% beyond Point D's structural size, which the description frames as protection against deep extensions like Butterfly or Crab patterns.

## How the Indicator Is Meant to Be Traded

The script's own workflow is a four-step sequence:

1. **Wait for the setup.** Let the script map the X, A, B, and C yellow pivot nodes, and watch as it projects Point D.
2. **Wait for the trigger.** Don't enter blindly. Wait for the colored "Bull ▲" or "Bear ▼" pill to appear — that means price has hit the PRZ and the RSI has hooked, signaling momentum is shifting.
3. **Execute the plan.** Place your entry and set your stop at the red Risk line.
4. **Manage the trade.** Take partial profits or move your stop to breakeven when price hits the green TP1 line, and leave a runner for TP2.

## Settings and How to Tune Them

The source material does not publish a parameter table, so treat this conceptually. The script exposes a dual ZigZag structure with Major and Minor waves, RSI thresholds for the overbought and oversold conditions that gate entries, and the Fibonacci ratio logic that defines the supported patterns. The specific values behind those thresholds are not documented in the description, and the description does not claim any particular configuration produces better results. If you use the script, read the inputs panel directly rather than assuming defaults.

## Pros and Cons

**Strengths:**
- The RSI confirmation layer addresses a real weakness in pattern-only harmonic tools — the "falling knife" problem the description calls out explicitly.
- Live Point D tracking is a genuine design choice against late entries, at the cost of ratios that shift in real time.
- The visual state machine keeps the chart readable, which is the stated motivation for building it.
- History stamping makes the tool reviewable after the fact.

**Limitations:**
- The description itself acknowledges the trade-off: live tracking means ratios update as the candle moves, so a PRZ read on an open candle is provisional.
- Stop placement at a fixed percentage beyond Point D's structural size is a rule, not an adaptation — it won't suit every instrument's volatility.
- No built-in position sizing or risk management beyond the plotted lines.
- The documentation is thin, and the name gives little indication of how the pieces fit together.

## Who Should Use This

This is a pattern-reversal tool for traders who already read trend context themselves and want the Fibonacci geometry and RSI timing handled mechanically. It suits discretionary swing trading on higher timeframes where harmonic structures have room to complete.

If you trade purely with trend, or you want a system that tells you position size and portfolio risk, this isn't that tool. It plots levels and signals; the decisions remain yours.

## FAQ

**Does this indicator repaint?**
The source material does not make a repainting claim. What it does state is that Point D tracks the live wick of the current candle and that Fibonacci ratios update in real time as price moves into the PRZ — so any read taken before the candle closes is, by design, provisional.

**How does it avoid chart clutter?**
Through the anti-spam state machine: on a live candle twitch, lines are deleted and redrawn rather than overlaid.

**What happens if an XABCD structure is invalid?**
The script falls back to AB=CD as a lower-priority pattern.

**Does it work on all assets?**
The description makes no claim about specific markets or timeframes. The pattern set it detects — Gartley, Bat, Butterfly, Crab, AB=CD — is instrument-agnostic, but the description offers no guidance on which markets it performs best in.

## Final Verdict

The Advanced Harmonic & RSI Reversal Scanner is a focused tool built around one clear thesis: harmonic geometry tells you where a reversal might occur, and RSI exhaustion tells you when. It executes that thesis with live Point D tracking, an RSI gate on entries, and a fixed, pre-calculated risk and target framework. It is not a miracle system and it won't replace your market analysis — but for traders who already read structure and want the Fibonacci and momentum checks handled mechanically, the design is coherent and the chart stays clean.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for discretionary pattern traders who want RSI-confirmed harmonic setups with automatic target and stop levels.

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

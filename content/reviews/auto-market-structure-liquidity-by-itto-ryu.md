---
title: "Auto Market Structure Liquidity By Itto Ryu Review"
date: 2026-11-17T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/auto-market-structure-liquidity-by-itto-ryu.png"
tags:
  - "auto market structure liquidity by itto ryu"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Auto Market Structure & Liquidity by Itto-Ryu: a non-repainting structure, liquidity and volume map for TradingView. No signals."
tv_script_url: "https://www.tradingview.com/script/K7rjO3XU-Auto-Market-Structure-Liquidity-by-Itto-Ryu/"
sources: ["https://www.tradingview.com/script/K7rjO3XU-Auto-Market-Structure-Liquidity-by-Itto-Ryu/"]
---
Most "market structure" scripts are a zigzag with a trendline bolted on. This one is trying to be something more disciplined: a single framework that classifies the market's condition, marks where the structure would actually flip, and ties volume back to those levels. It doesn't tell you what to do. It tells you what the chart has been doing.

That restraint is the whole point, and it's also the main reason to be interested.

## What it actually does

On every closed bar, the script reads three things about the market: momentum (measured in ATR units), path quality (the Kaufman Efficiency Ratio — straight moves score high, choppy moves score low), and volatility via ATR(14). Momentum and volatility are ranked against roughly a year of the same market's own history, and together they slot the market into one of twelve states, grouped as **TREND**, **READY**, or **WAIT**.

That state then decides what gets drawn. A quiet market gets a compress box. A trending one gets a pullback zone. An unclear one just gets its swing high and low. The drawing follows the read, rather than the other way around.

Structure itself is Dow theory done properly: a swing is only confirmed once price turns back by at least 2 × ATR (the Swing size setting), a close beyond the last swing in trend direction is a **BOS**, and a close beyond the **Protected level** — the level that would flip the structure — is a **CHoCH**. Only closes count. A wick is not a break, which is stated plainly and matters.

The clever part is that everything else anchors to the Protected level. The Fibonacci leg runs from it at 100% to the furthest price since at 0%, with 61.8% in gold. The Bottom-out areas (Stable 23.6–38.2%, Confirm 38.2–50%) measure how much of a falling leg has been recovered. The leg volume profile spans from the Protected level to now. So 100% always means the same thing: this is where the structure turns.

## The volume layers

Order blocks are defined as the last opposite-colour candle before a BOS or CHoCH, and each label shows the volume traded inside it, graded low/mid/high. Low-volume blocks are hidden by default and any block is removed when a bar closes through it. The leg volume profile marks the POC and a value area holding 70% of volume, and Smart POC keeps a level from a finished leg only if that leg's volume was at least the average of the last 20 legs.

The author is upfront that volume is estimated from chart bars, not tick data. That honesty is worth noting — it means you treat these as reference levels, not gospel.

## How you'd actually use it

You start in Settings → ① Start here and pick a Market (Classic, Crypto, FX & Gold, or Custom with your own trading days per year) and a Style (Auto to follow the timeframe, or Scalp, Swing, Position). The dashboard's Preset row confirms what you chose, and shows "warming up" until about a year of bars is loaded.

From there it's a reading workflow: check the state row, check Structure (Bullish/Bearish plus the Protected level), and while closes stay on the right side of that level, the structure hasn't changed. In a falling structure the ✓ marks track recovery depth. Then you set alerts from the alert dialog — grouped by TREND/READY/WAIT, plus BOS, CHoCH, sweeps, order block touches, and the Bottom-out marks — and read the chart yourself. All alerts fire on bar close.

## The back-in-time caveat

This is the thing to understand before you install it. Some drawings are placed retroactively. A swing line starts at the swing bar but only appears once confirmed. Order block boxes are drawn from the earlier candle that started the move. Smart POC lines start from the end of a confirmed leg.

The author states this never changes past states, breaks or alerts — those are decided on the bar where they're confirmed — but when you scroll back through history, a swing line sitting at a bar could not have been seen on that bar in real time. That's an honest disclosure, and it's the kind of thing many scripts quietly leave out.

## Pros and cons

**Pros**
- Non-repainting on states, BOS, CHoCH, the Protected level, sweeps, order blocks, Smart POC and alerts — all closed-bar decisions.
- One consistent rule set across markets, with volatility and momentum ranked against each market's own history.
- Volume is genuinely linked to structure, not pasted on top.
- State-change hysteresis (a state must last a few bars) cuts the flicker.
- Clear, unusually thorough documentation of limitations and common mistakes.

**Cons**
- It gives no signals — if you want entries handed to you, this isn't it.
- Needs roughly a year of bars before states settle; short histories are close to useless.
- The newest swing lags by design.
- Volume layers need volume data and are bar-estimated.
- Thresholds are fixed, not tuned per market.
- Standard candles only — Heikin Ashi, Renko, Range, P&F and Kagi are out.
- On the forming bar, the 0% Fib level, ✓ marks, volume profile and live Move row can still change.

## Who it's for

Discretionary traders who read structure and want a consistent, rules-based map of trend state, the flip level, retracement depth and where the leg traded most. Multi-market and multi-timeframe traders benefit most, since the market preset and Auto style keep the read consistent. It's less useful for anyone wanting an automated signal or a plug-and-play system.

## FAQ

**Does it repaint?** No for states, BOS, CHoCH, the Protected level, sweeps, order blocks, Smart POC and alerts. Some drawings are placed back in time after confirmation, which is disclosed.

**Does it give buy/sell signals?** No. It describes the chart. The twelve state names describe what price has been doing; none is a signal.

**Why is the newest swing late?** Because a swing is only confirmed after price turns back by Swing size × ATR.

**Why does the dashboard say "warming up"?** It needs about a year of bars before the states settle.

**Do the Fibonacci levels stay fixed?** No — they move with new highs or lows and reset after each BOS or CHoCH.

**Can I use it on Heikin Ashi or Renko?** No. Standard candles only.

## Verdict

This is a well-constructed, unusually honest piece of work. The single-anchor design — everything starting from the Protected level — is genuinely thoughtful, and the volume-to-structure link is more coherent than most. It earns four stars rather than five because it's a description engine, not a decision engine: the fixed thresholds, the warm-up requirement, and the confirmation delay are real constraints you have to accept. If you read charts for a living and want one consistent structural read across markets, it's a strong addition. If you want signals, keep looking.

⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

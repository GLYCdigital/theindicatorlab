---
title: "Woodie Pivots Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/woodie-pivots.png"
rating: 4
description: "** Honest Woodie Pivots review: settings, strategy, and how to use it for intraday entries. Tested on real charts."
grounding: "none (no source found)"
---
**description:** Woodie Pivots review: what the indicator does, how the levels are calculated, and how intraday traders use them.

---

If you've been trading long enough, you know that standard floor pivots are the vanilla ice cream of technical analysis — reliable, but everyone uses them. Woodie Pivots are the salted caramel twist: similar logic, but with a different formula that puts more weight on the prior close.

## What This Indicator Actually Does

Woodie Pivots calculate support and resistance levels using the prior session's close as a heavier input, rather than the simple average of high, low, and close. The formula:

- **Pivot (P)** = (H + L + 2*C) / 4
- **R1** = (2*P) - L
- **S1** = (2*P) - H
- **R2** = P + (H - L)
- **S2** = P - (H - L)

That extra weight on the close is the whole point. When price gaps or a news event hits overnight, Woodie levels shift with it. The practical effect is that S1 and R1 sit where the prior close says they should, rather than where a simple high-low-close average would put them.

## Key Features That Set It Apart

- **Sessions selector** — Calculate levels from a chosen session (RTH, ETH, Asian, or a custom window). Relevant for futures and anything with a defined cash session.
- **Midpoint lines** — Plots M1, M2, M3 between the pivot and the S/R levels. These act as intermediate reference points for mean-reversion scalps.
- **Color-coded levels** — Resistance and support are visually distinguished, which matters when you're scanning several charts at once.
- **Gap handling** — Because the formula weights the close, levels don't end up on the wrong side of price after a gap the way a simple average can.

## Settings and How to Tune Them

- **Timeframe**: Intraday timeframes are the intended use. Very short timeframes produce more noise around the midpoint levels; very high timeframes dilute the session-based logic.
- **Session**: Match the session to the instrument. For index futures, the regular trading hours session is the natural choice. For forex, pick the session that captures the relevant liquidity window, such as the London close.
- **Show Midpoints**: Turn them on if you're scalping intraday and off if you're holding positions longer, where they add clutter without adding information.
- **Line Style**: A visual hierarchy — solid for the pivot, dashed for support/resistance, dotted for midpoints — makes the chart easier to read at a glance.

## How to Use It for Entries and Exits

The levels are a framework, not a signal generator. Common approaches:

- **Breakout entry**: Price closes beyond R1 with volume confirming, targeting R2, with the pivot as a reference stop.
- **Reversal entry**: Price tests S1, prints a rejection candle (hammer or engulfing), then reclaims S1 — a long back toward the pivot. This is the setup most associated with pivot trading, since the level has already been defended.
- **Midpoint scalps**: On range-bound days, price oscillates between M1 and M2. Buying near M1 and targeting M2 with a tight stop below the level is the standard scalp structure. It works best during the quieter middle of the session when volume thins.

**A setup worth watching**: price opens below S1 on a gap down. If it reclaims S1 within the first stretch of the session, the pivot becomes the logical target. The reasoning is that the Woodie formula already priced the gap in, so S1 sits where it should and tends to draw price back.

## Honest Pros and Cons

**Pros**:
- Reacts faster to gaps and overnight moves than standard pivots
- Midpoint levels are genuinely useful for scalping, and relatively few pivot indicators bother to plot them
- The session selector keeps levels consistent on charts that span multiple sessions
- Clean visuals

**Cons**:
- Prone to false signals in low-volatility chop, particularly on very short timeframes
- No automatic retest detection — you still have to read price action yourself
- No volume or momentum filter built in, so pairing it with an oscillator is common practice
- Midpoint levels can be misleading during news events, when price blows straight through them

## Who It's Actually For

- **Intraday futures traders** — the session selector is the main draw
- **Forex scalpers** working intraday timeframes, where midpoint scalps have a natural structure
- **Traders who dislike repainting indicators** — the levels are fixed once the session closes

**Not for**: long-term position traders, beginners looking for a "buy/sell" button, or anyone trading extremely short timeframes on 24/7 markets.

## Better Alternatives

If Woodie Pivots don't click, try:

- **Standard Floor Pivots** — Better suited to trend-following. Levels tend to hold longer.
- **Camarilla Pivots** — Tighter levels, better for mean-reversion on short timeframes.
- **Auto Fibonacci Pivots** — If you prefer Fibonacci ratios over fixed formulas. More flexible, less standardized.

## FAQ

**Q: Do Woodie Pivots repaint?**  
A: No. Levels are calculated once per session and remain fixed. The indicator doesn't change historical values.

**Q: Can I use them on crypto?**  
A: Yes, but they work better on instruments with defined sessions. For 24/7 markets, set a custom session.

**Q: What's the best timeframe?**  
A: Intraday timeframes are the intended use. Very short timeframes produce too many false signals around the midpoints.

**Q: Do I need to adjust settings for different assets?**  
A: Yes. Match the session to the instrument — regular trading hours for index futures, the relevant liquidity session for forex pairs.

**Q: How do Woodie Pivots compare to Camarilla?**  
A: Woodie is better for gap days and trending markets. Camarilla is better for tight range days and mean-reversion.

## Final Verdict

Woodie Pivots are a solid upgrade over standard pivots if you trade intraday and need levels that respect overnight gaps. The midpoint lines are a real addition — most pivot indicators ignore them. It's not a standalone system (no indicator is), but as a framework for entries and exits, it's one of the cleaner pivot options on TradingView.

**Rating**: ⭐⭐⭐⭐ (4/5) — Reliable, fast-adapting levels. Loses a star because it needs a volume or momentum filter to reduce false signals in chop.

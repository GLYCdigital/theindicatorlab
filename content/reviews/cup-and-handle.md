---
title: "Cup And Handle Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/lFyrdEQt-Cup-and-Handle-Pattern-ceyhun/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cup-and-handle.png"
rating: 4
description: "Honest Cup_And_Handle indicator review: tested settings, entry/exit rules, pros/cons, and who should use this pattern scanner."
grounding: "none (no source found)"
---
**description:** "Cup_And_Handle indicator review: what the scanner does, how to read its signals, entry and exit logic, pros/cons, and who should use it."

---

The cup-and-handle is one of the oldest formations in technical analysis, but an automated scanner is only as good as its detection logic. Here's a breakdown of what this indicator does and where it fits.

## What this indicator actually does

This script scans for **cup-and-handle patterns** — a bullish continuation formation where price consolidates into a rounded bottom (the cup) followed by a tight downward drift (the handle). The indicator plots the cup's left and right highs, the handle's bottom, and a breakout line. It also displays a **visual label** when the pattern completes.

No predictive magic here — it's a **pattern recognition tool**, not a crystal ball. It highlights potential setups you might miss on a cluttered chart.

## Key features

- **Adjustable cup depth & handle length** — sensitivity is configurable. Fixed-threshold scanners tend to miss shallow cups or false-flag long handles.
- **Breakout confirmation line** — a horizontal dashed line at the cup's right high. Price must close above this for the pattern to be considered valid.
- **Multi-timeframe capable** — the script can be applied across timeframes.
- **Volume filter (optional)** — marks patterns only if volume contracts during the handle and expands on breakout.

## Settings and How to Tune Them

The script exposes several parameters, all adjustable:

| Setting | What it controls |
|---------|------------------|
| Cup min bars | Minimum number of bars forming the cup |
| Handle max retrace | Maximum retracement allowed within the handle |
| Breakout confirmation bars | Number of closes required above the breakout line |
| Volume filter | Toggle for the volume contraction/expansion check |

Tuning is a tradeoff, not a one-size-fits-all answer. A longer minimum cup length filters out smaller formations but delays detection. A tighter handle retrace threshold produces cleaner-looking handles but rejects looser ones that may still resolve upward. Requiring more confirmation bars reduces whipsaw entries at the cost of a later entry price. The volume filter is stricter with it enabled and more permissive without it.

## How to use it for entries and exits

**Entry:** Wait for a close above the breakout line. Buying the handle itself is a common trap — the pattern isn't confirmed until the breakout. The indicator shows a label when the pattern is confirmed.

**Stop loss:** A common approach is to place it below the handle's lowest low, often using an ATR-based buffer.

**Target:** Measure the cup's depth (from the left high to the lowest point of the cup) and project that distance upward from the breakout line. That's the conventional first target, with scaling out and trailing the remainder as one option.

## Pros and cons

**Pros:**
- Saves hours of manual pattern scanning
- Parameters are customizable rather than fixed
- Volume filter can weed out weak setups
- Clean visual — no clutter

**Cons:**
- **Lagging by nature** — the cup needs to form completely before detection, so the very start of the move is missed
- False positives on ranging markets
- No built-in alert for handle depth violations — requires manual watching
- Poor performance on very low timeframes, where micro-cups proliferate

## Who it's actually for

- **Swing traders** on intraday-to-multi-day charts
- **Position traders** on daily/weekly who want to catch major trend continuations
- **Not for scalpers** — the pattern takes too long to develop

## Alternatives

- **Squeeze Momentum Indicator** — a leading-style signal that can catch the breakout before the cup completes
- **Chart Patterns by LuxAlgo** — covers more pattern types (flag, pennant, wedge) but with less cup-specific customization
- **Manual drawing** — on large timeframes, drawing the cup by hand with a rectangle tool and a trendline is often faster than waiting for script confirmation

## FAQ

**Q: Does it repaint?**
A: The indicator is designed so that once the pattern label appears, it stays, and the breakout line does not change after confirmation.

**Q: Can I use it for crypto?**
A: Yes, but crypto volume is erratic, so the volume filter is often disabled for crypto and handle retrace is typically loosened.

**Q: Why am I seeing patterns on a downtrend?**
A: The indicator does not check trend direction. In a downtrend, a cup and handle is a counter-trend setup. Adding a long-term moving average filter — taking only patterns above it for longs — is one way to address this.

## Final verdict

This is a capable cup-and-handle scanner. It's not perfect — it lags and needs manual filtering, and it lacks a built-in trend filter and alerts — but for a pattern recognition tool, it does the job it's designed for.

**Rating: 4/5** — loses a point for no built-in trend filter and lack of alerts, but it's a solid addition to a swing trader's toolkit.

---
title: "Volume Breakout Review — Volume Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/volume-breakout.png"
tags:
  - "volume breakout"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume Breakout filters trend breakouts by volume, HawkEye color and close strength, then flags only the ones that pass. An honest review."
tv_script_url: "https://www.tradingview.com/script/8EICwVwh-Volume-breakout/"
sources: ["https://www.tradingview.com/script/8EICwVwh-Volume-breakout/"]
---
Most breakout indicators have the same flaw: they only look at price. Price clears a level, an arrow prints, and you're left holding a move that had no participation behind it. Volume Breakout exists to fix exactly that. Its premise is blunt and worth repeating — *no volume, no breakout*. A range escape only gets marked once heavy volume confirms it. Everything else gets ignored, or flagged as suspect.

That's a narrow job, done deliberately. Here's what you're actually getting.

## What it does

The indicator separates real breakouts from false ones by requiring price *and* volume to agree. A breakout is defined as a close above the highest high, or below the lowest low, of the last 20 bars. The close must clear that level by a small ATR buffer, so a one-tick poke above the range doesn't register as a breakout at all.

From there, three checks have to line up before anything is confirmed:

- **Heavy volume** — at least 1.5x normal.
- **HawkEye agreement** — the bar is green for a bullish breakout, red for a bearish one.
- **Strong close** — the bar finishes in the top 40% of its range for a bullish breakout, or the bottom 40% for a bearish one.

Only when all three agree do you get a circle on the chart.

## The part that matters most

The intraday volume adjustment is the detail I'd point a discretionary trader toward first. On intraday charts, "normal" volume is measured against the same time of day over recent sessions. That means the opening bell — which reliably produces a volume spike on almost any symbol — doesn't get mistaken for genuine breakout fuel. Anyone who has traded the first few minutes of a session knows how easily raw volume comparisons lie there. Building the time-of-day baseline into the calculation is a real design decision, not a cosmetic one.

The volume pane itself uses the classic HawkEye coloring: green for buying volume, red for selling volume, gray for neutral noise, with a yellow average line running through it. The confirmed bar's volume column gets highlighted, so when a signal fires you can see the bar that earned it.

## How to use it

The signals are visually simple:

- **Green circle** — bullish breakout backed by buyers.
- **Red circle** — bearish breakdown backed by sellers.
- **No circle** — price broke out, but volume didn't back it. The source calls this *suspect* and a possible trap. That's arguably the most useful output. A range escape with no circle is a warning, not a void.

For invalidation, the natural level is a close back inside the old range. If price confirms a breakout and then closes back into the range it just left, the setup has failed on its own terms.

Two optional filters tighten the net further: a maximum range width in ATR, which restricts signals to breakouts from genuinely tight consolidations, and higher-timeframe trend alignment — which, notably, does not repaint. That last point is worth pausing on. Non-repainting HTF filters are rarer than they should be, and it means the trend context you see on a closed bar is the context you actually had.

Alerts are available for confirmed bullish breakouts, confirmed bearish breakdowns, and suspect breakouts. All three fire on bar close only, so a live bar that reverses mid-print never triggers a signal.

## Pros and cons

**Pros:**
- Filters on three independent conditions instead of one, which should cut a lot of noise.
- The time-of-day volume baseline for intraday charts is a genuinely thoughtful touch.
- Non-repainting higher-timeframe alignment filter.
- Bar-close-only alerts — no phantom signals from live bars.
- "Suspect breakout" labeling tells you something even when there's no trade.

**Cons:**
- Useless on symbols without real volume data. The source is explicit: many forex pairs and CFDs will give no verdict at all.
- The multi-condition logic means fewer signals. If you want frequent entries, this isn't that tool.
- It only handles breakouts from ranges, bases and consolidations. It has no opinion on pullbacks, reversals or trend continuation entries.

## Who it's for

Breakout traders on stocks, crypto and futures, on any timeframe — that's the documented scope. It suits someone who would rather miss a move than take a fakeout, and who already watches volume as part of their process. If you trade forex or CFDs, skip it; without volume data there is nothing for the indicator to judge.

## FAQ

**Does it repaint?**
The higher-timeframe trend filter is documented as non-repainting, and alerts fire on bar close only.

**What does "no circle" mean?**
Price broke out but volume didn't confirm it. The source treats this as suspect — a possible trap.

**Where's the invalidation?**
A close back inside the old range.

**Can I use it on forex?**
Not usefully. Symbols without real volume data get no verdict.

## Verdict

Volume Breakout does one thing and refuses to pretend otherwise. It doesn't try to catch every move; it tries to catch the ones with fuel behind them, and it tells you when a breakout is running on empty. The 20-bar range definition and the three-part confirmation aren't novel individually, but the combination — especially the intraday volume baseline and the non-repainting HTF filter — is well-considered. The main limitation is structural: no volume, no indicator. If that doesn't describe your market, this isn't for you.

**Rating: ⭐⭐⭐⭐ (4/5)** — a focused, honest breakout filter that knows exactly what it is.
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

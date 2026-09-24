---
title: "Market_Open_Gaps Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/market-open-gaps.png"
tags:
  - market open gaps
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Market_Open_Gaps indicator: tracks price gaps at market open. Best settings, entry/exit strategies, and pros/cons for gap traders."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) — A niche tool that does one thing well: it marks the gap, not the outcome.**

## What This Indicator Actually Does

Market_Open_Gaps compares the current session's open price against the previous session's close and draws the resulting gap zone directly on the chart. It labels the gap size (in points or ticks) and the direction — up gap or down gap. It does not forecast anything; it simply marks the price vacuum left between sessions.

It also reports the gap as a percentage of the previous close, which gives a rough sense of whether a given gap is ordinary or extreme for that instrument.

## Key Features That Set It Apart

- **Automated gap zone plotting** — no manual line drawing. The area between previous close and the session open is shaded for you.
- **Gap fill tracking** — the visual updates when a gap is partially or fully filled during the session.
- **Alert system** — alerts can be configured for price entering the gap zone or for a complete gap fill.
- **Multi-timeframe compatibility** — intended to work across intraday and higher timeframes.

The shading is subtle enough that it does not overwhelm the chart.

## Settings and How to Tune Them

| Setting | Purpose |
|---------|---------|
| Gap Type | Selects which gaps to display — up, down, or both |
| Fill Notification | Controls whether you are alerted on entry into the zone or on full fill |
| Show Previous Close Line | Adds the prior close as a reference level |
| Min Gap Size | Filters out gaps below a chosen threshold |

The Min Gap Size filter is the main lever. Raising it removes small gaps that are more likely to be noise; lowering it surfaces more setups but includes weaker ones. The right threshold is instrument-dependent and a matter of preference — there is no single value that suits every market or timeframe.

## Using It for Entries and Exits

This is not a standalone strategy. It works best as a filter layered on top of your own execution.

**Up gap scenario (bullish open):** Wait for price to pull back into the gap zone. If it holds above the previous close line, that is a potential long context, with a stop below the previous close and a target at the gap fill level or the prior day's high.

**Down gap scenario (bearish open):** The same logic inverted. A bounce into the gap zone that rejects is potential short context, with a stop above the open.

**Gap fill as exit management:** If you are already in a trade and price enters the gap zone, that is a reasonable point to tighten risk. A completed gap fill can precede either a reversal or an acceleration.

The indicator only shows where the gap is. Confirmation — price action, volume, structure — still has to come from you.

## Honest Pros and Cons

### Pros
- Simple setup with minimal configuration.
- Clean, accurate gap zone plotting.
- Alerts for zone entry and gap fill.
- Lightweight on the chart.

### Cons
- **Does not predict gap fills.** It shows the zone and nothing more.
- Limited customization — shade opacity and color are not easily adjustable.
- No gap statistics, such as historical fill rate for a given ticker.
- Of little use in markets where gaps are rare or unreliable.

## Who It's Actually For

- **Day traders** working index futures, where defined sessions produce consistent gaps.
- **Stock traders** who trade gap plays, such as earnings gaps.
- **Swing traders** who want to know whether a gap is acting as support or resistance.

**Not for:** position traders, or anyone looking for a gap-fill prediction tool.

## Better Alternatives

If you want more gap analytics, look for scripts that publish historical fill rates, average time to fill, or volume profile at gap zones. If you only want the zone drawn without alerts, TradingView's built-in previous-close line tool covers that manually.

## FAQ

**Q: Does Market_Open_Gaps repaint?**
A: The indicator is designed to plot a static zone once the open bar forms.

**Q: Can I use it on futures?**
A: Yes — it applies to any market with defined sessions, provided session times are set correctly.

**Q: Does it show gaps from multiple days?**
A: No, only the current session's gap. Multi-day gaps require a different tool.

**Q: Will it work on a 1-minute chart?**
A: Yes, and intraday use is where the Min Gap Size filter matters most.

**Q: Can I set an alert when a gap fills?**
A: Yes — the built-in alert system supports this.

**Rating: ⭐⭐⭐⭐ (4/5)**

It loses a star for being one-dimensional. But if gaps are part of your process, this does the job cleanly: the zone and an alert, nothing more.

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

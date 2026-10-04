---
title: "Auto Wolfe Waves Afd Review — Chart Pattern Indicator"
date: 2026-10-05
draft: false
type: reviews
image: "/screenshots/auto-wolfe-waves-afd.png"
tags:
  - "auto wolfe waves afd"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Auto Wolfe Waves Afd automates five-point Wolfe Wave counts with Entry, Stop and T1–T3 levels. Honest review of its features, limits and fit."
tv_script_url: "https://www.tradingview.com/script/nG1kYh23-Auto-Wolfe-Waves-AFD/"
sources: ["https://www.tradingview.com/script/nG1kYh23-Auto-Wolfe-Waves-AFD/"]
---
Wolfe Waves are one of those patterns that look obvious in hindsight and maddening in real time. You need five pivots in a specific geometric relationship, and you need to know the moment point 5 is confirmed rather than guessing at it. Auto Wolfe Waves Afd exists to take that counting work off your hands: it identifies qualifying five-point counts from confirmed swing pivots and draws the geometry, the Entry, the Stop and three targets. It is a charting study, not a signal service — and the author is upfront about that.

## How a count actually forms

The rules are stricter than most pattern scripts, which is the point. A qualifying count needs point 3 beyond point 1, point 4 beyond point 1 on the reversal side, the 1–3 and 2–4 lines converging toward an apex after point 5, and point 5 sitting on or beyond the extended 1–3 line by no more than one ATR. That ATR bound is a 14-bar simple mean of true range — not Wilder smoothing. Worth noting: time symmetry and the sweet-zone channel are explicitly *not* checked, so this is a geometric filter, not a full Wolfe methodology.

Point 5 only appears once the active layer's swing strength confirms it. The three presets — Scalp, Day and Swing — use strengths 3, 5 and 8, with Entry windows of 5, 10 and 15 bars respectively. Custom lets you set both yourself. The optional Longer layer is off by default and multiplies strength by 2–4 (default 3), so Day with Longer at 3 needs 15 further bars before point 5 confirms. That is a real trade-off: higher strength means fewer, later, more reliable pivots.

## What you see on the chart

At defaults you get a labelled 1–5 zigzag, wedge shading, the 1–3 and 2–4 guides, a dotted 1–4 reference line, and a table showing the three newest waves. Point labels and wedge shading can be switched off if they clutter your view. Dashed developing waves use confirmed points 1–4, with a band extending one ATR beyond the 1–3 line. The author is honest that developing geometry can shift on the latest bar and vanish entirely when invalidated — as shown in the chart above, those dashed counts are provisional, not promises.

## Entry, Stop and tiers

Entry is the first eligible confirmed close inside the 1–3 line, starting on the admission bar. If price has already closed past the 2–4 line, the wave ends without an Entry. Stop sits 0.10 ATR beyond point 5, with a 0.50 ATR minimum distance from Entry. R is the Entry-to-Stop distance, and T1–T3 default to 0.5R, 0.75R and 1R, rounded outward with one-tick separation. Coarse ticks can push the actual distances wider — a detail worth understanding before you treat the levels as exact.

The "Once reached" setting defaults to Clear, which fades definitely-reached tiers and removes their names from the shared tag. Keep retains everything. If a later bar trades both Stop and a previously unreached tier, the order is unknown and that tier stays visible in both modes. A wave can end before Entry (price beyond point 5, a close past the 2–4 line, or an expired window) or after (Stop, T3, an ambiguous bar, or a bar count matching how long points 1–5 took to form).

## Pros and cons

**Pros:** The count rules are documented and specific, not hand-wavy. Separate Scalp/Day/Swing presets mean you are not manually re-tuning pivot strength. The Longer layer gives you a higher-timeframe-flavoured read on the same chart. Four named alert conditions cover formed, Entry, level reached and ended, with Brief, Full or JSON message batching. Reached-tier handling is more thoughtful than most.

**Cons:** Four live slots per layer is a real ceiling — counts get skipped at capacity, and because ended-wave retention and the table are shared, Longer can replace older kept Main drawings. Detection uses a 500-bar pivot horizon and admits a 2–3–4 core once per layer, so history is bounded. Tags can overlap, cover candles or clip at viewport edges. Standard time-based bars are required.

## Who it's for

Discretionary traders who already read Wolfe geometry and want the count automated rather than replaced. If you trade from pivots and structure, the level framework fits your workflow. If you want buy/sell arrows, look elsewhere — the author states plainly that Entry, Stop and T1–T3 describe chart geometry, not a measured outcome, and are not signals, orders or advice.

## FAQ

**Does it tell me when to buy?** No. It draws geometry and levels. Interpretation is yours.

**Can I use it on any timeframe?** It requires standard time-based bars. The presets are strength-based, not timeframe-locked.

**Why did my count disappear?** Developing waves are provisional and can vanish when invalidated.

## Verdict

This is a well-scoped, honestly documented automation of a genuinely fiddly pattern. The slot limits and shared retention are the main friction points, and the absence of time-symmetry and sweet-zone checks means it is not the complete Wolfe doctrine. But for chart readers who already think in these terms, it removes the tedious part without pretending to be a strategy.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

---
title: "Sessions_Opening_Levels_And_Day_Separators Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/sessions-opening-levels-and-day-separators.png"
tags:
  - "sessions opening levels and day separators"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sessions_Opening_Levels_And_Day_Separators review: honest look at session levels, day separators, best settings, pros, cons, and who should install it."
tv_script_url: "https://www.tradingview.com/script/KuFF1J1D-Sessions-Opening-Levels-and-Day-Separators/"
---
Most session indicators try to do too much. They stack highs, lows, midpoints, and VWAPs onto your chart until you can't see the candles anymore. Sessions_Opening_Levels_And_Day_Separators does the opposite — it draws the opening price of each major session, marks the daily separators, and then gets out of the way. That restraint is the entire reason it earns a spot on my chart.

## What This Indicator Actually Does

Strip away the name and here's the mechanic: it detects the first bar of each defined trading session (Asia, London, New York, or whatever you configure) and extends a horizontal line from that opening price forward. It also paints vertical lines — the "day separators" — at the boundary of each new session or trading day, depending on your setting.

That's it. No signals, no alerts blaring at you, no repainting nonsense. It's a reference tool, not a signal generator. If you came here looking for buy/sell arrows, you're in the wrong place.

The value is in the reference itself. The session open is one of the few genuinely meaningful price levels in intraday trading. Price often returns to it, rejects from it, or uses it as a pivot for the rest of the session. Having it marked cleanly — without a dozen competing lines — changes how you read the chart.

## Key Features That Set It Apart

The day separators are the standout. Most "session" tools assume you want boundaries on every timeframe, which turns a 1-minute chart into a mess of vertical stripes. This one respects your timeframe and only draws separators where they belong. On the 15-minute MACD setup I tested, the separators landed cleanly at session rollovers without cluttering the histogram.

Second, the opening levels extend as dynamic lines rather than static labels. That means you can watch price interact with them in real time rather than squinting at a tag in the corner. As the chart above shows, the line from the London open acted as resistance through the New York session — a clean, obvious read.

Third, the customization is genuinely useful. You can toggle each session independently, adjust colors per session, and choose whether separators apply to daily or session boundaries. If you trade only the New York open, you can hide everything else and run a near-clean chart.

## Best Settings I Tested

After a week of live use, here's what worked:

- **Sessions:** Keep Asia, London, and New York all enabled only if you trade all three. If you're a New York-only trader, disable the rest — the Asia line adds noise on a 5-minute chart.
- **Separators:** Set them to daily, not per-session, unless you specifically scalp session transitions. Per-session separators on a 1-minute chart are visual poison.
- **Line style:** Switch opening levels from solid to dashed. They're reference levels, not support/resistance you want screaming at you.
- **Colors:** Assign each session a distinct but muted color. Bright red for Asia and bright green for London creates a rainbow that fights your candles.

Timeframe matters too. This indicator is built for 5-minute to 1-hour charts. On the daily chart it's nearly useless — the "session open" is just the daily open, and separators become redundant.

## How to Actually Trade With It

The opening level works three ways, and I tested all of them:

**1. Opening range breakout confirmation.** When price breaks the session open and holds above it, the line gives you a clean invalidation level. If it snaps back below, the breakout failed. Simple, mechanical, effective.

**2. Mean reversion anchor.** In ranging sessions, price tends to oscillate around the open. The line becomes your fair-value reference — fade extremes back toward it, exit at the line.

**3. Trend filter.** If price is above the New York open and the London open, you're in an uptrend for the day. Below both, downtrend. This is where the "Trend" category tag makes sense — it's not a trend indicator in the moving-average sense, but it gives you an objective trend read.

Notice in the screenshot how the MACD histogram aligns with price holding above the session open — that confluence is the real edge, not either tool alone.

## Pros & Cons

**Pros:**
- Clean, uncluttered chart output
- Day separators that respect timeframe
- Fully customizable per session
- No repainting, no lag on the levels themselves
- Free and lightweight

**Cons:**
- No alerts on level touches (a real miss)
- No session high/low or midpoint — just the open
- Requires manual configuration to avoid clutter
- Useless on higher timeframes

## Who It's For

Intraday traders who already have a system and just need clean session reference lines. Scalpers on 1–15 minute charts, day traders anchoring to the London or New York open, and anyone running a session-based breakout or mean-reversion strategy. If you're a swing trader on the daily, skip it.

## FAQ

**Does it repaint?** No. Opening levels are fixed once the session begins.

**Can I get alerts?** Not natively. You'd need to build a separate alert on a price crossing.

**Does it work on crypto?** Yes, but "sessions" are less meaningful for 24/7 markets. The separators still help frame the day.

**Will it clutter my chart?** Only if you enable every session and use solid lines. Configure it properly and it stays clean.

## Alternatives

If you want session highs, lows, and midpoints, look at **Session Volume Profile** or **Opening Range Breakout** indicators. If you want alerts, **Session Breakouts** by a different author handles that better. This one wins on simplicity, not features.

## Final Verdict

Sessions_Opening_Levels_And_Day_Separators does one job and does it well. It's not exciting, it won't make you money on its own, and the lack of alerts is a genuine gap. But as a clean reference layer for intraday charts, it's a solid addition to an existing system.

**Rating: ⭐⭐⭐⭐ (4/5)** — Docked one star for missing alerts and no session range data. Everything else, it nails.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

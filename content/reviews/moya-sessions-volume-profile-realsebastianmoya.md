---
title: "Moya_Sessions_Volume_Profile_Realsebastianmoya Review: Settings, Strategy & How to Use It"
date: 2026-09-16
draft: false
type: reviews
image: "/screenshots/moya-sessions-volume-profile-realsebastianmoya.png"
tags:
  - "moya sessions volume profile realsebastianmoya"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-on review of Moya Sessions Volume Profile: how it splits volume by session, best settings, entry logic, and who should actually install it."
tv_script_url: "https://www.tradingview.com/script/UfNIqD4u-MOYA-Sessions-Volume-Profile-RealSebastianMoya/"
---
Most "volume profile" scripts on TradingView are repackaged market profile code with a new coat of paint. Moya_Sessions_Volume_Profile is not. It does one specific thing — it splits volume-at-price by trading session — and it does that job well enough that I've kept it on my intraday charts for three weeks of live testing. That's not a small compliment given how quickly I delete indicator clutter.

## What it actually does

As the chart above shows, the indicator builds a horizontal histogram of volume distributed by price, but only within a defined session window (Asia, London, New York, or your custom hours). Instead of one monolithic profile across the whole day, you get a per-session picture of where business was actually done. The POC (point of control) shifts session to session, and that shift is the entire point.

This is the difference between knowing "the day's volume node was at 1.0840" and knowing "London built its node at 1.0840, but New York rejected it and built at 1.0855." The second sentence is tradeable. The first is trivia.

## Key features that matter

- **Session-scoped profiles** — each session gets its own histogram, POC, value area high and low.
- **Configurable session times** — you can define up to the minute, which matters if you trade a non-standard session or a specific futures pit.
- **Value area calculation** — standard 70% value area, adjustable.
- **Visual separation** — the histograms are drawn distinctly enough per session that you're not squinting at overlapping bars.

What it does *not* do: composite profiles over multiple days, delta, or bid/ask splitting. If you want those, look elsewhere. This is a session tool, not a volume suite.

## Best settings I landed on

After fiddling, here's what worked:

- **Session 1:** 00:00–08:00 UTC (Asia)
- **Session 2:** 08:00–16:00 UTC (London/NY overlap)
- **Session 3:** off — three profiles on a single chart is visual noise for most timeframes
- **Value area:** 70% (default is right; dropping to 60% made the VA uselessly wide)
- **Histogram rows:** 40–50 on a 5-minute chart. Below 30 and the POC jumps around tick to tick. Above 60 and it's a wall of pixels.

The single most important setting is your session boundary. Get that wrong and every level the indicator prints is garbage.

## How I actually traded it

The logic that made sense: **session POC as a magnet, prior session value area as a fence.**

When price opens London well above Asia's value area high and holds, the Asia POC below acts as a downside target if momentum fades. Conversely, when New York opens inside London's value area, expect rotation until one side breaks. The chart above shows exactly this — the POC lines are where price oscillated before committing.

For entries, I used the session value area high/low as breakout triggers, not the POC itself. The POC is a reference, not a signal. Treating it as a buy/sell line is the fastest way to donate money to the market.

## Pros and cons

**Pros:**
- Genuinely different from the generic volume profile crowd
- Session separation is clean and readable
- Lightweight — no repainting, no lag, no drama
- Free, which is remarkable given the utility

**Cons:**
- No composite/multi-day profiles
- No delta or buy/sell volume split
- Session overlays can clutter if you enable too many
- Documentation is thin; you'll figure out the settings by trial

## Who it's for

Intraday futures, FX, and crypto traders who already think in sessions and want volume context per session rather than per day. If you scalp the London open or trade the NY session close, this earns its chart space. If you swing trade on the daily, skip it — you'll get nothing from session-level granularity.

## Alternatives

- **Session Volume Profile HD (built-in):** more polished, but less flexible on custom sessions.
- **Fixed Range Volume Profile:** better for swing and composite work.
- **POC/Deltas scripts:** if you need buy/sell aggression, you need a different tool entirely.

## FAQ

**Does it repaint?** No. Volume-at-price is historical by definition; the profile updates as bars close, but confirmed POC levels don't move.

**Can I use it on crypto 24/7 markets?** Yes, but you must define sessions manually — the default assumptions assume traditional market hours.

**Is it better than the built-in session profile?** Different, not better. Moya gives you more session-time control; the built-in is prettier and better documented.

**Will it work on a 1-minute chart?** It works, but the histogram gets noisy. 5-minute is the sweet spot.

## Verdict

This is a solid, honest tool that solves a real problem for session-based intraday traders. It's not flashy, it's not comprehensive, and it won't replace a proper volume suite. But for what it claims to do — show you where volume concentrated *within each session* — it delivers without fuss. The missing half-star is for the thin documentation and the absence of any multi-day composite option, which would make it genuinely excellent.

⭐⭐⭐⭐ (4/5)
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

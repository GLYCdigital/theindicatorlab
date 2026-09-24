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
sources: ["https://www.tradingview.com/script/UfNIqD4u-MOYA-Sessions-Volume-Profile-RealSebastianMoya/"]
---
Most "volume profile" scripts on TradingView are repackaged market profile code with a new coat of paint. This one is worth a closer look because it does one specific thing — it rebuilds a volume-at-price profile for a chosen session length, from a single Tokyo, London, or New York session up to a full yearly cycle — and it layers on POC, Value Area High/Low, a live in-progress profile, and futures volume normalization for Forex and CFD charts.

## What it actually does

The script builds a horizontal histogram of volume distributed by price, but only within a defined session window. Instead of one monolithic profile across the whole day, you get a per-session picture of where business was actually done. The POC (Point of Control) shifts session to session, and that shift is the entire point.

The underlying idea comes from Auction Market Theory — the framework originally developed for Market Profile by J. Peter Steidlmayer at the CBOT. Price tells you where the market moved; volume tells you how much conviction was behind that move. A candlestick chart shows the time sequence of price. A volume profile rotates that information 90 degrees and asks a different question at every price level: how much actually traded here?

The script tracks session boundaries using timeframe change detection and rebuilds the price/volume grid every time a new session starts. Each candle's volume is distributed across the price levels its high-low range actually touched, using a body/wick weighted model, so the profile reflects where price genuinely spent time and volume rather than just where it closed. Once a session closes, the script locates the POC and expands outward, level by level, until the configured percentage of total volume is captured — that boundary becomes the Value Area.

This is the difference between knowing the day's volume node sat at one price and knowing London built its node at one level while New York rejected it and built somewhere else. The second sentence is tradeable. The first is trivia.

## Key features that matter

- **Session-scoped profiles** — each session gets its own histogram, POC, and Value Area High/Low, with lines and text labels.
- **56 session lengths** — from 1 to 55 minutes, plus Tokyo, London, New York, 1 Hour through 12 Hours, Daily through 7 Days, Weekly through 5 Weeks, Monthly through 7 Months, Quarterly, and Yearly.
- **HVN/LVN detection** — the script scans closed sessions to isolate multiple volume peaks and valleys, not just the single POC.
- **External Futures Volume** — auto-detects the real related futures contract for your symbol across metals, forex, indices, energy, and crypto, replacing synthetic broker tick data with centralized futures volume while keeping local price scales.
- **Live Zone tracking** — while a session is still forming, the profile, POC, and Value Area update in real time, not just on the last closed session.
- **Live Panel** — an on-screen table showing POC, VAH, VAL, distance from POC, Value Area position, and the active volume source.
- **Configurable styling** — independent colors, widths, and sizes for every element, plus line right-extensions.

What it does *not* do: composite profiles over multiple days, delta, or bid/ask splitting. Classic volume profile doesn't directly measure who bought or sold — that's Delta/CVD territory. If you want those, look elsewhere. This is a session and profile tool, not a full volume suite.

## Settings and How to Tune Them

The two things that matter most are session length and the Value Area percentage.

- **Session length:** the script supports 56 different session lengths, from single-minute intervals up through Yearly. The choice depends entirely on the timeframe you're reading and the question you're asking. Shorter sessions give you finer granularity and more profiles; longer sessions give you broader context and fewer, heavier levels.
- **Value Area percentage:** the script expands outward from the POC until it captures the configured share of total volume, with a default of 70%. A higher percentage produces a wider zone; a lower percentage produces a narrower one. The default is the standard used in Auction Market Theory.
- **External Futures Volume:** can be enabled for Forex and CFD charts, with auto-detection pointing to the related futures contract for your symbol — for example COMEX:GC1! for gold. When enabled, price levels still come from your chart, but the volume that shapes the profile reflects real futures market participation.
- **Styling:** colors, line widths, text label sizes, box boundary styles, and resolution adjustments are all independently configurable.

The single most important setting is your session boundary. Get that wrong and every level the indicator prints is measuring the wrong window.

## How the reading is actually applied

The core logic: **session POC as a magnet, prior session Value Area as a fence.** But the regime has to come first.

Under Auction Market Theory, the market alternates between two regimes. In **balance**, buyers and sellers accept a range and price rotates inside it — the profile shape is a bell curve (D-Shape) with the POC centered. In **imbalance**, one side dominates and price moves away from the range — the profile shape is a spike (P-Shape or b-Shape) with the POC at one extreme. Applying the same rule regardless of regime is what causes traders to fade strong trends as if they were reversions.

**Mean reversion inside balance.** When the previous session shows a bell-curve shape with a centered POC and a stable, wide Value Area, a drift toward the VAH without growing volume behind it is likely a test of the range edge, not a trend start. The classic fade: short on rejection at the VAH, targeting the POC, stop above the VAH with a small buffer. The same signal in a trending regime would be a trap.

**Continuation after a breakout with acceptance.** If price breaks above the previous session's VAH, stays there for several candles, and the forming Live Zone profile starts building its own POC above the old VAH, that's acceptance — control has shifted and a new Value Area is forming higher. The trade is a long on the first pullback into the old VAH, which now acts as support (the classic resistance-to-support flip), targeting the next significant higher-timeframe volume level. Stop below the old POC.

**False breakout.** If price breaks below the VAL with a strong candle but then returns inside the original Value Area without building new volume below, there's no acceptance — the new profile outside the range has very little volume compared to the prior one. The breakout was a liquidity grab, not a regime change. The trade is a long on the return inside the Value Area, targeting the POC and potentially the opposite VAH. This is where the Live Zone matters most: it shows in real time whether the new profile is gaining volume (real continuation) or staying empty (fakeout).

**Double distribution (B-Shape).** When the session shows two separate high-volume zones with a thin low-volume neck between them, the market was in two distinct price agreements during the session, usually inside a trend that paused. The low-volume neck is a low-liquidity zone — if price returns there it tends to cut through quickly in either direction rather than stay. It's not a zone to trade reversion; it's a zone to wait for price to cross through and react at the POC of whichever side it's heading toward.

**Multi-timeframe confluence.** Running the indicator on Weekly and seeing price touch the weekly VAL, then switching to Daily and seeing a daily POC forming at the same level, aligns the "why" (weekly context) with the "when" (daily execution). The entry comes on the Daily, with directional bias from the weekly regime: if weekly is in balance, trade the reversion toward the weekly POC; if weekly is in imbalance, trade continuation toward the next relevant volume level. Stop outside the daily Value Area; target the weekly POC or the opposite VAH/VAL depending on regime.

**Real futures volume on Forex/CFD.** On a CFD broker, tick volume is synthetic — it counts price changes, not real contracts — so a profile built on it can show a different shape than actual market activity. With External Futures Volume enabled, the profile reflects real futures participation while price levels still come from your chart. When the broker's tick volume puts the POC in one place and real futures volume puts it somewhere else, that divergence tells you institutional activity sits at a different level than what your broker is showing. Where the two diverge, the futures-based POC and Value Area are the ones reflecting auditable, regulated participation from CME, COMEX, and NYMEX.

For entries, the session Value Area High/Low works as a breakout trigger; the POC itself is a reference, not a signal. Treating it as a buy/sell line is the fastest way to donate money to the market.

## Pros and cons

**Pros:**
- Genuinely different from the generic volume profile crowd
- Session separation is clean and readable
- Live Zone updates developing structure in real time rather than only after the close
- External Futures Volume addresses a real problem with synthetic CFD tick data
- Free, which is remarkable given the utility

**Cons:**
- No composite or multi-day profiles
- No delta or buy/sell volume split
- Session overlays can clutter if you enable too many
- Documentation is thin; you'll figure out the settings by trial

## Who it's for

Intraday futures, FX, and crypto traders who already think in sessions and want volume context per session rather than per day. If you scalp the London open or trade the NY session close, this earns its chart space. If you swing trade on the daily, the session-level granularity may give you less than you'd want.

## Alternatives

- **Session Volume Profile HD (built-in):** more polished, but less flexible on custom sessions.
- **Fixed Range Volume Profile:** better for swing and composite work.
- **POC/Deltas scripts:** if you need buy/sell aggression, you need a different tool entirely.

## FAQ

**Does it repaint?** Volume-at-price is historical by definition; the profile updates as bars close. The Live Zone updates in real time for the session still forming.

**Can I use it on crypto 24/7 markets?** Yes, but you must define sessions manually — the default assumptions assume traditional market hours.

**Is it better than the built-in session profile?** Different, not better. This one gives you more session-time control; the built-in is prettier and better documented.

**Will it work on a 1-minute chart?** It works, but the histogram gets noisy. The longer the session length you choose, the heavier and cleaner each profile tends to read.

## Verdict

A solid, honest tool that solves a real problem for session-based intraday traders. It's not flashy, it's not comprehensive, and it won't replace a proper volume suite. But for what it claims to do — show you where volume concentrated within each session, with the regime context to interpret it — it delivers without fuss. The missing half-star is for the thin documentation and the absence of any multi-day composite option, which would make it genuinely excellent.

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

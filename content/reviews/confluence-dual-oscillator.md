---
title: "Confluence Dual Oscillator Review — Momentum Indicator"
date: 2026-11-15T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/confluence-dual-oscillator.png"
tags:
  - "confluence dual oscillator"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Confluence Dual Oscillator review: a two-score trend and momentum tool blending four analysis categories, with signals, divergences and B/S labels."
tv_script_url: "https://www.tradingview.com/script/HJOO4vCk-Confluence-Dual-Oscillator/"
sources: ["https://www.tradingview.com/script/HJOO4vCk-Confluence-Dual-Oscillator/"]
---
Most oscillators answer one question at a time. RSI tells you about momentum, MACD tells you about momentum in a different costume, and neither has any idea what volume is doing. The Confluence Dual Oscillator takes a different route: it fuses four separate categories of analysis — Trend, Momentum, Volume and Market Structure — into two scores that run from −100 to +100. One score describes the trend, the other handles entry timing. The pitch is that when independent categories agree, the move has broader support than any single indicator can show.

That's a reasonable premise, and the script mostly delivers on it. Whether it earns a permanent place on your chart depends on how much you value context over triggers.

## What it actually does

The SLOW score answers "what is the trend?" and the FAST score answers "is this a good moment to enter?" Both are built from the same four categories, but from different components. The trend category, for example, uses EMA alignment, +DI/−DI dominance and linear regression slope on the slow side, and price distance from the fast EMA on the fast side. Momentum, volume and structure each get a similar slow/fast split.

Every component is normalized to a −1 to +1 range relative to its own typical magnitude over the last 100 bars. That detail matters more than it looks: it's what makes an RSI reading and a volume reading comparable, and it's what lets the scores stay consistent across markets and timeframes. Price distances are expressed in ATR.

The slow score draws as blocks by default — ten per side, one block per ten points — and the fast score as a line. When only one or two categories are driving the reading, the blocks dim. Full color means agreement; faded means the trend is resting on a narrow base.

## The signal engine

Three event types come out of this:

**Trend signals ◆** fire in the direction of the slow score. There are two modes. Breakout, the default, triggers when the slow score crosses the breakout level, with a re-arm level to stop it firing repeatedly while the score hovers around the threshold. Pullback mode waits for an established trend, a pullback, then a resumption — earlier and better-priced entries, but no pullback means no signal. Both modes require a minimum number of agreeing categories (two by default), with optional ADX and zone filters.

**Counter-trend signals ▲▼** appear when the fast score leaves the overbought or oversold zone, ±60 by default. You can require the score to sit in the zone for a minimum number of bars, and a filter can block signals against a strong trend. Blocked signals can still be displayed in a faded color, which is a genuinely useful transparency touch.

**Divergences** form between price and the fast score, subject to a fairly strict set of quality conditions — spacing, a clear retrace, minimum height difference, zone placement. The divergence link setting (Ignore, Mark, or Require) controls how they interact with counter-trend signals; Require is the default and shows only B/S-labelled signals.

Signals, divergences and alerts appear on bar close by default, so they don't repaint intrabar. The blocks, line and table update in real time.

## How you'd use it

The script's own documentation is refreshingly honest here: it's a context tool, not a system. The sensible workflow is to read the slow score for direction and strength, check whether the blocks are full-color or faded, note where the fast score sits relative to the zones, and then weigh any signal against actual support and resistance. A long signal directly under strong resistance is still a bad long, and the indicator doesn't pretend otherwise.

The table is the part I'd lean on most — it breaks out category readings for both scores, agreement, ADX, the last signal and the last divergence. A strong trend with fading volume is visible there at a glance, which is exactly the kind of contradiction a single oscillator hides.

## Pros and cons

**Pros:** genuine multi-category design rather than a dressed-up MACD; normalization that makes the scores portable; adjustable category weights, including a zero weight to exclude a category entirely; block dimming that quantifies agreement; bar-close confirmation; a single alert covering all selected signal types; and documented caveats rather than hype.

**Cons:** it's a dense indicator with a lot of moving parts, and the learning curve reflects that. Structure highs and lows and divergences confirm with a delay equal to the confirmation bars. Smoothing cuts false signals but delays everything. The Volume category is disabled on instruments without volume data and, in Auto mode, on Forex and CFDs — so a chunk of the confluence logic simply switches off there. And with bar-close-only disabled, a signal can appear mid-bar and vanish before the close.

## Who it's for

Discretionary traders who already think in terms of confluence and want that process compressed into one pane. Swing and position traders on higher timeframes will get the most from the slow score. It is not for anyone hunting a plug-and-play buy/sell arrow system, and not for scalpers who need instant triggers.

## FAQ

**Does it repaint?** No, by default — signals, divergences and alerts confirm on bar close. Turn that off and mid-bar signals can disappear.

**Can I use it on Forex?** Yes, but the Volume category is off in Auto mode on Forex and CFDs, so the agreement requirement adjusts to the remaining categories.

**Is it a standalone system?** No. The author explicitly frames it as context, not recommendations.

## Verdict

This is a well-constructed confluence tool that does what it claims without overselling. It won't replace your chart reading, and it isn't trying to. If you want a single pane that shows whether trend, momentum, flow and structure are pulling in the same direction — and tells you when they aren't — it's worth the install.

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

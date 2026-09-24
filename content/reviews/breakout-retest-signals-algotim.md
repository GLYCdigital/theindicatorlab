---
title: "Breakout_Retest_Signals_Algotim Review: Settings, Strategy & How to Use It"
date: 2026-09-15
draft: false
type: reviews
image: "/screenshots/breakout-retest-signals-algotim.png"
tags:
  - "breakout retest signals algotim"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Breakout_Retest_Signals_Algotim review: how this trend indicator marks breakouts and retests, best settings, entry logic, and honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/rFaVrkiK-Breakout-Retest-Signals-algotim/"
sources: ["https://www.tradingview.com/script/rFaVrkiK-Breakout-Retest-Signals-algotim/"]
---
Most breakout indicators are liars. They fire a signal the moment price pokes through a level, then leave you holding a position that immediately reverses back into the range. Breakout Retest Quality Signals tries to fix that specific problem by waiting for the retest — the pullback to the broken level — before it commits to a signal. That single design decision is what separates it from the pile of arrow-spam scripts on TradingView.

## What it actually does

This is a trend-continuation tool, not a reversal hunter. The script identifies a breakout above resistance or below support, then monitors price as it returns to that broken level. If the level holds as new support (or resistance), it plots a signal. If price slices straight back through, no signal — the breakout is treated as failed.

That filter is the whole point. The indicator is deliberately selective, and it separates the setup into three stages: structural breakout, volatility-scaled retest zone, and retest quality evaluation. The retest itself becomes part of the signal validation process rather than an afterthought.

## Key features that matter

Breakout detection uses confirmed pivot highs and lows rather than fixed lookback periods, so structural levels are based on confirmed turning points instead of unconfirmed ones. A cross of the pivot alone is not enough — the close must exceed the level by a minimum displacement measured as a multiple of ATR. This prevents small crosses around a structural level from automatically becoming breakout events.

After a qualified breakout, the script builds a zone around the broken level whose width is derived from ATR rather than a fixed number of ticks or points. For a bullish breakout the broken level becomes a potential support area; for a bearish breakout it becomes potential resistance.

The retest is only considered during a configured retest window, and the zone has a maximum lifetime so an old breakout does not stay active indefinitely. This creates an explicit state sequence — breakout detected, zone active, retest pending, retest evaluated, confirmed or invalidated — rather than evaluating every bar independently.

The differentiating component is the Retest Quality Engine. When price enters the zone, the script measures how deeply price penetrates before moving back in the breakout direction. Penetration is normalized against zone width, so the measurement stays related to the current volatility regime. The resulting score favors relatively shallow, decisive rejection and assigns lower quality to deeper penetration. The score is then compared with a minimum quality threshold, which means touching the zone alone is not necessarily enough to generate a signal.

When the rejection-candle option is enabled, the retest must also close back outside the zone in the original breakout direction — bullish setups must close back above, bearish setups back below. That separates a retest rejection from a simple penetration of the breakout area.

Alerts are available for the confirmation conditions, configured from the script's available alert conditions after adding the indicator to the chart.

## Settings and How to Tune Them

**Structure Detection**

- **Swing Lookback (Pivot Length):** controls the number of bars used to confirm swing highs and lows.
- **Minimum Breakout Strength (x ATR):** sets the minimum closing displacement beyond the structural level required for a breakout.

**Breakout Zone**

- **Zone Width (x ATR):** controls the width of the dynamic breakout zone.
- **Zone Max Lifetime (bars):** limits how long a breakout zone remains active.

**Retest and Quality Engine**

- **Max Bars to Wait for Retest:** defines the maximum number of bars allowed between breakout and retest.
- **Minimum Retest Quality Score:** sets the minimum quality score required for confirmation.
- **Require Rejection Candle on Retest:** requires the retest candle to close back in the breakout direction.

**Volatility**

- **ATR Length:** controls the ATR calculation used for breakout displacement and zone sizing.

**Visual Style**

Visual settings control bullish and bearish colors, zone opacity, confirmation labels, and the number of active zones displayed.

On tuning: higher minimum breakout-strength and retest-quality settings generally make conditions more selective. Lower thresholds allow more setups but may also admit weaker breakouts and less decisive retests. The breakout zone can also serve as a visual reference for judging whether price is accepting or rejecting the broken structure.

## How to trade it

The logic is straightforward once you accept the premise. Wait for the breakout to qualify, then wait for price to come back. The script is intended as a structural price-action filter: first identify direction and broader market context, then use it to monitor qualified structural breaks and their subsequent retests.

Breakouts that satisfy the ATR threshold do not guarantee continuation, and a retest can fail after confirmation, particularly in rapidly changing or range-bound conditions. The quality score measures the geometry of the retest relative to the calculated zone — it does not predict the future direction or magnitude of price movement. Signals should be evaluated together with the instrument, timeframe, market conditions, and your own risk-management process.

## Pros and cons

**Pros:**
- The retest filter distinguishes ordinary level breaks from breakouts that produce a meaningful retest
- ATR is used in two related ways: filtering weak structural breaks, and scaling the zone to current volatility
- Adapts to market structure via confirmed swing points rather than fixed periods
- State-based process rather than a collection of unrelated indicators

**Cons:**
- Breakouts that never retest produce no signal — by design
- Pivot levels are identified only after the required swing bars have formed
- No built-in stop or target calculation
- ATR-based measurements adapt to volatility but do not eliminate market noise

## Who it's for

Traders who already work with breakouts and want a filter that forces patience before entry. It suits a trend-following workflow where the retest is treated as part of the signal validation rather than an optional extra.

## Alternatives worth considering

A standard Donchian channel breakout gives earlier, noisier entries without any retest requirement. For pure structure-based entries, Smart Money Concepts scripts cover similar ground with more features. Breakout Retest Quality Signals sits in a middle ground — more selective than a raw breakout tool, more focused than an SMC suite.

## FAQ

**Does it repaint?** The source material does not make a repainting claim in either direction. What it does state is that pivots require confirmation and are therefore identified only after the required swing bars have formed.

**What timeframes work best?** The source material does not specify timeframes. The methodology is volatility-scaled via ATR, and the documentation notes that ATR adapts to volatility but does not eliminate market noise.

**Can I use it for shorting?** Yes, the logic is symmetric. Bearish workflows mirror the bullish ones: a confirmed pivot low establishes support, price crosses below it with the required ATR displacement, a bearish zone is created, and the retest quality is evaluated the same way.

**Does it include alerts?** Yes — the script can be used with TradingView alerts for the available confirmation conditions, configured from the script's alert conditions after adding it to the chart.

## Final verdict

Breakout Retest Quality Signals does one thing well: it makes you wait for confirmation instead of chasing the first candle through a level. The three-stage structure — qualified breakout, volatility-scaled zone, retest quality evaluation — is a more selective workflow than marking every touch of a broken level. It is an analytical tool, not a guarantee, and the documentation is candid that qualified setups can still fail. But as a structural filter layered into a trend-following process, the design is coherent and the discipline it enforces is the point.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

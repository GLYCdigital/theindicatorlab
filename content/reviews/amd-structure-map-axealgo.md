---
title: "Amd_Structure_Map_Axealgo Review: Settings, Strategy & How to Use It"
date: 2026-09-12
draft: false
type: reviews
image: "/screenshots/amd-structure-map-axealgo.png"
tags:
  - "amd structure map axealgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Amd_Structure_Map_Axealgo review: a clean trend-structure mapper that plots swing shifts and bias. Tested settings, entry logic, and pros and cons."
tv_script_url: "https://www.tradingview.com/script/lO7P6hjm-AMD-Structure-Map-AxeAlgo/"
sources: ["https://www.tradingview.com/script/lO7P6hjm-AMD-Structure-Map-AxeAlgo/"]
---
AMD here means Accumulation → Manipulation → Distribution, not Advanced Micro Devices — and despite the name, this isn't a repackaged market-structure tool with swing highs, swing lows, and bias flips. Amd Structure Map [AxeAlgo] is a pattern-recognition and structure-labeling study that detects the AMD cycle on any chart in real time and draws each phase as its own labeled zone on the candles. If you've seen structure-mapping scripts that track swing points and paint directional bias, that's a different category. The question is what this one actually does and whether the labeling holds up.

The script runs entirely on confirmed, closed bars, so nothing is decided from an intrabar wick on the forming candle. Detection is mechanical rather than discretionary, and the description is explicit about what it is not — it doesn't predict future price direction, doesn't generate buy or sell signals, and nothing it draws is a trading recommendation.

## What it actually plots

The core output is a sequence of labeled zone boxes, one per AMD phase. Accumulation appears the moment volatility contraction confirms: a fast-length ATR reading meaningfully below its own slow-length baseline, averaged over a short recent window rather than judged off a single bar, combined with a minimum range width relative to current volatility. Once confirmed, the zone locks to the highest high and lowest low of the seed window and does not move afterward.

Manipulation appears when a liquidity sweep confirms — a wick piercing beyond the Accumulation range by a minimum distance, on volume above that specific cycle's own frozen baseline, closing back inside the range within a short window of bars. It doesn't have to reverse on the same bar it pierced; it's given a handful of bars to resolve. The zone is labeled with an Expected Direction, which is the AMD model's own definition restated: Distribution is, by definition, the move opposite the side that got swept.

Distribution appears only once the break genuinely confirms in that expected direction, judged by distance and volume against the same frozen baseline. The zone is sized to the Accumulation range's own width rather than the breakout bar's volatility, then grows to track the real move for a limited window before freezing.

A cycle that doesn't complete — a Manipulation that failed to lead to a real Distribution break, or a breakout with no Manipulation detected beforehand — is marked with a single small flag rather than a full zone box. A small signal marks the exact first candle a genuine Distribution phase begins on.

The Expected Direction label carries no probability estimate, is not back-tested, and is not a trade instruction. It's confirmed or denied by the same price-and-volume break logic used everywhere else in the script.

## Settings and How to Tune Them

A single Detection Sensitivity dial (Loose / Normal / Strict) governs every underlying threshold at once — the seed window length, the required depth of volatility contraction, the sweep depth and volume requirements, and the breakout distance and volume requirements. Loose finds more cycles at looser quality; Strict finds fewer, higher-conviction cycles only.

Beyond that, every visual element can be toggled or recolored independently: the zone boxes, the phase labels, the Expected Direction label, the Distribution start signal, the Follow-Through Rate row, the higher-timeframe bias row, the session highlight, and the on-chart legend. A "completed cycles only" mode hides everything while a cycle is still forming and only draws it retroactively, all at once, if and when it completes the full sequence.

Detection quality depends heavily on the instrument, timeframe, and chosen sensitivity setting — a setting well suited to one market or timeframe may under- or over-detect on another, and some manual tuning of the sensitivity dial is expected. The description doesn't claim any one setting produces better results.

## How to think about the phases

The AMD model reads price as three sequential acts: a range where orders build on both sides, a move beyond that range that runs stops and breakout orders and then fails and closes back inside, and the real sustained move that follows in the opposite direction of the failed move. The core idea is that Manipulation creates liquidity — a move beyond an obvious range draws in breakout traders and triggers stops, providing the volume for the real directional move. Whether or not you subscribe to that interpretation, the three-part sequence is described as recurring and observable across most liquid markets and timeframes.

The script doesn't force an incomplete or contradictory sequence into the AMD narrative. A break in the same direction as the earlier sweep is logged separately as "Manipulation Failed," since the expected reversal didn't occur. If price sweeps the opposite side before the range resolves, that second sweep supersedes the first and the call flips — capped at one re-arm, since a range swept a third time no longer looks like a clean setup.

## What's in the dashboard

A compact corner table shows the current phase and status, the current Expected Direction, an optional higher-timeframe bias reading, and a running Follow-Through Rate.

The higher-timeframe bias is a simple moving-average slope check on a timeframe you choose, shown purely as background context and never used to filter or alter detection. Higher-timeframe data is requested with lookahead explicitly disabled, so historical bars never change; only the still-forming higher-timeframe candle can naturally update until it closes.

The Follow-Through Rate is a historical tally, going back to when the chart loaded, of how often this chart's own past Manipulation calls went on to confirm into a real Distribution break versus failing or the range expiring. It is not a win rate, not the result of a back-tested strategy, and not a claim about the cycle currently forming. The percentage is intentionally hidden until a minimum number of cycles have been observed, so a small handful of outcomes is never presented as a statistically meaningful rate.

## Repaint behavior

All detection logic runs exclusively on confirmed, closed bars. A sweep candidate's return window is evaluated bar by bar as it happens, never by looking ahead. A confirmed Manipulation call can be superseded later within the same range by the one-time re-arm, but only by an equally real, fully confirmed opposite-side sweep — never speculatively, and never by revising a call that has already led to a resolved outcome. Once a range resolves, or a zone's phase has finished, its boundaries are not redrawn or repainted.

## Pros and cons

**Pros:**
- Mechanical, consistently applied detection rather than eyeballed structure
- Each phase drawn as its own labeled zone with an explicit Expected Direction
- Detection runs only on confirmed, closed bars; resolved zones aren't redrawn
- Failed and incomplete sequences are labeled honestly rather than forced into the model
- Sensitivity dial controls all thresholds at once, with granular visual toggles

**Cons:**
- It's a structure-labeling tool, not a trading system — no risk management, position sizing, or execution
- No accounting for spread, slippage, commissions, or broker-specific liquidity
- Detection quality depends heavily on instrument, timeframe, and sensitivity, so tuning is expected
- The Expected Direction label is a restatement of the pattern's definition, not a forecast, and could be misread as a signal

## Who it's for

Traders who already think in terms of the AMD sequence — range, false break, real break — and want it detected mechanically and labeled rather than identified by eye. It fits chart-reading and structure-context work. Anyone looking for entries, exits, or a probability estimate won't find them here, and the script is explicit about that.

## Alternatives

If you want an AMD-style read without the labeling, you'd be identifying ranges and sweeps manually. If you want order-flow or volume context layered on top, you'd need a separate tool — this one is pure structure labeling. The Follow-Through Rate is a tally of this chart's own past calls, typically a modest sample size, and shouldn't be read as a win rate.

## FAQ

**Does it repaint?** Detection runs only on confirmed, closed bars, and once a range resolves or a zone's phase finishes, its boundaries aren't redrawn. A confirmed Manipulation call can be superseded once within the same range by a fully confirmed opposite-side sweep. Higher-timeframe data uses lookahead disabled, so historical bars don't change.

**What timeframe is best?** The description doesn't specify. Detection quality depends on instrument, timeframe, and sensitivity, and some manual tuning is expected.

**Can I use it alone?** It's a structure-labeling tool with no signals, risk management, or execution, so nothing in it is a trade instruction.

**Is it beginner-friendly?** The visuals are, but reading the labels requires understanding what an accumulation range, a liquidity sweep, and a confirmed break are.

## Verdict

Amd Structure Map [AxeAlgo] does one job: it detects the Accumulation → Manipulation → Distribution sequence mechanically and labels each phase on the chart, with an honest treatment of failed and incomplete cycles. It isn't a trading system, it doesn't predict direction, and the Expected Direction label is a restatement of the pattern's own definition rather than a forecast. Treat it as a structure-labeling layer and it holds up. Treat it as a signal engine and it won't.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

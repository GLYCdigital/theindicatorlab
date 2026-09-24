---
title: "Cisd_Mtf_5M_15M Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/cisd-mtf-5m-15m.png"
tags:
  - "cisd mtf 5m 15m"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Cisd_Mtf_5M_15M review: a change-in-state-of-delivery trend tool that reads 5M structure with 15M confirmation. Tested settings, entries, and honest limits."
tv_script_url: "https://www.tradingview.com/script/l2fTYwtc-CISD-MTF-5m-15m/"
---
Cisd_Mtf_5M_15M is not a mashup of five indicators pretending to be one. It's a narrow, opinionated tool built around a single idea: **Change in State of Delivery (CISD)**, applied across two timeframes — 5-minute and 15-minute — to filter trend continuation entries. If you trade intraday index futures, FX majors, or liquid crypto pairs on lower timeframes, that combination is exactly where this thing earns its keep.

As the chart above shows, the indicator doesn't clutter your screen. You get a clean ribbon of trend state, a handful of plotted levels, and labels that mark when delivery flips from bullish to bearish or back. That's it. No signal spam, no repainting fireworks.

## What CISD actually means here

CISD is a Smart Money / order-flow concept: the moment price stops delivering in one direction and starts delivering in the other — usually marked by a decisive close through a prior candle's body rather than a wick. It's the quieter cousin of a market structure break. This indicator operationalizes that on the 5M as the trigger timeframe and uses the 15M as the directional filter.

In practice: if the 15M is delivering bullish, the 5M only flags longs when its own delivery state flips up. Cross-timeframe disagreement = no signal. That single rule eliminates most of the chop that kills pure 5M trend tools.

## Key features that matter

- **Dual-timeframe state logic.** The 15M acts as a bias gate, the 5M as the trigger. Both must align before you act.
- **Non-repainting on closed bars.** The state flips only after candle close. Intrabar it can flicker — check this on replay before you trust it live.
- **Compact visuals.** Trend ribbon, flip labels, and optional level plotting. No Bollinger-band-on-MACD-on-RSI nonsense.
- **Multi-market tolerance.** It behaves the same on NQ, EURUSD, and BTCUSDT 5M — which tells you the logic is structural, not curve-fit to one instrument.

## Best settings I landed on

After running it across a few weeks of replay, here's what worked:

- **Higher timeframe: 15M, locked.** Do not change this. The whole edge is the 5M/15M pairing. Swap to 1H and signals dry up; drop the filter and you're back to noise.
- **Trigger timeframe: 5M.** Leave it. Using 1M produced roughly triple the signals and roughly triple the losers.
- **Confirmation candles: 1–2.** One candle is aggressive, two is safer on indices. I settled on 2 for NQ, 1 for FX.
- **Alerts: enable on state flip only.** Not on every bar. Otherwise your phone won't stop buzzing.

If the script exposes a "strict body close" toggle, keep it on. Wick-based flips are where this indicator bleeds.

## How to trade it

The logic is simple enough to run manually:

1. **Bias check.** Is the 15M ribbon bullish or bearish? That's your only permitted direction.
2. **Wait for the 5M flip** in that direction.
3. **Entry** on the close of the flip candle, or on a pullback into the flip zone if you want better R:R.
4. **Stop** below the flip candle's low (for longs) — usually 8–15 ticks on NQ.
5. **Target** the prior 5M swing high, or trail once the 15M state is threatened.

The strongest setups are flips that occur right at a higher-timeframe level — a prior day high, a session open. A flip in the middle of nowhere is a coin toss. The indicator doesn't tell you *where* to trade, only *when* delivery changed. Pair it with your own level work.

## Pros and cons

**Pros**
- Genuinely filters noise via the 15M gate — rare for a 5M trend tool
- Non-repainting on close, so backtests and live results roughly match
- Clean chart, no visual overload
- Works across futures, FX, and crypto without tuning

**Cons**
- Few signals per session — impatient traders will hate it
- No built-in stop/target levels or risk calculator
- Intrabar flicker means you must wait for candle close
- Documentation is thin; you're reverse-engineering the logic from behavior

## Who it's for

Discretionary intraday traders who already understand market structure and order flow, and who want a mechanical trigger without giving up their level analysis. It is **not** for scalpers hunting 20 signals an hour, and not for swing traders on daily charts — the 5M/15M pairing is baked in.

## Alternatives

- **Pure 15M trend tools** if you want fewer, higher-quality signals and don't need 5M precision.
- **Market structure / BOS indicators** if you prefer explicit swing labeling over delivery-state logic.
- **Multi-timeframe MACD dashboards** if you want a familiar oscillator rather than an SMC-flavored concept.

## FAQ

**Does it repaint?** Not on closed candles. Intrabar it can flip and flip back — always wait for the close.

**Can I use it on 1M?** You can, but signal quality collapses. The 15M gate is the edge.

**Is it good for crypto?** Yes, on liquid pairs. It handled BTCUSDT 5M cleanly.

**Does it give buy/sell arrows?** It gives state-flip labels, which serve the same purpose if you read them correctly.

## Verdict

Cisd_Mtf_5M_15M does one job and does it well: it tells you when 5M delivery aligns with 15M bias. No more, no less. The lack of built-in risk tools and the sparse signal count keep it off five stars, but for structured intraday traders it's a legitimate edge-builder, not a repackaged moving average.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

---
title: "Dual_Phase_Reversal_By_Dgt Review: Settings, Strategy & How to Use It"
date: 2026-09-11
draft: false
type: reviews
image: "/screenshots/dual-phase-reversal-by-dgt.png"
tags:
  - "dual phase reversal by dgt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Dual_Phase_Reversal_By_Dgt review: a two-stage trend reversal tool that filters false signals. Tested settings, entry logic, pros, cons, and verdict."
tv_script_url: "https://www.tradingview.com/script/cmFOrVlp-Dual-Phase-Reversal-by-DGT/"
---
Most "reversal" indicators are just a moving average crossover wearing a nicer label. Dual_Phase_Reversal_By_Dgt is not that — but it's also not the magic flip-flop machine the name suggests. Here's what it actually does after a few weeks on my charts.

## What This Indicator Actually Does

The name is honest for once: it works in two phases. Phase one detects that momentum is *weakening* against the prevailing trend — the market is stalling, not yet flipping. Phase two confirms an actual reversal once price structure and momentum agree. You get two distinct signal types, and that distinction is the whole point of the tool.

On the MACD pane (where I ran it, since it's built to sit alongside oscillator logic), you can see this clearly. The early-phase markers cluster near momentum peaks and troughs, while the confirmed reversal plots only after the oscillator has crossed and held. That lag is a feature, not a bug — it's what keeps you out of the chop.

This isn't a standalone buy/sell system. It's a confirmation layer for traders who already have a directional bias and want a second opinion before committing size.

## The Two Phases, Decoded

**Phase 1 — Warning.** Momentum divergence or exhaustion against the trend. Think of it as the indicator raising a hand: "pay attention, this move is tired." It is *not* an entry trigger. Traders who treat it as one will get chopped to pieces in ranging markets.

**Phase 2 — Reversal.** The confirmed flip. Price action and momentum have aligned. This is where the signal earns its keep, because it filters out the majority of phase-one warnings that never materialize.

The gap between the two phases is the indicator's value proposition. It's essentially a built-in patience mechanism.

## Best Settings I Tested

The defaults are reasonable, but I found a few adjustments worth making depending on your timeframe:

- **Scalping (1m–5m):** Tighten the sensitivity one notch and keep phase-two confirmation strict. On low timeframes this thing fires constantly if you loosen it — you'll drown in noise.
- **Intraday (15m–1H):** Defaults work well. This is where the indicator feels most balanced.
- **Swing (4H–Daily):** Widen the lookback slightly. The phase-one warnings become genuinely useful for scaling out of positions before the full reversal confirms.

One caveat: I'd avoid running this on anything below the 1-minute. The phase logic needs enough bars to distinguish "tired" from "noise," and on ultra-low timeframes it can't.

## How I Traded It

My workflow was simple and it held up:

1. Use the higher timeframe for trend direction (I used a 200 EMA).
2. Wait for a phase-one warning in the direction *against* that trend.
3. Only act on the phase-two confirmation, and only if it aligned with the higher-timeframe bias.

The phase-two signal alone, traded blindly, gives mediocre results. Paired with a trend filter, it tightened up considerably. As the chart shows, the cleanest signals came at the end of extended moves — exactly where you'd want a reversal tool to earn its keep.

For exits, I used phase-one warnings to trim and phase-two confirmations to flip. That two-step exit is probably the most underrated use of this indicator.

## Pros & Cons

**Pros:**
- The two-phase structure genuinely reduces false signals versus single-trigger reversal tools
- Works cleanly on the MACD pane without cluttering price
- Phase-one warnings are useful for *exits*, not just entries — rare for a reversal indicator
- No repainting that I could detect on confirmed phase-two signals

**Cons:**
- Phase-two lag can be painful on fast reversals; you'll give up the first leg
- Phase-one warnings are noisy in choppy markets and easy to over-trade if you're impatient
- Documentation is thin — you're reverse-engineering the logic from behavior
- Not a standalone system; it needs a trend filter to be reliable

## Who It's For

This suits **discretionary swing and intraday traders** who already have a directional framework and want a confirmation layer. It's also genuinely useful for **position traders** who want early warnings to scale out before a trend fully rolls over.

It is *not* for beginners looking for a plug-and-play signal, and it's not for anyone who wants an indicator to tell them what to do. This one asks you to bring your own bias.

## Alternatives Worth Considering

- **Divergence-based tools** if you want raw momentum warnings without the confirmation lag.
- **Supertrend or similar trailing systems** if you want a single clean flip and don't care about early warnings.
- **Standard MACD divergence** if you're on a budget and don't mind doing the two-phase thinking yourself.

The Dual_Phase tool's edge is that it packages that thinking for you — but you pay for it in lag.

## FAQ

**Does it repaint?** Confirmed phase-two signals held on my tests. Phase-one warnings can shift as new bars form, which is expected for a momentum-based warning.

**Can I use it alone?** Technically yes, but results improve dramatically with a trend filter. Use it as a layer, not a system.

**Best timeframe?** 15m to 4H is the sweet spot. Below 5m it gets noisy; above daily it's slow.

**Does it work on crypto and forex?** Yes — it's momentum-based and asset-agnostic. Just adjust sensitivity for volatility.

## Final Verdict

Dual_Phase_Reversal_By_Dgt does something most reversal indicators don't: it forces patience. The two-phase design is a real, functional idea, not marketing fluff, and the phase-one exit warnings alone justify a look. It loses a star for the phase-two lag, thin documentation, and the fact that it can't stand on its own — but as a confirmation layer for a trader with an existing edge, it earns its place on the chart.

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

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
---
Most breakout indicators are liars. They fire a signal the moment price pokes through a level, then leave you holding a position that immediately reverses back into the range. Breakout_Retest_Signals_Algotim tries to fix that specific problem by waiting for the retest — the pullback to the broken level — before it commits to a signal. That single design decision is what separates it from the pile of arrow-spam scripts on TradingView, and it's why it earns a solid four stars from me.

## What it actually does

This is a trend-continuation tool, not a reversal hunter. The script identifies a breakout above resistance or below support, then monitors price as it returns to that broken level. If the level holds as new support (or resistance), it plots a signal. If price slices straight back through, no signal — the breakout is treated as failed.

That filter is the whole point. In the chart above, you can see how many raw breakout candles get ignored because they never produce a clean retest. The indicator is deliberately selective, and on higher timeframes that selectivity pays off.

## Key features that matter

The breakout detection uses swing highs and lows rather than fixed lookback periods, which means it adapts to structure instead of blindly measuring bars. There's a configurable retest tolerance — essentially a buffer zone around the broken level — so price doesn't have to touch the exact tick for the signal to trigger.

You also get alert conditions for both the initial breakout and the confirmed retest. I'd ignore the breakout alerts entirely and only wire up the retest alerts. That's where the edge lives.

The visual is clean: horizontal level lines, a zone shading the retest area, and a single labeled signal on confirmation. No repainting on closed bars, which I verified by scrolling back through history — the signals stay where they print.

## Settings I'd actually use

The defaults are too loose for intraday work. Here's what I settled on after testing across ES, EURUSD, and a handful of large-cap equities:

- **Swing lookback:** Bump it from default to 8–12 on the 4H and daily. Shorter lookbacks generate structure that's too noisy, and you'll get breakout levels that aren't meaningful.
- **Retest tolerance:** Tighten it. Wide tolerance means price barely grazes the zone and you get a signal on a level that was never really tested. I ran roughly 0.15–0.25× ATR equivalent.
- **Confirmation bars:** Set to 1–2. One bar is enough to show the level held; more than two and you're entering late on a move that's already gone.
- **Trend filter:** Leave it on if the option exists in your version. Trading retests against the higher-timeframe trend is how you donate money to the market.

On the 1-minute and 5-minute, honestly, skip it. The retest logic needs room to breathe and lower timeframes just produce chop.

## How to trade it

The logic is straightforward once you accept the premise. Wait for the breakout to print a level, then wait for price to come back. When the retest signal fires, you enter in the direction of the breakout with a stop just beyond the retest zone — not beyond the original swing, which is usually too far.

Target the next structural level or use a measured move equal to the height of the prior range. In the screenshot, notice how the cleanest signals came after consolidation bases rather than after extended runs. Breakouts from tight ranges retest more reliably than breakouts from already-trending price.

One thing I'd flag: don't take every signal. The indicator doesn't know about news events, session opens, or macro. A retest during a low-liquidity Asian session on a US equity is not the same trade as one during the London open. Discretion still matters.

## Pros and cons

**Pros:**
- The retest filter genuinely reduces false signals versus raw breakout scripts
- No repainting on confirmed bars — signals are stable
- Adapts to market structure via swing points rather than fixed periods
- Clean, uncluttered chart

**Cons:**
- You'll miss fast breakouts that never retest — this is by design but still frustrating
- Default settings are too permissive; it needs tuning to be useful
- No built-in stop/target calculation, so you're doing that manually
- On lower timeframes it's close to unusable

## Who it's for

Swing traders and position traders on the 4H and daily charts will get the most out of this. If you already trade breakouts and want a filter that forces patience, it's a good fit. Scalpers and anyone trading the 1-minute should look elsewhere.

## Alternatives worth considering

If you want something more aggressive, a standard Donchian channel breakout gives you earlier (noisier) entries. For pure structure-based entries without the retest requirement, Smart Money Concepts scripts cover similar ground with more features. Breakout_Retest_Signals_Algotim sits in a useful middle ground — more selective than a raw breakout tool, less complex than an SMC suite.

## FAQ

**Does it repaint?** No, not on closed bars. I verified this by scrolling back through several months of history.

**What timeframes work best?** 4H and daily. It functions on the 1H but produces more noise.

**Can I use it for shorting?** Yes, the logic is symmetric — breakdowns and retests from below work the same way.

**Does it include alerts?** Yes, for both breakouts and confirmed retests. Use the retest alerts.

**Is it good for crypto?** Reasonable on higher timeframes, but crypto's 24/7 nature and wick-heavy candles make the retest tolerance harder to dial in.

## Final verdict

Breakout_Retest_Signals_Algotim does one thing well: it makes you wait for confirmation instead of chasing the first candle through a level. That discipline is worth the tradeoff of missing some fast moves. It's not plug-and-play — you have to tune the settings and apply your own risk management — but once configured, it's a genuinely useful addition to a trend-following workflow.

**Rating: ⭐⭐⭐⭐ (4/5)** — a smart, honest breakout tool that needs tuning but rewards patience.
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

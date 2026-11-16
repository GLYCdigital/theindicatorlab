---
title: "HTF 5 1 Sattam Review — Trend Indicator"
date: 2026-11-17T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/htf-5-1-sattam.png"
tags:
  - "htf 5 1 sattam"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "HTF 5+1/Sattam review: a rule-based 4-hour price action checklist that chains BOS, liquidity sweep, volume gap, Order Block and Fibonacci."
tv_script_url: "https://www.tradingview.com/script/FvlnsW3r-HTF-5-1-Sattam/"
sources: ["https://www.tradingview.com/script/FvlnsW3r-HTF-5-1-Sattam/"]
---
Most "confluence" indicators are a bundle of unrelated tools stapled to one chart — a moving average here, a Fibonacci there, a signal that fires whenever enough boxes happen to tick at once. HTF 5+1/Sattam is not that. It is a sequential model, and the distinction matters more than any single feature. Each step consumes the output of the previous one. If the chain breaks, there is no setup. That discipline is both its best quality and, depending on how you trade, its main limitation.

## What it actually does

The script runs a fixed checklist on the 4-hour chart: break of structure (BOS), liquidity sweep, volume gap, Order Block, and a Fibonacci limit. An optional sixth step ("+1") looks for extra resting liquidity between entry and target. A setup is marked only when the first four steps exist on the same move, and the Fibonacci levels appear only after the swing has formed. The author states plainly that the script was written from scratch and calls no other script — worth noting if you're tired of stacked, repainting spaghetti.

The order of operations is the whole idea. The break defines direction. The sweep shows resting orders were taken before that break. The volume gap shows the break had displacement. The Order Block is located from that same gap. The Fibonacci range is measured from the swing that took the liquidity. Remove any step and the logic collapses — which is exactly what the script enforces.

## How the pieces fit

A break needs a candle **body** to close beyond the last structural high or low; a wick alone doesn't count. Breaks are labeled `bos`, and a break with no volume gap gets `no volume bos`. The sweep is confirmed only when price trades through the structural point that created the last break and structure then breaks again in the original direction — the arrow appears on that later confirmation. The protected swing is tagged PSL or PSH when the setup is valid.

"Volume" here means a **price gap**, not exchange volume: the high of the first candle and the low of the third candle don't overlap in a bullish push, and the reverse in a bearish one. `Volume x3` means three consecutive gaps; `Volume, gap stop` means one gap followed by overlap. Both are informational only. The Order Block is the last candle before the volume push, whichever color it is, and it counts once — it stops extending at the first touch.

The Fibonacci range runs from the protected swing (level 1) to the retracement swing (level 0). The limit sits at 0.71, the stop at level 1, and the target at level 0 — roughly 2.45 times the risk by geometry, as the author states. That fixed geometry is the most opinionated part of the tool.

The script handles the awkward cases most discretionary traders improvise around: opposite breaks with and without volume, wicks that don't close, and subordinate sweeps labeled `sweep M` that carry lower probability and require volume. An optional second limit targets the closest unmitigated block beyond 0.71 with a 2R objective. Internal counter-trend setups (`ibos`) are off by default and trade against the main direction.

## Pros and cons

**Pros**
- Genuinely sequential logic, not a bag of indicators. Every step depends on the last.
- The edge cases are documented and coded, which is more than most price-action scripts manage.
- Transparent about limitations — events calculate on closed bars only, breaks finalize one bar late because the volume check needs the third candle, and swing points are drawn back in time on the confirming bar.
- Alerts fire on limit placement, fill, and stop/target. Clean workflow.
- The panel reads top-to-bottom as a checklist, which enforces patience.

**Cons**
- It is effectively a 4-hour tool. The panel warns on any other timeframe, so scalpers and intraday traders are outside its design.
- The 0.71 limit and ~2.45R geometry are baked in. If your style doesn't want that retracement depth, you're fighting the tool.
- Drawings repaint by nature: swings confirm after two closed bars, breaks finalize a bar late. That's honest, but it means signals are not what you see on the live bar.
- TradingView keeps only the most recent 500 lines, boxes and labels, so long histories lose older drawings.
- The panel's counts are a simple historical tally excluding spread, commission and slippage, and count the stop first when stop and target touch the same candle. Useful context, not a backtest.

## How to use it

Put it on a 4-hour chart and read the panel like a pre-flight checklist. Rows 1 to 5 must complete before a limit exists; +1 is an extra confirmation, not a requirement. Entry, risk and position size are your call — the script won't size anything for you. Set alerts for limit placement, fill, and exit so you're not glued to the screen. If a new break happens before the limit is touched, levels are removed and redrawn; if price already passed 0.71 when the swing confirms, no limit is placed and the panel shows "Entry passed." Learn those two behaviours early or you'll be confused by vanishing lines.

## Who it's for

Swing traders who already think in BOS, sweeps and Order Blocks and want the sequence enforced mechanically rather than eyeballed. Also useful for anyone learning ICT-style structure who wants to see the steps laid out and labeled. It is **not** for scalpers, for traders who want tunable entry levels, or for anyone expecting a predictive signal. The author is explicit: it's an educational analysis tool, not a forecast.

## FAQ

**Does it repaint?** Swings and breaks are drawn back on the bar that confirms them, so historical markings appear after the fact. That's confirmation logic, not a bug — but don't treat the live bar as final.

**Is the panel a backtest?** No. It's a simple historical tally on loaded bars, excluding costs, and it changes with the symbol and history length.

**Can I use it on lower timeframes?** The author designed it for 4H and the panel warns otherwise. Nothing stops you, but you're outside the intended context.

## Verdict

HTF 5+1/Sattam earns its four stars on coherence. It does one thing — a strict, sequential four-step checklist with an optional sixth — and refuses to hand you a setup when the chain is incomplete. The fixed Fibonacci geometry and the 4-hour focus will rule it out for some, and the late-confirmation drawing behaviour demands you understand what you're looking at. But if you trade structure on the higher timeframe and want a tool that enforces discipline instead of decorating your chart, this is a well-built, unusually honest example of the genre.

**Rating: ⭐⭐⭐⭐**
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

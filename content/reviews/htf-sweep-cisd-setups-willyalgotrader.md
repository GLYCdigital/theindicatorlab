---
title: "HTF Sweep Cisd Setups Willyalgotrader Review"
date: 2026-11-16T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/htf-sweep-cisd-setups-willyalgotrader.png"
tags:
  - "htf sweep cisd setups willyalgotrader"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A structured ICT workflow that chains HTF sweeps, CISD and PD-array entries into one trade plan. Honest look at what it does — and its limits."
tv_script_url: "https://www.tradingview.com/script/M0FCXfZC-HTF-Sweep-CISD-Setups-WillyAlgoTrader/"
sources: ["https://www.tradingview.com/script/M0FCXfZC-HTF-Sweep-CISD-Setups-WillyAlgoTrader/"]
---
Most ICT-flavoured indicators are signal generators with a narrative attached. HTF Sweep CISD Setups is closer to a decision pipeline: it refuses to fire until a specific sequence has played out, then draws the trade in full and tracks it. Whether that's useful depends on how much you want the tool to think for you.

## What it actually does

The premise is stated plainly in the description: a sweep alone isn't a trade, and a fair value gap alone isn't a trade. The edge lives in the sequence — higher-timeframe liquidity taken, delivery flipped on your chart timeframe, price returning to the array that caused the flip. The indicator enforces that order bar by bar.

Mechanically, it builds its own higher-timeframe candles directly from chart bars rather than requesting another timeframe. That's a meaningful design choice: it means the exact chart bar that takes a level is known, so the swept extreme becomes a real anchor for the stop, the liquidity line and all subsequent structure. Arrays formed before the sweep are excluded by construction. Every new extreme resets the found arrays, so old legs don't contaminate the setup.

From there: CISD confirmation with a displacement requirement, five PD-array entry models (Order Block, FVG, IFVG, Breaker, Unicorn), quality and context filters, then a trade plan with entry, stop and three targets.

## Where the design holds up

The sweep engine is the part worth paying attention to. Four trigger types can fire — sweep of the previous HTF high/low, sweep plus close back inside the previous candle's body, sweep of any untaken HTF high/low within a lookback, and a confirmed 3-candle HTF pivot. An optional "wait for HTF candle to close" mode evaluates only on HTF close. HTF pairing is automatic from your chart timeframe.

The CISD logic is also more disciplined than the usual. It stores the run of opposite-coloured candles that delivered the extreme, then requires a close beyond the open of the first candle of that run — with a body at least half an ATR in the trade direction. A weak cross is ignored and a later, stronger candle can still confirm. A close back below the run low cancels it, and it can re-form. That's a reasonable model of "delivery actually changed."

The filter stack is where most tools get lazy. Here, every rejection produces a readable reason in the dashboard — "Blocked: risk 3.4 ATR > max 3", "Waiting: IFVG", "Skipped: entry already traded". You can see why a setup wasn't taken, which is more than most indicators offer.

The trade engine models limit fills, expiry, gap behaviour, break-even after TP1, and an intrabar conflict model with optimistic and conservative modes. Statistics are reported in R — net R, average R, profit factor — not just win rate, and the description is careful to define win rate as a TP1 hit rate rather than implying anything stronger.

## Where it asks a lot of you

This is a dense tool. The settings are organised into numbered steps — HTF condition, setup entry, required arrays, time and quality filters, context filters, risk management, visuals, HTF panel, dashboard, alerts — and understanding how they interact takes real time. The default entry model is Breaker Close; everything else in Step 3 (required PD arrays) is off by default, so out of the box you're seeing a fairly permissive version of the logic.

The honesty section is worth reading before you install it. Statistics reset on chart reload and are explicitly not a backtest. Partial exits and position sizing aren't modelled. The break-even stop is a price level, so after costs the result can be slightly negative. The Live Preview option repaints by design. None of that is a flaw — it's the tool refusing to oversell itself, which is rare and welcome.

One practical note: the structure replay is capped at 450 bars, and setups that need more are tagged "partial history." On very quiet instruments this may matter more than on active ones.

## Who it's for

ICT-style traders working 1m–15m charts paired with 15m–4H, who already understand what a CISD, a breaker and an FVG are — and who want the sequence enforced mechanically rather than eyeballed. Index futures traders get SMT divergence with automatic ES↔NQ and MES↔MNQ pairing. If you're new to ICT concepts, the dashboard will tell you things you don't yet know how to interpret; start with the documentation.

## FAQ

**Does it repaint?** No — orders, entries, exits and alerts are produced on confirmed bars only, and HTF candles are built from chart bars without lookahead. LTF pivots need three bars on each side, so pivot-based breakers are known with that delay. That's delayed confirmation, not repainting. The optional Live Preview does draw forming setups on the open bar and may change before close.

**Can I use it as a bot?** No. It's a setup detection and trade-planning tool. It places no orders and makes no decisions.

**Do the statistics reflect real trading?** They're a model. OHLC can't show the order of prices inside a bar, so the intrabar model and gap rules decide outcomes. They reset on reload and are not a backtest.

**Does it work outside intraday?** The description targets intraday timeframes with the HTF above the chart timeframe. It works on markets with OHLC data — futures, indices, forex, crypto, stocks.

## Final verdict

Four stars. The core sequence — sweep, anchored structure, displacement-confirmed CISD, PD-array entry — is coherent, and the components genuinely depend on each other rather than being bundled for feature count. The rejection reasons and the R-based statistics are the kind of transparency most ICT indicators skip. What keeps it off five stars: the configuration surface is large enough to misconfigure badly, the statistics are a model rather than a track record, and the tool still requires you to know what you're looking at. If you're already trading this style and want the workflow enforced consistently, it's a strong fit. If you're looking for signals to follow, keep moving.

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

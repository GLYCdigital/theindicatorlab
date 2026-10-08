---
title: "Maulers Raid To Delivery Review — Trend Indicator"
date: 2026-10-09
draft: false
type: reviews
image: "/screenshots/maulers-raid-to-delivery.png"
tags:
  - "maulers raid to delivery"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Maulers Raid To Delivery review: an ICT-style raid-to-CISD workflow tool that tracks HTF liquidity sweeps, SMT and entry confirmation in one script."
tv_script_url: "https://www.tradingview.com/script/xlWhYoco-Maulers-Raid-to-Delivery/"
sources: ["https://www.tradingview.com/script/xlWhYoco-Maulers-Raid-to-Delivery/"]
---
Maulers Raid To Delivery is a display-only study that tracks a single ICT-style sequence from start to finish: price raids liquidity resting beyond a higher-timeframe candle, a correlated index confirms or refuses that raid, and a lower-timeframe change in state of delivery (CISD) turns the whole thing into a setup with a level, a stop reference and targets. It is not a signal generator. It is a state machine for a specific trading model, and it says so plainly.

## What it actually does

The logic runs on a three-candle story. C1 is a finished higher-timeframe candle with stops resting beyond both sides. C2 trades through one side, takes those stops, then closes back inside C1's range — that close is the rejection. C3 is where the move away from the swept side is meant to deliver. The problem the script addresses is timing: the C2 is a higher-timeframe event and the entry is not, so the entry comes from a lower timeframe via a CISD — price closing through the open of the first candle in the run that pushed into the sweep.

Doing that by hand means watching three or four timeframes plus a second index simultaneously. This tool does the watching and reports what stage every setup is in.

## Key features

The headline feature is the automatic timeframe pairing. Pick the entry timeframe on a CISD selector and the C2 timeframe comes with it from a fixed table — 15m entry pairs to a 4H C2, 5m pairs to 1H, 1m pairs to 15m, and so on. A hunt only draws when your chart sits at or below its CISD timeframe, so a 1m chart can run several intraday pairs at once.

Up to three higher-timeframe candle lanes sit beside price as live mini candles, with countdown timers and timeframe labels. Sweep marks show the C1 level a C2 raided. SMT checks the chart symbol against its correlates — auto-detection covers the NQ, ES, YM and RTY futures complex, with manual symbol entry for everything else. When one index sweeps and the other holds, a line is drawn between the mini candles naming the correlate.

Around that core sit optional layers: standard-deviation targets (off by default), CISD FVG marking, nearby liquidity pools with labels like SSL · PDL when a pool sits on a prior day, week or month level, an LRLR staircase of unswept swing extremes, and two higher-timeframe FVG overlays. There is a trade plan with a stop level and position sizing from your dollar risk, and a CISD table tracking up to three C2 timeframes independently of the selectors.

## How setups live and die

This is where the tool earns its keep. Each setup moves through defined states: **Armed** when the C2 closes back inside C1, **Confirmed** only when a completed candle on the paired timeframe closes through the CISD level, **Retest** on the first tap back into the level after clean separation. A hunt that dies before confirmation (the C2's own extreme taken first) gets retired, leaving a muted stub. A confirmed setup whose C2 extreme is taken while still inside C3 reads FC2 — the targets come off and the line shortens to a stub.

One detail worth flagging: once C3 closes, a confirmed setup cannot fail. That single rule tells you a lot about how seriously the author thought through the failure model.

## Pros and cons

**Pros:**
- The timeframe pairing removes an entire layer of manual bookkeeping
- Honest state reporting — it explicitly tells you when not to take a setup, and much of the value is in the setups it filters out
- Documented non-repainting behaviour on the core reads: lanes, SMT, HTF FVGs and Daily Bias read the last closed higher-timeframe candle; C2s and SMT are judged on closed candles; CISDs confirm only on completed candles
- Open source under MPL 2.0, with the CISD engine, pairing resolver, SMT read and failure model all readable in the code
- Every layer can be switched off, with per-layer colour and style controls

**Cons:**
- It is a display-only mapping tool. If you want buy/sell arrows, this is not it
- The learning curve is real — C1/C2/C3, CISD, SMT, LRLR and FVG layers assume familiarity with the model
- A few events react to price touching a level by design (target hits, retests, FC2, dead hunts), so those do not reverse once printed
- SMT auto-detection is limited to the index futures family; other markets need manual correlates
- Defaults are tuned for a light NQ chart, so dark-theme users need to adjust line and label colours

## Who it's for

Discretionary intraday traders already working an ICT-style liquidity model — particularly index futures traders on NQ, ES, YM or RTY who juggle multiple timeframes and a correlate by hand. It suits traders who want the chart to track state and flag invalidation, not traders who want entries handed to them.

## FAQ

**Does it repaint?** The core reads use closed higher-timeframe candles and completed CISD candles, so history and realtime match. A handful of touch-based events fire intrabar by design, but a touch cannot un-happen, so they do not reverse once printed.

**Can I get alerts?** Yes. Alerts are off by default; enable them, then create one TradingView alert set to "Any alert() function call". A single alert carries everything, with two verbosity levels and an optional killzone filter. Create it on a 1m chart so every CISD selector runs.

**Which markets?** Any market. The lanes need a chart timeframe that divides evenly into them, and SMT auto-detection covers the index futures complex — other markets need correlates entered manually.

## Verdict

This is a well-scoped tool with a clear thesis, an honest failure model, and unusually thorough documentation. It does one sequence and refuses to bolt on extras that sequence does not use. The open-source code is a genuine plus — you can verify the description rather than trust it. The cost is a real learning curve and a display-only remit that will frustrate anyone hunting signals. For the right trader, that trade-off is worth it.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

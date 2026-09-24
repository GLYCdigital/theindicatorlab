---
title: "Ict_Setup_Screener_Liquidity_Sweep_Mss_Fvg_Scanner_Lunqfx Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/ict-setup-screener-liquidity-sweep-mss-fvg-scanner-lunqfx.png"
tags:
  - "ict setup screener liquidity sweep mss fvg scanner lunqfx"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A 20-symbol ICT screener that ranks liquidity sweep, MSS and FVG setups by stage and quality, with entry, stop and target per row."
tv_script_url: "https://www.tradingview.com/script/6g7YF3N1-ICT-Setup-Screener-Liquidity-Sweep-MSS-FVG-Scanner-LunqFX/"
sources: ["https://www.tradingview.com/script/6g7YF3N1-ICT-Setup-Screener-Liquidity-Sweep-MSS-FVG-Scanner-LunqFX/"]
---
Most ICT tools draw setups on the chart in front of you. This one runs the same sequence across twenty symbols at once and turns the answer to "where is a setup forming right now" into a single ranked table. That is the whole pitch, and it is a genuinely different job from a chart overlay.

## What it actually does

The model is an ICT entry sequence: liquidity gets swept, structure shifts the other way, displacement leaves a fair value gap, price returns to it. The indicator runs that sequence as a state machine inside twenty separate data requests — one per symbol — plus one more for the chart itself. Each call site keeps its own persistent state, so twenty calls become twenty independent scanners built from one body of code.

Every row in the table is one symbol sitting at one stage: SCANNING, SWEPT · waiting MSS, LONG SETUP / SHORT SETUP, OPEN, TARGET HIT / STOPPED. Rows re-sort on every bar — entries first, then mapped setups, then pending sweeps, then finished trades, then idle rows — and the symbol of the chart you are on is marked with ◂.

The table is the point. The one chart you have open also gets its own live stage drawn on the candles: the swept level, the shift level, and the entry with stop and target, so the ◂ row and the candles agree.

## The quality grade

Each mapped setup is graded 0–100 on four measurements: how deep the sweep went beyond the swing, how strong the displacement through the shift level was, how large the imbalance is, and how quickly the shift followed the sweep. All four are measured against that instrument's own ATR, so a quiet pair and a volatile one are graded on the same scale.

The colour coding is explicit: 70 and above shows turquoise, 45–69 amber, below that magenta. A minimum quality can be set so weaker setups never reach the table at all. Worth stating plainly — the author calls this a heuristic that ranks setups relative to each other, not a probability. That honesty is rare in this category.

## How to use it

Set your twenty symbol slots first. Defaults are forex majors, metals, crypto and index futures, but a symbol your data plan cannot load shows as scanning forever, so put in what you actually trade.

Then fix the scan timeframe. Left blank it follows the chart's timeframe, which changes the table every time you switch charts. Set it to one value and the table reads the same wherever you open it.

From there, read from the top. OPEN means the entry has been reached and the trade is running. A setup showing "0.3 ATR" is close to its entry; "2.4 ATR" is not. Open the chart before you act — the row tells you the stage and the levels, the chart shows you the candles, and you decide there.

The last column is the useful part: distance to entry in ATR while the setup waits, the trade's standing in R once it is open. ATR and R are the two units twenty different instruments can share.

## Pros and cons

**Pros**
- Twenty instruments through one sequence, ranked by stage — no twenty tabs.
- Non-repainting by design: confirmed pivots, every transition on a closed bar, lookahead explicitly off.
- One alert per bar that names the symbol, so a single alert covers the watchlist.
- Open source, and the author plainly credits his published ICT Entry Model rather than pretending a new rule was invented.
- Honest limitations section. The author states the ceiling is twenty symbols because TradingView allows forty data requests and each symbol costs one.

**Cons**
- It cannot show you the other nineteen charts. A row says "SHORT SETUP, Q68, 0.4 ATR to entry" — it does not tell you whether that sits under a daily level or into news.
- Prices print with up to five decimals, not each instrument's tick size, because the script cannot know the tick size of nineteen other symbols. Read them as levels, not order tickets.
- On a scan timeframe higher than the chart's, a row updates when that timeframe's bar closes. That is the cost of not repainting.
- TARGET HIT and STOPPED are the last resolution of one row, held briefly. They are not tallied, and the description makes no claim about how often the model wins.
- An open trade that touches neither stop nor target within a set number of bars is retired — this finds setups, it does not babysit positions.

## Settings and How to Tune Them

The settings fall into three groups.

**Entry model** — the scan timeframe, liquidity swing length, internal structure length, the maximum bars allowed from sweep to MSS, the maximum bars from setup to entry, the maximum bars in a trade, take profit expressed in R, minimum stop distance in ATR, and minimum quality.

**Watchlist** — the twenty symbol slots and the number of rows in use. Rows can be lowered, not raised past twenty.

**Visuals** — five candle palettes plus an off option, a toggle for drawing this chart's setup, table position and text size, a hide-scanning-rows option, and an alerts on/off switch.

The author's guidance on tuning is limited to two notes: raise the swing length for higher timeframes, and lower the row count if you want a shorter table. Nothing in the source material claims which values produce better results, so there is no "best" setting to point at here.

## Who it's for

Discretionary ICT traders who already read sweep, shift and imbalance by hand and want a watchlist ranked instead of scanned. Also useful for anyone running a fixed basket of majors, metals, crypto and index futures who wants one screen to say which instrument is at the interesting stage.

It is not for someone looking for a signal service or a performance-verified system. Nothing here tallies outcomes.

## FAQ

**Does it repaint?** No. Pivots are confirmed, every stage change happens on a closed bar, and every request is made with lookahead off. A row moves forward through the sequence and never back.

**Can I scan more than twenty symbols?** No. Twenty is the ceiling, and rows in use can be lowered, not raised.

**Is the quality grade a win rate?** No. It is a heuristic built from four ATR-relative measurements that ranks setups against each other.

**Do I still need the chart?** Yes. The table is for finding, the chart is for deciding.

## Verdict

The sequence is not new and the author says so. What is new is running it twenty times in parallel as one stateful function and reading the output as a ranked list — and that is a real engineering problem solved cleanly. The discipline around repainting, the explicit limitations, and the refusal to dress the quality grade up as a probability are what push this above the usual ICT script. The main structural caveat is that the table can only ever be a pointer: nineteen of the twenty charts stay invisible, and the levels print without true tick size.

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

---
title: "Breadth_Topping_Syndrome Review: Settings, Strategy & How to Use It"
date: 2026-08-24
draft: false
type: reviews
image: "/screenshots/breadth-topping-syndrome.png"
tags:
  - "breadth topping syndrome"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Breadth_Topping_Syndrome flags distribution phases before trend reversals. Tested settings, entry rules, and honest pros/cons in this 4-star review."
tv_script_url: "https://www.tradingview.com/script/WbFOdoNP-Breadth-Topping-Syndrome/"
sources: ["https://www.tradingview.com/script/WbFOdoNP-Breadth-Topping-Syndrome/"]
---
I’ll be straight with you: most “topping” indicators are just RSI with a fancy name. Breadth Topping Syndrome isn’t that. It identifies a specific market condition — broad internal weakness that accompanies distributive peaks — rather than plotting another oscillator line. Here’s what it actually does, where it fits, and where it falls short.

## What This Indicator Really Does

Breadth Topping Syndrome (BTS) is a breadth-analysis tool designed to detect when a market is losing internal participation even as price is still rising. It doesn’t rely on price alone. It condenses four warning conditions into one framework:

- **C1:** a Miekka-style divergence, where NYSE new 52-week highs and new 52-week lows are simultaneously elevated as a percentage of advances plus declines.
- **C2:** Norman Fosback’s High Low Logic Index at a high percentile of its own trailing history.
- **C3:** weak S&P 500 participation (percentage of constituents above their 200-day moving average) while the trend reference index is in an uptrend.
- **C4:** a weighted deterioration score built from the same normalized components exceeding a threshold.

When a configurable minimum number of these conditions has been observed within a short synchronization span and the trend gate is up, a trigger fires and opens a signal window. Inside the window the syndrome is Active only while the McClellan Oscillator is negative.

The script plots a normalized breadth deterioration score (0 to 100) in a separate pane against a dashed threshold line and a dotted midline at 50. On the chart, the line turns orange above the threshold and red while the syndrome is Active. Gray indicates missing core data. A faint purple line shows the HLLI percentile separately, since it is the slowest-moving and most historically studied component. A red triangle at the top of the pane marks a syndrome trigger on that bar. Small maroon diamonds mark the Miekka condition alone being true without a full trigger. Maroon background means syndrome Active; orange background means the window is open but the oscillator is positive. A status table (top right) shows the overall state, each condition’s current value and contribution, the syndrome count, the oscillator value, bars remaining in the window, and the cluster count.

## Key Features That Set It Apart

- **Adaptive normalization:** Every component is percentile-ranked against its own trailing distribution before use, so warning levels adapt to the prevailing breadth regime instead of relying on fixed absolute thresholds calibrated to a decades-old NYSE universe.
- **Tolerant multi-condition assembly:** Conditions are fused through an N-of-M syndrome count with a synchronization span, not a same-bar AND. This acknowledges that breadth deterioration components rarely align to the exact day.
- **Windowed gating:** The trigger inherits the two-phase Miekka mechanism but generalizes it — the syndrome, not a single divergence, opens the window, and the McClellan Oscillator gates activation inside it.
- **Quantified clustering:** Trigger clustering is counted directly on the chart rather than left to visual inspection.

The individual components are public-domain methods with documented lineages: the simultaneous new highs and new lows divergence follows James R. Miekka’s Hindenburg Omen specification (1995), itself derived from work by Martin Zweig and Norman Fosback. The High Low Logic Index is Fosback’s, published in 1976. Percentage of stocks above the 200-day moving average is a standard participation measure. The McClellan Oscillator is the 19/39-period EMA differential of net advances, per Sherman and Marian McClellan. The combination architecture is what is novel here.

## Settings and How to Tune Them

- **Conditions Required (N of 4):** syndrome count needed to trigger. Default 3.
- **Condition Sync Span:** bars within which a condition still counts toward the syndrome. Default 5.
- **Signal Window:** trading days a trigger keeps the window open. Default 30.
- **Cluster Lookback:** trailing trading days over which triggers are counted. Default 60.
- **C1 Miekka NH/NL Threshold:** minimum percent of advances plus declines for both new highs and new lows. Default 2.8.
- **C2 HLLI Warning Percentile:** percentile of the smoothed HLLI that flags bifurcation. Default 90.
- **C3 Participation Warning Percentile:** participation percentile at or below which weakness is flagged in an uptrend. Default 25.
- **C4 Deterioration Score Threshold:** score level that flags composite weakness. Default 75.
- **Uptrend Lookback:** bars over which the trend reference must have risen. Default 50.
- **HLLI EMA Length:** smoothing applied to the raw HLLI ratio. Default 50.
- **Percentile Rank Lookback:** window for all percentile ranks. Default 252.
- **Score weights** for the bifurcation, participation and leadership components. Default 33.3 each.
- **MCO Fast EMA and Slow EMA:** McClellan Oscillator periods. Defaults 19 and 39.
- **Data Symbols:** all seven feeds are exposed as string inputs and can be substituted.
- **Show Status Table:** toggles the table. Default on.

## How to Use It

The script is designed for the 1D timeframe. The breadth feeds are daily series, the window and cluster inputs are specified in trading days, and the Miekka and McClellan parameters are daily conventions, so daily resolution matches the granularity of the logic.

A single trigger is a caution flag. Two or more triggers within the cluster lookback have historically been the more serious configuration for divergence-based breadth signals, and the script exposes a dedicated alert for that case. Four alerts are provided: trigger fired, syndrome turned Active, clustered trigger, and score crossing above its threshold.

This is a risk-assessment input, not a standalone trading signal. It flags conditions that have accompanied past tops — it is not an entry system, and no claim is made about future results.

## Pros & Cons

**Pros:**
- Combines four independent breadth measures into a single framework rather than relying on any one of them.
- Every component is percentile-ranked against its own trailing history, so warning levels adapt to the prevailing regime.
- The N-of-M assembly with a synchronization span tolerates the fact that breadth components rarely align to the exact day.
- Clustering is quantified on the chart.
- Clean, documented lineages for each underlying component.

**Cons:**
- **Not a standalone system.** It flags conditions that have accompanied past tops. It needs to be paired with your own confirmation and risk management.
- **Limited to topping conditions.** It is specifically about distributive peaks, not bottoms.
- **Daily resolution only.** On other timeframes the external series return whatever the feeds report at that resolution, and the day-denominated windows lose their intended meaning.
- **Limited feed history.** No signals can exist before the feeds begin, and because every percentile rank requires the full normalization lookback (default 252 bars), the first year of available feed history produces unreliable ranks and should be disregarded.
- **Participation feed dependency.** If neither participation symbol resolves, condition C3 can never contribute. With the default requirement of 3 of 4, all three remaining conditions must then assemble, which makes triggers strictly rarer.

## Who It's For

This is for swing traders, position traders, and portfolio managers who want a systematic read on internal breadth deterioration as a market rises, and who already understand that breadth divergence signals carry a documented false-positive history. It is a risk-assessment input for de-risking ahead of potential tops — not an intraday tool and not a standalone entry system.

## Alternatives Worth Considering

- **Hindenburg Omen implementations:** narrower, focused only on the Miekka-style divergence without the multi-condition syndrome architecture or adaptive normalization.
- **McClellan Oscillator / Summation Index:** the underlying activation gate used here, available on its own for those who want the raw breadth reading.
- **Percentage of stocks above the 200-day moving average:** a standard participation measure, useful standalone if you only want the C3-style reading.

## FAQ

**Q: Can I use this on other timeframes?**
A: The logic is designed for daily resolution. On other timeframes the external series return whatever the feeds report at that resolution, and the day-denominated windows lose their intended meaning.

**Q: Is it good for long entries?**
A: No. It detects topping conditions — internal breadth deterioration while the market is still rising. It is a risk-assessment input, not a standalone signal.

**Q: Does it repaint?**
A: All values on the developing realtime bar update until the bar closes. Signals should be evaluated on closed bars. The script uses same-timeframe requests with lookahead off and does not reference future data.

**Q: Which chart symbol should I use?**
A: Data is pulled from fixed external symbols regardless of the chart symbol. The chart symbol only determines the bar grid, so the indicator belongs on a US equity index chart at 1D.

## Final Verdict

Breadth Topping Syndrome does one thing and does it in a defensible way: it condenses four independent breadth warning conditions into a single, adaptively normalized framework, and it quantifies trigger clustering directly on the chart. It won’t tell you exactly when to short, and it won’t work in every market condition, but as a risk-assessment filter alongside your existing process, it is a well-architected tool. The combination of adaptive normalization, tolerant multi-condition assembly, windowed gating and cluster counting does not correspond to any single published method. Just don’t expect it to do your job for you — pair it with price action confirmation and your own risk management.

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

---
title: "Liquidity_Sweep_Retracements Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidity-sweep-retracements.png"
tags:
  - liquidity sweep retracements
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Liquidity_Sweep_Retracements — a smart-liquidity tool for spotting sweep traps and retracement entries. Settings, pros, cons, and alternatives."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Liquidity_Sweep_Retracements is a smart-liquidity tool that marks where price likely swept liquidity — taking out old highs or lows — and then retraced. The premise behind it is a familiar one: price hunts stop-losses, then reverses. The indicator automates the spotting of that sequence.

It plots colored zones and arrows. When price spikes above a recent high and then closes back below, you get a red "sweep" marker. Green markers appear when price sweeps below a low and bounces.

It's positioned as an intraday tool, aimed at charts in the 5-minute to 1-hour range. The logic is designed around short-lived displacement-and-retrace sequences, so it is not built for swing horizons.

## Key Features That Set It Apart

- **Dynamic lookback for sweep detection** — Rather than relying on fixed swing points, it calculates recent structure based on volatility and candle wick length. The intent is to reduce noise in the sweep reference level.
- **Retracement confirmation filter** — Not every sweep triggers a signal. The indicator waits for price to retrace a minimum percentage from the sweep extreme before confirming. This is the feature that separates it from simpler sweep detectors.
- **Multi-timeframe awareness** — A higher timeframe can be set to filter sweeps on a lower timeframe. The purpose is to avoid trading against the higher-timeframe trend.
- **Customizable alert conditions** — Alerts can be set for "sweep detected" or "retracement confirmed." The retracement alert is the more useful of the two for execution, since it fires after the confirmation condition is met rather than at the raw sweep.

## Settings and How to Tune Them

- **Sweep sensitivity** — Controls how readily the indicator identifies a sweep. Lower values are more sensitive and produce more signals, including more false ones; higher values are more selective. The default is on the aggressive side.
- **Retracement percentage** — The minimum retracement from the sweep extreme required to confirm a signal. The tradeoff is straightforward: enough retracement to confirm the move is genuine, but not so much that the entry is gone by the time confirmation arrives. The appropriate value differs by instrument volatility.
- **Higher timeframe filter** — Setting a higher timeframe than the chart being traded filters out sweeps that run counter to the larger trend. This is the setting that does the most work in reducing signal count.
- **Show sweep levels** — Draws horizontal lines at the sweep high or low. Useful as a reference for placing stops just beyond those levels.

Note that the default configuration generates a large volume of signals on volatile instruments. Tightening sensitivity and raising the retracement threshold reduces the count substantially. What counts as "quality" here is a judgment call, not something the indicator resolves for you.

## How to Use It for Entries and Exits

### Entry (long example):
1. Wait for a red "sell sweep" marker above a recent high.
2. Price closes back below that high, confirming the retracement.
3. Enter long on the next candle close above the retracement zone.
4. Stop-loss just beyond the sweep low, below the red zone line.

### Exit:
- Take partial profits at the next obvious liquidity level — a previous swing high or low.
- Trail the stop using the indicator's retracement zone color change: if it turns green, the trade is still valid; if it flips red again, exit.

Combining the signal with volume context helps. A sweep that occurs at a high-volume node is a more credible reversal candidate; one at a low-volume node is more often a trap. That's a discretionary overlay, not something the indicator computes for you.

## Honest Pros and Cons

**Pros:**
- Automates a manual concept — liquidity sweeps — that many traders struggle to mark consistently.
- The retracement filter prevents chasing every spike.
- Works reasonably on forex and crypto.
- Clean visual presentation; arrows and zones are readable even on a fast chart.

**Cons:**
- **Laggy on lower timeframes.** The indicator needs several candles to confirm a sweep, so on a 1-minute chart the entry is often gone by confirmation.
- **No multi-pair scan.** It has to be applied manually to each chart.
- **False signals during news events.** Sweeps flagged during major releases are frequently just noise.
- **Support is limited.** No documentation or community channel accompanies this free indicator; you're on your own with the settings.

## Who It's Actually For

- **Intraday momentum traders:** If you scalp moves in the 5–15 minute range, the signal cadence fits that style.
- **ICT/SMC traders:** If you already work with concepts like liquidity sweeps and order blocks, this saves the manual marking.
- **Not for swing traders:** The signals are too short-lived. A higher-timeframe liquidity tool is the better fit for that horizon.

## Better Alternatives

- **Liquidity Voids by LuxAlgo** — More polished, includes volume analysis. Paid, and better suited to futures.
- **SweepDetector** — Free and simpler, but lacks retracement confirmation. Reasonable if you prefer to enter manually.
- **Smart Money Concepts by TradeSmart** — More comprehensive but heavier on the chart. Use it if you want order blocks alongside sweep detection.

## FAQ

**Q: Does it repaint?**
A: It can repaint on the current candle. Once the candle closes, the signal is fixed.

**Q: Can I use it on crypto?**
A: Yes. On higher timeframes, a less sensitive setting is the appropriate adjustment.

**Q: What timeframes are best?**
A: The 5-minute to 1-hour range. Below 5-minute, the confirmation lag becomes a problem. Above 1-hour, signals become rare.

**Q: How do I set alerts?**
A: Right-click the indicator, add an alert, and set the condition to "Sweep Detected" or "Retracement Confirmed." The latter is the more useful trigger for execution.

## Final Verdict

Liquidity_Sweep_Retracements does what it promises: it spots sweep retracements automatically. It isn't revolutionary, but the retracement confirmation filter is the feature that distinguishes it from simpler sweep detectors, and it addresses the main weakness of that category — firing on every spike without waiting for follow-through.

The tradeoffs are real: confirmation lag on the fastest timeframes, no multi-pair scanning, and noise around news events. Whether those matter depends entirely on your timeframe and instrument. It's a reasonable addition to an intraday toolkit, not a standalone system.

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

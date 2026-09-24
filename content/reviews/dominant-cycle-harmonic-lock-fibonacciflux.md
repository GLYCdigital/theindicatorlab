---
title: "Dominant_Cycle_Harmonic_Lock_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-30
draft: false
type: reviews
image: "/screenshots/dominant-cycle-harmonic-lock-fibonacciflux.png"
tags:
  - "dominant cycle harmonic lock fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Dominant_Cycle_Harmonic_Lock_Fibonacciflux review: real settings, entry logic, pros/cons, and who should use this trend indicator in 2026."
tv_script_url: "https://www.tradingview.com/script/iCIj2o7H-Dominant-Cycle-Harmonic-Lock-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/iCIj2o7H-Dominant-Cycle-Harmonic-Lock-FibonacciFlux/"]
---
Let me be blunt: the name sounds like someone smashed three trading buzzwords together and hit publish. But the source material tells a different story — this is a cycle-agreement experiment published with its own arithmetic bug, and then the fix.

**What It Actually Does**

Inside each of four timeframes (15m, 1H, 4H, 1D by default) the script detrends price against a 120-bar moving average and runs a causal autocorrelation scan over lags 5 to 60, taking the first local peak above zero as that timeframe's dominant cycle period. The period is smoothed, converted to minutes, and plotted as a log-period line, so four timeframes measured in different units land on one comparable axis. The white line is the weighted mean of those log-periods; the grey band is their weighted dispersion.

The lock test asks whether the four periods sit in the expected nested ratios — each timeframe's cycle roughly four, then four, then six times longer in wall-clock than the one below it. Each pair gets an exponential penalty on its log-ratio error, and the three are combined as a geometric mean. When that score clears the threshold and all four cycle phases sit in the same 90-degree quadrant, the pane marks a resonance diamond. An audit table prints every period in bars and in minutes, every phase and quadrant, the autocorrelation clarity behind each estimate, the three realised ratios against the expected ones, and the pair scores.

**Key Features That Stand Out**

The honest framing is the feature. This is published with the arithmetic error it shipped with, and the fix, rather than as a finished signal tool.

The error: the lock score could not reach its own threshold. Not rarely — never, on any instrument, on any timeframe. The three pair tests compared period counts in bars while the expected ratios describe wall-clock nesting. Because every leg searches the same 5-to-60 lag window in its own bars, the timeframe scaling silently divided out. An exhaustive search over all 9,834,496 integer-period combinations the estimator can produce confirms the maximum score is exactly 0.2500, against a threshold of 0.80. The fix is to compare in minutes, where the nested ratios mean what the header always claimed.

The validation is also unusually explicit. The whole computation — detrending, the autocorrelation scan with its first-peak rule, the EMA smoothing, the phase estimate, the weighting and the lock score — was reimplemented outside Pine and cross-checked against the chart's Data Window: eight quantities on ten bars, all agreeing to the four decimals TradingView prints. The check discriminates: changing the period smoothing from 5 to 4 breaks 65 of the 80 values; changing the autocorrelation window from 60 to 59 breaks 64; reading the higher timeframes in developing rather than confirmed mode breaks 35.

**What the Scale Actually Says**

Worth knowing before reading anything into a lock. Every leg searches the same 5-to-60 lag window in its own bars, so the periods come out near-identical in bar counts across the four timeframes — medians of 14.6, 14.2 and 14.1 bars on BTCUSDT 15m. In minutes that is close to the nested structure the lock test looks for, which means part of the agreement the score rewards is a property of the shared lag window rather than of the market. The estimator also hits its lower bound often enough to matter.

No edge is claimed and none was measured. There is no forward-return figure here and no suggestion that a resonance diamond predicts anything.

**Settings and How to Tune Them**

Each leg needs 242 bars of its own timeframe before it returns anything, so the daily leg needs 242 daily bars of history behind the chart. The four higher-timeframe reads use lookahead together with a one-bar shift inside the requested context, which is the non-repainting idiom: what arrives is the last fully closed bar of that timeframe. Switching the HTF data mode to Developing removes that shift and the values then change until the higher-timeframe bar closes.

The four attention weights are normalized, so only their ratios matter — but they own the plotted shape: driving the profile onto a single timeframe moves the weighted centre line by 3.5 log units, a 33-fold change in the implied period.

The tolerance default moved from 0.5 to 1.0, because at 0.5 the repaired score reaches 0.99 but never on a bar where all four phases share a quadrant, so the resonance state stayed empty on BTCUSDT. Do not read that as a recommendation; it is the change the author made and the reason given for it.

**What It Does After the Fix, Measured**

Over 5,757 scored bars of BINANCE:BTCUSDT 15m at the new defaults, the lock score has a median of 0.416, a 95th percentile of 0.667 and a maximum of 0.995. Sixty-two bars clear the 0.80 threshold; all four phases share a quadrant on 543 bars; both conditions hold together on 10 bars, which is 0.17% of them. On ETHUSDT over the same window: median 0.434, maximum 0.928, 67 bars over threshold, 1,302 same-quadrant bars, and 55 resonance bars, or 0.96%.

The background shading is also visible now, which it was not before. It is driven by the lock score, and with the score capped at 0.11 the shading sat at 99% transparency on 41% of bars and never got below 92%.

**Pros & Cons**

Pros:
- The cycle-agreement concept is clearly specified, and the four timeframes are plotted on one comparable axis
- Published with its own bug and the fix, rather than presented as a finished signal
- The computation was reimplemented outside Pine and cross-checked against the Data Window, with the discriminating power of that check stated
- The audit table the settings already promised is now implemented, including realised minute-domain ratios next to the expected ones

Cons:
- No edge is claimed and none was measured — no forward-return figure exists here
- Part of the agreement the lock score rewards comes from the shared lag window rather than the market
- The resonance path could not be verified against TradingView, because at the old defaults it never fired anywhere; the only live confirmation of the repaired state is on the author's chart, not from the original capture
- An MPL header was added, a leftover compile-sentinel plot removed, and an unexplained lineage note deleted — housekeeping, not substance

**Who It's For**

This is for traders who want to inspect whether four timeframes agree about the length of the cycle they are looking at, and who will read the audit table rather than only the diamond. If you need a signal service or a profitability claim, this is not it — the source says so plainly. Open source under MPL 2.0.

**FAQ**

*Does it repaint?* The four higher-timeframe reads use lookahead together with a one-bar shift inside the requested context, which is the non-repainting idiom: what arrives is the last fully closed bar of that timeframe. Switching the HTF data mode to Developing removes that shift and the values then change until the higher-timeframe bar closes.

*Can I use it for crypto?* The measurements in the source are on BINANCE:BTCUSDT and ETHUSDT. No claim is made about other instruments.

*Does it work on all timeframes?* The default set is 15m, 1H, 4H and 1D. Each leg needs 242 bars of its own timeframe before it returns anything, so the daily leg needs 242 daily bars of history behind the chart.

*Is it worth it?* There is no forward-return figure here and no suggestion that a resonance diamond predicts anything. Judge it on whether the cycle-agreement question is one you want answered.

**Final Verdict**

The name oversells it; the source material undersells it. What you actually get is a four-timeframe cycle-agreement test, published with the arithmetic error it was shipped with and the fix, plus a validation pass that states its own limits — including that the resonance path could not be verified against TradingView. No edge is claimed and none was measured. That honesty is the reason to look, and the reason not to expect a signal.

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

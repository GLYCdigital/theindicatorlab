---
title: "Deepflow_Absorption_Proxy_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-28
draft: false
type: reviews
image: "/screenshots/deepflow-absorption-proxy-fibonacciflux.png"
tags:
  - "deepflow absorption proxy fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Deepflow_Absorption_Proxy_Fibonacciflux review: tested settings, entry/exit logic, pros & cons. Is this trend indicator worth installing? Honest verdict inside."
tv_script_url: "https://www.tradingview.com/script/AZhxuvzI-DeepFlow-Absorption-Proxy-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/AZhxuvzI-DeepFlow-Absorption-Proxy-FibonacciFlux/"]
---
Let me be upfront: the name invites skepticism. But the source material behind this script is unusually candid, and that candor is the story here. This is an OHLCV-only proxy for absorption, published together with the measurements that say how little it is entitled to claim. That framing matters more than the marks themselves.

**What it actually does**

The script marks a bar when four conditions hold at once: volume is at least 1.8 standard deviations above its 50-bar mean, the body is at most 36% of the bar's range, one wick is at least 38% of that range, and the bar is revisiting a level it already reacted to — within 0.28 ATR of the 18-bar extreme on that side. Sell marks sit at the high, buy marks at the low. An audit table shows each of those four quantities for the last bar and whether it passed, so the reason for a mark, or for its absence, is visible rather than implied.

The script is explicit about what this is: real absorption is an order-book event. Nothing in OHLCV can see resting size, and the script does not pretend otherwise. It marks a shape.

**How often, and where**

At default inputs, on the 6000 bars of BINANCE:BTCUSDT 15m ending 2026-08-18 13:00 UTC — 62 days — it marks 16 bars: 0.27% of them, 9 sell and 7 buy, no two closer than 26 bars apart, and no bar ever firing both sides.

That rate belongs to the symbol and the bar size, not to the indicator. Same defaults, same measurement: BTCUSDT 1h 0.57%, BTCUSDT 4h 0.50%, ETHUSDT 15m 0.32%, ETHUSDT 1h 0.30%. On daily bars it can go a very long time without marking anything — on BTCUSDT 1D it marked nothing at all across 1000 days. It is built for intraday bars, and that is a limit rather than a preference.

**What the measurement does not support**

The tempting reading of a script like this is that the four gates recognise one event together — that a volume spike means something different on an absorption-shaped bar than on any other bar. Measured, that is not visible here.

Over the 5,951 scored bars, a volume spike is no more likely on a bar that already passed the shape and level tests than on any other bar: the lift is 0.99x on the sell side (95% CI 0.53 to 1.80) and 0.75x on the buy side (CI 0.36 to 1.45). With 123 sell candidates, an interaction smaller than roughly 1.6x could not be seen at all, so the honest statement is that the joint structure is undemonstrated at this sample size, not that it has been disproved.

A second test points the same way. Circularly shifting the volume series against untouched candles — which destroys any alignment between volume and bar shape while preserving both series' own distributions — produces about 19 marks on average (5th to 95th percentile 12 to 26) where the real series produces 16. The real series sits below its own null rather than above it, though not significantly (two-sided p = 0.59). One plausible mechanism, measured: range and volume correlate at 0.69, so genuinely high-volume bars tend to be wide-range bars, and wide-range bars are exactly what the small-body gate throws away.

The level gate is the part that runs against intuition. At the shipped 18-bar lookback, a bar sitting at an 18-bar extreme is about 28% less likely to carry a volume spike than a bar that is not (0.72x, 95% CI 0.48 to 0.96 on BTCUSDT 15m; 0.62x on ETHUSDT 15m). The relationship does turn positive at longer lookbacks — around 60 bars it runs between 1.3x and 2.5x across BTC and ETH on 15m and 1h — but the headline BTCUSDT 15m cell does not separate from a volume-shift null even there. The default is left at 18 because every number quoted was measured at it, and the tooltip on that input says all of the above.

Two more things a user should know before turning knobs. "Require Same Price Reaction" is what makes the indicator rare: switching it off takes the same 6000 bars from 16 marks to 147, and it also silently disables the three inputs above it, which do nothing whatsoever while it is off. And the volume threshold's default of 1.8 sits in the middle of a flat plateau — every value from 1.7 to 2.2 produces exactly the same 16 marks — so nudging it one step will usually appear to do nothing.

No edge is claimed and none was measured. There is no forward-return figure here, no hit rate, and no suggestion that a mark predicts anything.

**Settings and How to Tune Them**

The four shape and level inputs — the volume threshold, the body-to-range cap, the wick share, and the level lookback — are all quoted above at their shipped values, and every measurement in this review was taken at those values. The volume threshold is the one whose default sits on a flat plateau, so small adjustments to it will usually change nothing. The level lookback is the one whose relationship to volume spikes is negative at the shipped value and turns positive at much longer settings, though the headline cell does not separate from the null even there.

The input that actually governs rarity is "Require Same Price Reaction." Turning it off multiplies the mark count many times over and silently disables the three inputs above it. Anyone tuning this script should start by understanding that input, because the others do nothing while it is off.

There is no basis in the source material for recommending any particular setting over another.

**What changed in this version**

The previous version declared a compact volume profile — six inputs, three colour pickers, box and line arrays and a colour helper — and drew none of it: the file simply ended before that code existed. Shipping inputs that do nothing is the thing this publication is trying not to do, so the profile is gone and the title no longer claims one. What remains is the absorption test, which is complete and testable, plus an MPL header, the audit table, and a clamp on "Max Body / Range" so that the part of its slider that could never matter stops pretending it does.

**How the numbers were checked**

The whole computation was reimplemented outside Pine and cross-checked against the chart's Data Window on five bars chosen in advance — three sell marks, one buy mark, and one bar that fires nothing so that a model marking everything could not pass. All five agree exactly, to the price rather than to a tolerance. The reimplementation then reproduces the entire firing set independently: the same 16 bars, at the same indices, over the same 6000.

**Who should use it**

Traders who want to see the audit trail behind a mark, and who are comfortable with a tool that states plainly what it has not demonstrated. The mark count is low by design, the daily-bar behaviour is effectively silent, and the script does not claim to predict anything. If what you want is a signal that asserts an edge, this is not it — and the source material says so directly. Open source under MPL 2.0. Nothing here is a forecast, a signal service, or a claim of profitability.

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

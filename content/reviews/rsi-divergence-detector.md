---
title: "Rsi Divergence Detector Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/zR6IkGDL-RSI-Divergence-Detector-DragonFly-Trading/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rsi-divergence-detector.png"
tags:
  - rsi divergence detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of RSI Divergence Detector: how it spots hidden & regular divergences, best settings, and why it’s a solid 4-star tool for reversal traders."
grounding: "none (no source found)"
---
**Review of RSI Divergence Detector: regular and hidden divergence marking for reversal and continuation traders.**

---

Divergence detectors on TradingView tend to fall into two camps: noisy, or laggy. The **RSI Divergence Detector** aims at the middle ground by automatically marking regular and hidden divergences on price and RSI, without requiring manual line drawing. What follows is a breakdown of what the tool claims to do, how its settings work, and where it fits in a workflow.

### What This Indicator Does

It scans the classic RSI (Relative Strength Index) for two categories of divergence:

- **Regular Bullish/Bearish**: Price makes a lower low (or higher high), but RSI does not confirm. This is read as a potential trend reversal.
- **Hidden Bullish/Bearish**: Price makes a higher low (or lower high) while RSI makes a lower low (or higher high). This is read as trend continuation.

The indicator plots arrows on the chart and labels them by type. Each divergence type can be toggled on or off in the settings, so you can run regular only, hidden only, or both.

### Key Features

- **Customizable RSI period and overbought/oversold thresholds** – The RSI length and the overbought/oversold levels are adjustable rather than fixed at the default values.
- **Divergence strength filter** – A minimum number of bars between divergence points can be set, which is intended to cut down on micro-divergences.
- **Alert integration** – New divergences can trigger a popup or sound, which matters if you monitor multiple charts.
- **Visual style** – Small arrows, adjustable colors, and non-overlapping labels. Presentation is clean rather than cluttered.

### Settings and How to Tune Them

The settings exposed by the indicator are:

- **RSI Period** – Shortens or lengthens the RSI lookback. A longer period produces a smoother oscillator and fewer signals; a shorter one reacts faster.
- **Overbought / Oversold levels** – Defines the thresholds RSI must reach for the oscillator-side condition of a divergence.
- **Minimum bars between divergences** – A spacing filter. Raising it suppresses closely clustered signals; lowering it lets more through.
- **Divergence types** – Regular and hidden can each be enabled or disabled independently.

There is no single correct configuration. The trade-off is consistent across all of these: tighter filters mean fewer, more separated signals, and looser filters mean more signals with more noise. Match the settings to the timeframe and instrument you actually trade rather than copying someone else's values.

**Entry logic commonly paired with divergence signals:**
- **Regular bullish divergence** at a key support level → long after a close above the divergence candle high.
- **Hidden bearish divergence** within a confirmed downtrend → short after price breaks below the divergence candle low.

**Exit logic commonly paired with divergence signals:**
- Trail with a moving average, or take profit at the next resistance/support zone.
- If price does not move in the expected direction within a small number of bars after the signal, the setup has failed and the trade can be cut.

### Pros and Cons

**Pros:**
- Higher timeframes produce cleaner output; signal quality improves as the timeframe lengthens.
- Alerts can be configured per divergence type.
- The indicator marks divergences without redrawing them after the fact, so historical arrows remain where they were plotted.

**Cons:**
- Lower timeframes produce a high volume of signals. The minimum-bars filter helps reduce this but does not eliminate it.
- No divergence strength scoring. Every divergence is marked with equal weight, regardless of how clean the underlying structure is.
- No automatic trendline drawing from divergence points; that remains manual work.

### Who This Is For

- **Swing traders** on higher timeframes are the natural fit, since that is where the signal-to-noise ratio is best.
- **Day traders** can use it on intraday charts with a strict minimum-bars filter, but need to be selective about which signals they act on.
- **Scalpers** will find it too slow for very short timeframes.

### Alternatives

Indicators offering divergence scoring and automatic trendlines exist at higher price points. Free alternatives exist as well, though some of them redraw past signals. This detector sits in the middle: functional and reasonably priced, without the extras.

### FAQ

**Q: Does it repaint?**
A: No. Arrows remain in place after the bar closes.

**Q: Can I use it for crypto?**
A: Yes. It works on BTC, ETH, and altcoins, with the same preference for higher timeframes.

**Q: What's the best timeframe?**
A: Higher timeframes. On lower ones, you will need to raise the minimum-bars filter to control signal count.

**Q: Does it work with other oscillators like Stoch?**
A: No, it is built around RSI specifically.

### Final Verdict

The RSI Divergence Detector is a straightforward tool: it marks regular and hidden divergences on RSI, offers adjustable period and threshold settings, and supports alerts. It performs best on higher timeframes and does not redraw its historical signals. It does not score divergence quality or draw trendlines for you, and it will overwhelm a low-timeframe chart unless the spacing filter is tightened. For swing traders who rely on RSI divergences, it removes a meaningful amount of manual scanning.

**Rating: 4/5** – Reliable and clean for higher timeframe traders, with the caveats above.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

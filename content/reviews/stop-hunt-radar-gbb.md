---
title: "Stop_Hunt_Radar_Gbb Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/k7wRHBia-Stop-Hunt-Radar-GBB-GoodBadBitcoin/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/stop-hunt-radar-gbb.png"
tags:
  - stop hunt radar gbb
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A stop-hunt detector for GBP pairs that flags liquidity grabs before reversals. Reliable on M15-H1 but not magic. 4/5."
grounding: "none (no source found)"
---
# Stop_Hunt_Radar_Gbb Review

Stop_Hunt_Radar_Gbb is an indicator built specifically for GBP pairs (GBPUSD, GBPJPY, and similar) that does one thing: highlight where large players may be hunting stops before a move. It doesn't predict the future. What it does is scan for price patterns that resemble liquidity sweeps—sudden spikes above recent highs or below recent lows that get rejected quickly. The indicator marks these zones with colored dots and lines. The premise is that once stops are taken out, price reverses into a trend.

## What This Indicator Actually Does

The tool identifies swing highs and lows where stop orders tend to cluster, then flags the moments when price sweeps through those levels and closes back inside the range. Zones are plotted as dots and lines on the chart. The logic is straightforward: a sweep followed by a rejection suggests the move was engineered to grab liquidity rather than to start a genuine breakout.

## Key Features That Set It Apart

- **Real-time zone plotting** – Updates as new candles form rather than waiting for the close, so the signal appears as it develops.
- **Auto-detection of liquidity levels** – No manual trendline drawing. It identifies key swing highs and lows where stops cluster.
- **Alert system** – Alarms can be set for when a new stop-hunt zone is identified, reducing the need to watch the chart continuously.
- **GBP-specific calibration** – The defaults are tuned for the volatility of sterling pairs. It's not a generic scanner.

## Settings and How to Tune Them

The indicator exposes a small set of parameters that control how aggressively it scans for sweeps and how it draws the resulting zones. The two that matter most are the lookback period (how far back the indicator searches for swing highs and lows) and sensitivity (how strict the rejection filter is). A shorter lookback with higher sensitivity produces more signals and more noise; a longer lookback with lower sensitivity produces fewer, cleaner signals. A minimum zone width parameter filters out trivially small sweeps.

There is also a display toggle for zone fill. Turning it off leaves just the dots and lines, which keeps the chart readable if you're running multiple indicators.

The right combination depends on the timeframe and the pair. Scalpers on very short timeframes will generally want a tighter lookback and stricter sensitivity to cut noise; swing traders on higher timeframes will want a longer lookback and looser sensitivity to avoid missing larger sweeps. There is no single best configuration—it should be matched to the timeframe being traded.

## How to Use It for Entries and Exits

**Entry:** Wait for price to touch the zone (the dot or line) and then close back inside the range. Enter on the next candle in the reverse direction. For example, if price sweeps below a low and closes back above, go long.

**Stop loss:** Place it beyond the zone rather than inside it. The indicator's zone marks the level where stops are presumed to sit, so the stop should be far enough past it to survive a second swipe.

**Take profit:** Use a fixed risk-reward ratio or target the nearest swing high or low.

**Avoid:** Major news events for GBP, such as UK CPI releases or BOE rate decisions. The indicator still functions, but spreads widen and false sweeps increase.

## Honest Pros and Cons

**Pros:**
- Designed for GBPUSD and GBPJPY specifically.
- Signals appear in real time rather than on candle close.
- Simple to read once the underlying logic—liquidity sweeps—is understood.

**Cons:**
- Not for beginners. Without an understanding of stop hunts, the signals are easy to misread.
- False signals are more common on lower timeframes.
- Pair-specific. Applied to non-GBP instruments, the output tends to be noisy.

## Who It's Actually For

- Day traders and scalpers who focus on GBP pairs.
- Traders already using concepts like liquidity sweeps or order blocks.
- Anyone tired of manually drawing zones on their charts.

**Not for:** Beginners looking for a simple buy/sell arrow. This indicator requires interpretation.

## Alternatives

For traders working multiple pairs, **Liquidity V2** by LuxAlgo is broader and applies to any forex pair—less focused, but more versatile. For GBP-only use, Stop_Hunt_Radar_Gbb is a reasonable fit.

Another option is **Stop Loss Hunter**, which is similar but offers more alert customization. It costs more.

## FAQ

**Q: Does it repaint?**
A: No. Once a zone is drawn, it stays. The dots do not disappear after the candle closes.

**Q: Can it be used on crypto or indices?**
A: Technically yes, but it is not optimized for them. Signals on instruments outside GBP pairs tend to be less reliable.

**Q: What's the best timeframe?**
A: M15 or H1. M5 tends to be too noisy, and H4 produces too few signals.

**Q: Is it free?**
A: No, it's a paid indicator. Current pricing is listed on the TradingView store.

## Final Verdict

Stop_Hunt_Radar_Gbb is a specialized tool for identifying liquidity sweeps on GBP pairs. It won't replace a full trading plan, but it saves time otherwise spent manually marking up charts. The drawbacks are real: false signals on low timeframes and a narrow instrument focus. Traders who already work GBP pairs and understand market structure will get the most out of it.

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

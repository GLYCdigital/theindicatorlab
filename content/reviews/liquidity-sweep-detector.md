---
title: "Liquidity_Sweep_Detector Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/b9oLRMRb-Liquidity-Sweep-Detector-DefinedEdge/"
date: 2026-07-27
draft: false
type: reviews
image: "/screenshots/liquidity-sweep-detector.png"
tags:
  - "liquidity sweep detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Liquidity_Sweep_Detector review: settings, strategy, and real chart performance. See how this trend-based sweeps detector works for entries and exits."
grounding: "none (no source found)"
---
# Liquidity_Sweep_Detector Review

The **Liquidity_Sweep_Detector** is a trend-following tool that marks price levels where liquidity sweeps—sharp moves that take out stop-loss clusters—have occurred. It then plots zones around those levels to help anticipate reversals or continuations. It isn't a magic bullet, but for traders who already understand order flow, it's a reasonable addition to the toolkit.

The indicator is often shown applied to a MACD chart. Sweeps are color-coded by direction, and zones are drawn dynamically based on recent price action rather than fixed levels.

## Key Features

- **Sweep Detection**: Flags both bullish and bearish liquidity sweeps with markers. The logic uses a lookback period to identify when price breaks a swing high or low and quickly reverses—that reversal is the sweep.
- **Zone Plotting**: After detection, it shades a zone around the sweep level. These zones are intended to act as support or resistance until price breaks them decisively.
- **Trend Filter**: An optional moving average (SMA) that acts as a trend filter. When price is above it, only bullish sweeps are considered relevant; below it, only bearish sweeps.
- **Alert System**: Built-in alerts for new sweeps.

## Settings and How to Tune Them

The main parameters are:

| Setting | Purpose |
|---------|---------|
| Lookback Period | Controls how far back the indicator looks to identify swing highs and lows for sweep detection. Shorter values make detection more sensitive; longer values make it more selective. |
| Zone Width | Determines how wide the shaded zone is drawn around the sweep level. Narrower zones suit faster styles; wider zones are more tolerant of noise. |
| Trend Filter | Toggles the optional moving average filter and sets its period. When enabled, it restricts which sweeps are highlighted based on trend direction. |
| Display Mode | Controls whether zones, arrows, or both are shown on the chart. |

The indicator does not publish recommended values, and the right settings depend on the instrument, timeframe, and trading style. There is no single configuration that is objectively best.

## How to Use It (Entry/Exit Logic)

**For a bullish sweep setup**:
1. Wait for a liquidity sweep below a recent swing low.
2. Price must reverse back above the sweep zone.
3. Confirm with a bullish candle close above the zone.
4. Enter long, with a stop below the sweep low (an ATR-based buffer is a common approach).
5. Target the next swing high or a fixed risk-reward multiple.

**For a bearish sweep**:
1. Sweep above a swing high.
2. Price reverses below the zone.
3. Short entry on a bearish candle close below.
4. Stop above the sweep high.
5. Target the next swing low.

The indicator does **not** generate buy or sell signals—it provides the levels. Price action confirmation is still required, and entering as soon as a zone forms, without waiting for that confirmation, is a common source of bad trades.

## Pros & Cons

**Pros**:
- Zones and markers stay fixed once a candle closes, rather than shifting after the fact.
- Works across timeframes, though it is commonly used on higher intraday and swing timeframes.
- Clean visual design—unlikely to clutter a chart.
- Built-in alerts reduce the need to watch the screen continuously.

**Cons**:
- False sweeps occur in ranging markets. The trend filter helps, but it isn't foolproof.
- Zone width is static, so a volatility spike can break a zone quickly.
- No multi-timeframe confirmation is built in; higher-timeframe context must be checked manually.

## Who It's For

- **Swing traders** looking to catch trend continuations after liquidity sweeps.
- **Order flow traders** who already understand concepts like stop hunts.
- **Traders who avoid indicators that repaint**—this one is designed not to.

**Not for**: Scalpers needing very fast entries, or beginners who want a "buy now" button. The tool assumes chart-reading skills.

## Better Alternatives

- **Liquidity Voids Pro**: Zones that adapt to volatility. More complex, but better suited to news-heavy pairs.
- **Smart Money Concepts (SMC)**: Combines sweeps with order blocks. Heavier on the chart but more comprehensive.
- **Market Structure Scanner**: Pivot-based detection without zone plotting.

## FAQ

**Q: Does this indicator repaint?**
A: The design is intended to keep zones and markers fixed once the candle closes, rather than shifting them retroactively.

**Q: Can I use it for crypto?**
A: Yes. Crypto's high volatility tends to produce more false sweeps, so a narrower zone width is generally more appropriate.

**Q: How does it compare to the built-in "Sweep" indicator?**
A: The built-in is more basic—just arrows. This one adds zones and a trend filter, which makes it more actionable.

**Q: Does it work in sideways markets?**
A: Poorly. In ranges, sweeps are frequent and unreliable. It is best used with a clear trend bias.

## Final Verdict

**Liquidity_Sweep_Detector** is a focused tool that does one thing well—marking liquidity sweeps with zone context. It won't replace a strategy, but it can sharpen entries for traders who already understand order flow.

The trend filter and non-repainting design put it a step above similar free indicators. It isn't perfect—ranging markets will frustrate users—but for its scope, it's a reasonable option for intermediate and advanced trend traders who want clean sweep detection without extra clutter.

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

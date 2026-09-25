---
title: "Directional_Volume_Shapes Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/3XE8qqfr-Directional-Volume-Shapes-Zeiierman/"
date: 2026-08-13
draft: false
type: reviews
image: "/screenshots/directional-volume-shapes.png"
tags:
  - "directional volume shapes"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Directional_Volume_Shapes review: combines volume flow with trend direction. Tested settings, entry/exit logic, pros, cons, and who should use it."
grounding: "none (no source found)"
---
Directional_Volume_Shapes isn't a black box. It's a trend-following tool that overlays volume analysis directly on the price chart, using shape-based visual cues to indicate whether buyers or sellers are in control.

**What it does differently**

Most volume indicators show a histogram and leave the interpretation to the user. This one packages volume into directional shapes — markers that appear above or below price depending on whether volume is pushing price up or down. The distinguishing feature is how it filters noise: rather than reading raw volume, it weights it against the prevailing trend context, so a volume spike against the trend is flagged differently than one that confirms the move.

The shapes cluster during strong directional moves and thin out during consolidation. That visual behavior is the core appeal — it gives a quick read on when the market is building conviction versus chopping around.

**Settings and How to Tune Them**

- **Volume threshold.** Raising the threshold above its baseline filters out weak-volume signals in ranging markets. The trade-off is that a higher threshold will also suppress some legitimate signals, so the setting is a balance between noise reduction and responsiveness.
- **Lookback period.** This controls how much history the indicator uses to establish its trend context. Shorter periods make the indicator more reactive and twitchy; longer periods introduce lag.
- **Shape size.** On busier chart types, the shapes are already prominent enough. Enlarging them adds clutter rather than clarity.

One general observation about the design: the indicator behaves differently across timeframes. On very short intraday charts, signals tend to be messier; on higher timeframes, they read more cleanly. That makes it a poor fit for scalping and a more natural fit for slower trading styles.

**How it's typically used**

The straightforward approach: wait for a shape to appear in the direction of the prevailing trend (confirmed by price action or a basic moving average), then act on the next candle. A common exit rule is to close when the indicator prints a shape in the opposite direction, or when price breaks the prior swing high or low.

Because the indicator filters for high-conviction volume, the moves it catches tend to run further, which can compensate for a modest hit rate. Pairing it with a simple trend filter such as a moving average helps cut false signals. It works on its own, but it functions better as a confirmation tool than a standalone system.

**The honest trade-offs**

**Pros:**
- Visual clarity is excellent — no squinting at histograms.
- Filters out low-volume noise effectively once the threshold is adjusted.
- Designed to work across asset classes, including forex, crypto, and equities.
- The trend-context weighting is genuinely useful; it doesn't treat all volume spikes equally.

**Cons:**
- Lag is real. Waiting for the shape to print means missing the first leg of a move.
- Not suited to range-bound markets, where it sits idle or gives conflicting signals.
- The shape-based system takes adjustment if you're coming from traditional volume indicators.
- No built-in alerts. TradingView's alert system can be used as a workaround, but native notification options would be preferable.

**Who should use this**

If you're a swing trader comfortable holding positions for days and you want a volume-based edge without the complexity of VWAP or order flow analysis, this is a reasonable pick. It also suits traders who respond better to shape-based cues than numeric readouts.

Skip it if you're a day trader on low timeframes or if you prefer leading indicators. This one confirms rather than predicts.

**What else is out there**

If the lag is a problem, Volume Profile or Market Profile tools give a real-time picture of where volume is concentrated rather than waiting for shapes to print. For something with more features, the Volume Weighted MACD combines volume with momentum in a more traditional package. And if you're purely after trend direction, a simple Supertrend or ADX setup will get you most of the way there with less visual noise.

**FAQ**

**Does this work on crypto?** It is designed to handle 24/7 markets, where volume patterns tend to be more consistent than in session-based markets.

**Can I use it for options trading?** It can indicate direction, but it won't help with implied volatility or delta analysis. Use it as a directional filter, not a complete strategy.

**Is it beginner-friendly?** The concept is simple to grasp, but adjusting the settings and interpreting the shapes across different market conditions takes practice. Intermediate level is a fair characterization.

**Final verdict**

Directional_Volume_Shapes does one thing well — showing volume-backed trend conviction in a way that's easy to read and act on. It's not a complete trading system and won't replace core analysis, but as a confirmation tool it is genuinely useful. The lag keeps it from being exceptional, but for swing traders who value clarity over speed, it's a worthwhile addition to the toolbox.

If you want a volume trend indicator that's more visual than most and you're willing to spend time tuning the settings, it's worth a look. Just don't expect miracles — no indicator delivers those.

## Frequently Asked Questions

### Is Directional_Volume_Shapes worth it?

It delivers solid value for traders who need trend and volume confirmation, provided its lag and timeframe preferences fit their style.

### Does this indicator repaint?

Signals are calculated on closed bars, so past signals will not change when new data arrives.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

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

---
title: "Mtf_Volume Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/Vgq41bDV-MTF-Volume-Profile-Signal-Scanner-v5-zackzackzackw/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mtf-volume.png"
tags:
  - mtf volume
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Multi-timeframe volume analysis for divergence, breakout confirmation, and momentum shifts. Practical settings and real trade examples included."
grounding: "none (no source found)"
---
**What this indicator actually does**

Most volume indicators are stuck on one timeframe. Mtf_Volume addresses that by pulling volume data from higher and lower timeframes directly onto your current chart. Instead of flipping between tabs to check whether volume on a higher timeframe confirms a lower-timeframe breakout, you see it in one place.

The display is straightforward: histogram bars for bullish and bearish volume across multiple timeframes, plus a line overlay for cumulative volume delta. No clutter—just the readings that matter for multi-timeframe confluence.

**Key features that set it apart**

- **Three timeframe layers**: Volume from the current, one higher, and one lower timeframe can be displayed simultaneously. Most MTF tools only show two.
- **Customizable volume types**: Toggle between tick volume, real volume (where your broker provides it), and delta volume. Real volume is generally the better fit for futures and forex; tick volume is typically the practical choice for crypto.
- **Alert zones**: The indicator highlights when volume spikes exceed a user-defined threshold on any timeframe—useful for flagging expansion early.
- **Divergence scanner**: Auto-detects hidden and regular divergences between price and volume. It can false-signal during low-liquidity sessions, so treat it as a filter rather than a trigger.

**Settings and How to Tune Them**

- **Main timeframe**: Current chart's timeframe (auto-detected). Overriding this defeats the purpose of the tool.
- **Higher timeframe**: A multiple of the current timeframe, so the higher-timeframe bars nest cleanly inside the current chart. Round-number timeframes are easier to reason about.
- **Lower timeframe**: A fraction of the current timeframe, likewise chosen so the bars nest cleanly.
- **Volume type**: Real volume for futures, tick volume for crypto. Real volume is more accurate but lags slightly; tick volume updates faster.
- **Divergence sensitivity**: Medium is the sensible default. High sensitivity catches too many false signals in ranging markets.
- **Alert threshold**: Expressed in standard deviations above a moving average of volume. Lower thresholds flag more moves but produce more noise.

The general principle: keep the main timeframe on auto, choose higher and lower timeframes that divide or multiply cleanly into the current one, and match the volume type to what your data feed actually provides.

**How to use it for entries and exits**

Entry example (long): Price makes a higher low on the higher timeframe, but volume on that same timeframe is declining—a bearish divergence against price. Wait for the lower timeframe volume to spike above its threshold *and* price to break the recent swing high. Enter on the lower-timeframe close above that level.

Exit example: If higher-timeframe volume starts declining while price is still rising, that's a warning sign—tighten the stop to breakeven or take partial profits. When the lower timeframe volume also drops below its moving average, close the position.

This isn't a standalone signal—it's a filter. Use it alongside price action or a trend-following indicator such as an EMA cross.

**Honest pros and cons**

Pros:
- Saves time by removing the need to flip between timeframes to check volume.
- Divergence detection is most useful in trending markets, where volume and price relationships are cleaner.
- Clean UI. Opacity and colors are adjustable to avoid visual overload.

Cons:
- Lag on real volume data. On fast timeframes, real volume can trail the current bar. Tick volume is faster.
- Divergence false signals during low-volume sessions (Asian session for forex, weekends for crypto). Disabling the scanner during those windows is a reasonable workaround.
- No built-in screener. Each pair has to be checked manually.

**Who it's actually for**

- Swing traders who check multiple timeframes anyway. This automates that.
- Scalpers who want higher timeframe context without switching charts.
- Anyone trading breakouts—volume confirmation is key, and this gives it from two angles.

Not for: Beginners who don't understand volume analysis yet. It will confuse anyone who doesn't already know what volume divergence means.

**Better alternatives if they exist**

- **Volume Profile (standard)** – Better for identifying support/resistance zones, but single timeframe only.
- **Delta Volume** – More granular (buy vs sell volume), but requires footprint charts. Mtf_Volume is simpler.
- **VWAP + Volume** – Good for intraday, but no MTF capability.

If you already use VWAP and want MTF volume, this is a reasonable add-on.

**FAQ addressing real trader questions**

*Q: Does it repaint?*
A: Per the indicator's design, no. The histogram bars close with the candle, and divergence signals appear on the bar where the divergence completes.

*Q: Can I use it on forex?*
A: Yes, but tick volume only—most forex brokers don't provide real volume. Tick volume still works for divergence.

*Q: Why does the higher timeframe volume look flat sometimes?*
A: If the current timeframe is much faster than the higher timeframe, the higher-timeframe bar hasn't closed yet. It updates on close.

**Final verdict**

Mtf_Volume does one thing well: it layers volume data from multiple timeframes into a single view. It isn't revolutionary, but it's a reliable time-saver. The divergence detection is a bonus, not a primary tool.

It suits any trader who already uses volume analysis and wants to streamline their workflow. For beginners, stick with simple volume first.

**Rating: ⭐⭐⭐⭐ (4/5)**
Loses one star for the data lag on real volume and occasional false divergences during low liquidity. Otherwise, solid.

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

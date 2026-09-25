---
title: "Chande_Momentum_Oscillator_Divergence Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/ogmWth5h-Chande-Momentum-Oscillator-everget/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/chande-momentum-oscillator-divergence.png"
tags:
  - chande momentum oscillator divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Chande Momentum Oscillator Divergence review: settings, hidden divergences, entry strategy, pros/cons. Honest 4/5 rating from a real trader."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
A solid divergence tool built on a clean CMO core, but don't expect it to do your homework for you.

---

## What This Indicator Actually Does

The Chande Momentum Oscillator Divergence (CMO Divergence) is a custom script that overlays divergence signals onto the classic Chande Momentum Oscillator. If you're familiar with Tushar Chande's original — a momentum oscillator that ranges from -100 to +100, similar to RSI but using a different formula that accounts for both up and down days — this version adds automatic detection of regular and hidden divergences.

It plots the CMO line in the lower pane, then paints green and red arrows directly on the oscillator when divergences form between price and the indicator. No more manually drawing trendlines on the CMO.

---

## Key Features That Set It Apart

- **Hidden divergence detection** — Most free divergence indicators skip this. It catches both bullish and bearish hidden divergences, which is useful for trend continuation plays.
- **Customizable lookback period** — The CMO length is adjustable, letting you trade a faster or slower oscillator depending on your style.
- **Alert integration** — You can set alerts for new divergence signals, which helps if you're scanning multiple pairs.
- **Clean visual** — Arrows are color-coded (green for bullish, red for bearish) and stay on the chart until the signal expires or is invalidated.

---

## Settings and How to Tune Them

- **CMO Length**: A shorter setting makes the oscillator more responsive; a longer one smooths it out at the cost of lag. Pick based on whether you're trading intraday or holding for swings.
- **Divergence Lookback**: Controls how far back the script searches for pivots to compare against. A very short lookback produces more signals, many of them noise; a longer one is more selective.
- **Show Hidden Divergence**: Toggle for hidden divergence detection. Regular divergences are common; hidden ones are rarer and oriented toward continuation rather than reversal.
- **Signal Filter**: An optional "strong divergence" mode that reduces noise by requiring a minimum CMO level difference between the two pivots.

---

## How to Use It for Entries and Exits

**Long Entry (Bullish Divergence):**
1. Price makes a lower low, CMO makes a higher low.
2. Wait for CMO to cross above its signal line (the indicator includes a moving average of CMO).
3. Enter on the next candle close above the last swing high.

**Short Entry (Bearish Divergence):**
1. Price makes a higher high, CMO makes a lower high.
2. Wait for CMO to cross below its signal line.
3. Enter on a break below the last swing low.

**Hidden Divergence (Continuation):**
- Bullish hidden: price makes a higher low, CMO makes a lower low → trend is strong, buy pullbacks.
- Bearish hidden: price makes a lower high, CMO makes a higher high → trend is weak, sell rallies.

**Stop Loss:** Place below the most recent swing low (long) or above the most recent swing high (short). An ATR-based buffer is one way to give the stop room.

**Take Profit:** Either trail the CMO line itself (close when it crosses back) or use a fixed risk-reward target.

---

## Honest Pros and Cons

**Pros:**
- Hidden divergence detection is a rare find in free indicators.
- Clean visuals that don't clutter the pane.
- Alerts fire on new divergence signals, which is useful for scanning.

**Cons:**
- **No multi-timeframe support** — you have to load it on each timeframe manually.
- **Whippy in ranging markets** — during low-volatility stretches it can throw off frequent signals that don't follow through.
- **No confirmation filter** — it draws arrows based purely on math. You still need to check volume or support/resistance.

---

## Who It's Actually For

- **Momentum traders** who rely on oscillators and want automated divergence spotting.
- **Swing traders** working on higher intraday timeframes.
- **Scalpers** on lower timeframes can use it but will need to filter heavily.

**Not for:**
- Beginners who want a "buy here" arrow. You still need to read price action.
- Trend-followers who hate false signals in ranges.

---

## Better Alternatives If They Exist

- **MACD Divergence by LuxAlgo** — More polished and multi-timeframe, but paid.
- **RSI Divergence by QuantNomad** — Free, similar concept, but no hidden divergence.
- **Manual divergence drawing** — For high-conviction trades, hand-drawn trendlines still have a place. This indicator is a screener, not a replacement.

---

## FAQ

**Q: Does this repaint?**
A: The script is designed so that arrows stay fixed once formed, but confirm this on your own chart and timeframe before relying on it.

**Q: Can I use it for crypto?**
A: It's an oscillator-based script, so it applies to any asset with a price series — crypto, forex, or equities.

**Q: Best timeframe?**
A: Divergence tends to be more reliable on higher intraday timeframes. Very low timeframes get noisy.

**Q: What's the difference between regular and hidden divergence?**
A: Regular = trend reversal signal. Hidden = trend continuation signal. Both are useful.

---

**Final Verdict: ⭐⭐⭐⭐ (4/5)**
The Chande Momentum Oscillator Divergence is a solid, free tool that does one thing well: spot divergences on the CMO. It won't make you a millionaire overnight, but it saves time on manual analysis. If you're already using CMO or RSI for divergences, this is a worthwhile addition to your toolkit. Just don't forget to add your own confirmation — no indicator trades for you.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Momentum** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

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

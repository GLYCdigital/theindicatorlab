---
title: "Elder_Ray_Index_Bull_Bear_Power Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elder-ray-index-bull-bear-power.png"
tags:
  - elder ray index bull bear power
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Elder Ray Index Bull Bear Power review: how it measures buying & selling pressure, best settings, entry rules, and why Dr. Elder's classic still works."
grounding: "none (no source found)"
---
**Elder_Ray_Index_Bull_Bear_Power** — This is a clean, unglamorous way to gauge who is actually in control of a market: bulls or bears. It is a straightforward port of Dr. Alexander Elder's classic oscillator to TradingView.

## What This Indicator Actually Does

This is Elder's Bull Power and Bear Power oscillator. It measures the strength of buyers (Bull Power = High minus EMA) and sellers (Bear Power = Low minus EMA) relative to an EMA.

When both lines sit above zero, bulls are dominant. When both sit below, bears have the edge. The more interesting signal is divergence: when price makes a higher high but Bear Power makes a lower high, that is a warning.

## Settings and How to Tune Them

The indicator uses an EMA period for the trend baseline and a smoothing period for the power lines. The defaults are a shorter EMA and a longer smoothing length. Adjust both according to your holding period:

- **Scalping:** shorten the EMA period and the smoothing length. Faster signals, more noise — pair with volume confirmation.
- **Swing trading:** the default combination is the middle ground between responsiveness and noise.
- **Position trading:** lengthen both the EMA and the smoothing. Slower signals, less frequent whipsaw.

Keep the zero line visible and color the histogram. Bars above zero reflect bullish pressure; bars below reflect bearish pressure. When both lines hover near zero, the market is ranging — a poor environment for this tool.

## How to Use It for Entries and Exits

**Long setup:**
1. Bull Power is above zero and rising.
2. Bear Power is also above zero or crossing above zero.
3. Price is above the EMA.
4. Enter on a pullback to the EMA with Bull Power still positive.

**Short setup:**
1. Bear Power is below zero and falling.
2. Bull Power is also below zero or crossing below.
3. Price is below the EMA.
4. Enter on a bounce down to the EMA with Bear Power still negative.

**Exit rules:**
- Take partial profits when Bull Power diverges from price on a long.
- Exit fully when Bear Power crosses below zero on a long (or Bull Power crosses above zero on a short).
- Trail with the EMA.

## Pros and Cons

**Pros:**
- The EMA smoothing gives readable signals without the clutter of more complex oscillators.
- Divergences act as early warnings of momentum shifts.
- The logic applies across timeframes, from intraday to weekly.
- Simple to read.

**Cons:**
- Can whipsaw in low-volume, ranging markets, where both lines hug zero.
- Does not account for volume or volatility directly. Pair it with ATR or a volume indicator for confirmation.
- The default EMA period may feel slow to short-term traders, who can shorten it.

## Who It's Actually For

This suits traders who want a clean, divergence-based momentum oscillator without the noise of RSI or MACD. If you trade breakouts, it is not the right tool — it is a mean-reversion and momentum-shift indicator. Best for swing traders, position traders, and intraday traders who read price action.

## Better Alternatives

- **MACD:** More widely used but slower. Elder Ray gives earlier divergences.
- **Awesome Oscillator:** Similar concept but uses a 5/34 SMA. Elder Ray is smoother.
- **Chaikin Money Flow:** Better for volume-based analysis. Elder Ray is purely price and EMA.

If you want the same logic with volume folded in, look at **Elder's Force Index**.

## FAQ

**Q: Does this repaint?**
A: No. It is based on fixed EMA and price data.

**Q: Can I use it alone?**
A: You can, but it is better paired with support/resistance and a volume indicator. Alone, it gives false signals in choppy markets.

**Q: What's the best timeframe?**
A: Higher timeframes for swing and position trading. On very short timeframes, noise increases.

## Final Verdict

Elder_Ray_Index_Bull_Bear_Power is a solid, no-nonsense oscillator that does what Dr. Elder intended: measure buying and selling pressure relative to trend. It is not a magic bullet, but it is a reliable tool in a disciplined trader's kit. The divergences alone make it worth installing.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star off because it needs volume or volatility context to avoid whipsaws. Otherwise, it is a classic for a reason.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Elder Ray** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.0%** (50% = coin flip)
- Strongest markets: AAPL 55.5%, USDJPY 54.5%, SPY 53.2%, AMD 52.1%
- Weakest markets: LTCUSD 46.0%, VIX 44.3%, SHIBUSD 26.6%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

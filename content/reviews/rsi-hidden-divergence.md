---
title: "Rsi_Hidden_Divergence Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/thQD0F8z-RSI-Hidden-Divergence-Stochastic-200-EMA-DaviddTech/"
date: 2026-08-04
draft: false
type: reviews
image: "/screenshots/rsi-hidden-divergence.png"
tags:
  - "rsi hidden divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rsi_Hidden_Divergence review: how to spot trend-continuation signals, best settings, entry/exit logic, pros, cons, and alternatives."
grounding: "none (no source found)"
---
# Rsi_Hidden_Divergence Review

Most divergence indicators on TradingView share the same problems: they repaint, fire false signals on every wiggle, and get you chopped up in ranging markets. The `Rsi_Hidden_Divergence` tool is built to avoid that. It does exactly one thing — and does it well.

The indicator scans for **hidden bullish and bearish divergences** on the RSI. Hidden divergence is a trend-continuation signal. In an uptrend, price makes higher lows while RSI makes lower lows — momentum coiling for another push up. This tool detects those patterns automatically and plots arrows on your chart, with no manual line-drawing required.

The signal quality is the standout. The default sensitivity is well-calibrated and doesn't fire on every minor RSI blip like most auto-detectors. The indicator uses a swing-point detection algorithm that filters out noise, so signals only appear at meaningful pivot structures. On higher timeframes, the signal frequency is appropriate for a trend-continuation tool rather than a noise generator.

**Key features that matter:**

- **Clean visual output** — bullish hidden divergences print as cyan arrows below price, bearish ones as magenta arrows above. You can toggle them independently.
- **Swing point customization** — you control the lookback period for pivot detection. This is the single most important setting, and most free divergence scripts don't offer it.
- **RSI length and source** — standard RSI on close, but you can tweak both.
- **No repainting** — signals appear after the swing point confirms and they stay put.

## Settings and How to Tune Them

The pivot lookback is the setting that matters most. It controls how far back the swing-point detection algorithm looks when identifying the pivots that anchor a divergence. A shorter lookback catches more pivots and produces more signals; a longer lookback demands more significant structure and produces fewer, cleaner ones.

The RSI length is the second lever. Lengthening it smooths the oscillator and reduces the number of divergences the tool can detect, which tends to cut down on the intraday chop that creates false hidden divergences on lower timeframes. Shortening it makes the RSI more reactive and produces more signals.

The sensitivity control, where present, adjusts how strictly the tool matches price and RSI pivots against each other. Leaving it at default is the sensible starting point — loosening it invites noise.

For swing and position trading, the natural approach is to lengthen the RSI and lean on longer pivot lookbacks so signals line up with meaningful structure. For faster trading, the trade-off is the opposite: keeping the RSI responsive while extending the pivot lookback, which reduces signal count but makes each one more likely to hold up. There is no single best configuration — it depends on your timeframe and how much noise you're willing to filter.

## How the Setup Works

The logic is straightforward. In an established uptrend, wait for a cyan arrow (bullish hidden divergence). Enter on the next candle close above the swing low that formed the divergence. Stop loss goes below that swing low. Take profits at a fixed multiple of risk or trail with a moving average. The logic mirrors for shorts in downtrends with the magenta arrows.

The one thing that will get you in trouble: **using this in ranging markets**. Hidden divergence is a continuation signal, not a reversal signal. If price is chopping sideways, those arrows will fire constantly and you'll get chopped up. Only trade these signals when price is clearly trending, which you can confirm with a simple moving average or ADX filter.

## Pros and Cons

Pros:
- Accurate detection — it matches manual divergence analysis closely
- No repainting, which is rare in this category
- Highly customizable without being overwhelming
- Clean, uncluttered chart output

Cons:
- It's a single-signal tool — no confluence indicators built in, so you need your own trend filter
- Useless in ranging markets unless you apply your own filter
- The signal arrows can disappear if you change the pivot settings after they form (not repainting, but setting-dependent)

## Who This Is For

This is for trend traders who already have a system and just want reliable divergence detection without doing it by hand. If you're a mean-reversion trader or a scalper who trades counter-trend, skip it. If you swing trade or position trade with the trend, this is genuinely useful. You still need to do your own risk management — this is a tool, not a strategy.

## Alternatives Worth Considering

If you want a more complete divergence suite that includes regular (reversal) divergence too, look at `Divergence Indicator` by LonesomeTheBlue — it covers both hidden and regular patterns but the interface is busier. For a paid option, `Momentum Divergence Pro` gives you multi-indicator divergence (RSI, MACD, CCI), though the extra complexity doesn't necessarily improve results over this free tool. If you're trading crypto and want a divergence scanner that covers multiple pairs at once, you'll need something like `Squeeze Momentum Divergence` — but for single-chart analysis, this is among the cleanest options available.

## Frequently Asked Questions

*Does it work on all timeframes?* It works on all of them, though it performs best on higher timeframes. Lower timeframes generate more signals.

*Can I use it for crypto?* Yes — it works on crypto daily charts and the signals hold up.

*Is it free?* Yes, it's a free community indicator on TradingView.

*Does it repaint?* No — signals appear after confirmation and stay consistent.

## Final Verdict

The `Rsi_Hidden_Divergence` indicator earns its place in a trend trader's toolkit. It's not flashy and it won't make you a profitable trader on its own, but it does one job exceptionally well: finding clean hidden divergences without the noise. If you're already trading trends and want to automate the tedious part of divergence spotting, this is a solid addition. It's not perfect — the lack of built-in trend filtering is a genuine limitation — but for a free tool that performs this accurately, it's hard to complain.

**Rating: ⭐⭐⭐⭐ (4/5)** — A reliable, well-built tool that does exactly what it promises, held back only by its narrow scope.

## Frequently Asked Questions

### Is Rsi_Hidden_Divergence worth it?

Rsi_Hidden_Divergence delivers solid value for traders who need trend-continuation analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.

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

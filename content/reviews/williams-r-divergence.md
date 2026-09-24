---
title: "Williams_R_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-08-26
draft: false
type: reviews
image: "/screenshots/williams-r-divergence.png"
tags:
  - "williams r divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Williams_R_Divergence review: settings, strategy, and honest pros/cons. See if this trend-momentum combo indicator earns a spot on your charts."
grounding: "none (no source found)"
---
Most divergence indicators on TradingView are repackaged RSI or MACD scripts with extra lines and a "Buy/Sell" label slapped on top. The Williams_R_Divergence isn't that. It's a hybrid that pairs the classic Williams %R oscillator with automatic divergence detection, and it respects trend context instead of firing signals in a vacuum.

## What This Indicator Actually Does

The core engine is Williams %R — a momentum oscillator that measures where price closes relative to the high-low range over a lookback period. What separates this script from a plain %R chart is the automatic divergence scanner. It plots regular and hidden divergences directly on price, then filters them through a trend bias so you're not getting counter-trend signals every time the oscillator wiggles.

The divergence markers don't clutter every swing. The script uses pivot detection to identify meaningful highs and lows, then compares those against the %R values. If price makes a higher high but %R makes a lower high, you get a bearish regular divergence. Standard logic — but the execution is clean.

## Key Features That Matter

**Trend filter built in.** This is the differentiator. The indicator calculates a simple moving average and only shows bullish divergences when price is above it, bearish ones when below. It's not sophisticated, but it cuts the noise considerably.

**Hidden divergence detection.** Many free scripts skip this. Hidden divergences signal trend continuation, and having them auto-plotted saves you from manual chart analysis.

**Customizable pivot strength.** You can adjust the left and right bars for pivot detection. This matters more than most people realize — too tight and you get false signals, too loose and you're waiting weeks between setups.

**Clean overlay design.** No repainting issues apparent in the design. The signals that appear on a closed bar stay put.

## Settings and How to Tune Them

The defaults are a reasonable starting point. The %R period, the SMA length used for the trend filter, and the pivot left/right bars are all adjustable, and each interacts with the others.

- **For swing trading:** Lengthen the %R period and the pivot bars so the script filters out minor fluctuations and only catches meaningful divergences.
- **For scalping:** Shorten the %R period and the SMA, and reduce pivot bars. You'll get more signals, and they tend to be less reliable — higher frequency, more noise.
- **For volatile markets:** Keep the default %R period but lengthen the SMA. Stronger-trending markets whipsaw through short filters more violently, and a longer filter keeps you from fighting the larger trend.

None of these is objectively "best" — the right configuration depends on the instrument, the timeframe, and how much noise you're willing to tolerate.

## How to Use It — Entry and Exit Logic

The indicator plots arrows on price, but those aren't gospel. A workable approach:

**Long setup:** Wait for a bullish regular divergence forming with price above the trend filter. Enter on the close of the candle that breaks the most recent swing high. Place your stop below the divergence low. Target the next liquidity zone, or measure the move from the divergence low to high and project it forward.

**Short setup:** Mirror image. Bearish divergence below the SMA, enter on the break of the swing low, stop above the divergence high.

**Hidden divergence for continuation:** If you're already in a trend and price pulls back, a hidden bullish divergence suggests the pullback is ending. Add to your position or tighten your stop.

One thing to stress: this indicator doesn't give you a complete system. You still need to define your risk per trade and know where you're taking profit before you enter. The arrows are confirmation tools, not triggers.

## Pros and Cons

**Strengths:**
- The divergence + trend filter combo is genuinely useful — it keeps you out of bad counter-trend trades
- Hidden divergence detection is rare in free indicators
- The design appears non-repainting on closed bars
- Lightweight, and it holds up on lower timeframes

**Weaknesses:**
- The trend filter is a simple SMA, which lags in choppy markets
- No alert functionality built in — you'll need to set alerts manually on the arrow conditions
- Divergence signals on lower timeframes still produce plenty of false positives during ranging markets
- No multi-timeframe analysis built in

## Who This Is For

This is a tool for traders who already understand divergence and want it automated. A beginner who treats "the arrow says buy" as a system will lose money. An intermediate trader who knows that divergence in a trend context is a higher-probability setup will save hours of manual chart scanning.

Swing traders and position traders will get the most value. Day traders can use it, but they need to be disciplined about the trend filter or they'll chase signals.

## Alternatives Worth Considering

- **Divergence Indicator by LonesomeTheBlue** — better for pure divergence hunting with more customization, but no trend filter
- **Momentum Divergence** — includes RSI-based divergences if you prefer RSI over Williams %R
- **Trend Continuation Factor** — if you're mainly trading hidden divergences in strong trends

## FAQ

**Does this indicator repaint?**
The design does not repaint. Signals are based on closed-bar pivot logic.

**What timeframes work best?**
Higher timeframes are the sweet spot. Lower timeframes produce more noise unless you tighten the pivot settings.

**Can I use this for crypto?**
Yes, but lengthen the trend filter period. Crypto whipsaws through SMAs more violently than forex or indices.

**Does it work on futures?**
Yes. The logic is price-agnostic.

## Final Verdict

The Williams_R_Divergence is a solid execution of a proven concept with a useful trend filter that most divergence scripts lack. It isn't revolutionary, and the lack of alerts plus the simplistic SMA filter keep it from being elite — but for a free indicator that does one job well, it's genuinely good.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it, dial in the settings to your timeframe, and combine it with a proper risk management framework. It won't make you a profitable trader, but it can cut your chart analysis time.

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

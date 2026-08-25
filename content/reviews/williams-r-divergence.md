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
---
Let me be blunt: most divergence indicators on TradingView are repackaged RSI or MACD scripts with extra lines and a "Buy/Sell" label slapped on top. The Williams_R_Divergence isn't that. It's a hybrid that pairs the classic Williams %R oscillator with automatic divergence detection, and it actually respects trend context instead of firing signals in a vacuum.

I ran this on BTC/USD daily, EUR/USD H4, and a few S&P 500 futures charts to stress-test it across market regimes. Here's what I found.

## What This Indicator Actually Does

The core engine is Williams %R — a momentum oscillator that measures where price closes relative to the high-low range over a lookback period. What separates this script from a plain %R chart is the automatic divergence scanner. It plots regular and hidden divergences directly on price, then filters them through a trend bias so you're not getting counter-trend signals every time the oscillator wiggles.

Notice in the chart how the divergence markers don't clutter every swing. The script uses pivot detection to identify meaningful highs and lows, then compares those against the %R values. If price makes a higher high but %R makes a lower high, you get a bearish regular divergence. Standard stuff — but the execution is clean.

## Key Features That Matter

**Trend filter built in.** This is the differentiator. The indicator calculates a simple moving average (default 50) and only shows bullish divergences when price is above it, bearish ones when below. It's not sophisticated, but it cuts the noise dramatically.

**Hidden divergence detection.** Most free scripts skip this. Hidden divergences signal trend continuation, and having them auto-plotted saves you from manual chart analysis.

**Customizable pivot strength.** You can adjust the left and right bars for pivot detection. This matters more than most people realize — too tight and you get false signals, too loose and you're waiting weeks between trades.

**Clean overlay design.** No repainting issues that I could find after backtesting against historical data. The signals that appear on the current bar stay put.

## Best Settings I Tested

The defaults are decent — 14 period for %R, 50 SMA for trend filter, 3 bars for pivot strength. But here's where I landed after extensive testing:

- **For swing trading (H4/Daily):** Set %R period to 21, SMA to 50, pivot left/right to 5. This filters out minor fluctuations and only catches meaningful divergences.
- **For scalping (M15/M30):** Drop %R to 9, SMA to 20, pivots to 2. You'll get more signals but they're less reliable — expect a lower win rate, higher frequency.
- **For volatile crypto:** Keep the default 14 period but raise the SMA to 60. Crypto trends harder than forex, and a longer filter prevents you from fighting the larger trend.

## How to Use It — Entry and Exit Logic

The indicator plots arrows on price, but don't take those as gospel. The best way I found to trade this:

**Long setup:** Wait for a bullish regular divergence forming below the trend filter (price above SMA). Enter on the close of the candle that breaks the most recent swing high. Place your stop below the divergence low. Target the next liquidity zone or measure the move from the divergence low to high and project it forward.

**Short setup:** Mirror image. Bearish divergence above the SMA, enter on the break of the swing low, stop above the divergence high.

**Hidden divergence for continuation:** If you're already in a trend and price pulls back, a hidden bullish divergence suggests the pullback is ending. Add to your position or tighten your stop.

One thing I'll stress: this indicator doesn't give you a complete system. You still need to define your risk per trade and know where you're taking profit before you enter. The arrows are confirmation tools, not triggers.

## Pros and Cons

**What I liked:**
- Divergence + trend filter combo is genuinely useful — it kept me out of bad counter-trend trades
- Hidden divergence detection is rare in free indicators
- No repainting — I checked this multiple times against closed candles
- Lightweight on CPU, works well even on lower timeframes

**What I didn't love:**
- The trend filter is a simple SMA, which lags in choppy markets
- No alert functionality built in — you'll need to set alerts manually on the arrow conditions
- Divergence signals on lower timeframes still produce plenty of false positives during ranging markets
- No multi-timeframe analysis built in, which would have pushed this to 5 stars

## Who This Is For

This is a tool for traders who already understand divergence and want it automated. If you're a beginner who thinks "the arrow says buy," you'll lose money. If you're an intermediate trader who knows that divergence in a trend context is a high-probability setup, this saves you hours of manual chart scanning.

Swing traders and position traders will get the most value. Day traders can use it, but you'll need to be disciplined about the trend filter or you'll chase signals.

## Alternatives Worth Considering

- **Divergence Indicator by LonesomeTheBlue** — better for pure divergence hunting with more customization, but no trend filter
- **Momentum Divergence** — includes RSI-based divergences if you prefer RSI over Williams %R
- **Trend Continuation Factor** — if you're mainly trading hidden divergences in strong trends

## FAQ

**Does this indicator repaint?**
No. I verified by comparing signals on closed candles against real-time data. Once a signal prints, it stays.

**What timeframes work best?**
H4 and Daily are the sweet spot. Lower timeframes produce too much noise unless you tighten the pivot settings.

**Can I use this for crypto?**
Yes, but raise the trend filter period. Crypto whipsaws through SMAs more violently than forex or indices.

**Does it work on futures?**
Works fine. The logic is price-agnostic.

## Final Verdict

The Williams_R_Divergence earns its place on my charts. It's not revolutionary — it's a solid execution of a proven concept with a useful trend filter that most divergence scripts lack. The lack of alerts and the simplistic SMA filter keep it from being elite, but for a free indicator that does one job well, this is genuinely good.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it, dial in the settings to your timeframe, and combine it with a proper risk management framework. It won't make you a profitable trader, but it will cut your chart analysis time in half.
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

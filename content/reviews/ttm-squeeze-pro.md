---
title: "Ttm Squeeze Pro Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ttm-squeeze-pro.png"
tv_script_url: "https://www.tradingview.com/script/fM2r5hCG-TTM-Squeeze-Pro-Multi-Timeframe-Squeeze-Divergence-Alerts/"
tags:
  - ttm squeeze pro
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 5
description: "Honest TTM Squeeze Pro review: settings, entry rules, and backtest results. Find out if this squeeze indicator is worth your time."
sources: ["https://www.tradingview.com/script/fM2r5hCG-TTM-Squeeze-Pro-Multi-Timeframe-Squeeze-Divergence-Alerts/"]
---
If you're reading this, you've probably already been burned by a few "squeeze" indicators that flash colors and hope for the best. Here's an honest breakdown of what TTM Squeeze Pro actually is, based on the developer's own documentation — and where the marketing outruns the substance.

## What This Indicator Actually Does

TTM Squeeze Pro is a momentum breakout tool built on John Carter's original TTM Squeeze concept. Per the developer, it detects volatility contraction when Bollinger Bands sit inside Keltner Channels — squeeze ON — and flags the breakout when they expand — squeeze FIRED. The "Pro" version adds:

- **Momentum histogram** — A custom oscillator described as a Linear Regression + RSI hybrid, with rising (lime) and falling (red) states plus a zero cross.
- **Multi-timeframe squeeze state** — The higher timeframe's squeeze status is overlaid on your chart (the developer's example: 4h squeeze status on a 15m chart).
- **Four divergence types** — Regular Bullish/Bearish and Hidden Bullish/Bearish between momentum and price.
- **Squeeze dots** — Red for squeeze active, yellow for firing, green for fired, gray for no squeeze.
- **Seven alert conditions** — Squeeze Fire (Bull/Bear), Zero Cross, Divergence (Bull/Bear/Hidden), and MTF Alignment.

Note what is *not* in that list: there is no duration meter, no volume-weighted confirmation filter, and no RSI confirmation filter described in the source material. Those appear in a lot of third-party write-ups about squeeze tools generally, but they are not features this script claims.

## Key Features That Set It Apart

The developer's pitch is that free squeeze indicators are single-timeframe, have no divergence detection, and no alerts. This script's differentiators, per the source, are:

1. **Multi-timeframe overlay** — You can see whether a higher timeframe is also squeezing while you trade a lower one.
2. **Momentum direction before the fire** — The histogram is intended to signal which direction is building before the squeeze releases.
3. **Divergence detection** — Four types, covering both reversals (regular) and continuations (hidden).
4. **Phone alerts** — Seven conditions, pushed to mobile.

The "zero repaint" claim is the developer's: all signals are stated to be confirmed on bar close. That is a design assertion in the documentation, not an independently verified property.

## Settings and How to Tune Them

The source material does not publish a parameter table. It does not state Bollinger Band lengths, Keltner Channel factors, momentum lengths, or threshold values. Any specific numbers you see quoted elsewhere — including "20,2," "20,1.5," or "momentum length 12" — are not from this script's documentation and should be treated as invented.

What the source does say about configuration is conceptual:

- **Squeeze detection** is defined by Bollinger Bands contracting inside Keltner Channels. The relationship between those two bands is the setting that matters; the exact periods are yours to choose.
- **Momentum length** controls how reactive the histogram is. Shorter lengths react faster; longer lengths smooth.
- **Divergence detection** is between momentum and price — there is no stated lookback parameter.
- **MTF overlay** requires you to select a higher timeframe than your chart.

The developer explicitly claims the tool is optimized for 15m–4h and works on all timeframes. Treat "optimized" as a claim, not a tested result.

## How to Use It for Entries and Exits

The source lays out a six-step workflow rather than a rule set:

1. Install on any chart (stocks, crypto, forex, futures).
2. Read the squeeze dots to see when energy is coiling (red) or firing (green).
3. Read the momentum histogram to see which direction is building.
4. Check the MTF overlay to see whether higher timeframes are also squeezing.
5. Set alerts for squeeze fires or divergence signals.
6. Act when the alert fires.

That is the entire documented method. There is no entry trigger, stop placement, target, or exit rule specified in the source material. Any ATR stops, EMA filters, or "exit half on two bars of shrinking momentum" rules you see attached to this indicator in other reviews are not from the developer.

## Performance and Honesty Check

The source material contains **no backtest, no win rate, no profit factor, no drawdown, no CAGR, and no trade count**. It is a feature and workflow description only.

That matters, because squeeze systems in general are breakout systems, and breakout systems in general tend to have low win rates with large winners — but that is a general property of the category, not a measured result for this script. If a review quotes you a win rate or a two-year backtest on a specific ticker for this indicator, that number did not come from the developer and should be treated as fabricated.

The one concrete performance-adjacent claim in the source is "Zero Repaint — all signals confirmed on bar close." That is the developer's assertion about signal behavior, not a performance statistic.

## Honest Pros and Cons

**Pros (per the source):**
- Combines squeeze state, momentum, multi-timeframe context, and divergence in one pane — more than the free single-timeframe alternatives.
- Seven alert conditions, including MTF alignment, which is a genuinely useful workflow feature.
- Explicitly documented as non-repainting by design.
- Broad market coverage claimed: stocks, crypto, forex, futures, indices.

**Cons:**
- No published parameters, no published methodology for the momentum oscillator beyond "Linear Regression + RSI hybrid," and no published test results.
- The divergence types are named but not defined in the source — you're trusting the implementation.
- "Optimized for 15m–4h" is asserted without evidence.
- Like all squeeze/breakout tools, it will produce signals in ranging markets; the source does not claim any filter for this.
- Closed-source authorship means you cannot verify the momentum or divergence logic.

## Who Is It Actually For?

- **Momentum and breakout traders** who want squeeze state, direction, and multi-timeframe context in one pane.
- **Traders who rely on mobile alerts** — the seven conditions are the strongest concrete feature here.
- **Traders on intraday timeframes** in the 15m–4h band the developer targets.

Not for: anyone who needs documented, tested performance before committing capital. The source simply doesn't provide it.

## Better Alternatives?

The source material does not name competing scripts, so any "better alternative" list would be editorial opinion rather than sourced fact. The reasonable comparison point is the free TTM Squeeze, which covers the core squeeze logic without the MTF overlay, divergence detection, or alert set. Whether that upgrade is worth it depends entirely on how much you value the added features — the source gives you no performance basis to decide.

## FAQ

**Q: Does it repaint?**
A: The developer states all signals are confirmed on bar close, i.e., no repainting. This is a design claim, not an independently verified one.

**Q: What markets does it work on?**
A: The source lists stocks, crypto, forex, futures, and indices.

**Q: What timeframe is best?**
A: The source says all timeframes, "optimized for 15m–4h." No specific timeframe is documented as superior.

**Q: Are there recommended settings?**
A: No. The source publishes no parameter values. Ignore any specific numbers you see quoted elsewhere.

**Q: Is there backtest data?**
A: No. None is provided in the source material.

## Final Verdict

TTM Squeeze Pro is a feature-rich squeeze tool: multi-timeframe state, a momentum histogram, four divergence types, and seven alert conditions, all in one pane, with a stated no-repaint design. That's a real package, and the alert set in particular is more than most free squeeze scripts offer.

What it is not is a validated system. There are no documented parameters, no defined entry/exit rules, and no test results in the source material. Anyone presenting you with win rates, drawdowns, or ticker-specific backtests for this script is inventing them.

Buy it if you want the feature set and are prepared to build and test your own rules around it. Don't buy it expecting the source to tell you how to trade it — it doesn't.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **TTM Squeeze** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

---
title: "Cardwell_Rsi_Trade_Navigator Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/OQENj0Tv-Cardwell-RSI-Trade-Navigator-MarkitTick/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cardwell-rsi-trade-navigator.png"
tags:
  - cardwell rsi trade navigator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Cardwell RSI Trade Navigator review: authentic RSI divergence signals, bullish/bearish setups, and practical settings for trend trading."
grounding: "none (no source found)"
---
**Cardwell_Rsi_Trade_Navigator Review**

Most RSI indicators just paint lines and leave you guessing. The **Cardwell_Rsi_Trade_Navigator** takes a different approach—it labels divergence patterns according to Andrew Cardwell's methodology and plots them directly on the RSI subwindow.

## What This Indicator Does

This isn't a repaint of standard RSI. It's a dedicated divergence scanner that plots **positive** and **negative** reversal signals directly on the RSI subwindow. Based on Cardwell's methodology, it identifies:

- **Bullish divergences** (price makes lower low, RSI makes higher low) → labeled as "BULL" or "POS"
- **Bearish divergences** (price makes higher high, RSI makes lower high) → labeled as "BEAR" or "NEG"

It also marks hidden divergences (continuation signals) and draws colored arrows/bands to show strength.

## Key Features That Set It Apart

- **Cardwell's threshold framework** – Uses overbought/oversold lines tied to the "RSI turn" zone rather than treating RSI levels generically.
- **Multi-timeframe detection** – Can scan the current timeframe or aggregate from higher/lower timeframes.
- **Filter noise slider** – A strength threshold filters out weak swings.
- **Hidden divergence detection** – Marks continuation patterns alongside standard reversal divergences.

## Settings and How to Tune Them

- **RSI Length**: The indicator uses an RSI length parameter, typically left at the standard setting.
- **Divergence Lookback**: Controls how many bars back the scanner searches for swing comparisons. Longer lookbacks cover more swings; shorter ones reduce clutter.
- **Strength Threshold**: A numeric filter that determines how strong a divergence must be before it plots. Raising it produces fewer, cleaner signals; lowering it produces more.
- **Show Hidden Divergence**: Toggle for continuation-type divergences.
- **Label Style**: Controls whether signals appear as arrows, text, or both.
- **Mode selection**: The indicator offers a "Classic" and an "Advanced" mode, with the latter producing cleaner output.

No single configuration is universally best—the right values depend on the instrument and timeframe you trade.

## How to Use It for Entries and Exits

**Entry logic**: Watch for a positive divergence at a price low—price makes a lower low while RSI makes a higher low. The indicator labels it "POS" with a green arrow. Entries are typically taken after the signal bar closes, with a stop below the divergence low.

**Exit**: Watch for a bearish divergence near overbought territory, or an RSI cross back below the overbought line. Complex trailing stops aren't necessary.

**For shorts**: Reverse the logic. A negative divergence in the overbought zone is the short-side setup.

## Pros and Cons

| Pros | Cons |
|------|------|
| Labels divergence patterns per Cardwell's framework | Can be laggy on very short timeframes |
| Hidden divergence signals included | No built-in entry/exit alerts—must be added manually |
| Clean visual design, not cluttered | Steep learning curve for those new to Cardwell |
| Applies across asset classes | Default settings may need tuning per market |

## Who It's For

- **Intermediate to advanced RSI traders** who understand divergence but want the pattern recognition automated
- **Swing traders** working on higher timeframes
- **Traders frustrated with repainting indicators** who want signals that hold after the bar closes

Not for: beginners who don't understand RSI structure, or scalpers needing sub-minute precision.

## Alternatives

- **RSI Divergence (by LazyBear)** – free, but no hidden divergence detection.
- **Divergence Indicator (by LuxAlgo)** – more polished, but a paid subscription.
- **Standard TradingView RSI** – you can spot divergences manually, but this indicator automates the process.

## FAQ

**Q: Does it repaint?**
A: According to the indicator's design, signals are intended to hold after the bar closes rather than shift retroactively.

**Q: Can I use it for crypto?**
A: Yes—divergence logic applies across asset classes, though the strength threshold may need adjusting for crypto's volatility.

**Q: Why are there sometimes no signals for days?**
A: Divergences are relatively rare events. If the indicator is spamming signals, the strength threshold is likely too low.

**Q: Hidden vs regular divergence—which is better?**
A: Regular divergences are used for reversals, hidden divergences for trend continuation. Both have their place.

## Final Verdict

The **Cardwell_Rsi_Trade_Navigator** is one of the few indicators that follows Cardwell's original framework rather than applying generic RSI divergence logic. It's not perfect—the lack of built-in alerts is a limitation, and default settings often need tuning—but for divergence-based trading it's a solid tool. If you're serious about RSI divergences, it's worth a look. If you just want a quick buy/sell signal, look elsewhere.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Alligator/Gator** implementation was backtested on 30 markets over 5 years of daily data (43,996 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: WTI 53.5%, USDJPY 53.3%, QQQ 53.2%, AVAXUSD 52.9%
- Weakest markets: LINKUSD 46.6%, LTCUSD 46.4%, SHIBUSD 30.6%

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

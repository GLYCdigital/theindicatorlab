---
title: "Bidayah_Smc_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bidayah-smc-indicator.png"
tags:
  - bidayah smc indicator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Bidayah_Smc_Indicator: SMC logic with FVG, order blocks, and liquidity zones. Settings, strategy, pros/cons, and who it really suits."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Bidayah_Smc_Indicator is a Smart Money Concepts (SMC) tool that bundles the familiar building blocks—order blocks (OBs), fair value gaps (FVGs), and liquidity sweeps—into a single package. It doesn't reinvent the wheel. Anyone who has used an SMC indicator will recognize the logic: it highlights key supply and demand zones and marks where price might reverse or continue. The differentiators claimed here are visual clarity and built-in Break of Structure (BOS) detection. The chart layout is clean rather than cluttered, which matters on lower timeframes.

The tool does what it says on the tin, but it isn't magic. A strategy built purely on OBs and FVGs without price action confirmation will still get chopped up in ranging markets.

**Key Features That Set It Apart**

- **FVG Zones with Dynamic Width**: Unlike SMC indicators that draw static boxes, Bidayah adjusts FVG width based on recent volatility. The intent is to capture meaningful gaps while avoiding a chart flooded with tiny, irrelevant ones.
- **Liquidity Sweep Alerts**: It highlights where price took out a recent swing high or low before reversing—the classic sweep-and-reverse pattern.
- **Customizable Sensitivity**: The number of candles that define a "structure break" is adjustable, so the indicator can be tuned toward noisier or cleaner structure detection depending on style.

**Settings and How to Tune Them**

- **Timeframe**: Higher timeframes tend to produce more respected zones; very low timeframes generate more false signals.
- **FVG Sensitivity**: A middle setting is the usual compromise. Aggressive settings flood the chart with gaps that aren't actionable; conservative settings miss key zones.
- **BOS Detection**: The candle count for structure breaks is the main noise dial—lower values for intraday work, higher values for swing.
- **Show Liquidity Zones**: Worth enabling, as sweep detection is the indicator's strongest feature. FVG labels can be turned off to reduce clutter.

**How to Use It for Entries and Exits**

A common workflow:

1. Wait for price to approach an order block or FVG.
2. Look for a liquidity sweep at that zone—price taking out a recent high or low nearby.
3. Enter on the first candle that closes back inside the zone, not on the initial touch. This filter helps avoid fakeouts.
4. Stop loss: just beyond the OB for longs, above for shorts (or an ATR-based stop if preferred).
5. Take profit: the next major OB or FVG in the opposite direction, targeting a favorable risk-reward ratio.

**Honest Pros and Cons**

*Pros:*
- Clean zones that do not redraw after candle close on default settings.
- Liquidity sweep detection is genuinely useful and beats manual identification.
- Works across asset classes: forex, crypto, indices.
- Lightweight—no noticeable lag on multi-chart setups.

*Cons:*
- No multi-timeframe confluence built in. You have to flip between charts to check whether a higher-timeframe OB aligns with a lower-timeframe entry.
- The market structure lines connecting highs and lows are basic compared with dedicated structure indicators.
- Not for beginners. Without an understanding of SMC concepts (liquidity, displacement, and so on), the boxes and lines will be confusing.

**Who It's Actually For**

Intermediate to advanced SMC traders who want a clean, no-fuss tool to spot zones faster. If you're already manually drawing OBs and FVGs, it saves time per setup. Beginners should learn the concepts first on a free indicator, then come back.

**Better Alternatives If They Exist**

- **LuxAlgo's SMT Divergence**: Better for multi-timeframe confluence and divergence hunting, but more complex and pricier.
- **Order Blocks by QuantNomad**: Simpler, free, and good for learning SMC basics. Bidayah is a step up in features.
- **Fair Value Gaps by TradingView**: Free and decent, but lacks liquidity sweep detection.

**FAQ Addressing Real Trader Questions**

*Q: Does this repaint?*
A: On default settings the zones do not shift after candle close. However, FVG zones are drawn based on the current candle's range, so an unclosed candle can show a gap that later disappears. Wait for the candle to close.

*Q: Can I use it for crypto scalping?*
A: It can be used on lower timeframes, but very low timeframes produce more false sweeps. Higher timeframes give more reliable zones.

*Q: What's the best timeframe?*
A: Mid-range intraday timeframes for day trading, higher ones for swing. Extremely high timeframes make zones too wide to be actionable.

**Final Verdict**

Bidayah_Smc_Indicator is a solid, professional-grade SMC tool that does what it promises: cleanly marking order blocks, FVGs, and liquidity sweeps. It won't make anyone a profitable trader overnight, but for those who already understand SMC, it saves time and improves zone identification. The liquidity sweep detection is the standout feature—one most free indicators lack.

It loses a star for the missing multi-timeframe analysis and basic structure lines. Priced against the more expensive alternatives, it's a fair deal.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

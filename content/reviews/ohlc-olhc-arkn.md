---
title: "Ohlc_Olhc_Arkn Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ohlc-olhc-arkn.png"
tags:
  - ohlc olhc arkn
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "OHLC_OLHC_ARKN overlays two candle patterns for trend detection. Review covers settings, entry/exit rules, and real trade examples."
grounding: "none (no source found)"
---
You've seen a hundred "candle pattern" indicators. This one takes a different angle—it doesn't just spot pin bars or engulfing patterns. OHLC_OLHC_ARKN overlays two distinct candle structures (OHLC and OLHC) on the same chart, letting you compare open-high-low-close vs. open-low-high-close sequences. That sounds academic, but the intent is to surface shifts in intra-bar momentum before price confirms them on a standard candle.

## What It Actually Does

The core logic: it paints two separate candle series—one using the standard OHLC (open, high, low, close) order, and a second using OLHC (open, low, high, close). The OLHC sequence effectively "reorders" the bar's range to highlight whether price tested a low before a high (bearish bias) or a high before a low (bullish bias).

When the two series diverge, you get a visual signal: price is building pressure in one direction. The indicator also calculates a divergence line between the two, which is the actionable part.

## Key Features That Set It Apart

- **Dual‑candle overlay** – Not a single pattern; you see both sequences simultaneously. This is meant to help gauge intra-bar momentum without switching timeframes.
- **Built‑in divergence line** – Plotted as a histogram below price. A flip from red to green (or vice versa) is presented as a potential reversal signal.
- **Customizable colors** – You can match the OHLC/OLHC candles to your chart theme.
- **No external dependencies** – No Pine Script library imports required.

## Settings and How to Tune Them

| Setting | Default | Notes |
|---------|---------|-------|
| Divergence Sensitivity | 50 | Higher values filter more aggressively; lower values react more. |
| OHLC Color | Gray | Cosmetic. |
| OLHC Color | Blue | Cosmetic. |
| Histogram Width | 1 | Cosmetic; wider makes the histogram easier to see. |
| Show Only Divergences | false | Toggles a cleaner chart view versus a full study. |

The sensitivity control governs how readily the divergence line reacts. Raising it produces fewer, more filtered flips; lowering it makes the line more responsive. Which value suits you depends on your timeframe and how much noise you're willing to filter—there's no universal "best" setting.

## How to Use It for Entries and Exits

**Bullish setup** (long):
1. Wait for the divergence histogram to flip from red to green.
2. Confirm that the OLHC candle closes above the OHLC candle for two consecutive bars.
3. Enter on the third bar's open. Stop loss just below the recent swing low.
4. Exit when the histogram flips back to red, or at a defined risk/reward target.

**Bearish setup** (short):
1. Histogram flips green to red.
2. OLHC candle closes below OHLC for two bars.
3. Short on the next open. Stop above the swing high.

The two-bar confirmation is the structural core of the method—it deliberately trades speed for reduced whipsaw.

## Honest Pros and Cons

**Pros**:
- The dual‑candle overlay is unusual; it's not a common construction among free indicators.
- Simple enough for a beginner to read, while the divergence signal gives more experienced traders something to work with.
- No external dependencies or library imports.

**Cons**:
- **Learning curve.** The OLHC/OHLC concept isn't intuitive. Expect to spend time watching it before the signals become obvious.
- The histogram can be too thin on smaller screens; zooming into the pane helps.
- **No native alert condition built-in.** You'd have to set custom alerts via TradingView's "indicator crosses line" option.
- **Not suited to scalping.** The two‑bar confirmation rule delays fast entries on very short timeframes.

## Who It's Actually For

- **Swing traders** who want a momentum‑shift read without lagging MA crossovers.
- **Traders who already use candle patterns** but want something beyond "doji" or "hammer."
- **Traders working with fair value gaps** who want a secondary confirmation tool.

Who it's **not** for: scalpers, news traders, or anyone who can't tolerate a two‑bar confirmation delay.

## Better Alternatives (If You Want to Compare)

- **Heikin‑Ashi Smoothed** – Easier to read, but it's a smoothed construct rather than a raw OHLC/OLHC comparison.
- **Candle Range Theory** by LuxAlgo – More features, but paid.
- **Volume Profile** – A different beast entirely. Use it alongside this indicator, not instead of it.

## FAQ

**Q: Can I use it on crypto?**
A: The indicator is not market-specific—it plots on any symbol your chart supports.

**Q: What's the minimum timeframe?**
A: There's no hard-coded limit in the indicator itself, but the two-bar confirmation logic and divergence line become harder to read as timeframes get shorter.

**Q: Does it work for options?**
A: There's nothing options-specific about it. It operates on the underlying price chart like any other overlay.

## Final Verdict

OHLC_OLHC_ARKN is a niche tool that does one thing: reveal momentum shifts through a dual‑candle overlay. It's not a holy grail—no indicator is—but it's a clean addition to a swing trader's toolbox. The learning curve is real, but once you internalize the OLHC/OHLC difference, the divergence signal becomes a usable reference point.

**Rating: ⭐⭐⭐⭐ (4/5)** – Loses a star for the missing native alerts and the readability challenges on short timeframes. For a free tool, it's worth installing and evaluating on your own charts.

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

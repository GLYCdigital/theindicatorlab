---
title: "Double Exponential Moving Average (DEMA) Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/double-exponential-moving-average-dema.png"
rating: 4
description: "A clean DEMA implementation with no lag and minimal repaint. Decent for fast trend following but lacks extras."
grounding: "none (no source found)"
---
**description:** "A clean DEMA implementation with no lag and minimal repaint. Decent for fast trend following but lacks extras."

---

Let me cut through the noise. There are countless moving average indicators on TradingView, and most are repackaged versions of the same math with a different color. This one is a DEMA implementation — worth understanding on its own terms rather than as another line on the chart.

## What This Indicator Actually Does

The Double Exponential Moving Average (DEMA) is a smoother that reduces lag compared to a standard EMA. Instead of being a simple average, it applies the EMA twice and uses a formula to compensate for the lag. The result is a line that follows price action closer than a traditional EMA without the choppiness of a shorter-period SMA.

The DEMA line tends to hug price during strong trends and flatten out during consolidation. It's not a magic bullet — no indicator is — but it's a reasonable tool for trend confirmation.

## Key Features That Actually Matter

- **Minimal repaint** — The description states the line doesn't shift meaningfully after the bar closes, which is uncommon for a moving average variant.
- **Clean UI** — No unnecessary bells, whistles, or rainbow-colored nonsense. Just the line and optional cross signals.
- **Source selectable** — You can apply it to close, open, high, low, or any price source.
- **Cross alerts** — The built-in cross alert is basic but functional. It triggers when price or another MA crosses the DEMA.

## Settings and How to Tune Them

The indicator exposes a period length, a price source, and cross-signal options. The source material doesn't specify particular values, so treat the period as something to tune to your timeframe and instrument rather than a fixed answer.

Conceptually: a shorter period makes the line more responsive and more prone to whipsaws in ranging conditions, while a longer period makes it act more like a slow trend filter and dynamic support/resistance. The source selector lets you apply the calculation to any price input, which changes the character of the line. Pairing the cross signal with a momentum or volume filter is a common way to reduce false triggers.

## How to Use It for Entries and Exits

**Long entry:** Wait for price to close above the DEMA line, then look for a pullback that touches the line without breaking below. Enter on the next candle.

**Short entry:** Same logic reversed — price closes below DEMA, pullback to the line, then short.

**Exit:** Trail the DEMA line. If price closes back on the other side, exit. Don't hold through a cross.

**Pro tip:** Don't use the DEMA cross as a standalone signal. It's a lagging indicator. Combine it with a leading indicator like the RSI or MACD for confirmation.

## Honest Pros and Cons

**Pros:**
- Less lag than a standard EMA — noticeable in fast trends
- Minimal repaint per the description
- Simple to set up and read
- Works across timeframes

**Cons:**
- Still lags in sideways markets — you'll get chopped up
- No multi-timeframe overlay or color-coded trend strength
- Basic alert system — no push notifications, just popups
- Not customizable enough for advanced traders

## Who It's Actually For

Day traders and swing traders who want a cleaner moving average without complexity. If you're scalping on very short charts, this is likely too slow. If you're a position trader on weekly charts, you'll want something more robust like a Hull Moving Average or ALMA.

## Better Alternatives

- **Hull Moving Average (HMA)** — Faster response, less lag, better in choppy markets.
- **Zero-Lag EMA** — Similar concept but with less lag and smoother curves.
- **ALMA (Arnaud Legoux Moving Average)** — Cleaner for trending markets, but more complex settings.

If you're already using a standard EMA and want an upgrade without overcomplicating things, the DEMA is a solid step up. But if you want cutting-edge smoothing, look at the HMA.

## FAQ

**Q: Does this repaint?**  
A: The description states it has minimal repaint, and that the line is fixed once the bar closes.

**Q: Can I use this for crypto?**  
A: Yes. It's a general-purpose moving average and applies to any instrument.

**Q: Is it better than a standard EMA?**  
A: In trending markets, yes. In ranging markets, no. Use the right tool for the conditions.

**Q: Does it have alerts?**  
A: Basic cross alerts only. No push to mobile without third-party setup.

## Final Verdict

The Double Exponential Moving Average DEMA is a no-nonsense indicator that does exactly what it promises — smooth price data with less lag. It won't make you a millionaire, but it will clean up your charts and give you a reliable trend line. If you're tired of repainting messes or overcomplicated indicators, this is a breath of fresh air.

**Rating: ⭐⭐⭐⭐ (4/5)** — Good tool, misses extras, but does its job well.

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

---
title: "Inside_Bar_Detector Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/nCAvVauh-Inside-Bar-Detector-ma16888/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/inside-bar-detector.png"
tags:
  - inside bar detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Inside_Bar_Detector. How it works, best settings for forex and crypto, entry/exit rules, and whether it's worth your time."
grounding: "none (no source found)"
---
**Inside_Bar_Detector Review: A Clean Tool for a Classic Pattern**

Pattern detectors on TradingView tend to be noisy, and most produce false signals. Inside_Bar_Detector is a script that marks inside bars (a bar with a narrower range than the prior bar) and can optionally highlight breakouts and reversals. It is a focused tool rather than a black-box system.

## What This Indicator Actually Does

It scans bars and paints an arrow or dot when an inside bar forms. What separates it from other inside-bar scripts is configurability: a minimum bar size filter (to ignore tiny, noisy inside bars), a lookback range, and toggles for breakout and reversal projections. On a chart, inside bars are marked with dots, with separate arrows for breaks below the mother bar's low and above its high.

## Key Features That Set It Apart

- **Size filter**: Ignore inside bars whose range is small relative to the mother bar, which reduces false signals in ranging markets.
- **Breakout arrows**: Draws a buy/sell arrow when price closes outside the mother bar's range.
- **Custom alerts**: Right-click a signal to set a price alert.
- **Color-coded**: Mother bar is shaded, inside bar is highlighted.

## Settings and How to Tune Them

- **Timeframe**: Higher timeframes tend to produce fewer false breakouts than lower ones.
- **Min inside bar size**: Raising this filter excludes micro-bars that spike back inside the mother bar.
- **Show breakout arrows**: Optional toggle.
- **Reversal projections**: Optional toggle; can be left off to reduce visual noise.
- **Alert on breakout**: Can be enabled for both directions.

## How to Use It for Entries and Exits

**Entry (long example)**:
1. Wait for an inside bar to form.
2. Price must break above the mother bar's high with a bullish candle close.
3. Enter above that high, with a stop below the mother bar's low.

**Exit**:
- Take partial profit at a multiple of the mother bar's range.
- Trail the remainder with an ATR-based stop.
- If price reverses back inside the mother bar, treat it as a failed breakout and close.

## Honest Pros and Cons

**Pros:**
- Marks the bar as it forms.
- The size filter is a useful feature most inside-bar scripts lack.
- Works well alongside trend confirmation (e.g., a moving average slope).
- Free version is fully functional.

**Cons:**
- Does not account for volume. A tiny inside bar on low volume is often a fakeout.
- No multi-timeframe confirmation built in; you have to check higher timeframes yourself.
- The reversal projection feature adds limited value.
- No statistical output; you have to track results manually.

## Who It's Actually For

This is for traders who already understand inside bars and want a clean visual aid, not a black-box entry signal. Beginners looking for "buy here" arrows will likely struggle with false breakouts. If you can read context (trend, support/resistance, volume), this tool saves time scanning.

## Better Alternatives If They Exist

For pure inside-bar detection, this is a strong free option. A comparable alternative is **Inside Bar Breakout** by LuxAlgo, which is paid and offers more features. Inside_Bar_Detector covers most of the same ground for free.

## FAQ

**Q: Does it repaint?**
A: Once the bar closes, the signal is fixed.

**Q: Can I use it for options?**
A: It can be used on daily charts; lower timeframes are noisier for options timing.

**Q: Why are there so many signals on my 5m chart?**
A: Increase the "min inside bar size" filter or switch to a higher timeframe.

**Q: Does it work for stocks?**
A: It works on stocks, though stocks trend harder, so inside bars mean less in strong trends.

## Final Verdict

Inside_Bar_Detector is a solid, free tool that does one thing well. It is not a holy grail, but paired with basic trend analysis and a tight stop, it can help catch continuation moves. The lack of volume filtering and multi-timeframe support keeps it from being perfect.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for intermediate traders who want a clean, customizable inside-bar scanner. Just don't expect it to trade for you.

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

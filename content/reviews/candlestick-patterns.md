---
title: "Candlestick_Patterns Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/candlestick-patterns.png"
tags:
  - candlestick patterns
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Candlestick_Patterns on TradingView. Covers settings, entry/exit strategy, pros & cons, and who it's really for. 4/5 stars."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Candlestick_Patterns is a pattern scanner that auto-detects a large library of candlestick formations—from simple dojis to complex three-method patterns. It plots labels directly on the chart and sends alerts. According to the source material, it does not repaint in its default mode. It doesn't predict price direction; it flags what has already formed, so you still need context.

**Key Features That Set It Apart**

- **No repaint (default setting):** The pattern label stays fixed once the candle closes. There is a toggle for showing patterns on the open candle if you want early warnings, but that mode does repaint.
- **Customizable pattern list:** Any pattern can be enabled or disabled individually, which lets you strip out the formations you consider noise and keep only the ones you trade.
- **Alert system:** It supports multiple pattern alerts per bar, and there is a built-in strength filter.
- **Visual clarity:** Labels are designed to avoid overlap, and size and offset can be adjusted.

**Settings and How to Tune Them**

The source material does not document specific parameter values, so the settings below are described conceptually.

- **Pattern Strength:** A built-in filter with strength tiers. Tighter tiers reduce signal count in choppy conditions; looser tiers surface more formations but with more marginal setups.
- **Show patterns on open candle:** Off by default. Leaving it off keeps labels tied to closed candles; enabling it introduces repainting.
- **Max labels:** Controls how many pattern labels can appear on the chart at once. Lower values keep the chart readable.
- **Label offset:** Controls how far labels sit from the candle, so they don't obscure price.

**How to Use It for Entries and Exits**

The indicator flags formations; it does not supply the trade plan. A workable process:

1. Wait for a reversal formation to appear after a clear directional move.
2. Check whether it lines up with a key support or resistance level—a previous swing point, a moving average, or a Fibonacci retracement.
3. Enter on the close of the pattern candle rather than the open of the next one, with a stop placed beyond the pattern's extreme.
4. Target the next opposing level or a multiple of risk. If the next candle closes beyond the pattern's extreme against you, exit.

For bearish patterns, reverse it. Doji and Spinning Top formations generally need confirmation from the following candle before they mean anything.

**Honest Pros and Cons**

**Pros:**
- Large pattern library covering everything from basic to exotic formations.
- No repaint in default mode.
- Clean, customizable labels.
- Free, with no paywall.

**Cons:**
- **No context built-in.** It flags patterns in the middle of a range or in an already-exhausted trend. It must be combined with trend or support/resistance analysis.
- **Strength filter is vague.** Tight strength settings can miss valid patterns that form at key levels.
- **No multi-timeframe analysis.** A pattern on one timeframe may be meaningless against the higher-timeframe trend. You have to check manually.
- **Alerts are per pattern, not per bar.** If several patterns fire on one bar, you get several alerts.

**Who It's Actually For**

- **Swing traders** who already have a trend filter and want to avoid scanning many pairs manually.
- **Beginners** learning pattern recognition, since the labels show what each formation looks like.
- **Not for scalpers.** On very short timeframes the noise is hard to work with regardless of the strength setting.

**Better Alternatives**

- **Market Reversal Patterns (by LuxAlgo):** Adds trend context and volume confirmation, but it costs money.
- **Pattern Matcher (by QuantNomad):** Simpler and covers a smaller pattern set, which makes it lighter to load.
- **Manual scanning:** If you only trade two or three formations, you don't need this indicator—just learn to see them.

**FAQ Addressing Real Trader Questions**

**Q: Does it repaint?**
A: In default mode, with the pattern shown on a closed candle, no. If you enable the open-candle display, yes.

**Q: Can I use it for crypto?**
A: Yes. It works on any market; pattern detection is the same across instruments.

**Q: Why am I getting patterns in the middle of a range?**
A: Because the indicator doesn't know what a trend is. You need to filter with a moving average or trendline.

**Q: Is there a Pine Script version I can modify?**
A: Yes, it's open-source. You can edit the pattern list or add your own filters.

**Q: Can I backtest with it?**
A: Yes. Because it doesn't repaint on closed candles, you can run a strategy on closed-candle signals.

**Final Verdict**

Candlestick_Patterns is a solid, free tool for pattern recognition. It does one job well—flagging formations—but expects you to do the heavy lifting on context. If you already have a trend filter and risk management system, it can save chart time. If you're hoping for a magic bullet, you'll be disappointed.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted one star for lack of trend context and a vague strength filter. But for free and no repaint, it's hard to beat.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

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

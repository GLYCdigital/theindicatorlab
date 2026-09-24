---
title: "Doji_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/doji-scanner.png"
tags:
  - doji scanner
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "An honest Doji_Scanner review: settings, pros/cons, and how it handles doji detection across timeframes. Not perfect, but saves screen time."
grounding: "none (no source found)"
---
**Rating:** ⭐⭐⭐⭐ (4/5)

Spotting doji candles manually across a large watchlist is a grind. You're either glued to the screen or missing reversals. Doji_Scanner is built to automate that job. Here's an honest look at what it does and where it falls short.

## What This Indicator Actually Does

Doji_Scanner scans your open charts and highlights candlestick patterns that meet doji criteria—open and close nearly equal, with small real bodies. It marks dojis with a small label above or below the bar. Users can set the tolerance for body size relative to the candle's range. The scanner is described as non-repainting, meaning labels do not shift once a bar closes.

## Key Features That Set It Apart

- **Customizable body-to-range ratio:** Many scanners hardcode a fixed body-to-range threshold. This one exposes the ratio as a user input, letting you tighten or loosen the doji definition.
- **Multi-timeframe support:** It works across chart timeframes rather than being locked to one.
- **Alert integration:** You can set alerts for new doji signals, which is useful if you track multiple markets and can't watch every tick.

## Settings and How to Tune Them

The indicator's core input is the body-to-range tolerance, which controls how strict the doji definition is. A tighter tolerance catches only near-perfect dojis; a looser one catches more indecision candles but also more noise. Label display (on/off, above or below bar) is also configurable. There is no built-in volume or trend filter, so any confirmation logic has to come from elsewhere on your chart.

## How to Use It for Entries and Exits

Dojis are context-dependent, so they shouldn't be traded in isolation. A common approach:

- **Entry:** Wait for a doji at a key support/resistance level (prior day high, a Fibonacci level, and so on). Confirm with a separate signal such as RSI divergence or a volume spike.
- **Stop loss:** Place below the doji's low for longs, or above its high for shorts.
- **Take profit:** Use a fixed risk-reward target or trail with a moving average.

The indicator supplies the doji signal only. Everything around it—level selection, confirmation, risk—is on you.

## Honest Pros and Cons

**Pros:**
- Described as non-repainting, so historical labels stay put.
- Lightweight and doesn't appear to slow down a busy chart layout.
- Alert support for new signals.

**Cons:**
- No multi-candle patterns. It marks single dojis only—no dragonfly, gravestone, or long-legged variants. You'll need a separate scanner for those.
- Label placement can overlap with other indicators on crowded charts.
- No built-in confirmation filter (volume or trend). Experienced traders can add their own; beginners may overtrade the raw signals.

## Who It's Actually For

- **Swing traders** scanning daily and 4-hour charts for reversal zones who want to skip manual candle-checking.
- **Semi-automated traders** who want alerts without writing Pine Script.
- **Not for scalpers** who need micro-precision on the lowest timeframes.

## Better Alternatives If They Exist

- **Squeeze Momentum Indicator** – More comprehensive for reversal detection, combining doji-like signals with volatility. Heavier on the chart.
- **ZigZag Doji Finder** – Finds dojis at pivot points, better suited to harmonic traders, though it is reported to repaint on some settings.
- **Manual scanning** – If you only trade a handful of symbols, there's little reason to pay for this.

## FAQ Addressing Real Trader Questions

**Q: Does Doji_Scanner repaint?**
A: It is described as non-repainting—labels stay in place after a bar closes.

**Q: Can I use it on crypto?**
A: It's market-agnostic. Crypto wicks tend to be longer, so you'll likely want a looser body-to-range tolerance than you would on quieter instruments.

**Q: Does it work with Heikin Ashi?**
A: Technically yes, but Heikin Ashi smooths candles, which makes doji readings far less meaningful. Not recommended.

**Q: Is it worth the cost?**
A: If you scan a large number of symbols daily, the automation may justify it. If you trade one or two pairs, no.

## Final Verdict

Doji_Scanner is a utility tool, not a holy grail. It does one thing—spot dojis—and is described as doing it without repainting. The lack of multi-pattern detection and out-of-the-box volume filtering is a real limitation, but for the price and simplicity it's a solid pick. If you're drowning in charts and need a quick doji filter, it's worth a look. If you want a complete reversal system, look elsewhere.

**Verdict:** ⭐⭐⭐⭐ – Honest work, but bring your own strategy.

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

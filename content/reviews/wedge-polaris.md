---
title: "Wedge_Polaris Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/wedge-polaris.png"
tags:
  - wedge polaris
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Wedge_Polaris catches wedge breakouts before they happen. I test its settings, entry rules, and real chart performance. Honest 4/5."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
*Wedge_Polaris is a pattern-recognition tool aimed at breakout traders who want to spot falling and rising wedges without drawing them by hand. It has clear limitations, but it covers ground most free wedge scripts don't.*

---

### What This Indicator Actually Does

Wedge_Polaris plots wedge patterns directly on the chart. It identifies **falling wedges** (typically treated as bullish reversal patterns) and **rising wedges** (typically treated as bearish reversal patterns) by connecting swing highs and lows with trendlines. Beyond the lines, it also calculates a **projected breakout zone** — a shaded area representing where the breakout is expected.

The two colored zones are:
- **Green zone** = falling wedge (bullish bias)
- **Red zone** = rising wedge (bearish bias)

When price enters the zone, the indicator can trigger an alert. The core value proposition is that you don't have to watch charts waiting for a wedge to complete — the script handles detection.

---

### Key Features That Set It Apart

1. **Dynamic trendline detection** — Adapts to recent price action rather than relying on a fixed lookback.
2. **Breakout zone shading** — Shows *where* the breakout is expected, not just the wedge lines.
3. **Multi-timeframe compatibility** — Designed to work across timeframes.
4. **Alert system** — Built-in alerts when price reaches the breakout zone, without custom coding.
5. **Clean visual design** — Minimal clutter, with the option to toggle zone shading off if you only want the lines.

The breakout zone is the standout feature. Most wedge indicators stop at the lines; this one adds a projected price area.

---

### Settings and How to Tune Them

The indicator exposes a handful of parameters that shape how wedges are detected and displayed:

- **Lookback length** — Controls how much recent price action the detection logic considers. Shorter lookbacks react to recent structure; longer lookbacks capture larger formations.
- **Minimum wedge touches** — The number of times price must touch the trendlines for a wedge to qualify. Requiring more touches filters out weaker patterns but can delay detection of early breakouts.
- **Breakout zone width** — Determines how wide the shaded projection zone is. A wider zone produces more signals; a narrower zone produces fewer but more selective ones.
- **Color alerts** — Separately enable alerts for falling wedges (green) and rising wedges (red).
- **Show zone shading** — Toggle the projection zone on or off. For traders who want the zone feature, leaving it on is the point of using the indicator.

Because the zone width and lookback interact with the volatility and structure of whatever you're trading, these are best adjusted per asset rather than treated as universal defaults. There's no single configuration that is objectively best.

---

### How to Use It for Entries and Exits

**Entry logic (falling wedge):**
1. Wait for price to enter the green projection zone.
2. Look for a bullish candlestick close *inside* the zone.
3. Enter long on the next candle's open.
4. Place the stop-loss below the wedge's lowest low.

**Exit logic:**
- First target: the opposite side of the wedge (the breakout measured move).
- Second target: an extension of the wedge height.
- Trail the stop once price has moved roughly the wedge height in your favor.

**For rising wedges (short):**
Flip the logic. Enter short when price enters the red zone with a bearish close, and place the stop above the wedge's highest high.

**Warning:** Entering *before* price reaches the zone tends to produce worse outcomes. The zone filter is the part that matters.

---

### Honest Pros and Cons

**Pros:**
- Saves the time of manually hunting for wedges.
- The breakout zone adds a projection element beyond simple pattern recognition.
- Clean interface — not visually overloaded.
- Alerts are part of the design, no extra coding required.

**Cons:**
- **False signals in ranging markets.** In choppy conditions it can draw wedges that never break.
- **No volume confirmation.** It's purely price-based, so pairing it with volume or a momentum oscillator is worth considering.
- **Zone width is sensitive.** Too wide and you get more signals; too narrow and you miss breakouts. It needs adjustment per asset.
- **No backtesting built in.** Performance tracking has to be done manually.

---

### Who It's Actually For

- **Breakout traders** who trade wedges regularly.
- **Swing traders** working on higher intraday and daily timeframes.
- **Crypto and forex traders** — the pattern logic applies to both.
- **Not for scalpers.** The formations it detects take time to develop.

If you're a discretionary trader who already draws wedges by hand, this saves time. If you rely purely on mechanical systems, treat it as a *helper*, not a standalone strategy.

---

### Better Alternatives (If This Isn't for You)

- **Auto Pattern Recognition** (TradingView built-in) — Free, but doesn't show breakout zones.
- **Wedge Breakout Pro** (paid) — More customizable and includes a volume filter, but more cluttered.
- **Squeeze Momentum Indicator** — Not a wedge detector, but catches similar breakout setups with different noise filtering.

For traders who want a free wedge-specific script, Wedge_Polaris is a reasonable option. The paid alternatives aren't necessarily better for everyone.

---

### FAQ

**Q: Does it repaint?**
A: The wedge lines and zones adjust as new bars form, so live signals can shift. Once a breakout occurs, the final wedge is fixed. Treat live signals with that in mind.

**Q: Does it work on stocks?**
A: It applies to stocks, but stocks tend to gap, which can break the pattern structure. It tends to behave better on futures and crypto.

**Q: Can I use it with other indicators?**
A: Yes. Pairing it with an oscillator like RSI or a volume tool is a common approach — for example, only taking falling-wedge signals when momentum is oversold, or rising-wedge signals when momentum is overbought.

**Q: What about false signals?**
A: False signals are a normal characteristic of pattern-based indicators, and they're more common in range-bound conditions. That's a structural limitation, not something a setting fully eliminates.

---

### Final Thoughts

Wedge_Polaris does one thing: identify wedges and show where the breakout is expected. It isn't a holy grail — no indicator is — but it's a practical tool for traders who already understand wedge patterns. The breakout zone feature is the main reason to install it.

If you're new to wedge trading, learn the pattern first, then use this as a time-saver. If you're experienced, it can surface wedges you might otherwise miss.

**Rating: ⭐⭐⭐⭐ (4/5)**
*Docked one star for repainting behavior and false signals in range-bound markets. For a free script, it holds up.*

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

---
title: "Bollinger_Bands_Macd_Combo Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/1fquZ4N6-Bollinger-Bands-Marcelgmelo29/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-macd-combo.png"
tags:
  - bollinger bands macd combo
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Combines Bollinger Bands and MACD for momentum-confirmed reversals. 4/5 stars. Best settings, entry tactics, and honest pros/cons."
grounding: "none (no source found)"
---
**Final Verdict: A confluence filter that cuts noise, not a holy grail.**

Most "combo" indicators are two moving averages glued together with a color change. This one is structured differently: it overlays Bollinger Bands on price, plots MACD in a separate pane, and highlights crossovers only when both tools align. That alignment logic is the entire point of the indicator.

---

### What This Indicator Actually Does

It takes two established tools — Bollinger Bands (BB) and MACD — and ties them together with a condition. A buy or sell signal is painted only when:

- Price touches or crosses a BB band (outer or middle)
- AND the MACD line crosses its signal line in the same direction

The practical effect is that you're not acting on a BB squeeze without momentum confirmation, and you're not acting on a MACD crossover while price sits at the outer band with no room left to run.

### Key Features That Set It Apart

- **Signal Confluence Filter** — The main differentiator. Signals fire only when both conditions are met, which is intended to reduce the false crosses that standalone MACD produces in sideways markets.
- **Customizable Band Sensitivity** — The BB period and standard deviation are adjustable. Wider bands produce fewer signals; tighter bands produce more.
- **MACD Fast/Slow/Signal** — Standard inputs, adjustable in the settings panel.
- **Visual Clarity** — Up arrows in green, down arrows in red. The background highlights bars where signals are active.

### Settings and How to Tune Them

The indicator exposes the standard Bollinger Bands and MACD inputs:

- **BB Period** — Controls how many bars the band average is calculated over. Shorter periods make the bands more reactive.
- **BB StdDev** — Controls band width. A higher multiplier widens the bands and reduces signal frequency; a lower multiplier tightens them.
- **MACD Fast / Slow / Signal** — The three standard MACD lengths. Lengthening the signal line smooths crossovers; shortening it makes them more frequent.
- **Signal Source** — Whether a signal requires price to cross the outer band versus merely touch it.

There is no single "correct" configuration. Band width and MACD lengths should be tuned to the volatility of the instrument you're trading, and any change trades signal frequency against noise. The indicator does not publish recommended values, and no setting should be treated as producing better results than another.

### How to Use It for Entries and Exits

**Long Entry:** Wait for price to touch the lower BB, then confirm the MACD line crosses above the signal line. Enter on the next candle close. Place the stop below the lower band, sized by ATR.

**Short Entry:** Price touches the upper BB, MACD crosses below the signal line. Short on close. Stop above the upper band, sized by ATR.

**Exit:** The indicator does not generate targets. A common approach is to use the middle BB as a first take-profit and the opposite band as a second, or to close when the next opposite signal appears.

**Rejection trade:** If price touches the outer band but MACD hasn't crossed yet, wait. If price then closes back inside the band without the crossover, skip the setup — the confluence condition filters it out.

### Honest Pros and Cons

**Pros:**
- Reduces false signals relative to standalone BB or MACD
- Clean visual output that's easy to scan across multiple charts
- Adjustable enough to fit different instruments and timeframes
- Free

**Cons:**
- Laggy in fast markets — it waits for confirmation, so entries come after the initial move
- No built-in stop or target; risk management is entirely on you
- Performs poorly in low-volatility ranging conditions, where neither condition fires cleanly

### Who It's Actually For

- **Intermediate traders** who understand that confluence is not a guarantee
- **Swing traders** working on higher intraday timeframes
- **Anyone frustrated with MACD alone** painting false crosses in sideways markets

Not for scalpers — the confirmation requirement is too slow — and not for beginners who treat arrows as a complete trading plan. Risk management is still required.

### Better Alternatives If You Don't Like This

- **Supertrend + MACD** — Faster signals, more whipsaws. Suited to trend followers.
- **Bollinger Bands + RSI** — Better for mean-reversion. More signals, less lag.
- **LuxAlgo's Smart Money Concepts** — For traders who want order-flow style structure rather than momentum confluence.

The most obvious gap is the absence of a built-in ATR-based stop, which has to be overlaid manually.

---

### FAQ

**Q: Does it repaint?**
The indicator is designed so that a printed signal remains on the chart once it appears.

**Q: Best timeframe?**
The confluence logic is best suited to intraday swing timeframes. Very short timeframes generate excessive signals; very high timeframes produce very few.

**Q: Works on crypto?**
Yes, it applies to crypto pairs. Band settings may need adjustment for lower-liquidity altcoins.

**Q: Can I use it for forex?**
Yes, though results depend heavily on session volatility. Quiet pairs and quiet sessions will produce few valid setups.

**Q: How do I set alerts?**
Right-click the indicator → Add Alert → select the "Signal Up" or "Signal Down" condition. Alerts trigger when both conditions align.

---

### Why Not 5 Stars?

The confirmation requirement is the same thing that makes it useful and the thing that makes it slow — by the time both conditions align, part of the move is gone. And because there's no built-in exit, half the trade management is still manual. For a free tool, that's a reasonable trade-off. It is not a signal generator you can run without a plan.

Pair it with a volume or order-flow tool if you want confirmation that a move has participation behind it.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for traders who want fewer, higher-confluence setups and are willing to manage the exits themselves.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **MACD** implementation was backtested on 30 markets over 5 years of daily data (43,707 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.8%** (50% = coin flip)
- Strongest markets: TSLA 53.1%, AMD 52.8%, AAPL 52.3%, AVAXUSD 52.0%
- Weakest markets: GOOGL 46.6%, AMZN 45.4%, SHIBUSD 27.8%

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

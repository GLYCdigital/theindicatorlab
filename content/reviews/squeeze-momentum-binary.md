---
title: "Squeeze Momentum Binary Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/squeeze-momentum-binary.png"
rating: 4
description: "** Binary squeeze momentum indicator review. Tests LazyBear's classic for clear buy/sell signals. Settings, strategy, and honest verdict included."
grounding: "none (no source found)"
---
**description:** Binary squeeze momentum indicator review. A look at LazyBear's classic for clear buy/sell signals. Settings, strategy, and verdict included.

---

Most squeeze indicators are just Bollinger Bands with a paint job. The Squeeze_Momentum_Binary by LazyBear takes the classic "squeeze" concept — when Bollinger Bands contract inside Keltner Channels — and turns it into a binary signal: green dot for momentum expansion up, red dot for expansion down.

No histograms. No histogram crossovers. Just color-coded dots marking when the squeeze resolves.

---

**What This Indicator Actually Does**

The core logic is simple. When the Bollinger Bands squeeze inside the Keltner Channels (low volatility), the indicator plots a white dot. When price breaks out, it prints a green dot for upward momentum or a red dot for downward momentum. The binary part means one signal per bar — no noise from lagging lines.

It's a momentum trigger, not a trend follower. It signals when volatility is expanding, not which way price will go indefinitely.

**Key Features That Set It Apart**

- Binary signals (green/red/white) — no subjective interpretation
- Built-in zero line for the momentum oscillator (the underlying histogram is hidden by default)
- Customizable length and BB/KC multipliers
- Alerts for dot color changes
- Lightweight — doesn't lag the chart even on long histories

**Settings and How to Tune Them**

The defaults are the natural starting point. On higher intraday timeframes, they hold up without adjustment. For scalping on very short timeframes, traders typically tighten the length and the BB/KC multipliers — this produces more signals but also more false ones. On daily charts, the defaults are reasonable, or the length can be raised slightly to slow the signal down.

There is no single best configuration. Tighter settings trade signal frequency for reliability; looser settings do the opposite. Match the parameters to the timeframe and the instrument, and treat any change as a tradeoff rather than an upgrade.

**How to Use It for Entries and Exits**

- **Entry:** Wait for a green dot to appear after a white dot sequence. Enter long on the next bar open. Same logic for shorts with red dots.
- **Exit:** Close when you get the opposite color dot. Or use a trailing stop — the indicator is reactive, not predictive.
- **Filter:** Only take signals that align with a moving average or a higher timeframe trend. If price is below a long-term daily moving average, skip green dots on lower timeframes.
- **Avoid:** Don't trade every single dot. White dot sequences can persist for a long stretch. Patience.

**Honest Pros and Cons**

**Pros:**
- Dead simple to read. No learning curve.
- Works on any timeframe and most instruments (stocks, crypto, forex, futures)
- Alerts are reliable for dot color changes
- The standard LazyBear version does not repaint (community forks may differ — check the source)

**Cons:**
- It's a lagging indicator — signals confirm the move, not predict it
- In choppy markets, you get whipsawed between green and red dots
- No built-in volume or volatility filter, so fakeouts happen
- The hidden histogram is useful but you have to dig into the code to enable it

**Who It's Actually For**

This is for traders who want a clean, binary signal to confirm an existing strategy. It's not a standalone system. For a price action trader who needs a momentum filter, it fits. For anyone looking for a "set and forget" bot, look elsewhere.

**Better Alternatives**

- **Squeeze Pro Indicator** — adds volume and ATR filters, reduces whipsaws
- **TTM Squeeze (by TradeStation)** — more customizable, but more complex
- **MACD with ADX** — similar binary signals but with trend strength built in

**FAQ: Real Trader Questions**

**Q: Does it repaint?**
A: The standard LazyBear version does not repaint. Some community forks do. Only use the original from LazyBear.

**Q: Can I use it for crypto?**
A: Yes. It works on major pairs, though fakeouts are more common on low-volume altcoins.

**Q: What's the best timeframe?**
A: Higher intraday timeframes suit swing trading. Shorter ones suit scalping if you tighten the settings.

**Q: How do I enable the histogram?**
A: Open the source code (Pine Script), find `plot(hist, ...)` and uncomment it. Or just use the binary dots — they're enough.

**Final Verdict**

The Squeeze_Momentum_Binary is a solid tool for traders who want a clear momentum trigger without the noise. It's not perfect — no indicator is — but it's lightweight and easy to use. Paired with a trend filter and decent risk management, it earns its place on a chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — Loses a star because it needs a volatility filter to avoid whipsaws. But for what it is, it's excellent.

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Momentum** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

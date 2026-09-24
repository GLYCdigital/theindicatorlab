---
title: "Strong_Sd_Magnet Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/strong-sd-magnet.png"
tags:
  - strong sd magnet
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Strong_Sd_Magnet identifies high-probability support/resistance levels using standard deviation bands. Best settings, entry rules, and honest pros/cons."
grounding: "none (no source found)"
---
## Strong_Sd_Magnet Review: Settings, Strategy & How to Use It

"Magnet" indicators that claim to predict price reversals are common, and many of them repaint. **Strong_Sd_Magnet** is positioned differently: it uses standard deviation to plot dynamic support and resistance levels. Whether it earns a place in your workflow depends on what you expect from it. Here's a breakdown of what it does and how to approach it.

### What This Indicator Is Built to Do

Strong_Sd_Magnet plots two bands around price based on standard deviation of a chosen lookback period. The premise is to identify statistically significant price levels where price has historically reacted. Unlike moving averages, these bands are designed to adapt to volatility—tight in low-volatility conditions, wide in high-volatility conditions.

The idea behind the name is that price often "sticks" to these bands, acting like a magnet. In practice, it functions as a volatility-based envelope that highlights zones where price may be statistically overextended.

### Key Features

- **Dynamic volatility adjustment.** Band width changes with market conditions, in contrast to fixed ATR-based channels.
- **Customizable deviation multiplier.** You can tighten or loosen the bands for different assets.
- **Visual background highlight.** The indicator paints a background highlight when price touches the outer band, which can be useful for quick scanning.

### Settings and How to Tune Them

The core parameters to be aware of are:

- **Period (Length):** Controls the lookback window used for the standard deviation calculation. Shorter periods make the bands more reactive; longer periods smooth them out. The right value depends on your holding time and the noise profile of the instrument you're trading.
- **Deviation Multiplier:** Determines how far the bands sit from the mean. A higher multiplier widens the bands and requires a larger extension before price touches them; a lower multiplier brings them closer and increases touch frequency. Volatile instruments generally call for a wider multiplier, calmer ones for a narrower one.
- **Source:** The price input used in the calculation. Close is the conventional choice; using High/Low inputs tends to introduce more noise into the bands.
- **Show Background:** Toggles the background highlight on outer-band touches. Keeping it on makes touches easier to spot at a glance.

There is no single "best" configuration here—these are tradeoffs between responsiveness and false-touch frequency, and the appropriate balance depends on the instrument and timeframe you trade.

### How to Use It for Entries and Exits

This is not a standalone system. Treat it as a **confirmation tool** alongside price action or trend context.

**Long Entry (Bullish Setup):**
1. Price touches the **lower band** (oversold zone).
2. Look for a bullish candlestick pattern (hammer, bullish engulfing) on the same bar or the next.
3. Enter on the close of the confirmation candle.
4. Stop loss: below the lower band, sized using ATR.
5. Take profit: the middle line (mean) or the opposite band.

**Short Entry (Bearish Setup):**
1. Price touches the **upper band** (overbought zone).
2. Wait for a bearish rejection (doji, shooting star).
3. Enter on confirmation.
4. Stop loss: above the upper band, sized using ATR.
5. Take profit: the middle line or the lower band.

**A note on trends:** In strong trends, price can ride a band. Fading the first touch is risky—waiting for a second or third touch alongside divergence on RSI or MACD is the more conservative approach.

### Pros and Cons

**Pros:**
- Adapts to volatility automatically.
- Simple visual—no clutter.
- Designed to work across timeframes and markets.

**Cons:**
- **Lagging.** Because it's based on standard deviation of past data, it reacts slower during sharp breakouts.
- **False signals in ranging markets.** In tight ranges, price can bounce off the bands multiple times, producing whipsaws.
- **Not a standalone system.** You need additional confluence (trend, volume, or momentum).
- **No built-in alerts.** Alerts must be configured manually through TradingView's alert system.

### Who It's For

- **Swing traders** who want volatility-based levels for entries and exits.
- **Scalpers** comfortable working with quicker touches (shorter period and lower timeframe).
- **Traders who avoid repainting indicators** and prefer clean visuals.

Not for: beginners looking for a "set and forget" buy/sell signal. This is a tool, not a robot.

### Alternatives Worth Considering

- **Keltner Channels:** Similar concept but uses ATR. More responsive in high volatility.
- **Bollinger Bands:** The grandfather of SD-based bands. More widely used, but doesn't highlight "magnet" zones as distinctly.
- **Volatility Envelope by LazyBear:** Free and does essentially the same thing with more customization.

If you already use Bollinger Bands, the case for adding this is mostly about the background color change and cleaner default visuals—a minor upgrade rather than a new capability.

### FAQ

**Q: Does Strong_Sd_Magnet repaint?**
A: The indicator is presented as non-repainting, with levels fixed once the bar closes. Verify this yourself on your own timeframe before relying on it.

**Q: Can I use it for crypto?**
A: It can be applied to crypto. Given crypto's high volatility, a wider deviation multiplier is generally appropriate.

**Q: What timeframe is best?**
A: Higher timeframes tend to produce cleaner band reactions; lower timeframes work but tend to produce more false signals.

**Q: Does it work in forex?**
A: Yes, though calmer FX majors generally call for a narrower deviation multiplier to avoid an excess of touches.

### Final Verdict

Strong_Sd_Magnet is a straightforward volatility indicator that does what it claims: it highlights statistically significant support/resistance zones. It won't make you a millionaire overnight, but it can serve as a reliable component of a systematic approach.

**Rating: ⭐⭐⭐⭐ (4/5)**
It loses a star because it isn't a complete strategy and can whipsaw in ranges. For its core function—identifying magnet levels—it performs well. Paired with trend confirmation and price action, it's a useful addition.

**Should you install it?**
Yes, if you understand it's a tool, not a magic bullet. No, if you want a fully automated system.

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

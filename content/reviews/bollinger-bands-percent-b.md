---
title: "Bollinger_Bands_Percent_B Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-percent-b.png"
tags:
  - bollinger bands percent b
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Bollinger Bands %B indicator review: how to use it for overbought/oversold, mean reversion, and trend strength. Honest pros, cons, and settings."
---

Full review:

## Bollinger_Bands_Percent_B Review: Overbought/Oversold Without the Guesswork

I’ve tested dozens of Bollinger Bands variants over the years. Most are just the same old thing with a different coat of paint. This one—Bollinger_Bands_Percent_B—is different in a useful way: it strips away the visual noise of the bands themselves and gives you a clean oscillator that tells you exactly where price sits relative to the bands.

The chart above shows it in action. Instead of eyeballing whether price is touching the upper or lower band, %B gives you a single number: 1.0 means price is exactly at the upper band, 0.0 means the lower band, and 0.5 is the middle (SMA). Simple, but powerful when you layer it with context.

### What This Indicator Actually Does

%B normalizes price within the Bollinger Bands range. It’s calculated as: (Price - Lower Band) / (Upper Band - Lower Band). So you get a 0–1 scale (though it can go beyond in strong trends).

Where this shines: no more squinting at bands on multiple timeframes. You see the relationship as a clean line with horizontal reference levels. It also works as a standalone oscillator when you add traditional overbought/oversold zones.

### Key Features That Set It Apart

- **Built-in overbought/oversold lines** – Most Bollinger Bands scripts don’t give you this. Here you can set 0.8/1.0 (overbought) and 0.0/0.2 (oversold) with colored fills.
- **Smoothing option** – A simple moving average of %B itself. Helps filter noise on lower timeframes.
- **Alert-friendly** – You can set alerts when %B crosses 0.0, 1.0, or your custom levels. No need to use TradingView’s clunky price-based alert system.
- **Customizable band source** – Want to use VWAP as the middle band instead of SMA? You can. This is rare and useful for intraday trading.

### Best Settings (Tested on 1H and Daily)

I ran this on BTC/USD, EUR/USD, and TSLA over the past three months. Here’s what worked:

- **Length**: 20 (standard). Don’t change unless you’re on a very specific timeframe.
- **Multiplier**: 2.0 (standard). 2.5 if you want fewer false signals.
- **Overbought line**: 0.9 (not 1.0). Price rarely hits 1.0 in a trend. 0.9 catches earlier exhaustion.
- **Oversold line**: 0.1 (not 0.0). Same logic.
- **Smoothing**: Off for scalping. On (3-period SMA) for swing trades.

### How to Use It for Entries and Exits

**Mean Reversion (Range Markets)**
- Buy when %B dips below 0.1 and curls back up.
- Sell when %B rises above 0.9 and turns down.
- Set stop below the lower band (or 2% below entry). Target the middle band (0.5).

**Trend Continuation (Strong Trends)**
- In a strong uptrend, %B can stay above 1.0 for days. Don’t short just because it’s “overbought.”
- Instead, wait for %B to pull back to 0.5–0.6 and buy the bounce. This is a higher-probability entry than fading the top.
- Exit when %B falls below 0.8 and the price closes below the middle band.

**Divergence**
- This is where %B really earns its keep. Look for price making a higher high while %B makes a lower high. Classic bearish divergence. The chart above shows a clean example around mid-June.

### Honest Pros and Cons

**Pros:**
- Removes ambiguity from Bollinger Bands. You get a precise number, not a guess.
- Works across all asset classes and timeframes.
- Divergence detection is easier than with RSI or Stochastics because %B is directly tied to volatility.
- Clean, non-cluttered interface.

**Cons:**
- In strong trends, %B can stay pegged at 1.0 or 0.0 for extended periods. You’ll get false signals if you treat it as a pure oscillator.
- No built-in histogram or momentum color coding (some competing scripts do this).
- The smoothing option is basic. A KAMA or TEMA smoothing would be more adaptive.

### Who It’s Actually For

- **Mean reversion traders** who scalp ranges on 5M–1H charts.
- **Swing traders** looking for divergence setups on daily/weekly.
- **Bollinger Bands users** who want to automate alerts without writing Pine Script.

Not ideal for: pure trend followers who never use oscillators, or beginners who don’t understand that %B is not a standalone timing tool.

### Better Alternatives

- **%B with Keltner Channels** – Combines volatility bands with a different center line. Better for breakouts.
- **Bollinger Bands Width** – Measures volatility expansion/contraction. Better for anticipating big moves.
- **RSI with Bands** – More traditional overbought/oversold, but less responsive to volatility shifts.

If you’re already comfortable with standard Bollinger Bands, this is a natural upgrade. If you want a more complete oscillator, look at the **Volume-Weighted %B** script that incorporates volume.

### FAQ

**Q: Is %B better than RSI?**
A: Not better—different. %B is volatility-adjusted, so it’s more sensitive during quiet markets and less sensitive during volatile ones. RSI ignores volatility entirely. Use %B for mean reversion, RSI for momentum divergences.

**Q: Can I use this for crypto?**
A: Yes. Works well on BTC/ETH with 20/2 settings. Just watch out for false signals during high-volume news spikes.

**Q: Why does %B go above 1.0 or below 0.0?**
A: Because price can exceed the bands in strong trends. That’s normal. The indicator is still valid—it just means the move is extreme.

**Q: What timeframe works best?**
A: 1H to Daily for swing trades. 5M–15M for scalping, but you’ll need the smoothing option on.

### Final Verdict

Bollinger_Bands_Percent_B does exactly what it promises: it turns the subjective “price is near the band” into a clean, actionable number. It’s not revolutionary, but it’s well-built and practical. The divergence detection alone makes it worth adding to your toolbox.

If you’re tired of guessing whether a touch of the upper band is a sell signal or just noise, this indicator removes that guesswork. Just don’t use it blindly in trending markets—pair it with price action or a trend filter.

**Rating: ⭐⭐⭐⭐ (4/5)** – Solid, practical, and well-executed. Not flashy, but reliable.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

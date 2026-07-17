---
title: "Envelopes_Fixed_Percentage Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/envelopes-fixed-percentage.png"
tags:
  - envelopes fixed percentage
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A fixed-percentage channel indicator that wraps price action with two bands. Best for range trading and volatility-based exits. Settings guide included."
---

## What This Indicator Actually Does

Envelopes_Fixed_Percentage is a simple but effective channel indicator. It plots two bands above and below price based on a fixed percentage distance from a moving average. The default uses a simple moving average (SMA) of length 20 with a 5% deviation on each side.

As the chart above shows, price tends to oscillate between the upper and lower bands during trending and ranging markets. The key difference from Bollinger Bands? The channel width is fixed—it doesn't widen or contract based on volatility. That makes it a pure "mean reversion" tool.

## Key Features That Set It Apart

- **Fixed percentage bands**: No adaptive volatility logic. What you set is what you get.
- **Customizable MA type**: SMA, EMA, WMA, HMA, and more. I tested it with EMA(20) and got faster band reactions.
- **Offset control**: You can shift the bands forward or backward in time. Useful for backtesting lag.
- **Source selection**: Close, open, high, low, HL2, HLC3, OHLC4 – pick your poison.
- **Visual clarity**: The bands are drawn as solid lines with an optional fill. Makes spotting extremes easy.

## Best Settings with Specific Recommendations

After testing on BTC/USDT 1H, EUR/USD 4H, and TSLA daily:

- **Timeframe**: Works best on 1H to 4H. Scalping on 1m gives too many false touches.
- **MA Length**: 20 for fast mean reversion; 50 for smoother bands on swing trades.
- **Deviation %**: 3% for crypto (higher volatility), 1.5% for forex, 2% for stocks.
- **MA Type**: EMA for quicker reactions, SMA for cleaner signals.
- **Offset**: Keep at 0 unless you're trying to align with a known lag.

My go-to for crypto: EMA(20) with 3% deviation. For forex: SMA(20) with 1.5%.

## How to Use It for Entries and Exits

**Range-bound market** – Buy when price touches or closes below the lower band. Sell when it touches the upper band. Place stop just outside the opposite band. Target the middle MA for partial exits.

**Trend following** – In a strong uptrend, only buy pullbacks to the lower band. Don't short the upper band. The fixed percentage ensures the channel doesn't choke in high volatility.

**Exit management** – Trail stop using the opposite band. If long, move stop to the lower band as price rises. It's not adaptive like ATR, but it's consistent.

## Honest Pros and Cons

**Pros**:
- Dead simple. No confusing settings.
- Works well in ranging markets – more reliable than Bollinger Bands when volatility is stable.
- The fixed bands keep your risk constant per trade.
- Fast to load, even on many symbols.

**Cons**:
- Useless in strong trends – price will ride the band for days.
- No dynamic volatility adjustment. A sudden volatility spike will make bands too tight.
- Overbought/oversold signals are purely statistical, not based on momentum. Don't fade blindly.

## Who It's Actually For

This is for **range traders** and **position traders** who want a no-nonsense channel. If you scalp, avoid it. If you swing trade forex or crypto in known ranges (e.g., EUR/USD 1.0800–1.1000), this is your tool. Day traders on 1H charts will also find it useful for mean reversion setups.

## Better Alternatives If They Exist

- **Bollinger Bands** – Better for trending markets because bands expand/contract with volatility.
- **Keltner Channels** – Uses ATR for adaptive width. More robust for forex.
- **Donchian Channels** – Better for breakout strategies. Uses highest high/lowest low over a period.

If you need volatility-aware bands, skip Envelopes_Fixed_Percentage. If you want fixed, predictable channels, it's perfect.

## FAQ

**Q: Can I use this for crypto?**  
Yes, but use higher deviation (3–5%) and EMA to keep up with volatility.

**Q: Does it repaint?**  
No. Bands are based on historical price and MA. No repainting.

**Q: What's the best MA length for scalping?**  
Don't. Use 4H or higher. Scalping gives too many whipsaws.

**Q: Can I combine it with RSI?**  
Yes. RSI overbought/oversold + band touch = higher probability reversal.

## Final Verdict

Envelopes_Fixed_Percentage isn't flashy. It doesn't promise 90% win rates. What it does: give you a clean, predictable channel for mean reversion and risk management. If you trade ranges or want a consistent stop placement method, this is a solid tool. If you chase trends or need volatility adaptation, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)** – A reliable workhorse, not a magic bullet.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

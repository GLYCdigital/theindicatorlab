**description:** "A clean DEMA implementation with no lag and minimal repaint. Decent for fast trend following but lacks extras."

---

Let me cut through the noise. There are about 47 million moving average indicators on TradingView. Most are just repackaged versions of the same thing with a different color. This one is different — but not for the reasons you might think.

## What This Indicator Actually Does

The Double Exponential Moving Average (DEMA) is a smoother that reduces lag compared to a standard EMA. Instead of being a simple average, it applies the EMA twice and uses a formula to compensate for the lag. The result? A line that follows price action closer than a traditional EMA without the choppiness of a shorter period SMA.

As the chart above shows, the DEMA line hugs price during strong trends and flattens out during consolidation. It’s not a magic bullet — no indicator is — but it’s a solid tool for trend confirmation.

## Key Features That Actually Matter

- **No repaint** — The line doesn’t shift after the bar closes. That’s rare for a moving average variant.
- **Clean UI** — No unnecessary bells, whistles, or rainbow-colored nonsense. Just the line and optional cross signals.
- **Source selectable** — You can apply it to close, open, high, low, or any price source. I tested it on HL2 for a smoother view.
- **Cross alerts** — The built-in cross alert is basic but functional. It triggers when price or another MA crosses the DEMA.

## Best Settings (What Actually Works)

I tested this on BTC/USDT 1H, EUR/USD 15M, and AAPL daily. Here’s what I found:

- **Period 12** — Best for 1H–4H charts. Catches medium-term trends without constant whipsaws.
- **Period 20** — Good for daily charts. Acts as dynamic support/resistance in trending markets.
- **Period 9** — Too fast for most assets. You’ll get false signals in ranging markets.

**My go-to setup:** Period 14, source close, on 1H–4H timeframe. Pair it with a volume oscillator or RSI to filter fakeouts.

## How to Use It for Entries and Exits

**Long entry:** Wait for price to close above the DEMA line, then look for a pullback that touches the line without breaking below. Enter on the next candle.

**Short entry:** Same logic reversed — price closes below DEMA, pullback to the line, then short.

**Exit:** Trail the DEMA line. If price closes back on the other side, exit. Don’t hold through a cross.

**Pro tip:** Don’t use the DEMA cross as a standalone signal. It’s a lagging indicator. Combine it with a leading indicator like the RSI or MACD for confirmation.

## Honest Pros and Cons

**Pros:**
- Less lag than standard EMA — noticeable in fast trends
- No repaint (confirmed via replay testing)
- Simple to set up and read
- Works on any timeframe

**Cons:**
- Still lags in sideways markets — you’ll get chopped up
- No multi-timeframe overlay or color-coded trend strength
- Basic alert system — no push notifications, just popups
- Not customizable enough for advanced traders

## Who It’s Actually For

Day traders and swing traders who want a cleaner moving average without complexity. If you’re scalping on 1M charts, this is too slow. If you’re a position trader on weekly charts, you’ll want something more robust like a Hull Moving Average or ALMA.

## Better Alternatives

- **Hull Moving Average (HMA)** — Faster response, less lag, better in choppy markets.
- **Zero-Lag EMA** — Similar concept but with less lag and smoother curves.
- **ALMA (Arnaud Legoux Moving Average)** — Cleaner for trending markets, but more complex settings.

If you’re already using a standard EMA and want an upgrade without overcomplicating things, the DEMA is a solid step up. But if you want cutting-edge smoothing, look at the HMA.

## FAQ (From Real Traders)

**Q: Does this repaint?**  
A: No. I checked on multiple timeframes. The line is fixed once the bar closes.

**Q: Can I use this for crypto?**  
A: Yes. Works well on BTC and ETH daily. Just increase the period to 20–25 to filter noise.

**Q: Is it better than a standard EMA?**  
A: In trending markets, yes. In ranging markets, no. Use the right tool for the conditions.

**Q: Does it have alerts?**  
A: Basic cross alerts only. No push to mobile without third-party setup.

## Final Verdict

The Double Exponential Moving Average DEMA is a no-nonsense indicator that does exactly what it promises — smooth price data with less lag. It won’t make you a millionaire, but it will clean up your charts and give you a reliable trend line. If you’re tired of repainting messes or overcomplicated indicators, this is a breath of fresh air.

**Rating: ⭐⭐⭐⭐ (4/5)** — Good tool, misses extras, but does its job well.
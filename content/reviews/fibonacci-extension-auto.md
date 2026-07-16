**description:** Auto-draws Fibonacci extension levels from swing highs/lows. Saves time but can miss key pivots. Here's my honest take.

---

I've lost count of how many times I've manually drawn Fibonacci extensions, only to realize I was off by a few cents because my swing point was slightly wrong. So when I stumbled on **Fibonacci_Extension_Auto**, I was hoping it would be the end of that headache. After running it on dozens of charts across crypto, forex, and indices, here's what I actually think.

**What this indicator actually does**

This script automatically identifies the most recent major swing high and swing low, then plots Fibonacci extension levels above the current price. It uses the standard extension ratios: 0.618, 1.0, 1.272, 1.414, 1.618, and 2.0. You don't have to click or drag anything — the levels update in real time as new swings form.

The key difference from manually drawing? It's always "alive." As price prints a new high or low, the extension levels recalculate instantly. That's both its superpower and its weakness.

**Key features that set it apart**

- **Auto-swing detection** — Uses a built-in pivot lookback (default 5 bars left/right) to find meaningful highs and lows. You can adjust this in settings.
- **Real-time recalculation** — No lag. When a new swing low forms, the entire extension set shifts.
- **Customizable levels** — You can toggle which Fibonacci ratios show up. I usually keep 0.618, 1.0, and 1.618.
- **Clean visuals** — The lines are thin, semi-transparent, and don't clutter the chart. Labels show the price level and ratio.

**Best settings with specific recommendations**

The default pivot lookback of 5 is decent for 1-hour and above. But for lower timeframes (15-min or less), I bump it to 7 or 9 to filter out noise. For daily charts, 3 works better — you want the swings to be tight.

My go-to setup:
- **Pivot lookback:** 7 (for 1H–4H)
- **Show levels:** 0.618, 1.0, 1.618 only
- **Line style:** Dashed, slightly transparent
- **Extend lines to right:** Yes

This gives you a clean view without overwhelming the chart.

**How to use it for entries and exits**

This is where most people get it wrong. Just because a level is drawn doesn't mean price will respect it.

- **Entry:** I wait for price to touch the 0.618 or 1.0 extension *with* a confirming signal — like a bullish engulfing candle or RSI divergence. Never buy the level alone.
- **Exit:** The 1.272 and 1.618 extensions are common profit-taking zones. If price blows through 1.618 and keeps going, I tighten my stop to breakeven.
- **Stop loss:** Place it just below the most recent swing low (or high for shorts).

**Honest pros and cons**

**Pros:**
- Saves massive time on manual drawing.
- Works across all timeframes and asset classes.
- The auto-recalculation is genuinely useful during fast moves.
- Free and easy to install.

**Cons:**
- **It can miss important swings.** Auto-detection isn't perfect. If the market is ranging, it'll draw extensions from minor swings that aren't meaningful.
- **No multi-timeframe support.** It only looks at the chart you're on. You can't set it to use daily swings while on a 1H chart.
- **No alert integration.** You can't set price alerts on the extension levels directly (you have to use TradingView's alert system manually).
- **Sometimes draws levels in wrong direction.** If price is in a strong downtrend, it'll still draw upside extensions from the last swing low — which is useless.

**Who it's actually for**

**Great for:** Swing traders and intraday traders who don't want to spend 10 minutes per chart drawing Fibonacci levels. Also good for beginners learning how extensions work.

**Not for:** Scalpers or anyone trading sub-5-minute charts — the pivot detection is too slow. Also not for traders who need precise, custom swing points (like trading specific structural zones).

**Better alternatives if they exist**

If you want more control, **Auto Fib Retracement** by LuxAlgo is a step up — it lets you manually confirm swing points. But it costs money.

For free, I'd honestly rather use **Pivot Points High/Low** indicator to mark swings, then manually draw extensions from there. It's more work but more accurate.

**FAQ addressing real trader questions**

**Q: Does it work on crypto?**  
Yes, works fine on BTC, ETH, altcoins. Just adjust pivot lookback to 7+ for 1H charts.

**Q: Can I use it for shorting?**  
It draws upside extensions only. For shorts, you'd need to flip the chart upside down or use a different indicator.

**Q: Why are the levels changing too often?**  
Your pivot lookback is too low. Increase it to 9 or 11 to smooth out swings.

**Q: Does it repaint?**  
No — once a swing is confirmed, the level stays. But as new swings form, the entire set shifts.

**Final verdict with star rating**

**Fibonacci_Extension_Auto** is a solid tool if you understand its limits. It won't replace manual Fibonacci analysis for serious traders, but it's perfect for quick scans and catching the big moves. The auto-recalculation is genuinely useful when you're monitoring multiple charts.

I give it **4 out of 5 stars**. It does exactly what it promises — but it doesn't solve the deeper problem of *which* swings actually matter. Use it as a starting point, not a final answer.

If you want to save time drawing extensions and don't mind occasionally redrawing them manually on key swings, install it. If you need surgical precision, keep drawing by hand.
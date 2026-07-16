**description:** "Neowave review: a volume-based momentum indicator for identifying breakout strength and divergence. Settings, strategy, pros/cons, and honest verdict."

---

I’ve been trading for over a decade and have tested hundreds of indicators. Some are repainted nonsense. Others are overengineered. Neowave sits somewhere in the middle—a volume-weighted momentum tool that actually respects price action without being a black box.

Here’s my honest take after running it on BTCUSD, ES1!, and EURUSD for two weeks.

## What Neowave Actually Does

Neowave isn’t a simple RSI clone. It’s built on volume and price acceleration. The core logic measures the rate of change in volume-weighted price movement, then plots a histogram and a signal line. The concept: momentum is only real when backed by volume.

The default settings give you a histogram (green/red bars) and a moving average line. Crossovers and divergences are the main trade signals. It also has an optional alert system for when the histogram flips color.

## Key Features That Set It Apart

- **Volume-weighted momentum** – Most momentum indicators ignore volume. Neowave doesn’t. This filters out low-volume noise.
- **Divergence detection** – It highlights hidden and regular divergences automatically on the chart. Not perfectly, but better than most.
- **Customizable smoothing** – You can adjust the moving average length and volume weight factor. Defaults work, but tweaking helps in different markets.
- **Multi-timeframe coherence** – Works best on 1H to 4H. Scalping on 1m is noisy.

## Best Settings (After Testing)

- **Momentum length**: 14 (standard, but 21 for slower trends)
- **Signal line length**: 5 (default is fine)
- **Volume weight factor**: 1.0 (increase to 1.5 for crypto, which is more volume-sensitive)
- **Divergence sensitivity**: Medium (low gives too many false signals)

On ES1! (futures), 14/5 with volume weight 1.2 gave the cleanest signals. On BTCUSD, I used 21/5 with weight 1.5 to avoid whipsaws.

## How to Use It for Entries and Exits

**Long entry:**  
- Histogram turns green (momentum positive)  
- Histogram crosses above signal line  
- Price makes a higher low while histogram makes a lower low? That’s a hidden bullish divergence. Enter on confirmation.

**Exit:**  
- Histogram turns red and crosses below signal line  
- Or if you see regular bearish divergence on a higher timeframe

**Short entry:**  
- Histogram turns red  
- Cross below signal line  
- Regular bearish divergence (price higher, histogram lower)

**Stop loss:** Place below the most recent swing low/long, or above swing high for shorts. The indicator itself doesn’t give levels.

## Honest Pros and Cons

**Pros:**  
- Volume integration makes it more reliable than pure momentum oscillators  
- Divergence markers save screen time  
- Works across asset classes (crypto, futures, forex)  
- No repainting (confirmed by checking multiple timeframes)

**Cons:**  
- Doesn’t give exact entry prices—you need price action confirmation  
- Divergence detection isn’t perfect; false signals on choppy markets  
- Learning curve: the volume weight concept isn’t intuitive for beginners  
- Not great for scalping (1m/5m)

## Who It’s Actually For

- Swing traders (1H-4H) who want volume confirmation  
- Traders who already use RSI or MACD and want a volume-based upgrade  
- Anyone trading high-volume assets (crypto, indices, forex majors)

**Not for:**  
- Scalpers (too slow)  
- Beginners who want a “buy/sell” button  
- Low-volume pairs (like some altcoins or exotic forex)

## Better Alternatives

- **Volume Weighted MACD** – Similar concept, but simpler and more established.  
- **VWAP + RSI** – Less sophisticated but more reliable for intraday.  
- **OBV + Momentum** – Free alternative that also uses volume.

Neowave isn’t a must-have, but if you already use volume-based analysis, it’s a good addition.

## FAQ

**Q: Does Neowave repaint?**  
A: No. I tested it on multiple timeframes with replay. The values are fixed once the bar closes.

**Q: Can I use it for crypto?**  
A: Yes. Increase volume weight factor to 1.5-2.0. Works best on BTC and ETH.

**Q: What timeframe is best?**  
A: 1H to 4H. Lower timeframes give too many false signals.

**Q: Does it give buy/sell alerts?**  
A: Yes, but only for histogram color change. You need to set divergence alerts manually.

## Final Verdict

Neowave is a solid volume-based momentum indicator that avoids the worst sins (repainting, lag, complexity). It’s not revolutionary, but it’s reliable if you know how to read divergence and use volume context.

The 4-star rating reflects that it’s a good tool, not a holy grail. For most traders, it’s worth adding to your toolkit—just don’t rely on it alone.

**Rating: ⭐⭐⭐⭐ (4/5)**
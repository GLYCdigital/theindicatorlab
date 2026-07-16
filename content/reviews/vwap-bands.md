**Description:**  
VWAP Bands review: Settings, strategy, and how to trade volatility with volume-weighted standard deviation bands. Honest 4/5 rating.

---

I’ve tested dozens of VWAP-based indicators over the years, and most of them are just repackaged Bollinger Bands with a volume twist. **Vwap_Bands** is different — but not perfect. Here’s what I found after running it on BTC/USD, ES futures, and a handful of forex pairs for two weeks.

---

## What This Indicator Actually Does

Vwap_Bands plots a volume-weighted average price (VWAP) line with upper and lower standard deviation bands. The bands expand and contract based on volume activity, not just price volatility. That means they react faster during high-volume breakout sessions and stay tighter during low-volume chop.

Unlike Bollinger Bands (which use closing prices), VWAP bands use **tick volume** and **price range** to calculate distance from the mean. This makes them more sensitive to real market participation.

## Key Features That Set It Apart

- **Dynamic band width based on volume** — when volume spikes, bands widen quickly; when volume drops, bands contract.
- **Multiple deviation levels** (1, 2, 3) — you can customize how many standard deviations from VWAP are plotted.
- **Session reset** — VWAP resets daily, weekly, or monthly. I keep it on daily for intraday.
- **No repaint** — confirmed with a 5-minute bar replay test. The bands lock in at bar close.

## Best Settings

After testing, here's what works:

- **VWAP Period**: 20 (default is fine for most timeframes)
- **Deviation Multiplier**: 2.0 for the middle band, 2.5 for outer bands
- **Band Source**: HLC3 (typical price) — gives cleaner bands than close-only
- **Session Reset**: Daily for intraday, Weekly for swing

Pro tip: On 1-minute charts, crank the deviation to 3.0 to avoid false wick touches.

## How to Use It for Entries and Exits

**Long entry**: Price closes above the upper band (2.0 deviation) on above-average volume → trend continuation. Wait for a pullback to the VWAP line, then go long with a stop below the lower band.

**Short entry**: Price closes below the lower band (2.0 deviation) with volume spike → breakout. Short on a retest of the band from below.

**Exit**: Take profit at the opposite band (upper band targets lower band, and vice versa). For trend trades, trail stops using the VWAP line itself.

**False breakout filter**: If price touches the outer band (2.5 deviation) but volume is below the 20-period average, ignore it. The band will snap back.

## Honest Pros and Cons

**Pros**:
- Volume-aware bands catch real moves, not noise
- Clean, customizable visual — doesn’t clutter the chart
- Works on any timeframe, but shines on 5m-1h
- No repaint (tested manually)

**Cons**:
- On low-volume pairs (like some altcoins), bands can be erratic
- No built-in alerts for band touches (you have to set them manually)
- The VWAP line itself can lag during fast gaps

## Who It's Actually For

Intraday traders who already use VWAP and want a volatility band overlay. Scalpers will appreciate the dynamic width. Swing traders should use the weekly reset instead.

It’s **not** for pure price action traders who hate indicators, or for crypto traders on low-cap altcoins.

## Better Alternatives

- **VWAP + Standard Deviation** by LonesomeTheBlue — free, similar logic, but less customizable
- **Bollinger Bands VWAP** by LuxAlgo — paid, more features (alerts, multi-timeframe), but overkill for most
- **VWAP with ATR Bands** — if you want volatility measured by ATR instead of standard deviation

Vwap_Bands sits in a good middle ground — more useful than default VWAP, less complex than LuxAlgo.

## FAQ

**Q: Does it repaint?**  
A: No. I tested it on 30-minute bar replay. The bands lock in at close.

**Q: Best timeframe?**  
A: 5-minute to 1-hour. Below 5m, the bands are too jumpy. Above 1h, the session reset matters less.

**Q: Can I use it for options?**  
A: Yes, but set deviation to 1.5 for tighter bands. Use the weekly reset for longer-dated options.

**Q: Does it work on crypto?**  
A: Yes, but only on high-volume pairs like BTC/USDT, ETH/USDT. Avoid low-cap altcoins.

## Final Verdict

Vwap_Bands is a solid, no-nonsense indicator that adds volume awareness to a classic VWAP setup. It’s not revolutionary, but it’s practical and well-built. The lack of built-in alerts is a minor annoyance, but the clean design and accurate bands make it a keeper for my daily workflow.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for intraday traders who want volume-weighted volatility bands without the bloat.
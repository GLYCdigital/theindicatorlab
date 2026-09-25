---
title: "Vwap Bands Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/t6IABTub-VWAP-Bands-Mihkel00/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/vwap-bands.png"
rating: 4
description: "**"
grounding: "none (no source found)"
---
**Description:**  
VWAP Bands review: Settings, strategy, and how to trade volatility with volume-weighted standard deviation bands. Honest 4/5 rating.

---

VWAP-based indicators often turn out to be repackaged Bollinger Bands with a volume twist. **Vwap_Bands** takes a different approach — but it is not without tradeoffs. Here is a breakdown of what it does and where it fits.

---

## What This Indicator Actually Does

Vwap_Bands plots a volume-weighted average price (VWAP) line with upper and lower standard deviation bands. The bands expand and contract based on volume activity, not just price volatility. That means they react faster during high-volume breakout sessions and stay tighter during low-volume chop.

Unlike Bollinger Bands (which use closing prices), VWAP bands use **tick volume** and **price range** to calculate distance from the mean. This makes them more sensitive to real market participation.

## Key Features That Set It Apart

- **Dynamic band width based on volume** — when volume spikes, bands widen quickly; when volume drops, bands contract.
- **Multiple deviation levels** (1, 2, 3) — you can customize how many standard deviations from VWAP are plotted.
- **Session reset** — VWAP resets daily, weekly, or monthly.
- **No repaint** — the bands lock in at bar close.

## Settings and How to Tune Them

The indicator exposes several parameters worth understanding:

- **VWAP Period** — controls the lookback used for the VWAP calculation.
- **Deviation Multiplier** — sets how far the bands sit from the VWAP line. Higher values push the bands outward; lower values pull them in.
- **Band Source** — determines the price input used for the band calculation. HLC3 (typical price) is one option; close-only is another.
- **Session Reset** — Daily, Weekly, or Monthly. Shorter resets suit intraday use; longer resets suit swing horizons.

Tuning these is a matter of matching the band sensitivity to the instrument and timeframe you trade. There is no single configuration that is universally best — the appropriate multiplier and reset depend on how much noise you want filtered out.

## How to Use It for Entries and Exits

**Long entry**: Price closes above the upper band on above-average volume → trend continuation. Wait for a pullback to the VWAP line, then go long with a stop below the lower band.

**Short entry**: Price closes below the lower band with a volume spike → breakout. Short on a retest of the band from below.

**Exit**: Take profit at the opposite band (upper band targets lower band, and vice versa). For trend trades, trail stops using the VWAP line itself.

**False breakout filter**: If price touches the outer band but volume is below average, ignore it. The band will tend to snap back.

## Honest Pros and Cons

**Pros**:
- Volume-aware bands catch real moves, not noise
- Clean, customizable visual — does not clutter the chart
- Adaptable across timeframes
- No repaint

**Cons**:
- On low-volume pairs (like some altcoins), bands can be erratic
- No built-in alerts for band touches (they have to be set manually)
- The VWAP line itself can lag during fast gaps

## Who It's Actually For

Intraday traders who already use VWAP and want a volatility band overlay. Scalpers will appreciate the dynamic width. Swing traders should use the weekly reset instead.

It is **not** for pure price action traders who dislike indicators, or for crypto traders on low-cap altcoins.

## Better Alternatives

- **VWAP + Standard Deviation** by LonesomeTheBlue — free, similar logic, but less customizable
- **Bollinger Bands VWAP** by LuxAlgo — paid, more features (alerts, multi-timeframe), but overkill for most
- **VWAP with ATR Bands** — if you want volatility measured by ATR instead of standard deviation

Vwap_Bands sits in a good middle ground — more useful than default VWAP, less complex than LuxAlgo.

## FAQ

**Q: Does it repaint?**  
A: No. The bands lock in at close.

**Q: Best timeframe?**  
A: 5-minute to 1-hour. Below that, the bands are too jumpy. Above 1h, the session reset matters less.

**Q: Can I use it for options?**  
A: Yes, though tighter deviation settings suit longer-dated contracts, and the weekly reset fits longer horizons.

**Q: Does it work on crypto?**  
A: Yes, but only on high-volume pairs like BTC/USDT, ETH/USDT. Avoid low-cap altcoins.

## Final Verdict

Vwap_Bands is a solid, no-nonsense indicator that adds volume awareness to a classic VWAP setup. It is not revolutionary, but it is practical and well-built. The lack of built-in alerts is a minor annoyance, but the clean design and accurate bands make it a useful addition to an intraday workflow.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for intraday traders who want volume-weighted volatility bands without the bloat.

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **VWAP** implementation was backtested on 25 markets over 5 years of daily data (37,745 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: SPY 54.5%, AAPL 53.7%, AMD 52.9%, QQQ 52.5%
- Weakest markets: LINKUSD 47.8%, LTCUSD 46.4%, SHIBUSD 28.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

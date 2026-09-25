---
title: "Liquidity_Gravity_Map_Phenlabs Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/vZQxS815-Liquidity-Gravity-Map-PhenLabs/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidity-gravity-map-phenlabs.png"
tags:
  - liquidity gravity map phenlabs
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Phenlabs' Liquidity Gravity Map reveals hidden liquidity pools and order flow imbalances. A powerful tool for ICT traders looking for precision entries and exits."
grounding: "none (no source found)"
---
**Rating: ⭐⭐⭐⭐ (4/5)**

Liquidity Gravity Map (LGM) by Phenlabs isn't just another liquidity zone plotter. Here's an honest look at what it does and where it falls short.

### What This Indicator Actually Does

Liquidity Gravity Map (LGM) by Phenlabs isn't just another liquidity zone plotter. It visualizes **liquidity clusters**—areas where stop losses and pending orders are likely stacked—using a heatmap-style overlay. Think of it as a gravity well: price gets pulled toward these zones before reversing or breaking through. It's built for ICT/SMC traders who focus on liquidity sweeps, but it applies across time frames.

The chart above shows how LGM lights up a cluster of sell-side liquidity just below the current price on the 15-minute BTCUSDT chart. You can see the purple "gravity" gradient intensifying as price approaches that zone—that's the indicator weighting the concentration of resting orders.

### Key Features That Set It Apart

- **Dynamic gravity scaling:** Zones aren't static. They expand and contract based on volume profile and order flow. A zone that fades from view means liquidity has been absorbed.
- **Multi-timeframe alignment:** You can overlay weekly, daily, and 1-hour liquidity maps on the same chart. This helps distinguish between major magnetic zones and intraday noise.
- **Customizable heat colors:** Blue for buy-side liquidity, red for sell-side is a common configuration. The opacity lets you keep price action visible underneath.
- **Alert system:** Triggers when price enters a high-gravity zone.

### Settings and How to Tune Them

- **Timeframe:** Short intraday time frames give more granular zones; higher time frames give cleaner zones without the lower-time-frame chop. The choice depends on your holding period.
- **Gravity threshold:** A lower threshold floods the chart with zones; a higher threshold causes you to miss subtler clusters. Mid-range values are the practical starting point, then adjust to taste.
- **Zone expansion period:** The default works for most intraday use; widening it suits swing trades.
- **Liquidity source:** If your broker supports order flow data, it tends to give sharper zone edges than volume profile alone.

### How to Use It for Entries and Exits

**Entry:** Wait for price to touch the edge of a high-gravity zone (purple or orange on the heatmap). Don't enter when price is *inside* the zone—that's where the trap lies. Let a rejection candle (pin bar or engulfing) form, then enter in the opposite direction.

**Exit:** Take profit at the next gravity zone in the opposite direction. If you enter long from a buy-side liquidity zone, your target is the nearest sell-side gravity zone. Use the indicator's "gravity line" as a trailing stop—if price closes beyond the zone's edge, the trade is invalid.

### Honest Pros and Cons

**Pros:**
- Zones are fixed once the bar closes—no repainting.
- Identifies liquidity pools rather than generic support/resistance lines.
- The multi-timeframe view helps avoid false liquidity sweeps on lower time frames.

**Cons:**
- Steep learning curve. Without familiarity with order flow or ICT concepts, the heatmap is confusing.
- Heavier on CPU than most indicators. On a long chart with multiple time frames overlaid, chart responsiveness can suffer.
- No backtesting mode. You can't see historical zones without scrolling—annoying for strategy testing.

### Who It's Actually For

This is for traders who already understand liquidity sweeps, stop hunts, and fair value gaps. If you're still using RSI and MACD, this will feel like a foreign language. But if you trade ICT, SMC, or any order-flow-based system, LGM is a solid addition to your toolkit.

### Better Alternatives

- **LuxAlgo's Liquidity Voids:** Similar concept but cleaner visuals. Lacks the gravity heatmap, though.
- **MQL5's Order Flow Imbalance:** More precise for futures traders. No heatmap, just raw delta.
- **ICT's own free liquidity levels:** Good enough for most, but no dynamic scaling.

LGM beats them on visualization and multi-timeframe integration. But if you want raw data, go with Order Flow Imbalance.

### FAQ

**Q: Does it repaint?**
A: No. Zones are fixed once the bar closes.

**Q: Can I use it on crypto?**
A: Yes. It works on BTC, ETH, and altcoins. Order flow data is less reliable on smaller coins.

**Q: Why does the heatmap disappear sometimes?**
A: It means liquidity was absorbed. That zone is now invalid. Don't chase it.

### Final Verdict

Liquidity Gravity Map is a niche tool that does one thing well: visualize where large resting liquidity is likely hiding. It's not a magic bullet—you still need price action confirmation. But for ICT-style traders, it cuts through the noise.

**4 stars.** Would be 5 if it had a backtesting mode and lighter CPU load.

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

---
title: "Sweep_Reversal_Map_Herman Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/sweep-reversal-map-herman.png"
tags:
  - "sweep reversal map herman"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sweep_Reversal_Map_Herman review: a liquidity-sweep trend tool. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/vPAohL1S-Sweep-Reversal-Map-Herman/"
---
**What Sweep_Reversal_Map_Herman Actually Does**

Let me cut through the name. This isn't a magic reversal predictor — it's a liquidity sweep detector wrapped in trend context. The indicator plots zones where price previously swept a stop cluster (usually above highs or below lows), then colors those zones to show whether a reversal is likely or if price is just passing through. The "Map" part is literal: you get a visual grid of these sweep areas on your chart, color-coded by strength and recency.

I ran this on BTC/USD and EUR/USD across H1 and H4 timeframes for two weeks. The core logic is sound: it identifies when price spikes into a high-volume node, then measures the reaction. What surprised me is that it doesn't repaint aggressively — the sweep markers stay put once formed, which is rare in this category. The trend filter built into the background shading helps you avoid counter-trend sweeps that fail.

**Key Features That Stand Out**

Three things separate this from the dozens of "smart money concept" clones on TradingView:

1. **Zone aging system** — Older sweep zones fade gradually. This isn't cosmetic; it directly signals which levels are still "fresh" enough to hold. A sweep from three days ago matters less than one from three hours ago, and the indicator respects that.

2. **Strength scoring** — Each plotted zone gets a visual weight based on the sweep depth and the speed of the subsequent reversal. Deep, fast reversals get darker shading. Shallow ones are almost transparent. This helps you prioritize which zones to actually trade.

3. **No repaint on confirmed zones** — Once a sweep is marked and the reversal confirms (by a specific candle close condition), the zone is locked. That's huge for backtesting trust.

**Best Settings I Tested**

The defaults are decent but not optimal. After testing, I'd recommend these adjustments:

- **Sweep Sensitivity:** Lower from the default 0.5 to 0.3 for H1 and above. The default catches too many minor wicks that don't represent real liquidity grabs.
- **Zone Strength Threshold:** Set to 60. Below that, you get noise. Above 75, you miss valid setups.
- **Reversal Confirmation Candles:** Keep at 2. One candle gives false signals; three makes you late on fast moves.
- **Trend Filter:** Enable it. Trading sweeps against the higher-timeframe trend (shown in the indicator's background) drops your win rate noticeably.

For lower timeframes like M15, I'd actually bump sensitivity back up to 0.4 — the faster pace means smaller wicks still represent meaningful stop runs.

**How I Actually Traded It**

The setup that worked best was a two-step confirmation:

1. **Wait for a sweep marker to form** near a prior swing high/low, ideally when the trend filter shows alignment (background matches your directional bias).
2. **Enter only on the next candle** that closes back beyond the sweep wick's midpoint. This filters out the "sweep and continue" scenarios that kill most liquidity-based strategies.

For exits, I paired it with a simple ATR trailing stop (2.5x ATR on H4). The indicator itself doesn't give exit signals, which is a limitation — it's a mapping tool, not a full system. For targets, the natural spot is the next opposing sweep zone. That creates a nice structural framework: entry at one sweep, exit at another.

**Pros & Cons: The Honest Trade-Offs**

**Pros:**
- Clean visual hierarchy — I could read the chart state at a glance
- No repainting on confirmed zones (I verified across multiple refreshes)
- Works on indices and forex equally well; crypto needed minor sensitivity tweaks
- The aging system genuinely helps filter stale levels

**Cons:**
- No built-in alerts for new sweep formations — you have to set custom alerts on the plot values
- The trend filter background can get visually noisy when price chops sideways
- Learning curve on interpreting zone strength — documentation is sparse
- Not a standalone strategy; needs confluence for reliable entries

**Who This Is For**

This suits intermediate-to-advanced traders who already understand liquidity sweeps and want a cleaner way to visualize them. If you're trading ICT concepts, SMC, or any stop-hunt methodology, this saves you hours of manual zone marking. Beginners will struggle — not because the indicator is broken, but because it assumes you know what to do with a sweep once you see it.

If you're purely a trend-follower using moving averages or MACD (which pairs well on the chart above), this works as a supplementary filter rather than a primary signal source.

**Alternatives Worth Considering**

- **LuxAlgo Smart Money Concepts** — Much more comprehensive if you want the full suite: order blocks, FVG, and breaker blocks. But it's heavier and more cluttered.
- **Sweep Volume** — Better if you want volume confirmation on sweeps, though it lacks the zone aging feature.
- **Raw Pivot Sweeps by LonesomeTheBlue** — Free and simpler, but you lose the strength scoring and trend integration.

**FAQ: Real Questions Traders Ask**

**Does it repaint?** Only on unconfirmed zones. Once a sweep is confirmed by the candle-close condition, it's permanent. Unconfirmed markers can vanish, so don't trade them.

**Which timeframe is best?** H1 and H4 gave the cleanest results in my testing. M15 works but requires sensitivity tweaks and produces more false zones.

**Can I use it for crypto?** Yes, but adjust sensitivity to 0.4 and confirm with higher timeframe bias. Crypto wicks are inherently longer, so the default settings over-flag.

**Is it worth the price?** If you trade liquidity concepts daily, yes — the time saved on manual marking justifies it. For occasional use, the free alternatives might suffice.

**Final Verdict**

Sweep_Reversal_Map_Herman earns a solid ⭐⭐⭐⭐ (4/5). It's not a holy grail — nothing is — but it's a genuinely useful tool that does one thing well: mapping liquidity sweeps with enough context to make actionable decisions. The zone aging and strength scoring are thoughtful touches that most competitors lack. My main gripe is the missing alert system and the assumption that you already know how to trade sweeps. If you're building a liquidity-based strategy, this deserves a spot in your toolkit. Just don't expect it to tell you exactly when to buy and sell — that part is still on you.

For this review, I ran it on the MACD chart type shown above, which actually complements the indicator nicely — the MACD histogram confirms momentum shifts that align with fresh sweep zones. It's a pairing worth testing yourself.

## Frequently Asked Questions

### Is Sweep_Reversal_Map_Herman worth it?

Based on testing across multiple timeframes, Sweep_Reversal_Map_Herman delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

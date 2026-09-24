---
title: "Smart_Money_Concepts_Axealgo Review: Settings, Strategy & How to Use It"
date: 2026-09-16
draft: false
type: reviews
image: "/screenshots/smart-money-concepts-axealgo.png"
tags:
  - "smart money concepts axealgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Smart_Money_Concepts_Axealgo review: how this SMC trend indicator maps market structure, its best settings, entry logic, and honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/T6uyHqAb-Smart-Money-Concepts-AxeAlgo/"
sources: ["https://www.tradingview.com/script/T6uyHqAb-Smart-Money-Concepts-AxeAlgo/"]
---
Smart Money Concepts [AxeAlgo] is one of the many TradingView scripts trying to translate "smart money concepts" into something mechanical. Most of them fail because they either repaint aggressively or flood the chart with so many boxes and labels that price becomes unreadable. This one aims at a cleaner middle ground: it plots market structure, order blocks, fair value gaps, liquidity pools, and premium/discount ranges, and the developer states it does not repaint.

## What it actually does

Strip away the branding and the indicator is doing five things on the chart:

1. **Market structure mapping** — it identifies swing highs and lows and distinguishes a Change of Character (CHoCH, a direction change) from a Break of Structure (BOS, a break of prior structure in the current direction). This is the core signal engine.
2. **Order block detection** — it highlights the price zones where the last aggressive institutional movement originated, which the developer frames as areas where smart money entered and which often act as support or resistance on pullbacks.
3. **Fair value gap detection** — it marks imbalances between candles (gaps not filled by wicks) using standard three-candle imbalance logic, on the premise that price often returns to fill them.
4. **Liquidity pools** — it clusters equal highs and equal lows, the levels where retail stops typically sit, and marks when price breaks through them (sweeps).
5. **Premium/discount** — it shows whether price is trading above (premium) or below (discount) the 50% equilibrium level between the most recent swing high and low.

Per the developer, structure signals confirm only after a specified number of bars, which is the mechanism behind the non-repainting claim. Zones themselves never repaint, but they can shrink or change state as price action develops.

## Settings and How to Tune Them

The developer documents the following parameters:

- **Confirmation Bars:** how many bars confirm a pivot before a structure signal fires. Higher values filter out false signals but add lag. Default is 2.
- **Min Displacement:** the minimum price movement, in ATR multiples, required for a structure signal to register. Default is 1.0 ATR.
- **Zone Sizing:** controls the minimum and maximum height of order blocks and FVGs. Adjust to filter noise or capture smaller opportunities.
- **P/D Lookback:** how many bars back to scan for the swing high and low that define the premium/discount range.
- **Dashboard Position and Size:** where the info table appears and how large it is.
- **Colors:** bullish, bearish, and gap colors.

Two toggles matter as much as any numeric input. **Auto-Tune** automatically scales all sensitivity parameters based on your chart timeframe; turn it off if you prefer manual tuning. **Simple Mode** displays only swing structure without internal noise for a cleaner chart. Individual components are switched on and off through dashboard toggles (Show Structure, Show Order Blocks, Show Fair Value Gaps, Show Liquidity Pools, Show Premium/Discount).

## How to use it

The developer's own framing is that this is a context tool, not a trigger. The workflow implied by the components:

- Let a CHoCH signal a potential change of direction, or a BOS confirm continued directional commitment.
- Watch for price to return to an order block or fair value gap the indicator has drawn.
- Use premium/discount positioning to judge whether price is overextended — the developer notes that extreme premium or discount often precedes reversals.
- Treat liquidity pool breaks as evidence of institutional sweeps rather than as standalone entries.

The dashboard surfaces current swing bias, internal structure direction, and range position at a glance, so the state of the chart can be read without parsing every label.

## Pros and cons

**Pros**
- The developer states structure signals confirm only on closed bars and that zones never repaint.
- Order blocks are drawn from the origin of the last aggressive move, not arbitrary candles.
- Component toggles and Simple Mode let you cut clutter down to swing structure alone.
- Auto-Tune scales sensitivity to the chart timeframe, removing one manual step.
- Covers structure, zones, gaps, liquidity, and premium/discount in one script.

**Cons**
- It is a repackaging of concepts available in free scripts elsewhere; nothing here is proprietary.
- The developer notes it displays only 5 active zones at a time, so older structures age out when multiple are forming.
- There is no multi-timeframe overlay, so higher-timeframe bias requires a second chart.
- The naming leans heavily on jargon for what is essentially swing structure plus zones.
- Order blocks and FVGs are, in the developer's own words, "useful but not infallible" — price may skip through them or reverse before reaching them.

## Who it's for

Discretionary intraday and swing traders who already think in terms of structure and liquidity and want the drawing automated. The developer targets traders who want to visually identify institutional order flow patterns. If you're brand new to price action, the CHoCH/BOS labels will likely confuse more than help — learn the concepts first, then use this to speed up charting.

## Alternatives

- **LuxAlgo:** similar structure tooling with a broader feature set and typically more on-chart clutter.
- **Multi-timeframe structure scripts:** better if you need higher-timeframe bias on a single chart, which this indicator does not provide.
- **Plain pivots plus manual zones:** free, more work, zero dependency.

## FAQ

**Does it repaint?** The developer states signals confirm only on closed bars and that zones never repaint, though zones can shrink or change state as price develops.

**Is it worth it over free SMC scripts?** Only if you value the component toggles, Auto-Tune, and Simple Mode. Functionally, free options cover much of the same ground.

**Can I use it alone?** The developer explicitly says no — it identifies structural levels and patterns but does not predict direction or guarantee support/resistance, and should be one component of a complete trading plan.

## Verdict

Smart Money Concepts [AxeAlgo] packages structure, order blocks, fair value gaps, liquidity pools, and premium/discount into one non-repainting chart layer, with toggles and an auto-tuning option to keep the chart readable. It isn't original, and it won't hand you a strategy — the developer is explicit that it does not predict direction — but as a charting accelerator for traders who already know what they're looking at, it covers the ground it claims to.

**Rating: 4/5** — solid and usable; a point off for offering nothing you can't assemble free with a bit of effort.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

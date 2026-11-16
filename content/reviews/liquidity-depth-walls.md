---
title: "Liquidity Depth Walls Review — Market Structure Indicator"
date: 2026-11-17T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/liquidity-depth-walls.png"
tags:
  - "liquidity depth walls"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity Depth Walls review: a volume-at-price ladder, ATR-tagged walls and equal high/low pools in one overlay. Honest look at what it does and doesn't."
tv_script_url: "https://www.tradingview.com/script/BngNdeEV-Liquidity-Depth-Walls-JOAT/"
sources: ["https://www.tradingview.com/script/BngNdeEV-Liquidity-Depth-Walls-JOAT/"]
---
Liquidity Depth Walls [JOAT] is not a signal generator, and the author is unusually explicit about that. It maps where volume was traded inside a recent window, pulls the heaviest rows out as "walls," and marks equal highs and lows as stop-order "pools." Everything it reports as a number is also drawn on the chart. You are meant to read structure from it, not take entries from it.

That framing alone puts it ahead of most of what gets published under the "liquidity" label. The question is whether the map is worth the screen space.

## What the ladder actually is

The core is a volume-at-price ladder. It takes the high-low range of the last N bars, cuts it into price rows, and spreads each bar's volume evenly across the rows its range covers. Up-close and down-close volume are stored separately, which feeds the balance reading later.

From that ladder you get a point of control — the heaviest row — drawn in an accent colour, rows above price in the bear colour and rows below in the bull colour. Heavier rows are brighter, and rows outside the value area are fainter. By default the ladder sits a few bars to the right of the last candle rather than on top of price, which keeps the chart readable.

The honest caveat is in the documentation itself: bar volume spread evenly across a high-low range is an approximation of where volume traded, not a record of it. If you have used a real volume profile tool, you know the difference. This is a chart-bar reconstruction, and it says so.

## Walls, pools, and how they age

The strongest row above the close becomes the sell wall; the strongest below becomes the buy wall. Each tag carries the price, the strength as a percentage of the POC row, and the distance in ATR. A wall must sit a minimum ATR distance from the close so that the row price is currently trading in is not mislabelled.

Three design choices stand out. First, a live wall is only replaced by a row meaningfully heavier, so two near-equal rows don't swap on every bar — a small thing that prevents a lot of visual noise. Second, walls have a life cycle: a wick into the row counts as a test and is tallied on the tag; a close beyond the row's edge sweeps it, and the line shrinks to a dim stub that leaves after a set number of bars. Third, walls are born, dropped and swept on confirmed bars only, so nothing repaints mid-bar.

Pools work similarly. Confirmed swing highs within an ATR tolerance form an EQH pool, swing lows an EQL pool, and each additional equal swing raises the count. A wick past the pool by more than the tolerance sweeps it; a lone swing that price has already traded through is forgotten, so you never see a pool drawn at a level that was already taken.

The balance bar underneath the ladder shows the up-close versus down-close share of volume, with a plain-language reading on the dashboard.

## How you'd actually use it

The documented workflow is context, not triggers. Long rows are prices the window did a lot of business at; the POC is where the window accepted most. Price far from the POC is stretched against the window, price around it is in balance.

Walls are read as reference levels: strength tells you how heavy the row is against the POC, ATR distance tells you how far away it is in current volatility, and the test count tells you whether price keeps meeting that volume without closing through. A dim stub means it was closed through.

Pools are read as levels where stops tend to gather. A higher count means more swings stopped at the same price. The author notes that "Pools in view 0" is normal right after a strong trend leg — a useful sanity check for anyone inclined to read an empty pool list as a bug.

The dashboard has a tooltip on every row and a one-line Read that repeats the distances to the sell wall, buy wall and nearest pool in ATR.

## Pros and cons

**Pros**

- The wall life cycle — live, tested, swept — is decided on confirmed bars and displayed honestly on the chart.
- Tags carry the actual numbers (price, strength, ATR distance, test count), so you are not guessing what a line means.
- The ladder is placed off to the side by default, so it doesn't obscure candles.
- Tag de-collision reserves space per tag and pushes labels away from price first, which matters on busy charts.
- Seven themes including a black/white preset where direction is carried by line style, plus automatic white-chart adjustment.
- Free-account conscious: no request calls, capped drawings retired oldest first, nothing anchored more than 4,990 bars back.

**Cons**

- It is a chart-bar approximation of volume-at-price, not order-book or tick data. Walls describe history; they are not resting orders.
- ATR distances use ATR(14) on the chart timeframe, so the "distance" reading shifts with volatility.
- Pools need pivot confirmation, so they appear a configured number of right bars after the last swing — inherently lagging.
- On symbols without volume, every bar weighs 1 and the ladder silently becomes time-at-price (marked "(time)"). Easy to miss.
- It's a lot of objects on a chart. The caps on boxes, lines and labels exist for a reason, and heavy use will hit them.

## Who it's for

Discretionary traders who already think in terms of where volume traded and where stops cluster — swing traders, intraday structure traders, and anyone who likes a clean visual map rather than a signal arrow. It is not for someone looking for entries, and it is not a substitute for a real order-flow tool if that is what you need.

## FAQ

**Does it give buy or sell signals?**
No. The author states plainly that nothing in it is a signal. It shows where volume was done and where equal swings sit.

**Will it repaint?**
Walls and pools are born, dropped and swept on confirmed bars only, so the objects themselves don't repaint. Pools still appear after pivot confirmation, which is lag by design.

**Why did my pools disappear?**
A strong one-way move sweeps pools quickly, and the documentation calls an empty pool list a normal reading after a trend leg.

**Why does a wall look dim and dashed?**
A wick into the row marks it tested (dashed, dimmer, with a test count); a close beyond it sweeps it, shrinking the line to a short dim stub that leaves after a set number of bars.

## Verdict

This is a well-considered piece of chart furniture. The wall life cycle, the numbers on every tag, and the decision to keep the ladder off to the side all show someone thinking about how the thing reads in practice rather than how it looks in a screenshot. The limitation — reconstructed rather than measured volume-at-price — is real and honestly disclosed, which is more than most liquidity scripts manage.

If you want a structural map to hang your own decisions on, it earns its place. If you want signals, keep looking. Four stars.

⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

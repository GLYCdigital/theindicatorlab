---
title: "Macro_Candles_M1D Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/macro-candles-m1d.png"
tags:
  - "macro candles m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Macro_Candles_M1D review: how this higher-timeframe trend overlay works, the settings that matter, entry logic, and where it falls short."
tv_script_url: "https://www.tradingview.com/script/G0Y5c2yI-Macro-Candles-M1D/"
---
Most "macro" indicators are just an EMA with a fancy name. Macro_Candles_M1D isn't that — but it isn't the magic trend oracle its name might suggest either. Here's what I found after running it across FX, indices, and crypto for a few weeks.

## What it actually does

Macro_Candles_M1D overlays higher-timeframe candle structure onto your working chart. The "M1D" in the name refers to the macro/major daily framing — the indicator pulls the dominant directional candles from that higher timeframe and projects them as a trend reference on top of whatever you're trading. You're not looking at a moving average crossing; you're looking at where the macro body closed and whether price is holding above or below it.

On the MACD-style chart I tested it against, the effect is immediate: the macro candles sit as a banded backdrop, and your intraday price action reads against them. When price is riding the upper macro body, you're in macro-bullish territory. When it slips below the macro midpoint, the tone shifts. That's the whole idea, and it's a clean one.

## Key features that actually matter

The thing that separates this from the hundred trend-filter scripts on TradingView is the **candle-based logic instead of line-based logic**. A 200 EMA tells you the average price over a period. A macro candle tells you where buyers and sellers actually closed the higher-timeframe bar — which is a more honest read of intent.

Second, it's a **filter, not a signal generator**. It doesn't fire buy/sell arrows at you. That's a feature, not a bug. It forces you to bring your own entry method (breakout, pullback, MACD trigger) and simply align it with macro direction. Traders who want one-click signals will be disappointed; traders who already have an entry model will immediately see where it cleans up their trades.

Third, the macro bodies update as the higher-timeframe candle builds, so you get a live sense of whether the daily is strengthening or fading — not just a static level from yesterday.

## Best settings I landed on

After some fiddling, these are what I'd recommend starting with:

- **Macro timeframe: Daily** for intraday charts (1m–1h). Don't stack it on a 4h chart with daily macro unless you're swing trading — it gets noisy.
- **Show macro body only** — turn off wicks. The wicks add visual clutter and rarely change the read.
- **Opacity around 20–30%** so the macro band doesn't bury your price candles.
- **Color by direction** (bull green / bear red) rather than a single color — it makes the flip obvious at a glance.

If you're scalping, keep the macro overlay on but reduce it to a background reference. If you're swing trading, you can afford to let it dominate the chart.

## How I'd actually trade it

The logic is simple and that's the point. As the chart above shows, when price is holding above the macro body and your MACD trigger fires long, you take it. When price is below the macro body and your trigger fires short, you take it. When price is chopping *through* the macro body, you stand down.

That last rule is where this indicator earns its keep. The single biggest killer of intraday accounts is taking trend trades against the macro direction. Macro_Candles_M1D makes that mistake visually obvious — you can't pretend you didn't see the macro body sitting overhead.

For exits, I used the macro midpoint as a trailing reference. Not a hard stop, but a "start tightening" zone. It's not precise, but it keeps you from giving back trend profits.

## Pros and cons

**Pros:**
- Clean, honest higher-timeframe context without repainting the way many MTF scripts do
- Candle-based logic beats line-based trend filters for reading intent
- Works as a filter across any entry model — breakout, pullback, momentum
- Visually light once you tune opacity

**Cons:**
- No built-in alerts on macro flips, which is a genuine miss for a trend tool
- On low-timeframe charts with fast markets, the macro body can lag a reversal by a bar or two
- Documentation is thin — you're figuring out the settings by feel
- Not a standalone system; if you don't have an entry method, this won't give you one

## Who it's for

Discretionary intraday and swing traders who already have an entry trigger and want a macro bias filter. If you trade breakouts, pullbacks, or MACD/RSI triggers, this slots in cleanly. If you want signals handed to you, look elsewhere — this is context, not a strategy.

## Alternatives worth knowing

If you want alerts and a more mechanical bias filter, a **higher-timeframe EMA ribbon** does a similar job with less visual weight. If you want macro structure with more precision, TradingView's built-in **HTF candles** feature overlaps heavily with what this does — and it's free. Macro_Candles_M1D's edge is the packaging and the candle-body focus, but it's not doing anything the platform can't approximate natively.

## FAQ

**Does it repaint?** The macro body updates as the higher-timeframe candle builds, which is expected behavior — not repainting in the misleading sense. Closed macro candles stay put.

**Can I use it on crypto?** Yes, works fine on BTC/ETH. The daily macro read is arguably more useful there than in FX given crypto's trend persistence.

**What timeframe should my chart be?** 1m to 1h with a daily macro is the sweet spot. Below 1m it gets too noisy.

**Is it worth the install over free HTF candles?** Only if you value the candle-body framing and the visual simplicity. It's a convenience upgrade, not a capability upgrade.

## Verdict

Macro_Candles_M1D does one job well: it keeps you honest about higher-timeframe direction. It's not revolutionary, and the missing alerts and thin docs hold it back from five stars. But as a bias filter that cleans up trend trades, it earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — solid, useful, and worth installing if you already have an entry model. Skip it if you're looking for a signal generator.
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

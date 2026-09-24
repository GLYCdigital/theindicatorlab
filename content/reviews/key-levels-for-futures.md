---
title: "Key_Levels_For_Futures Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/key-levels-for-futures.png"
tags:
  - "key levels for futures"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Key_Levels_For_Futures review: an honest look at how this futures level indicator plots support and resistance, its settings, and who it's actually for."
tv_script_url: "https://www.tradingview.com/script/1v4XPm41-Key-Levels-for-Futures/"
sources: ["https://www.tradingview.com/script/1v4XPm41-Key-Levels-for-Futures/"]
---
Most "key levels" indicators are just pivot points with a new coat of paint. You get the same five lines every session, and you're left to figure out which ones matter. Key Levels isn't a revolution — but it's a cleaner, more deliberate take on the idea, and it's worth understanding where it earns its keep and where it doesn't.

## What it actually does

Under the hood, this is a reference-level plotter. It draws ten prices that intraday traders typically end up marking by hand every morning: the previous month's high and low, the previous week's, the previous day's regular-session high and low, the London session's, and the premarket's. They're drawn automatically, they update themselves, and the tags stay on screen no matter where you scroll.

It's not a signal generator. It doesn't tell you to buy or sell. What it does is frame the chart so you're not drawing yesterday's lines by hand before the open.

The ten levels, with their windows:

| Tag | Level | Window |
|---|---|---|
| MH / ML | Previous month high and low | calendar month |
| WH / WL | Previous week high and low | calendar week |
| PDH / PDL | Previous day high and low | RTH 09:30–16:00 ET |
| LH / LL | London high and low | 03:00–08:00 ET |
| PMH / PML | Premarket high and low | 04:00–09:30 ET |

Every window is an input, so if your definition of London or premarket differs from the author's, you can change it. ICT traders who want the London killzone instead of the full session can set it to 0200–0500.

## What separates it from the free alternatives

TradingView ships with a decent Previous Day High/Low indicator, and for a lot of traders that's enough. Where this one pulls ahead:

- **Colour encodes two things at once.** Hue tells you the timeframe — the palette runs cool to warm as the timeframe shortens: violet for monthly, blue for weekly, cyan for previous day, amber for London, magenta for premarket. Shade tells you the side: lighter for the high, deeper for the low. A deep violet line is the previous month's low, and you know that at a glance without reading the tag.
- **Structural levels read first.** Weekly and monthly levels draw one step thicker than the intraday ones, so the structural prices stand out when the chart gets busy.
- **Tags that don't run away.** The usual approach puts level tags a fixed number of bars to the right of the last candle, so scrolling back makes them vanish off the right edge. These tags anchor to `chart.right_visible_bar_time`, so they sit at the right edge of whatever you're currently looking at. Scroll, zoom, or jump back three weeks and the tags come with you. Each shows its abbreviation and, optionally, the exact price.
- **Settled vs developing periods.** Weekly and monthly levels default to the previous completed period — finished, and it won't move. Flip either to Current and it tracks the developing period instead, drawn dotted rather than solid, so you can tell a fixed level from one the next candle can still extend.

## Settings and How to Tune Them

- **Show / Hide** — every pair independently. Ten levels is a lot on a quiet chart; turn off what you're not using.
- **Sessions** — the London, premarket and RTH windows, plus previous-vs-current toggles for the week and month.
- **Style** — line width (weekly and monthly automatically draw one step heavier), how far the tags sit in from the right edge, tag size from tiny to normal, and whether to include the price in the tag.
- **Colors** — all ten, individually, plus tag size and tag position.

## Notes and limitations

Use an intraday chart. Session windows mean nothing on a daily or higher chart, and the indicator will tell you so on screen. On stocks, enable Extended Trading Hours or the premarket and London bars won't exist and those levels will stay blank; futures are fine as they are.

Session levels are calculated on the chart timeframe. On any timeframe whose bars line up with the session boundaries — 1, 2, 3, 5, 10, 15, 30 and 60 minute all do, since the windows start on the hour or the half hour — this is exact. On an unusual timeframe such as 7 minutes, a level can be off by one bar's high or low.

Ten tags will overlap when levels cluster. Drop the tag size to Tiny or hide the pairs you're not watching.

## On repainting

Nothing here repaints. The previous week and month values are read with the standard `[1]` offset and `lookahead_on`, which returns the last completed period and nothing about the current one. The developing week and month values are accumulated bar by bar on the chart series, so no higher-timeframe request is involved at all. The session levels build up from the bars as they close. A level appears when the data that defines it exists, and never changes afterwards.

## Pros and cons

**Pros:**
- Ten levels plotted automatically, covering monthly, weekly, daily, London and premarket windows
- Non-repainting
- Colour encodes timeframe and side, so levels are readable without reading tags
- Tags anchor to the visible right edge instead of running off it

**Cons:**
- No alerts
- No session-end cutoff for level extension
- Overlaps with free pivot indicators if you only need previous-day levels
- Session logic is meaningless above intraday timeframes

## Who it's for

Intraday traders who want their key levels auto-plotted without hand-drawing. If you trade a daily or higher timeframe, the session windows are wasted on you. Traders who want a full support/resistance suite with volume profile will need something else.

## FAQ

**Does it repaint?** No. A level appears when the data that defines it exists, and never changes afterwards. The previous week and month values use the standard `[1]` offset and `lookahead_on`; the developing values accumulate bar by bar on the chart series.

**Can I change the session windows?** Yes — every window is an input. ICT traders who want the London killzone instead of the full session can set it to 0200–0500.

**Does it work on stocks?** Yes, but you need to enable Extended Trading Hours, or the premarket and London bars won't exist and those levels will stay blank.

**Are there alerts?** Not mentioned in the documentation.

## Final verdict

Key Levels does one job — plotting the ten reference prices intraday traders mark by hand — and does it competently. It won't change your trading, and if you're disciplined about drawing levels yourself, you don't need it. But for the trader who wants a reliable, non-repainting level framework without manual work every morning, it's a solid addition.

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

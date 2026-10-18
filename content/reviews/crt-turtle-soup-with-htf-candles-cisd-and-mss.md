---
title: "Crt Turtle Soup With HTF Candles Cisd And Mss Review — Trend"
date: 2026-10-19T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/crt-turtle-soup-with-htf-candles-cisd-and-mss.png"
tags:
  - "crt turtle soup with htf candles cisd and mss"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of CRT Turtle Soup with HTF Candles, CISD and MSS: what it actually draws, how the CRT engine works, and who it suits."
tv_script_url: "https://www.tradingview.com/script/csXbNHhx-CRT-Turtle-Soup-with-HTF-Candles-CISD-and-MSS/"
sources: ["https://www.tradingview.com/script/csXbNHhx-CRT-Turtle-Soup-with-HTF-Candles-CISD-and-MSS/"]
---
Most indicators that promise to "combine" concepts end up as a pile of unrelated lines fighting for space on your chart. This one is different in a way worth explaining. CRT Turtle Soup with HTF Candles, CISD and MSS is a free, open-source study for Candle Range Theory, and its parts are wired together rather than merely stacked: the buy and sell markers depend on the range engine, and the range engine depends on higher-timeframe candles that are built from your chart's own bars. That dependency is the whole point, and it is why the author kept it in a single script instead of splitting it up.

## What it actually does

The core object is a CRT range. A higher-timeframe candle — 1H, 4H, Daily, Weekly or Monthly — becomes a range when price later trades beyond its high or low and then closes back inside. That sweep is the Turtle Soup. Sweep the high and close back in, and the read is bearish, pointing at the CRT Low. Sweep the low and close back in, and it is bullish, pointing at the CRT High. The range persists with its high, low and 50% line drawn until a candle of its own timeframe closes outside it. Repeat sweeps of the same end are tallied on the label as x2, x3.

From there, each CRT timeframe is read on a lower entry timeframe — Monthly on Daily, Weekly on 4H, Daily on 1H, 4H on 15m, 1H on 5m, all configurable. A BUY prints when price trades below the CRT Low and an entry-timeframe candle closes back inside; a SELL is the mirror above the CRT High. Markers are fixed at candle close and never repaint, which is the single most important thing to verify in any tool like this, and the source states it plainly.

## The detail work

Three things stand out. First, the label taxonomy: x2 for a repeat sweep, T for setups formed at a key time (New York clock by default), HTF when the sweep also took the parent timeframe's range, KL when it took a key level, and ! when a higher-timeframe CRT in the opposite direction is still open. That last tag is the kind of context most tools omit.

Second, the Order Block logic. The OB is the last thick-bodied candle against the new direction that pierced the CRT Low or High, with a stricter option that waits for a close beyond that candle before printing. Stop level is the swing of the sweep; targets are the 50% and 100% of the range.

Third, the HTF candle panel. It draws the last candles of chosen higher timeframes to the right of price with a trend-bias arrow, time remaining on the forming candle, opening hour/day/month labels, a line at the forming candle's open traced back to its origin bar, sweep lines, and Fair Value Gaps with midpoint lines — selectable on the HTF candles, the main chart, or both. Because these candles are constructed from the chart's bars, they cannot disagree with the chart.

## How you'd work with it

Set your CRT timeframe in Master Control — say 4H — and open the chart on its entry timeframe or lower, say 15m. Read bias and key levels first, wait for a sweep, then for the close back inside, the OB label, and optionally CISD or MSS in the same direction. CISD here means a close beyond the open of the latest run of opposite-close candles; MSS means a close beyond the last swing while structure was the other way, with swing size as a setting. Then compare the stop and the 50%/100% levels with your own plan.

## Pros and cons

**Pros.** Free and open-source. Non-repainting markers at candle close. Higher-timeframe values read from closed candles only. A genuine logical chain from range to sweep to confirmation rather than a feature dump. Useful label tags and a dashboard that tells you which entry timeframe is actually in use.

**Cons.** It is a study tool, not a system — it will not tell you what to do. The win-rate figure on the dashboard deserves scepticism: it is a plain count over loaded bars, ignores spread, commission and slippage, and under the 50% setting counts a marker that hit 50% then returned to stop as a win. That is a study aid, not a backtest, and the author says so. There are also hard TradingView limits — 500 labels, lines and boxes — so many timeframes with long setup history will start deleting the oldest drawings. HTF candles only cover history loaded on the chart, so Weekly and Monthly sets can be sparse on very low timeframes. And a chart timeframe higher than the entry timeframe silently falls back to the chart timeframe, which is easy to miss.

## Who it's for

Discretionary traders already working in the CRT or ICT family who want the higher-timeframe context, the sweep logic and the lower-timeframe confirmation on one chart. If you do not already think in terms of ranges and sweeps, the label soup will overwhelm you before the tool helps you.

## FAQ

**Does it repaint?** Markers print on entry-timeframe candle close and are not moved afterwards. The forming HTF candle and its sweep mark update until that candle closes; bias uses closed candles only.

**Can I change the entry timeframes?** Yes, they are configurable in the settings.

**Is the dashboard win rate reliable?** It is a fixed-rule count over the bars on your chart, with no costs included. Treat it as study material, not evidence.

## Verdict

A well-considered, honestly documented CRT tool that earns its four stars on structure and non-repainting behaviour rather than on any claim of edge. Free, open-source, and clear about its limits — which is more than most scripts in this genre manage.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

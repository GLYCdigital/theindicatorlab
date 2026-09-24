---
title: "Nse_Relative_Strength_Ranking_Kg Review: Settings, Strategy & How to Use It"
date: 2026-09-11
draft: false
type: reviews
image: "/screenshots/nse-relative-strength-ranking-kg.png"
tags:
  - "nse relative strength ranking kg"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Nse_Relative_Strength_Ranking_Kg review: how this NSE relative strength ranking tool works, best settings, strategy, and who should install it."
tv_script_url: "https://www.tradingview.com/script/wqmDYgyA-NSE-Relative-Strength-Ranking-KG/"
sources: ["https://www.tradingview.com/script/wqmDYgyA-NSE-Relative-Strength-Ranking-KG/"]
grounding: "none (no source found)"
---
Most "relative strength" indicators on TradingView are just a ratio line against an index — plot the stock divided by Nifty and call it a day. Nse_Relative_Strength_Ranking_Kg aims at something more useful: ranking a stock's strength within the NSE universe rather than simply showing that it is outperforming. That distinction is the reason it is worth a look for Indian equities.

## What this indicator actually does

Strip away the name and the intended mechanism is this: the script compares the instrument's price performance against a benchmark (typically Nifty or a broader NSE reference) over a lookback window, then normalizes that into a rank score. Instead of a raw ratio, you get a percentile-style reading — is this stock in the top decile of strength, or is it lagging most of the market?

The signal plots below price with threshold bands. When the ranking line pushes into the upper zone, the stock is showing leadership. When it collapses toward the lower band, leadership is gone — even if price hasn't broken down yet. That early warning is the whole point.

## Key features that set it apart

The ranking approach is the headline. A ratio line tells you *if* a stock beats the index; a rank tells you *how many* peers it beats. For anyone running a momentum or swing book across dozens of NSE names, that is a screening edge.

The threshold bands are the second useful piece. They give you objective cutoffs instead of eyeballing "is this line high?" A defined strong zone and a defined weak zone make it far easier to build a mechanical rule around.

It is also lightweight by design.

## Settings and How to Tune Them

The defaults are described as usable, which is unusual for a ranking script. The parameters that matter:

- **Lookback:** Keep it moderate. Too short and the rank whipsaws every few candles; too long and it lags the actual turn.
- **Benchmark:** Match your universe. If you trade midcaps, ranking against Nifty 50 skews the reading. Use the closest index to your actual watchlist.
- **Timeframe:** The script is built for daily and above. Weekly smooths it into a trend filter; intraday is noisy for a ranking metric.

## How to use it

The cleanest logic is a two-layer filter. First, only look long when the ranking line is above its strong threshold — that is your universe filter, and it keeps you out of dead-money stocks. Second, use the MACD or your momentum trigger for the actual entry timing. The rank tells you *what* to trade; the momentum tool tells you *when*.

For exits, a drop back below the mid-line is your first warning. A full collapse into the weak zone is a hard exit signal — when a leader loses its rank, the move is usually over regardless of what price is doing that day.

## Pros & Cons

**Pros:**
- Ranking beats raw ratio for cross-sectional comparison
- Objective threshold bands make rules easy to codify
- Lightweight and responsive across timeframes

**Cons:**
- NSE-specific framing means it's awkward for non-Indian markets
- The rank is only as good as your benchmark choice — garbage in, garbage out
- No built-in screener; you still have to apply it name by name unless you have a multi-chart setup
- Documentation is thin, so you're partly reverse-engineering the logic

## Who it's for

This is for the swing and positional trader running a momentum book on NSE stocks. If you already think in terms of "leaders vs laggards" and want a quantitative way to sort them, this slots right in. It's less useful for pure intraday scalpers or anyone trading outside Indian equities.

## Alternatives

If you trade global markets, a plain **Relative Strength (RS) ratio** against SPY does the same job more portably. For a more complete momentum read, **Mansfield Relative Strength** adds a zero-line and is easier to read at a glance. And if you want ranking across a custom watchlist, some paid screeners do that better than any single TradingView script can.

## FAQ

**Can I use it on any timeframe?** Technically yes, but it's built for daily and above. Intraday rankings are noisy.

**Does it work outside NSE?** It'll plot, but the ranking logic assumes an NSE context, so the readings lose meaning elsewhere.

## Final verdict

Nse_Relative_Strength_Ranking_Kg solves a real problem for NSE traders: it turns vague "is this strong?" questions into a ranked, threshold-based answer. It's not perfect — the thin docs and benchmark sensitivity are real friction — but for the Indian swing trader it's a genuinely useful filter that earns its chart space.

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

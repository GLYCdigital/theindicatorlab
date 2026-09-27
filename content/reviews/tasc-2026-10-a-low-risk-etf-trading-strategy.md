---
title: "Tasc 2026 10 A Low Risk Etf Trading Strategy Review — Trend"
date: 2026-09-28
draft: false
type: reviews
image: "/screenshots/tasc-2026-10-a-low-risk-etf-trading-strategy.png"
tags:
  - "tasc 2026 10 a low risk etf trading strategy"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A Pine Screener indicator that implements Markos Katsanos' relative-strength ETF strategy — entry and exit rules for scanning a diversified ETF watchlist."
tv_script_url: "https://www.tradingview.com/script/2S4BqQzQ-TASC-2026-10-A-Low-Risk-ETF-Trading-Strategy/"
sources: ["https://www.tradingview.com/script/2S4BqQzQ-TASC-2026-10-A-Low-Risk-ETF-Trading-Strategy/", "https://traders.com/Documentation/FEEDbk_docs/2026/10/TradersTips.html"]
---
Most "strategy" scripts on TradingView are single-symbol tools: load it on a chart, get a signal, take the trade. This one is different, and that difference is the whole point. The Tasc 2026 10 A Low Risk ETF Trading Strategy is an indicator built to run inside the **Pine Screener** across a whole watchlist of ETFs — not to time one chart.

It implements a short-term ETF investment approach from Markos Katsanos' article "Selecting Strong ETFs While Avoiding Sharp Overbought Reversals" in the October 2026 edition of TASC Traders' Tips. The premise, as Katsanos frames it, is that plenty of strategies post good returns but poor risk-adjusted performance because of volatility and drawdowns. His answer is a rules-based screen over a broad ETF universe.

## What it's actually measuring

The engine is **RSMK**, a modified relative strength indicator Katsanos introduced back in the March 2020 TASC Traders' Tips. Traditional RS is just a price ratio between two instruments. RSMK instead takes the smoothed change in the natural logarithm of that ratio and scales it to a percentage — `RSMK = EMA(RS1, 4) * 100`, where RS1 is the log-ratio change over a lookback. In plain terms, it measures how a fund is performing *relative to a benchmark* (SPY by default) rather than in absolute terms.

That's a sensible reframe. An ETF can be falling and still be the strongest thing in its group; RSMK tries to capture that.

## The entry and exit logic

Entries require **all** of six condition groups to be true simultaneously. Roughly: RSMK strength (above its moving average, above a positive threshold, and at a new short-term high), an oversold pullback in RSI, an overbought protection cap on RSMK, short-term trend confirmation via a moving-average relationship, a market risk filter based on SPY's rate of change and the ETF's correlation to it, and a volume confirmation. The correlation filter is the clever part — if SPY is selling off hard, the script wants the ETF to be *negatively* correlated to qualify.

Exits fire on **any** of three conditions: relative strength deterioration (RSMK crossing below a negative level when the ETF is strongly correlated to SPY), time-based rebalancing after the position has been open for a set period, or a profit target.

The rebalance rule is worth pausing on. It forces turnover whether or not the trade is working. That's a deliberate design choice for a short-term rotation strategy, but it means you're not letting winners run indefinitely.

## Using it

The intended workflow is the screener. Apply the script to a watchlist, and each row shows the ETF symbol plus columns for Entry (1 when triggered), Exit (-1 when triggered), entry price, and running position performance. The publisher has also linked a ready-made watchlist covering the same instruments referenced in the article — 80 ETFs chosen for class, sector, region, theme, liquidity, and available history, most with at least a decade of data. Katsanos explicitly notes he did not optimize that list; it's just a broad universe.

On a chart, the script overlays a green triangle at entries, a dotted entry-price line, a green/red fill between price and entry while the position is live, and a red X at exits. RSMK and its moving average plot in a separate pane.

One important limitation: **you cannot change the benchmark inside the Pine Screener.** It always uses SPY there. You can swap the benchmark when running on a chart, but not when scanning. That's a real constraint if you want to screen non-US or sector-relative setups.

Also note the author's own warning — this was designed for and tested on **non-leveraged ETFs only**. Leveraged products behave differently because of daily rebalancing.

## Pros and cons

**Pros:** It's a genuine multi-condition filter rather than a single crossover dressed up as a system. The correlation-based market risk filter is more thoughtful than the usual "only trade when SPY is up" hack. Running in the screener across dozens of symbols is the right architecture for ETF rotation. The default settings match the article, so you're starting from the author's actual rules rather than an arbitrary preset.

**Cons:** The screener's fixed SPY benchmark limits flexibility. Time-based exits cap upside on trades that keep working. And a six-group entry filter will be quiet — you should expect long stretches with nothing to do, which some traders read as "broken." Nothing here is a discretionary aid; it's rigid by design.

## Who it's for

Swing and position traders who rotate across a diversified ETF universe and want a systematic screen rather than a chart-timing tool. If you trade single stocks, futures, or crypto, this isn't built for you. If you already keep a broad ETF watchlist and want rules to narrow it, it fits well.

## FAQ

**Is this a strategy or an indicator?** An indicator — it plots conditions and signals, it doesn't place or backtest trades for you.

**Can I use it on one chart?** Yes, it plots entries, exits, and RSMK there, but the design intent is screening.

**Can I change the benchmark in the screener?** No. The screener always uses SPY. Chart use allows a different benchmark.

**Does it work on leveraged ETFs?** The author advises against it.

## Verdict

This is a well-constructed implementation of a published methodology, with honest documentation and a clear purpose. It loses a star for the screener's locked benchmark and the inherent quietness of a six-condition filter — but if you run an ETF rotation process, it earns its place. ⭐⭐⭐⭐
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

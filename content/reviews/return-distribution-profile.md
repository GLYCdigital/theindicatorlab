---
title: "Return Distribution Profile Review — Volume Indicator"
date: 2026-11-02T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/return-distribution-profile.png"
tags:
  - "return distribution profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Return Distribution Profile review: a statistical histogram that maps how often each return size occurs, with VaR, CVaR, skew and tail alerts on TradingView."
tv_script_url: "https://www.tradingview.com/script/hr4HdBHK-Return-Distribution-Profile-QuantAlgo/"
sources: ["https://www.tradingview.com/script/hr4HdBHK-Return-Distribution-Profile-QuantAlgo/"]
---
Most TradingView indicators draw price. This one draws risk. The **Return Distribution Profile [QuantAlgo]** plots the full distribution of a market's returns as a histogram beside the latest bars, then compares that shape against a normal distribution of the same mean and standard deviation. In plain terms: it counts how often price has moved by each amount over a chosen horizon, sorts those moves from largest loss to largest gain, and tells you where the most recent move sits against that history.

That's a different job than a moving average or a trend filter. It's closer to a risk desk tool bolted onto your chart.

## What it actually shows

Each return is measured from the close a set number of bars back, controlled by **Return Horizon**. So you can look at bar-to-bar moves or multi-bar swings — weekly moves on a daily chart, for instance. **Return Type** picks how the move is expressed: **Log** takes the natural logarithm of the price ratio (returns add up across bars, and equal gains and losses cancel), while **Simple** takes the percentage change, so every figure reads as the actual price move.

Returns are sorted into bins whose edges align to 0%, so every column holds either returns at or below zero or returns above it — never both. Columns take the negative or positive color to match, and the share of returns above zero lines up with the **Positive** figure in the dashboard. Column height can show a count of returns or a percent of sample, which keeps histograms from different symbols and timeframes comparable.

The histogram sits in its own pane with its right edge on the latest bar, so it's visible the moment the indicator loads. **Histogram Offset** pushes it further back or forward into the space ahead of price.

## The normal curve is the interesting part

A line traces the count each column *would* hold if returns followed a normal distribution with the same mean and standard deviation as the sample. This is the comparison that earns the indicator its keep. Columns rising above the line at the center and in the far tails, with shortfalls in between, reveal **fat tails** — the real-world tendency for extreme moves to happen more often than a bell curve implies. A longer run of columns on one side of center reveals **skew**.

Dashed tail markers sit at the lower and upper tail levels set by **Tail Level**, each labeled with its percentile and return. The columns beyond each marker hold the returns the tail alerts respond to.

## Reading the dashboard

The statistics table is where the tool gets genuinely useful for position sizing and stop placement. It reports observations, mean, median, standard deviation, annualized volatility, skewness, excess kurtosis, VaR at 95% and 99%, CVaR 95%, the 95th percentile, the positive share, and where the latest return ranks.

Two rows stand out. **VaR 95%** is the return that 5% of the sample fell below; **CVaR 95%** is the average of returns at or below that — how deep the worst 5% actually go. If you set stops by feel, these two numbers are a reality check. Skewness tells you whether large losses stretch further than large gains; excess kurtosis tells you how heavy the tails are versus normal.

Annualized volatility is handled thoughtfully: it derives bars-per-year from the chart itself, using 365.25 days for markets that trade every day and 252 for those with weekly closures, with a custom bars-per-year option for any specific convention.

## Configurable statistics — more than most traders need

Several measurements have competing conventions, and each can be switched to match whatever reference you're comparing against: **Statistics Basis** (Population vs Sample Adjusted), **Kurtosis Type** (Excess vs Raw), **Percentile Method** (Linear Interpolation vs Nearest Rank), **VaR Display** (Return vs Loss), **Positive Share** (All Returns vs Non-Zero), and **Latest Percentile Rank** (At or Below / Below / Midpoint). If you cross-check numbers against a spreadsheet or risk report, this is the feature that makes them agree.

**Bar Data** decides what counts as the latest return: **Confirmed** uses closed bars only, so figures hold steady while a bar forms; **Live** counts the forming bar, updating the highlight and dashboard with each price change.

## Pros and cons

**Pros**
- The normal-curve overlay makes fat tails and skew visible at a glance — something most retail tools ignore entirely.
- VaR and CVaR give concrete, sample-derived numbers you can use for position sizing and stop placement.
- Range trimming (**Full Range**, **Percentile**, **Std Dev**) keeps a few extreme returns from squashing the histogram, while statistics and alerts still use the full sample. End columns under trimmed ranges are dashed and labeled, with hover details on how many returns each holds.
- Three built-in tail alerts (Lower, Upper, Any) fire when a return lands beyond the tail level, judged against the sample as it stood before that bar.

**Cons**
- It's a statistics pane, not a signal generator. Nothing here tells you to buy or sell.
- The configurable-statistics section is deep enough that casual users will leave most of it untouched — and misconfigure it relative to their reference and numbers won't match.
- The histogram occupies its own pane, so it competes for screen space with your actual price chart.

## Who it's for

Discretionary and systematic traders who care about *how much* a market moves, not just which direction. If you size positions off volatility, set stops relative to actual tail behavior, or want a quick read on whether a move is ordinary or rare, this fits. Swing traders working multi-bar horizons on daily charts will get the most out of the Return Horizon setting. Pure trend-followers chasing crossovers will find little here.

## FAQ

**Does it predict price direction?** No. It describes the distribution of past returns and ranks the latest one. Direction is not its job.

**Will the histogram change as the current bar forms?** Only under **Live** bar data. Under **Confirmed**, everything holds until the bar closes.

**Can I compare across symbols and timeframes?** Yes — set column height to percent of sample rather than count.

**Does the trimmed range affect the statistics?** No. Range changes the display only; every statistic and alert uses the full sample.

## Verdict

This is a well-built statistical tool with a clear purpose: putting the shape of a market's risk on the chart. The normal-curve comparison, VaR/CVaR readouts, and tail alerts are the real substance, and the configurable conventions show the author understands where practitioners argue about definitions. It loses a star because it's a diagnostic, not a decision engine — and because the depth of settings will overwhelm anyone who just wants a quick read.

**Rating: ⭐⭐⭐⭐ (4/5)**

Install it if you treat risk as a number worth measuring. Skip it if you're looking for entries.
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

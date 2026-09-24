---
title: "Index_Peak_Dispersion Review: Settings, Strategy & How to Use It"
date: 2026-08-23
draft: false
type: reviews
image: "/screenshots/index-peak-dispersion.png"
tags:
  - "index peak dispersion"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Index_Peak_Dispersion review: honest take on trend strength, dispersion signals, best settings, and whether it beats MACD or RSI."
tv_script_url: "https://www.tradingview.com/script/LXTgseja-Index-Peak-Dispersion/"
sources: ["https://www.tradingview.com/script/LXTgseja-Index-Peak-Dispersion/"]
---
Let's cut through the noise. Index Peak Dispersion isn't another repackaged moving average crossover. It's a breadth tool that measures the *time domain* across a basket of equity indexes — specifically, how scattered their all-time-high dates are — and pairs that with a participation series showing how many are still printing record highs. The thesis, drawn from Dow Theory's non-confirmation principle, is that healthy advances register highs across indexes nearly simultaneously, while major distributive tops fragment, spreading peak dates across weeks or months.

It's a narrow, specific instrument. Here's what it actually does and where it breaks.

**What it does differently**

Most breadth and non-confirmation tools on this platform measure the price domain: divergences between an index and an internal line, counts of components above a moving average, or new-high/new-low tallies within one exchange universe. This script instead measures the time domain across whole indexes. It reduces the peak-date scatter of a user-defined index universe to a single bounded statistic — the in-window span of all-time-high ages — and pairs it with a participation series so that fragmentation is only flagged while a high is live.

Concretely, on each bar it runs one `request.security()` call per enabled symbol to track a running maximum of closing prices and record when that maximum was last exceeded. Each recorded timestamp becomes an age in calendar days. Indexes are then classified as Fresh (high within the fresh window), in-window (high within the topping window), or Stale (older than the topping window). When enough indexes are in-window, the dispersion span is the max in-window age minus the min in-window age, normalized as a percent of the topping window. The participation series is the count of Fresh indexes divided by the count of enabled indexes with data.

**Key features worth your attention**

- **Time-domain fragmentation measure** — The dispersion line answers: how spread out in time are the record highs? In a strong market the indexes peak together, so the columns are tall and the line stays low. At tops, one index peaks, then months later another, and the line climbs.
- **Participation series** — The columns answer a narrower question: how many enabled indexes hit a record high within the fresh window. Each new high carried by fewer indexes thins the columns out.
- **Fractured-top shading** — The pane background is shaded when dispersion is at or above the warning threshold *while* at least one index is Fresh. That's the specific combination where fragmentation is present at a live high rather than in an established downtrend.
- **Stale exclusion** — Stale entries are deliberately excluded from the span so a single long-dormant index doesn't saturate the statistic.
- **Status table** — On the last bar, an optional table lists each index with its all-time-high date, age in days, and classification, plus summary counts and the raw span.

**Settings and How to Tune Them**

- **Index universe** — Twelve slots, each with an enable checkbox and a symbol field. Defaults: DJI, DJT, DJU, DJA, SPX, NDX, IXIC, NYA, RUT, SOX, MID, SPXEW. All twelve are enabled by default. Any slot can be repointed to another symbol or disabled.
- **Fresh high window** (calendar days) — Default 7. An index whose all-time high printed within this many days counts as Fresh.
- **Topping window** (calendar days) — Default 378. An index whose all-time high printed within this many days participates in the dispersion span. Older highs are classified Stale.
- **Dispersion warning threshold** (percent of topping window) — Default 25. Sets the dashed reference line and the fractured-top condition. Note that because it's expressed as a percent of the topping window, changing the topping window changes the day-equivalent of the same percent threshold.
- **Minimum in-window index count for a valid span** — Default 4. Below this count the dispersion plot returns na, which prevents a span computed from too few indexes.
- **Show status table** — Default on.
- **Table position** — Default Top right.

**How to read it**

Read the two series together. Low dispersion with high participation describes a synchronized advance in which the enabled indexes are registering highs together. Rising dispersion while some indexes continue to print fresh highs describes fragmentation: leadership is narrowing and earlier leaders have stopped confirming. The shaded background marks bars on which dispersion is at or above the threshold while at least one fresh high exists.

The script is designed for the 1D timeframe. The running all-time high is intended to operate on daily closes, and both windows are specified in calendar days, so daily resolution matches the granularity of the logic. The condition is a warning context, not a timing trigger. It identifies an environment consistent with historical distributive tops — it does not predict the date or the existence of a decline. The same combination also appears during rotation phases that resolve higher, so treat it as a statement that conditions resemble past major tops, not as an instruction to act.

**The honest trade-offs**

**Pros:**
- Measures something most breadth tools ignore — the time domain of peak dates rather than the price domain
- The classification into Fresh, in-window, and Stale, with the Stale exclusion and the minimum-count gate, lets the scatter of a historical topping process be plotted as one continuous, comparable series across eras
- The status table provides attribution behind the numbers

**Cons:**
- The running all-time high is computed only over the bars loaded for each requested symbol. Symbols with short available history, and the early portion of any chart, understate the true age of the all-time high. The plot is only reliable after all enabled symbols have substantial loaded history.
- On intraday charts the running maximum operates on intraday closes and the calendar-day windows lose their intended granularity. On weekly or monthly charts a fresh window shorter than one bar cannot register.
- Ages and spans are measured in calendar days, not trading days, so weekends and holidays are included.
- The script issues twelve security calls; a slot that fails to resolve or returns no data is excluded from every count and appears in the table as "No data."
- The dispersion plot returns na whenever fewer than the minimum required indexes have an all-time high inside the topping window.

**Who should use this**

Traders studying broad equity index behavior at the daily timeframe, who want a mechanical, reproducible read on whether leadership is narrowing. It is not a standalone system and not a timing trigger.

**FAQ**

**Does Index Peak Dispersion repaint?**
All `request.security()` calls run on the chart timeframe with lookahead off. Values on the developing bar update until the bar closes and do not repaint afterward.

**What timeframe is it built for?**
The 1D timeframe. The running all-time high is intended to operate on daily closes, and both windows are specified in calendar days.

**Does it predict declines?**
No. It identifies an environment consistent with historical distributive tops. It does not predict the date or the existence of a decline, and the same condition can appear during rotation phases that resolve higher.

**Final verdict**

Index Peak Dispersion is a scalpel, not a Swiss Army knife. It measures one thing — the time-domain scatter of index peak dates, paired with live participation — and it measures it in a way that most breadth indicators don't attempt. Its real limitations are structural: it depends on the loaded history of every enabled symbol, it's designed for daily bars, and it issues a dozen security calls. Treat it as a warning context layered on top of your existing work, not as a system, and it earns its place.

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

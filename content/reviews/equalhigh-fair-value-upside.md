---
title: "Equalhigh_Fair_Value_Upside Review: Settings, Strategy & How to Use It"
date: 2026-09-12
draft: false
type: reviews
image: "/screenshots/equalhigh-fair-value-upside.png"
tags:
  - "equalhigh fair value upside"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Equalhigh_Fair_Value_Upside review: how this trend indicator maps fair-value upside targets, best settings, entry logic, and its real limitations."
tv_script_url: "https://www.tradingview.com/script/EKSezF8R-Equalhigh-Fair-Value-Upside/"
sources: ["https://www.tradingview.com/script/EKSezF8R-Equalhigh-Fair-Value-Upside/"]
---
Most "fair value" indicators on TradingView are repackaged moving averages with a fancy name. Equalhigh — Fair Value & Upside | SBC v1.1 is not that — but it is also not the magic target-finder the name implies. It is a fundamentals-based valuation tool, and it is explicit about what it does not do: it does not predict market turning points or calculate the probability of a price increase.

## What this indicator actually does

Stripped of marketing, this is a valuation model that combines financial data pulled through TradingView with user-defined assumptions. It displays three things: an orange base-case fair value line, a green buy-zone threshold set by your margin of safety, and an optional blue dashed nominal target at a selected horizon. Labels show price levels and potential upside or downside, and a dashboard reports the underlying financial inputs, valuation multiples, calculation status, and projected annualized price return.

The green level marks the maximum price within the model's buy zone. It is not an automatic entry signal.

Three valuation methods are available:

- **EPS:** diluted earnings per share × target P/E.
- **FCF after SBC:** FCF after deducting stock-based compensation, divided by diluted shares, multiplied by the target FCF multiple.
- **Hybrid:** a weighted combination of both.

In Hybrid mode, an EPS weight of 50% gives equal weight to the two components; 100% uses only EPS, and 0% uses only FCF.

## Key features that stand out

The explicit SBC deduction is the core differentiator. Many FCF-based valuations treat stock-based compensation as a non-cash add-back, which flatters the multiple. Here the calculation is stated plainly: FCF after SBC = FCF before SBC − SBC, then FCF after SBC per share = FCF after SBC ÷ diluted shares. That is a more conservative treatment than the default in a lot of retail valuation work.

Second, the buy-zone threshold is derived rather than eyeballed: buy-zone threshold = fair value × (1 − margin of safety). Upside/downside is computed as (fair value ÷ chart price − 1) × 100, so a negative percentage simply means the chart price exceeds the model's fair value.

Third, the dashboard exposes the inputs and the calculation status rather than hiding them. When a required component is missing or invalid, the script reports the reason instead of silently substituting a value.

## Settings and How to Tune Them

**Financial period:** choose FY (latest available fiscal-year data) or TTM (trailing-twelve-month EPS and FCF). Note that selecting TTM does not automatically reconstruct missing financial data from individual reports.

**Valuation model and EPS weight:** select EPS, FCF after SBC, or Hybrid. In Hybrid, the EPS weight determines the split between the two components.

**Target multiples:** enter a target P/E and a target FCF multiple. Both default to zero, and the relevant valuation component remains suspended until a positive multiple is entered. The choice of multiple is an assumption, not a retrieved fact.

**SBC:** entered manually in this version, in millions of the chart currency, for the same reporting period as the FCF. The confirmation checkbox is required even when SBC is zero — missing SBC is never silently treated as zero.

**Share-data frequency (TTM mode):** Auto uses a positive FQ value first, otherwise FH, otherwise FY. Auto follows an availability order; it does not compare publication dates to identify the newest report. In FY mode, automatic share retrieval uses FY data regardless of the TTM frequency setting. A manual share-count override takes priority over automatic retrieval.

**Manual overrides:** diluted EPS (per-share amount in chart currency), FCF before SBC (total, in millions), and diluted shares (in millions). Record the source and period end in the source field. Manual values remain fixed until changed and should be reviewed whenever you switch stocks. Check whether your FCF source deducts lease repayments — the script does not harmonize different FCF definitions.

**Projection:** enabling projection assumptions requires a horizon in years, annual diluted EPS growth, and annual FCF after SBC per share growth. Growth rates are entered as percentages. Each active component grows at its own rate; target multiples and Hybrid weights stay constant. The projection is a reference level for a future nominal target, not a forecast price path or a discounted present value, and the growth inputs are your assumptions rather than retrieved guidance or consensus.

**Display:** the dashboard can be positioned in any chart corner, and "Label offset (bars)" moves labels horizontally relative to the latest bar. Labels are not pinned to the price axis.

## How it fits into a workflow

The script is built to make valuation assumptions visible and comparable. A defensible process is: select the period, choose the model, enter target multiples, verify the retrieved financials, apply overrides where the data is wrong or unavailable, and then read the output as one input among several.

The tool's own guidance is to combine its output with company research, financial-statement review, and your own risk-management process. It does not normalize exceptional items, does not independently audit filings, and does not add net cash or subtract net debt. It may be unsuitable for banks, loss-making businesses, or companies requiring specialized valuation methods.

## Pros and cons

**Pros:**
- Explicitly deducts stock-based compensation in the FCF component
- Three model options with a stated Hybrid weighting formula
- Buy-zone threshold tied to a user-defined margin of safety
- Dashboard reports inputs, multiples, and the specific reason a calculation is suspended
- Manual overrides for EPS, FCF, and share count, with a source field

**Cons:**
- SBC must be entered manually; there is no automatic retrieval in this version
- Financial data availability depends on the stock and reporting frequency
- No automatic net cash or net debt adjustment
- Does not normalize exceptional items
- Financial-data revisions and manual overrides make this version unsuitable as a historical point-in-time valuation backtest

## Who it's for

Traders and investors who work from fundamentals and want a repeatable, transparent way to test valuation assumptions on a chart. It assumes you can supply a defensible target multiple, a verified SBC figure, and a share count. Anyone looking for entry signals or price predictions is looking at the wrong tool — the green level is a buy-zone boundary, not a trigger.

## Alternatives worth considering

If you want a purely technical target projection, measured-move drawing tools do the same job manually. If you want a valuation model with automatic SBC retrieval and net-debt adjustments, you will need a fuller fundamental data stack than this script provides.

## FAQ

**Does it repaint?** The source material does not address repainting. It does state that valuation lines begin at the latest bar and extend to the right, and that the indicator deliberately avoids applying today's manual inputs retrospectively across the chart.

**Does it work on any stock?** Availability of diluted EPS, free cash flow, and diluted shares depends on the stock and reporting frequency. The model may be unsuitable for banks, loss-making businesses, or companies requiring specialized valuation methods.

**Why does the dashboard say "suspended"?** The dashboard explains what prevents calculation. Possible causes include missing or non-positive EPS, missing FCF, missing or non-positive share count, unverified SBC, non-positive FCF after SBC, or an unconfigured target multiple. Only components required by the selected model and weight must be valid — in Hybrid mode, the script does not silently redistribute weight when a required component is unavailable.

## Final verdict

Equalhigh — Fair Value & Upside | SBC v1.1 does one thing and documents it carefully: it turns a small set of financial inputs and your own assumptions into a fair value line, a margin-of-safety buy zone, and an optional projection. The SBC deduction and the transparency of the dashboard are the parts that matter. The limitations are equally clear — manual SBC entry, no balance-sheet adjustments, no backtest validity — and the script states them itself. Treat it as a structured way to make valuation assumptions explicit, not as a signal generator.

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

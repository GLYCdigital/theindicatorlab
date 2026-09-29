---
title: "Fo Market Trend Sector Stock Ranking Review — Trend"
date: 2026-09-29
draft: false
type: reviews
image: "/screenshots/f-o-market-trend-sector-stock-ranking.png"
tags:
  - "f o market trend sector stock ranking"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "F O Market Trend Sector Stock Ranking review: a one-screen NSE F&O dashboard ranking 210 stocks across 18 sectors with trend scores and OI buildup."
tv_script_url: "https://www.tradingview.com/script/QgtuLBE1-F-O-Market-Trend-Sector-Stock-Ranking/"
sources: ["https://www.tradingview.com/script/QgtuLBE1-F-O-Market-Trend-Sector-Stock-Ranking/"]
---
Most "market dashboards" on TradingView are either a single table glued to your chart or a pile of unrelated oscillators. This one takes a different angle: it tries to answer the three questions an Indian F&O trader actually asks each morning — what's the market doing, which sector is leading, and which stocks inside that sector are strongest — on a single screen.

Here's what it does, who it suits, and where it gets awkward.

## What It Actually Is

F O Market Trend Sector Stock Ranking is a study built specifically for the NSE F&O universe. It covers all 210 NSE F&O stocks (per the September 2026 list), grouped into 18 sectors, plus 18 NSE sector indices and the Nifty 50.

It renders as three panels:

1. A **Market Trend panel** giving an overall verdict — Strong Bullish, Bullish, Sideways, Bearish or Strong Bearish — with a score and a one-line view.
2. A **Sector Ranking table** that sorts 18 sector indices from strongest to weakest by % change, each with a trend label.
3. A **Stock table** where you pick a sector (or "All F&O") and see the stocks ranked, with price change, OI change, buildup type, relative volume and a trend label.

That's the whole product. No signals, no arrows, no alerts promising entries. It's a context tool.

## How the Trend Score Is Built

This is the part worth understanding, because the dashboard is only as good as its engine.

Each symbol gets five votes, +1 bullish or -1 bearish:

- Close above/below the 20 EMA
- 20 EMA above/below the 50 EMA
- RSI(14) above 55 or below 45 (in between = zero)
- Supertrend (10, 3) direction
- +DI above/below -DI

Futures OI buildup then adds a fractional vote on top: Long Buildup gets +1, Short Covering +0.5, Short Buildup -1, Long Unwinding -0.5.

The score maps to a label: +4 or more is Strong Bullish, +2 to +3 Bullish, -2 to -3 Bearish, -4 or less Strong Bearish, everything else Sideways. There's also an ADX filter — if ADX is below 20, the trend is treated as weak and labelled Sideways regardless.

All lengths, thresholds and the buildup weight are adjustable in settings, which matters if the defaults don't match your style.

## The Practical Workflow

The intended flow is top-down: read the Market Trend panel, identify the leading sector in the ranking table, then switch the stock table to that sector and look for the strongest names with confirming buildup.

Use the Daily timeframe. On Daily, the price % column becomes today versus yesterday, and it updates live during market hours.

There's one workflow quirk worth flagging before you buy in: if you keep both the OI/Buildup columns and the Sector table switched on, the stock table caps at 10 rows and ranks only within each page. Turn the Sector table off and a whole sector ranks together. That's a real design trade-off, not a bug — but it means the "full picture" view isn't the default one.

Paging is manual: lower "Rows per page" to around 10 and change "Page" in settings. Auto-flip only works while live ticks are arriving, so on weekends you'd need to attach it to a 24/7 chart such as BTCUSDT to keep it usable.

## Pros and Cons

**Pros**

- Genuinely one-screen. Market, sector and stock context without flipping between tabs.
- The scoring logic is transparent and documented — five votes plus an OI adjustment. You can see exactly why a label was assigned, which is rare for dashboard-style scripts.
- Buildup classification (Long Buildup, Short Covering, Short Buildup, Long Unwinding) is the vocabulary F&O traders already use, and pairing it with price change and relative volume gives a fast read.
- Deep customisation: trend engine inputs, colour rules per label, and per-table position, sizing, borders and cell dimensions.

**Cons**

- TradingView's roughly 40 data-request limit per script means all 210 stocks cannot be ranked in one table. Sector-by-sector scanning is a hard constraint, not a preference.
- The F&O stock list and sector groupings are hard-coded. When NSE revises the F&O list, the indicator needs updating.
- OI depends on TradingView's "_OI" futures data. Where it's missing, you get "n/a" — a gap you can't fix from settings.
- Live values need real-time NSE data on your plan. Delayed data makes a live dashboard considerably less useful.
- It's NSE-only by construction. Nothing here transfers to other markets.

## Who It's For

Indian F&O traders who already run a top-down process and want the sector-rotation layer automated. It suits swing and positional traders working off the Daily timeframe, and anyone who currently builds a sector leaderboard by hand each morning.

It is not for intraday scalpers, options-only traders looking for strike selection, or anyone trading non-Indian markets.

## FAQ

**Does it give buy or sell signals?**
No. It classifies trend and buildup. The disclaimer is explicit that it is not investment advice or a recommendation.

**Why can't I see all 210 stocks at once?**
TradingView caps data requests per script at roughly 40, so each sector (max 19 stocks) is scanned at a time, and "All F&O" is scanned page by page.

**Can I change the trend thresholds?**
Yes — EMA, RSI, ADX, Supertrend settings and the buildup weight are all editable.

**Why does a stock show "n/a" for OI?**
TradingView's "_OI" futures data is missing for that symbol.

## Verdict

This is a well-scoped tool that does one job properly. The scoring engine is transparent, the OI buildup layer is genuinely useful for F&O work, and the customisation is deeper than most dashboards bother with. The hard-coded stock list, the data-request ceiling and the manual paging are real friction points — but they're honest limits, disclosed up front rather than hidden.

If you trade NSE F&O and want sector rotation on one screen, this earns its place. If you trade anything else, it isn't for you.

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

---
title: "Liquidity_Label_Above_Bar Review: Settings, Strategy & How to Use It"
date: 2026-09-10
draft: false
type: reviews
image: "/screenshots/liquidity-label-above-bar.png"
tags:
  - "liquidity label above bar"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Liquidity_Label_Above_Bar review: how it marks liquidity zones, optimal MACD settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/3C7bqZb3-Liquidity-Label-above-Bar/"
sources: ["https://www.tradingview.com/script/3C7bqZb3-Liquidity-Label-above-Bar/"]
---
# Get started — Liquidity Label Review

The name undersells it. "Liquidity Label" sounds like decoration — a floating text element pinned above your chart. But the official description is more specific than the title suggests: it shows a single label above the latest candle displaying the stock's average traded value, so you can judge at a glance whether a stock is liquid enough to trade without opening a screener.

That's the entire premise. This is not a signal indicator, a pattern detector, or a directional bias tool. It is a liquidity readout — a single number that answers one question: is there enough traded value here to bother?

## What It Actually Does

One label is drawn, always on the last bar, and it updates live. The value shown is the average traded value over a configurable number of periods, based on a chosen price source. By default that's the close over 50 periods.

The display unit is where the tool earns its keep. Crore and Lakh units make this handy for NSE/BSE traders, while Million and Billion covers global markets. There's also a Raw option if you want the unformatted figure. Decimals and an optional unit suffix (Cr, L, M, B) let you control how the number reads.

That's it. No boxes, no zones, no multi-timeframe overlay. Just a number, placed where you can see it.

## What Sets It Apart

Most liquidity tools on TradingView try to map where liquidity *sits* — pools, zones, sweep levels. This one does something narrower and arguably more useful for a first-pass filter: it quantifies how much value is actually changing hands.

The practical distinction matters. A chart can look clean and tradeable while the underlying instrument is too thin to fill an order without slippage. Conversely, a busy-looking chart on a small-cap may have less real liquidity than a quiet one on a large-cap. The label gives you a direct read on that without leaving the chart to run a screener.

The unit flexibility is the other differentiator. Regional conventions differ, and having Crore/Lakh alongside Million/Billion means the same indicator reads naturally for an Indian equity trader and a US equity trader without mental conversion.

## Settings and How to Tune Them

The official parameter set breaks into four groups.

**Calculation:**
- **Time unit:** Days or Minutes
- **Period count:** the number of periods used for averaging (default 50)
- **Price source:** close by default
- **Display unit:** Crore, Lakh, Million, Billion, or Raw
- **Decimals and optional unit suffix** (Cr, L, M, B)

**Label look:**
- Text size, text color, background color
- Shape: down arrow, box, or plain text

**Margins:**
- **Vertical margin:** how far above the high the label sits, as a percent of price
- **Horizontal margin:** shift the label left or right by bars

Tuning notes, kept general since the source doesn't prescribe values: the period count governs how smooth the average is — a shorter window reacts faster to recent volume shifts, a longer one gives a more stable baseline. The time unit determines whether you're averaging daily or intraday periods, which changes what "average liquidity" means for your use case. The display unit should match your market convention; pick the one you'd use in conversation. Label look and margins are pure ergonomics — set the size and offset so the label doesn't obscure price action on your specific chart.

## How to Use It

The indicator works on any symbol and any chart timeframe, and the source notes it can be used for intraday as well.

The natural workflow is as a pre-trade filter. Before committing to a setup, glance at the label. If the average traded value is below whatever threshold you consider tradeable for your size, the setup doesn't matter. This replaces the step of opening a screener or checking a separate data source.

Because the label updates live on the last bar, it reflects current conditions rather than a static historical figure — useful if you're watching an instrument's activity change during a session.

## The Honest Trade-Offs

**Pros:**
- Single, uncluttered readout — no chart pollution
- Unit options cover both Indian and global market conventions
- Works on any symbol and any chart timeframe
- Label updates live, so the figure stays current
- Removes the need to leave the chart for a screener

**Cons:**
- It's a filter, not a signal. It tells you nothing about direction, entry, or exit.
- One label on the last bar only — no historical context, no trend in liquidity over time
- No alerting, no scanning, no multi-symbol view
- The value is an average over a lookback; a sudden liquidity shift won't show immediately

## Who Should Install This

Traders who routinely check liquidity before entering — particularly those trading instruments where thin books are a real risk — will get direct value from this. NSE/BSE traders get the Crore/Lakh formatting; global traders get Million/Billion. Intraday users can run it on minute time units.

If you already have a screener workflow you trust, or you trade only highly liquid instruments where the answer is always "yes, liquid enough," this adds little. It's also not for anyone looking for trade signals — there are none here.

## Final Verdict

Get started (Liquidity Label) is a narrow tool that does its narrow job cleanly. It answers one question — is this instrument liquid enough to trade — and answers it on the chart, in your preferred unit, without ceremony. The lack of clutter is the feature.

It won't make trading decisions for you, and it doesn't pretend to. For traders who understand that liquidity is a precondition rather than a signal, it's a reasonable addition to the toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)** — Deducting a star for the absence of historical context and any alerting or scanning capability. But for what it does, it does well.

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

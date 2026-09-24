---
title: "Prop_Firm_Artillery Review: Settings, Strategy & How to Use It"
date: 2026-08-17
draft: false
type: reviews
image: "/screenshots/prop-firm-artillery.png"
tags:
  - "prop firm artillery"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Prop_Firm_Artillery review: tested settings, entry logic, and honest verdict. Does this trend indicator justify its name for prop firm traders?"
tv_script_url: "https://www.tradingview.com/script/PkUPYbw7-Ultimate-Prop-Firm-Artillery/"
sources: ["https://www.tradingview.com/script/PkUPYbw7-Ultimate-Prop-Firm-Artillery/"]
---
Ultimate Prop Firm is a pivot-reversal supply/demand strategy built around the risk limits that funded-account traders have to respect. It consolidates the earlier "Ultimate Prop Firm" strategy and its separate "UPF Visual" companion indicator into a single open-source script, so the trading logic and the visual layer now live in one publication. It is not magic, but it does address a real problem most zone-trading scripts ignore: enforcing the daily drawdown, trade-count and session rules that funded accounts require.

## What This Strategy Actually Does

The core logic is reversal trading at recent pivot-based supply and demand zones. Confirmed pivot highs and lows, using left/right bar counts as inputs, define supply and demand levels, which are extended into zones using an ATR multiple.

The long setup requires a confirmed pivot low, price trading down into the demand zone, a bullish bar, RSI above a floor, and volume at or above its moving average. The short setup is the mirror image at a supply zone: confirmed pivot high, price into the zone, bearish bar, RSI below a ceiling, and volume confirmation.

Exits use a three-stage ATR-based take-profit ladder, with partial exits at TP1 and TP2 and the remainder at TP3, plus a common ATR stop and a hard flatten at session end.

Each filter answers a different failure mode of naked zone-trading. The pivot definition keeps zones objective, the RSI floor and ceiling reject entries against collapsing momentum, the volume check rejects dead-tape touches, and the session, drawdown and trade-count rails force the discipline that funded accounts demand. The zones decide where, the filters decide whether, and the rails decide whether you are still allowed to.

## Key Features That Matter

**The Safety Rails** — This is the standout element for prop-firm-style trading. No new entries are taken once the daily drawdown cap is hit, the max-trades-per-day count is reached, or price is outside the session window. The strategy also forces a flat at session end, so positions are not carried past the close.

**Pivot-Based Zones** — Zones come from confirmed pivot highs and lows, with left and right bar counts as inputs, extended into zones using an ATR multiple. Because pivot confirmation requires the right-side bars to close, a zone appears only after its pivot is confirmed, and zones do not repaint once drawn.

**ATR-Based Exits** — A three-stage take-profit ladder takes partial exits at TP1 and TP2, with the remainder at TP3, alongside a common ATR stop. Risk per trade is bounded by the ATR stop.

## Settings and How to Tune Them

The script exposes pivot left/right bar counts, an ATR multiple for zone extension, RSI floor and ceiling thresholds, a volume moving average, the ATR stop and take-profit ladder, the daily drawdown cap, the max-trades-per-day count, and the session window. The documented backtest uses a fixed size of one micro futures contract, with defaults tuned for MNQ on the 5-minute chart during the New York session.

Every threshold is an input, and the source is explicit that other symbols or timeframes need their own settings. The visual layers can be switched off in the Visuals input group.

## What You See On the Chart

- Green and red shaded boxes for the active demand and supply zones
- Triangles and the strategy's own trade markers at entries and exits
- On each signal: the entry line and price label, dashed TP1/TP2 lines, a gold TP3 line, a solid red stop line, and shaded target and stop zones
- Background tint for session closed, trending up, trending down, or choppy, based on EMA structure and ADX context
- A dashboard showing market state, current position, session status, trades left today, volume state, and the active SL/TP3 levels

## Behaviour Notes

Signals are evaluated on bar close, with no intrabar order generation, no higher-timeframe requests, and no lookahead. Pivot confirmation requires the right-side bars to close, so a zone appears only after its pivot is confirmed, and zones do not repaint once drawn. Three alert conditions are available: long entry, short entry, and end-of-session flatten.

## Backtest Properties

The documented report uses realistic properties for one micro futures contract: 10,000 initial capital, fixed size of one contract, commission of 0.62 per contract per side, 1 tick of slippage, and orders processed on bar close. Risk per trade is bounded by the ATR stop, roughly 1.5 ATR by default, which is a small fraction of capital on a micro contract. Backtest results are historical, vary with the tested window, and do not predict future performance.

## Pros & Cons

**Pros:**
- The safety rails enforce daily drawdown, trade-count and session limits rather than leaving them to discretion
- Zones are objective, derived from confirmed pivots rather than drawn by hand
- The filters are interdependent — zones, momentum, volume and session rules each address a distinct failure mode
- No repainting once a zone is drawn
- Original code written with Pine built-ins only, no reused open-source components

**Cons:**
- Defaults are documented for MNQ on the 5-minute New York session; other symbols and timeframes need their own settings
- It is not a standalone edge — it is a rules-based reversal process, and results depend on the tested window

## Who This Is For

This is built for funded-account and prop-firm-style traders who have to respect a daily drawdown cap, a maximum number of trades per day, a fixed session window and a forced flat at the close. It is an educational and analytical tool for studying a rules-based reversal process. It is not financial advice.

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

---
title: "Cisd_Mtf_5M_15M Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/cisd-mtf-5m-15m.png"
tags:
  - "cisd mtf 5m 15m"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Cisd_Mtf_5M_15M review: a change-in-state-of-delivery trend tool that reads 5M structure with 15M confirmation. Tested settings, entries, and honest limits."
tv_script_url: "https://www.tradingview.com/script/l2fTYwtc-CISD-MTF-5m-15m/"
sources: ["https://www.tradingview.com/script/l2fTYwtc-CISD-MTF-5m-15m/"]
---
CISD MTF is not a mashup of five indicators pretending to be one. It is a narrow, opinionated tool built around a single idea: **Change in State of Delivery (CISD)**, applied across two timeframes — 5-minute and 15-minute — and designed to show the reference levels price must close through before the current delivery state can be considered changed.

That framing matters. The indicator is not trying to tell you when to buy or sell. It is answering one question: what level does price need to close through before the current delivery state can be considered changed? Everything else — entries, stops, targets — is left to you.

## What CISD actually means here

CISD is a Smart Money / order-flow concept: the moment price stops delivering in one direction and starts delivering in the other, marked by a decisive close through a prior reference level rather than a wick. It is the quieter cousin of a market structure break.

This indicator operationalizes that across two timeframes. It displays the active 5-minute and 15-minute CISD reference levels directly on a lower-timeframe chart. A **Bull CISD** is the level price must close above to confirm a bullish change in delivery. A **Bear CISD** is the level price must close below to confirm a bearish change in delivery.

The important distinction: unlike a simple candle-color or crossover signal, the indicator maintains the current delivery state until the relevant CISD level is actually confirmed. An opposite-colored candle, a wick through the level, or a temporary swing by itself does not automatically change the displayed direction. A Bull CISD remains active during bearish delivery until price confirms above it, and a Bear CISD remains active during bullish delivery until price confirms below it. When the delivery state does change, the previous CISD reference is automatically replaced.

## Key features that matter

- **Dual-timeframe levels.** Displays 5m and 15m CISD levels on lower-timeframe charts, tracking only the currently relevant CISD direction for each timeframe.
- **Confirmed closes only.** Uses confirmed higher-timeframe candle closes, not intrabar price.
- **Wicks don't count.** A wick through a CISD level does not confirm a state change.
- **Persistent state.** Bull CISD stays active during bearish delivery until price confirms above it; Bear CISD stays active during bullish delivery until price confirms below it.
- **Automatic replacement.** The previous CISD reference is swapped out when the delivery state changes.
- **Right-edge labels.** Active levels are labeled at the right edge for quick identification.
- **Alerts.** Alerts fire when active CISD references change.

## Settings and How to Tune Them

The source material describes the indicator as a 5-minute and 15-minute CISD tool, so those are the timeframes the logic is built around. Beyond that, the documentation does not publish a parameter table.

Conceptually, the settings you would expect to matter are the timeframe pairings for the CISD reference levels and whatever controls how the confirmed close is evaluated. Treat the 5m/15m pairing as the design intent rather than a starting point to optimize — the indicator is described specifically as a 5m/15m tool, not a general-purpose multi-timeframe engine. If the script exposes toggles for level display or labels, those are cosmetic and do not change the underlying state logic.

## How to use it

The author's stated approach is to use CISD as confirmation and context rather than a standalone entry signal. During bearish delivery, the Bull CISD shows the level price would need to reclaim on a confirmed close before there is evidence of a bullish character change. During bullish delivery, the Bear CISD marks the level price would need to close below before bearish delivery is confirmed.

The author combines CISD with market structure, EMA structure, liquidity, displacement, and pullback locations rather than entering immediately when a CISD occurs. The indicator tells you *when* delivery changed, not *where* to trade — pair it with your own level work.

## Pros and cons

**Pros**
- Focused, single-concept tool rather than an indicator mashup
- Persistent state logic avoids flipping on every opposite-colored candle
- Uses confirmed closes, not intrabar price
- Wicks through the level do not trigger a state change
- Right-edge labels make active levels easy to identify
- Alerts on reference changes

**Cons**
- Documentation is thin beyond the concept description
- No built-in stop/target levels or risk calculator
- Requires confirmed closes, so you cannot act intrabar
- Only tracks the currently relevant CISD direction per timeframe, not a full history of levels

## Who it's for

Discretionary intraday traders who already work with market structure and order flow and want a mechanical reference for delivery-state changes without giving up their own level analysis. It is a market-structure visualization and research tool, not a signal generator, and it does not provide financial advice or guarantee that a trend reversal or continuation will occur.

## FAQ

**What does the indicator actually plot?** The active 5m and 15m CISD reference levels, displayed on a lower-timeframe chart with right-edge labels.

**Does a wick through the level count?** No. A wick through a CISD level does not confirm a state change — only a confirmed close does.

**Does an opposite-colored candle flip the state?** No. The current delivery state is maintained until the relevant CISD level is actually confirmed.

**Does it give buy/sell signals?** It shows CISD reference levels and state changes. The author uses it as confirmation and context, not as a standalone entry signal.

**Does it include alerts?** Yes — alerts fire when active CISD references change.

## Verdict

CISD MTF does one job: it shows the 5m and 15m levels price must close through before delivery state changes, and it holds that state until the close actually confirms. The persistent-state logic and confirmed-close requirement are the parts that separate it from a candle-color flip. The lack of built-in risk tools and the sparse published documentation keep it from being a complete package, but for traders already working from market structure it is a legitimate context tool rather than a repackaged moving average.

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

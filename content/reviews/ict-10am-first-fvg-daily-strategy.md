---
title: "Ict_10Am_First_Fvg_Daily_Strategy Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/ict-10am-first-fvg-daily-strategy.png"
tags:
  - "ict 10am first fvg daily strategy"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest ICT 10AM First FVG Daily Strategy review: how the fair value gap logic works, tested settings, entry rules, and whether it beats manual FVG marking."
tv_script_url: "https://www.tradingview.com/script/Za5HKgrL-ICT-10AM-First-FVG-Daily-Strategy/"
sources: ["https://www.tradingview.com/script/Za5HKgrL-ICT-10AM-First-FVG-Daily-Strategy/"]
---
Most "ICT" indicators on TradingView are repackaged moving averages with a fancy name and a liquidity sweep label slapped on top. This one isn't that. The **ICT 10AM First FVG Daily Strategy** does one specific thing: it isolates the first fair value gap that forms *after* the 10:00 AM candle and uses that as the day's directional bias. That's a real ICT concept, mechanically defined, and the script executes it without much hand-waving.

## What the Strategy Actually Does

The logic is narrow by design. Per the official description, the strategy identifies one setup per New York trading day. It records the 10:00 AM opening price, waits for the first valid three-candle Fair Value Gap, and places a limit order at the FVG's first-touch boundary. Both bullish and bearish setups are supported.

The timing rule is the core constraint: the middle, or displacement, candle of the FVG must begin at or after 10:00 AM New York time. The 09:59–10:00–10:01 structure is valid; the 09:58–09:59–10:00 structure is rejected. Only the first confirmed FVG of the day is used, and later FVGs are ignored even when the first setup remains unfilled.

Once the gap is identified, a limit order goes in at the FVG's first-touch boundary, with a stop and take-profit prepared as a linked bracket.

## Key Features Worth Noting

- **Time-locked bias.** The 10:00 AM filter is the entire point. Structures beginning before that candle are rejected, which is what separates this from generic FVG scripts.
- **One signal per day.** The strategy allows only one setup per New York trading day. Later FVGs are ignored even if the first setup never fills.
- **Non-repainting design.** FVGs are accepted only after the third candle has closed and the structure is confirmed. The script does not use future bar references, request.security(), or look-ahead settings.
- **Visual levels that terminate.** All visual levels stop at the actual TP or SL candle. No line or FVG box is extended indefinitely after the trade is completed.

## Settings and How to Tune Them

The configuration options are structural rather than cosmetic:

- **New York setup starting hour.** This anchors the 10:00 AM logic. Setting it to match the intended session is what makes the rest of the strategy coherent.
- **Session cancellation and closing hour.** Pending orders are cancelled at the configured session ending time, and open positions can optionally be closed at session end.
- **Fixed contract quantity.** Position sizing is set directly rather than derived.
- **Long and short permissions.** Each direction can be enabled or disabled independently.
- **Friday and weekend protection.** These can prevent new setups near the market transition. The default Friday protection time is 15:45 New York time.
- **FVG and trade-level visibility.** Controls whether the 10:00 AM opening level, the first valid FVG zone, and the entry, stop-loss and take-profit levels are drawn.

## How the Setup Works

The mechanics are defined per direction rather than left to discretion:

**Long:** The first confirmed bullish FVG is selected. A buy limit order is placed at the FVG's first-touch boundary. The stop-loss sits below the displacement candle's low. The take-profit is set at the highest directional extreme formed after 10:00 AM and before entry.

**Short:** The first confirmed bearish FVG is selected. A sell limit order is placed at the FVG's first-touch boundary. The stop-loss sits above the displacement candle's high. The take-profit is set at the lowest directional extreme formed after 10:00 AM and before entry.

While the limit order is waiting, each newly completed pre-entry candle may update the directional target. The candle in which the entry is filled is excluded from target calculation, which prevents the strategy from using price movement that occurs after or during the first-touch entry.

## Order Management

The complete protective bracket is prepared together with the pending entry: entry as a limit order, take-profit as a limit order, stop-loss as a stop order. The TP and SL are linked to the entry and become active as soon as the limit order fills. Pyramiding is disabled.

## Pros and Cons

**Pros:**
- Genuinely mechanical ICT concept, not a buzzword wrapper
- One setup per session, with FVGs confirmed only after the third candle closes
- The 10:00 AM filter is a real constraint, not a cosmetic label
- Target logic explicitly excludes the entry candle

**Cons:**
- One setup per day is restrictive if you want more activity
- No performance statistics or win-rate display in the script
- The 10:00 AM anchor is tied to New York session time, so behavior on 24/7 markets differs from the intended use case

## Who This Is For

This suits discretionary day traders who already understand ICT concepts and want a rule-based guardrail for the first FVG of the New York session. It's also useful for traders who enter too early — the time lock enforces patience. If you're a scalper looking for many setups a day, or a swing trader on the daily, this isn't built for you.

## Alternatives

If you want broader FVG coverage without the time lock, other smart-money-concepts scripts are more flexible. If you want pure ICT with more signal types, scripts covering order blocks and liquidity sweeps alongside FVGs offer more breadth. This strategy's edge is its narrowness — the alternatives are better if you want breadth, worse if you want discipline.

## FAQ

**Does it repaint?**
Per the official description, FVGs are accepted only after the third candle has closed and the structure is confirmed, and the script uses no future bar references, request.security(), or look-ahead settings. Normal historical testing and Bar Magnifier testing produced identical trades across the validated MNQ 1-minute test window. Same-candle entry and exit behavior may still depend on TradingView's historical broker-emulator assumptions.

**What timeframe should I use?**
The source material does not prescribe a timeframe. The validated test window referenced is MNQ 1-minute.

**Can I use it on crypto?**
The source material does not address crypto. The strategy is defined around the New York session, so the 10:00 AM anchor assumes a session-based market.

**Does it give buy/sell signals?**
It places a limit order at the FVG's first-touch boundary with a linked TP and SL, and it can display the 10:00 AM opening level, the first valid FVG zone, and the entry, stop-loss and take-profit levels on the chart.

## Final Verdict

The ICT 10AM First FVG Daily Strategy does one thing and does it well. It's not a complete trading system — you still need context, risk management, and a target framework. But as a mechanical filter for the first fair value gap of the New York session, the logic is coherent and the 10:00 AM lock is a genuinely useful constraint.

The official notice is worth repeating: this strategy is intended for research, backtesting and educational use, historical performance does not guarantee future results, and commission, spread, slippage, contract specifications and real execution conditions should be configured and independently evaluated before live use.

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

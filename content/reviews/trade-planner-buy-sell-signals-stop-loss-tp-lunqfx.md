---
title: "Trade Planner Buy Sell Signals Stop Loss Tp Lunqfx Review"
date: 2026-10-13
draft: false
type: reviews
image: "/screenshots/trade-planner-buy-sell-signals-stop-loss-tp-lunqfx.png"
tags:
  - "trade planner buy sell signals stop loss tp lunqfx"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Trade Planner review: a trend-pullback signal tool that prints entry, stop, three R-multiple targets and position size on one bar. Honest 4-star look."
tv_script_url: "https://www.tradingview.com/script/pdfPtD0d-Trade-Planner-Buy-Sell-Signals-Stop-Loss-TP-LunqFX/"
sources: ["https://www.tradingview.com/script/pdfPtD0d-Trade-Planner-Buy-Sell-Signals-Stop-Loss-TP-LunqFX/"]
---
Most signal indicators stop at the arrow. This one keeps going — entry, stop, three targets and a position size, all printed on the bar the setup confirms. That's the whole pitch, and it's worth examining on its own terms.

## What It Actually Does

Trade Planner is a trend-pullback system. It defines trend with two exponential moving averages, draws a "value zone" band around the fast EMA scaled by ATR, and waits for price to pull back into that band. When price closes back beyond the fast EMA in the trend's direction — with RSI on the right side of 50 and moving that way — a plan prints.

That plan isn't just an arrow. It's a complete trade ticket: entry at the trigger bar's close, a stop anchored on the pullback's own extreme plus an ATR buffer, and three targets set in R multiples of that stop. Plus a lot size calculated from your account.

The claim worth testing is the sizing. Risk money is balance times risk percentage, divided by what one unit loses over the stop distance, converted into your account currency. That's real position sizing math, not a static label.

## The Setup Logic

The trend rule is stated plainly: up while the fast EMA sits above the slow EMA, price holds above the slow, and the slow isn't falling. Down is the mirror. When neither condition holds, the panel says there's no trend and nothing prints.

The value zone is a band around the fast EMA whose width is a fraction of ATR — drawn and tinted by trend direction. A pullback "counts" once price trades into it while the trend is intact.

The trigger requires three things on the closing bar: a close back beyond the fast EMA in the trend's direction, a close in that direction, and RSI on the trend's side of 50 and rising (falling for shorts). The RSI does one job here — confirming momentum turned back — and the description says so rather than overselling it.

## The Stop and Targets

This is where the design gets thoughtful. The stop isn't a fixed pip count. It's placed beyond the lowest low (highest high for shorts) of the last few bars — the pullback's own extreme, not some older swing — plus an ATR buffer.

Two guards wrap it. If the stop would be tighter than a minimum ATR distance, it widens to the minimum, so one noisy candle doesn't kill the trade. If it would be wider than a maximum ATR distance, the setup is skipped entirely. No plan prints. The reasoning is stated: a stop five ATR away isn't a pullback trade anymore.

Targets sit at 1R, 2R and 3R by default, each adjustable, drawn as dotted lines with price tags and shaded risk/reward zones.

## Position Sizing

The size comes out in lots for forex, gold and silver, contracts for futures, and units for everything else. If your broker uses a different lot size, you enter it directly. The entry label shows the size, the stop tag shows what the stop costs, and the TP1 tag shows what the first target is worth at that size.

Worth repeating what the source says plainly: this is an estimate from TradingView's data. Broker contract sizes, conversions, commissions, spreads and minimum lot steps aren't known to the script.

## Tracking and Honesty

A plan stays open until the stop or TP3 is reached, or optionally until an opposite plan appears. Targets get ticked on their tags as they're hit. The panel shows the open plan, current R position, and how the last plan ended.

One detail tells you a lot about the author's intent: if a single bar touches both the stop and a target, it counts as the stop. The order of fills inside a bar is unknown, and the conservative reading is the loss. That's the opposite of how most signal tools handle ambiguity.

The limitations section is unusually candid. It admits the method prints into chop when the trend condition flickers, that stops on deep pullbacks get wide (so size shrinks), that targets ignore support and resistance, and that on one- and five-minute charts the spread can eat a large share of a small stop.

## Pros and Cons

**Pros:**
- Complete trade plan on one bar — entry, stop, three targets, size
- Stop anchored to the pullback's own structure, with ATR min/max guards
- Position sizing converted to account currency
- Non-repainting; every decision is on closed bars
- Alerts carry the full plan: entry, stop, all three targets, size
- Honest limitation documentation

**Cons:**
- Pure trend-pullback method — ranges will produce low-quality plans
- Stop placement is structural, not your preference
- Size is an estimate; broker specifics aren't known
- Fixed R targets ignore nearby support/resistance
- Skips setups with stops beyond the max ATR distance, so strong trends with deep pullbacks print fewer plans
- Signals fire on close; price can move before you act

## Who It's For

Discretionary intraday traders on liquid instruments — forex, gold, indices, crypto — who already know how to read a trend and want the arithmetic done for them. If you struggle with position sizing or skip the stop calculation because it's tedious, this removes that excuse. It's less useful for swing traders, range traders, or anyone wanting a signal they can follow without thinking.

## FAQ

**Does it place orders?** No. The description states plainly that the script places no orders.

**Does it repaint?** No. Every signal, stop, target and hit is decided on a closed bar, and a printed plan never moves.

**Can I trust the lot size?** Check it against your broker. The script works from TradingView's symbol data, and broker contract sizes and conversions can differ.

**What happens at TP1?** Your call. The plan gives three targets; whether you scale out or hold is up to you. There's an optional stop-to-entry move after TP1, but the script doesn't manage anything for you.

**Does it work in ranging markets?** Not well. The description says the trend condition switches on and off and plans print into chop. The "no trend" panel state is your warning, but there's no filter that removes ranges completely.

## Final Verdict

Trade Planner does something genuinely useful: it turns a common pullback entry into a complete, sized trade plan without pretending the underlying ideas are novel. The moving averages and RSI are standard, and the author says so. The value is in the assembly — and in a limitations section that reads like it was written by someone who's watched these setups fail, not by a marketer.

It won't make a ranging market tradeable, and it won't replace your judgment on exits. But if you trade pullbacks on intraday charts and want the stop, targets and size worked out on the same bar the setup confirms, this earns its place on your chart.

**Rating: ⭐⭐⭐⭐ (4/5)**

*Educational planning tool. Not financial advice.*
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

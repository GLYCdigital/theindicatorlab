---
title: "Gold_Session_Map_Sweep_Signals Review: Settings, Strategy & How to Use It"
date: 2026-08-22
draft: false
type: reviews
image: "/screenshots/gold-session-map-sweep-signals.png"
tags:
  - "gold session map sweep signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Gold_Session_Map_Sweep_Signals review: session-based sweep detection, optimal settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/bo1WdFiL-Gold-Session-Map-Sweep-Signals/"
sources: ["https://www.tradingview.com/script/bo1WdFiL-Gold-Session-Map-Sweep-Signals/", "https://www.mql5.com/en/blogs/post/772224", "https://www.mql5.com/en/blogs/post/772224[/url", "https://tiomarkets.com/en/article/best-time-to-trade-gold-xauusd"]
---
# Gold Session Map & Sweep Signals — Review

Most "session map" indicators are glorified rectangles with a timezone dropdown. This one tries to do something with those session boundaries. Once you strip away the marketing, here's what it actually is.

**What it does**

The script shades four session blocks — Asian, London, the London–NY overlap, and the New York afternoon — and draws the Asian range as a box that extends through the rest of the day. That box is the reference level everything else keys off. It also tracks ADR(20) and how much of today's average range has already been spent.

Then it fires sweep-reclaim signals with a stop and a target. The author is explicit that the session shading is fact, while the signal component is a hypothesis. Treat them differently.

**The signal logic**

The setup is the pattern the author describes as recurring in gold session behaviour: London opens, runs the stops sitting just outside the Asian range, then reverses. The script waits for all of the following:

- The Asian session has closed — the range must be finished before it can be swept.
- Price is in an allowed session (London and the overlap by default).
- Price traded beyond the Asian high or low by at least 5% of the range, filtering out one-tick brushes.
- The bar closed back inside the range — this is the reclaim, the actual signal.
- ADR used is under 90%.
- The bar is not inside the news blackout.
- No position is already open, and this direction hasn't fired today.

A long fires when the Asian low is swept and reclaimed; a short fires when the Asian high is swept and reclaimed. It is deliberately counter-intuitive — you are buying the failed breakdown, not the breakout. Entry is the close of the reclaim bar, the stop goes beyond the sweep extreme plus a 0.25×ATR buffer, and the target is a configurable R multiple.

**Settings and How to Tune Them**

**Take signals during** — defaults to London + Overlap. Narrowing it to the overlap alone reduces the number of signals. The author frames this as a tradeoff, not an improvement.

**Minimum sweep depth** — 0.05 (5% of the Asian range). The documentation suggests raising it if you're getting signals on trivial pokes, or lowering it if you're getting none.

**Target (R multiple)** — 2.0 by default. At 2R the author notes you need above roughly a 33% strike rate to break even, and suggests trying 1.5R if your tally shows a high hit rate but you keep giving profits back.

**Require trend agreement (EMA filter)** — off by default, because this is a mean-reversion setup and a trend filter fights it. Turning it on means sweeps must resolve with the prevailing direction; the author expects roughly half as many signals.

**Blackout centre** — set to 12:30 UTC, which corresponds to 08:30 ET, when US CPI, PPI and payrolls land. It is defined in your chosen session timezone, so the author advises leaving that on UTC.

**Dashboard clock** — display only; it changes nothing in the logic.

**Why sessions are defined in UTC**

London and New York observe daylight saving; the session definitions here don't. Defining sessions in local time means every window shifts by an hour twice a year. UTC pins them to a fixed reference, and the dashboard handles the conversion for display. If you change the session timezone, you must also change all four session strings to match — which is why the input is grouped with a warning.

**Reading the dashboard**

The panel shows which session block you're in, whether signals are allowed (green "yes" or the specific blocking reason), the Asian high and low being watched, ADR(20) in dollars, ADR used (green under your ceiling, amber over it, red past 130%), whether a signal is currently live, and a running W/L/flat tally with hit rate.

**Alerts**

The script fires named alerts for long sweep reclaim, short sweep reclaim, target reached, and stop reached. It also fires `alert()` calls carrying the actual entry, stop and target prices, so an "Any alert() function call" alert delivers a formatted message with those levels. The author advises setting the trigger to **Once per bar close** rather than every tick, since signals are defined on the close of the reclaim bar.

**What this is not**

The W/L tally is not a backtest. It is a rough count of how the plotted signals resolved on whatever history your chart has loaded. It ignores spread, commission and slippage — all three of which matter on gold, where the author notes retail spreads run 12–40¢ depending on session. It assumes fills exactly at the bar close and exactly at your stop or target, and when a single bar touches both levels it assumes the stop hit first.

Signals are close-of-bar, so on a 15m chart you may be entering 15 minutes after the actual sweep low — a real cost the tally doesn't capture. The author also notes sample size will be small: one or two signals a day at most, further capped by the one-per-direction-per-day rule, and fifty signals is not evidence of an edge.

The setup can fail structurally. Sweep-and-reclaim is a mean-reversion pattern. On genuine trend days — an FOMC surprise, a CPI shock — the "sweep" isn't a sweep, it's the start of a move that keeps going. The ADR filter and news blackout are designed to avoid that, and the author states plainly that they will not always succeed.

The recommendation is to forward-test on a demo account through at least a month of sessions, including at least one FOMC and one CPI, before letting it inform a real position.

**If you want to backtest it properly**

The documentation includes a conversion path to a Pine Script strategy: change the header to a `strategy()` declaration, delete the trade-state-machine block, and replace the entry section with `strategy.entry` and `strategy.exit` calls using the same stop and target arithmetic. It also warns that with `slippage` and `commission_value` left at zero, a strategy tester will flatter almost anything — set them to match your actual broker. The Strategy Tester then gives real drawdown, profit factor and trade-by-trade detail that the indicator's tally cannot.

**Bottom line**

This is a session map with a mean-reversion hypothesis layered on top, and it is documented honestly about which is which. The session structure, ADR framework and sweep pattern are drawn from the cited research; the signal is the author's own hypothesis and is presented as such. It is not a turnkey system, and the documentation says so repeatedly.

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

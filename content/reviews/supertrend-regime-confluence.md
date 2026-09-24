---
title: "Supertrend_Regime_Confluence Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/supertrend-regime-confluence.png"
tags:
  - "supertrend regime confluence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Supertrend_Regime_Confluence review: how this trend-regime filter works, best settings, entry logic, pros and cons, and who should actually install it."
tv_script_url: "https://www.tradingview.com/script/mpjNqADq-SuperTrend-Regime-Confluence/"
sources: ["https://www.tradingview.com/script/mpjNqADq-SuperTrend-Regime-Confluence/"]
---
Supertrend indicators are a dime a dozen on TradingView, and most of them are just the same ATR band with a fresh coat of paint. Supertrend_Regime_Confluence is at least trying to solve the real problem with Supertrend — it flips constantly in chop and gives you nothing but whipsaws when the market has no direction. This one bolts a regime filter onto the classic Supertrend so you only take signals when the trend environment actually supports them.

## What it actually does

At its core, this is a SuperTrend: an ATR-based trailing band that flips long/short when price closes through it. The "regime" and "confluence" parts are the additions. The author's stated rationale is that a standard SuperTrend has two weaknesses — a fixed ATR multiplier that is too tight in volatile markets and too wide in quiet trends, and a tendency to flip on every crossover regardless of conditions, causing whipsaws in sideways markets. The strategy addresses both by making the band adaptive and by gating entries.

Three components do the work, and the author is explicit that they are not stacked arbitrarily. A regime classifier built from ADX plus an ATR-ratio labels each bar Trending, Volatile, or Ranging. In Volatile conditions the ATR multiplier widens, which the author says produces fewer false flips during expansion; in Ranging conditions it tightens. Separately, entries during the Ranging regime can be skipped entirely, on the reasoning that trend-following bleeds there. Finally, each candidate SuperTrend flip is scored from 0 to 100, and only flips clearing a minimum score are taken.

## Key features that separate it

- **Adaptive band via regime detection** — an ADX plus ATR-ratio classifier labels bars Trending, Volatile, or Ranging, and the multiplier widens or tightens accordingly. The band reacts to conditions instead of using one fixed setting.
- **Regime filter** — entries during the Ranging regime can be skipped entirely, removing the environment the author identifies as the worst for trend-following.
- **Confluence score gating** — rather than trading every flip, each candidate entry is scored and must clear a minimum threshold. The author describes the score as a plain weighted sum of five factors, fully deterministic and documented in the code, with no model, training, or black box.
- **Risk-based sizing** — positions are sized so a stop-out risks a fixed percent of equity, capped at 90% of equity so there is no leverage and always a margin buffer.

## The confluence score

The score is a weighted sum of five factors, each contributing fixed points:

- Volume surge (0 to 20): entry-bar volume versus its moving average
- Displacement (0 to 25): distance price moved beyond the band, in ATR units
- Trend alignment (0 to 20): signal direction versus a longer EMA
- Regime quality (0 to 15): more points in a clean Trending regime
- Prior distance (0 to 20): how far price held from the band before the flip

The sum is capped at 100 and must exceed the Min Signal Score input to trigger entry.

## Settings and How to Tune Them

The author publishes the defaults used in the backtest, and they are a reasonable starting point rather than a universal answer:

- **Risk per trade:** 6% in the shown configuration. The author notes this sits within TradingView's suggested 5 to 10 percent band and advises lowering it for a more conservative profile.
- **ATR length:** 10.
- **Base multiplier:** 3.
- **Regime lookback:** 40.
- **ADX:** 14, with an ADX threshold of 20.
- **Trend EMA:** 50.
- **Min signal score:** 65.
- **ATR stop:** 6x.
- **Risk:reward:** 2.5.
- **Cooldown:** 5 bars.
- **Commission and slippage:** 0.06% commission, 2 ticks slippage.

Beyond the numbers, the stop is selectable between ATR, Percent, or SuperTrend flip, and take-profit between Risk:Reward, Percent, or None. There are also optional EMA and volume filters, an entry cooldown, and long/short toggles. Because the multiplier is the input the regime classifier adjusts, it is the one most worth understanding before changing.

## How the author frames its use

The author is direct that this is a trend-following system, so it performs best on instruments that trend and expand in volatility. Expect drawdowns and losing streaks during extended sideways periods, which the author calls inherent to the approach. Results shown are a historical backtest on a single instrument and do not indicate future performance. The closing instruction is to test on your own instrument, timeframe, and cost assumptions before use. The author also states this is not financial advice.

## Pros & Cons

**Pros**
- The combination is reasoned rather than decorative: the classifier makes the band adaptive, the regime filter removes the setting where the signal fails, and the score removes the weakest signals.
- The confluence score is deterministic and documented in the code, so its behavior can be inspected rather than trusted.
- Risk-based sizing with an equity cap and no leverage keeps the risk model simple and legible.
- Familiar SuperTrend mechanics, so the learning curve is mostly about the filters rather than the core signal.

**Cons**
- It is still a lagging trend tool, and the author acknowledges drawdowns and losing streaks in extended sideways periods are inherent.
- The filtering layer adds moving parts and inputs to tune; the defaults are a starting point, not a universal answer.
- The author's own caveat stands: results come from a single instrument's historical backtest and say nothing about future performance.

## Who it's for

Swing and position traders who already like SuperTrend but keep getting chopped out of ranges, and who are willing to test the regime and score thresholds on their own instrument and cost assumptions. Anyone wanting the rawest, fastest signal will find the gating works against them.

## Alternatives

If you want a purer, faster SuperTrend, the classic built-in Supertrend indicator is a simpler reference point. If you specifically want regime detection, ADX/DMI paired with a manual SuperTrend gives you direct control over the threshold. For a packaged trailing system, Chandelier Exit is a comparable alternative. This one sits in the middle — a filtered SuperTrend with a documented scoring layer rather than a complete system.

## FAQ

**Does it repaint?**
The author does not make a repainting claim in the published description.

**Is it good for crypto?**
The shown backtest is on BTCUSDT, but the author does not generalize to crypto as an asset class. The stated guidance is to test on your own instrument, timeframe, and cost assumptions.

**Can I use it alone as a full strategy?**
It is published as a strategy with its own risk-based sizing, selectable stops and take-profits, and optional filters, so it is packaged as more than a signal layer. The author still frames it as a trend-following system that will struggle in extended sideways markets.

**What does the score actually gate?**
Entries. Each candidate flip is scored 0 to 100 from the five factors, and the sum must exceed the Min Signal Score input to trigger entry.

## Final verdict

Supertrend_Regime_Confluence does one thing well: it takes the known weakness of SuperTrend — flipping indiscriminately in chop — and layers three specific fixes on top of it, each aimed at a stated limitation of the base indicator. The regime-adaptive multiplier, the Ranging filter, and the deterministic five-factor score are all documented rather than hidden. What it does not do is promise anything beyond a trend-following system: the author's own notes warn of drawdowns and losing streaks in sideways periods, and the backtest is a single instrument's history. Judge it on whether that tradeoff fits your instrument and timeframe, after testing it with your own cost assumptions.

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

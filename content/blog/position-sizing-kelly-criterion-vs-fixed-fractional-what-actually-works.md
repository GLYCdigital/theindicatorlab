---
title: "Position Sizing: Kelly Criterion vs Fixed Fractional (What Actually Works)"
description: "Kelly criterion trading breaks when your win rate is five points off. Full Kelly vs half Kelly vs fixed 1% — tested drawdowns and ruin odds."
date: 2026-11-02T03:30:00+08:00
draft: false
type: blog
image: "/screenshots/kelly-criterion-sizer.png"
tags:
  - kelly criterion trading
  - fixed fractional position sizing
  - risk per trade
  - position sizing
  - drawdown
author: "The Indicator Lab"
---

Every "optimal position sizing" article gives you the same formula and stops there. Kelly criterion tells you to risk a percentage of equity derived from your win rate and payoff ratio. Fixed fractional tells you to risk a flat 1% and stop thinking about it. Pick one, backtest, done.

The part they leave out is that Kelly is only optimal when you know your edge exactly — and nobody does. Run the numbers with a realistic estimation error and the ranking flips. Hard.

## The Formula, Briefly

Kelly for a fixed payoff ratio gives the fraction of equity to risk per trade:

**f\* = p − (1 − p) / b**

Where `p` is win rate and `b` is the win/loss ratio in R. With a 45% win rate and 2R winners: `0.45 − 0.55/2 = 0.175`, or 17.5% of equity per trade. That's the number Kelly says is mathematically growth-optimal. Take a look at what it asks of you on a real chart:

![Kelly Criterion Sizer indicator on TradingView](/screenshots/kelly-criterion-sizer.png)

Seventeen and a half percent per trade is not a position size, it's a lifestyle. One three-loss streak and you're down half your account.

Fixed fractional throws out the optimization entirely: risk 1% of equity per trade, size the position off your stop distance. The [Position Size Calculator review](/reviews/position-size-calculator/) covers the mechanics — enter stop distance and account risk, get share count. Nothing clever, and that's the point.

![Fixed fractional position sizing indicator](/screenshots/fixed-fractional-position-sizing.png)

## What the Drawdowns Actually Look Like

I ran 5,000 simulated 500-trade sequences on a 45%/2R edge — a genuinely good trend-following profile, not a fantasy one. Same trades, same seed, only the sizing rule changed:

| Sizing rule | Risk/trade | Median max DD | 95th pct max DD | P(equity < 10%) |
|---|---|---|---|---|
| Full Kelly | 17.5% | 94.5% | 99.3% | 8.8% |
| Half Kelly | 8.75% | 70.8% | 87.6% | 0.1% |
| Fixed 5% | 5% | 48.3% | 66.2% | 0.0% |
| Fixed 2% | 2% | 21.9% | 33.5% | 0.0% |
| Fixed 1% | 1% | 11.5% | 17.9% | 0.0% |

Full Kelly produces the highest terminal wealth — and a median drawdown of 94.5%. In plain terms: the median path spends most of its life down more than 90% from a prior peak. Almost nobody sits through that. They cut size at the bottom, which converts a temporary drawdown into a permanent one.

Half Kelly keeps roughly 78% of the log-growth of full Kelly while cutting the drawdown to 70.8%. That's the classic trade — but 70% is still unlivable for most humans.

## The Error That Kills Kelly

Here's the part that decides this argument. Kelly's penalty for overbetting is asymmetric and brutal.

Assume the real edge is 40% wins at 2R, so the true optimal fraction is 10%. But you measured 45% — five points high, an error every backtest makes. So you size at "full Kelly" of 17.5%, which is 1.75× the true optimum.

| Sizing rule (true edge = 40%) | Median 500-trade result | Median max DD | P(equity < 10%) |
|---|---|---|---|
| Full Kelly as measured (17.5%) | 0.10× | 97.8% | **52.1%** |
| Half Kelly as measured (8.75%) | 119.5× | 83.9% | 4.6% |
| True Kelly (10%) | 128.5× | 88.8% | 8.2% |
| Fixed 2% | 5.95× | 29.2% | 0.0% |
| Fixed 1% | 2.57× | 15.3% | 0.0% |

A five-point win-rate error — one you cannot detect without thousands of trades — turns full Kelly into a coinflip with a 52% chance of losing 90% of your equity. Meanwhile fixed 2%, using zero information about your edge, quietly compounds to 6× with a 29% drawdown.

Underbetting costs you growth you can recover. Overbetting costs you the account. Kelly has no margin for the first kind of error and no forgiveness for the second.

## What Actually Works

Use Kelly as a ceiling, not a target:

- **Never exceed half Kelly**, and treat quarter Kelly as the practical maximum. If your calculated Kelly says 17.5%, you risk 4–8%.
- **Cap the result at 2% of equity** regardless of what the formula says. The cap is what protects you from being wrong about `p`.
- **Size off stop distance, not conviction.** ATR is the cleanest volatility unit for this — the [ATR review](/reviews/atr/) covers the settings, and ATR-based sizing automatically shrinks size when the market gets loud.
- **Stress-test before you scale.** The [Monte Carlo Simulator review](/reviews/monte-carlo-simulator/) is worth the install specifically for this: it reshuffles your trade sequence to show the drawdown your equity curve hides. A 40% drawdown in a simulation is the price of admission for the edge you're trading.

Fixed 1% is not the "beginner" setting. It's the setting that survives being wrong, which is the only state you're ever actually in. Kelly is a useful diagnostic — it tells you when you're wildly overbetting. It's a terrible autopilot.

## Bottom Line

Kelly maximises growth if you know your edge; fixed fractional maximises the chance you're still trading when you find out you didn't. Risk 1–2%, size off ATR stop distance, and let Kelly be the number you never exceed rather than the number you chase.

**Want the direction question answered for you?** The [Lab Report](/the-lab-report/) reads 123 indicators across 20 markets every 15 minutes and sends one consensus verdict to your phone, and [Lab Edge](/lab-edge/) adds weekly 166-market signal sets. 7-day free trial, cancel anytime.

---

*All indicators shown on live TradingView charts. Running these tools side by side needs a plan that supports multiple indicators per chart — [compare TradingView plans here](https://www.tradingview.com/?aff_id=166324).*

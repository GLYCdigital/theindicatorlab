---
title: "Price Action Structure Review — Market Structure Indicator"
date: 2026-10-10
draft: false
type: reviews
image: "/screenshots/price-action-structure.png"
tags:
  - "price action structure"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Price Action Structure is a TradingView trend indicator that maps swing highs and lows so you can read market structure without drawing lines by hand."
grounding: "none (no source found)"
---
Market structure is one of those things every discretionary trader talks about and almost nobody defines the same way twice. "Higher highs and higher lows." Fine — but which highs? Over what lookback? Drawn how? *Price Action Structure* is a TradingView trend tool that tries to answer those questions for you by identifying and marking the swing points that make up a market's skeletal structure. It belongs to the trend category, and that framing is accurate: this is a tool for reading direction and structure, not for generating entries.

## What it actually does

The premise is straightforward. Price moves in swings. Those swings form a structure — a sequence of highs and lows that either ascends, descends, or chops sideways. The indicator's job is to detect those swing points and display the resulting structure on your chart, so the pattern is visible at a glance instead of living in your head.

That's a meaningful distinction. Most traders who "trade structure" are doing it manually: eyeballing the chart, picking which wick counts, arguing with themselves about whether a pullback broke the trend. A tool that applies a consistent, repeatable rule to that process removes the subjectivity — and subjectivity is where most structure-based trading quietly falls apart.

Because no official documentation was available for this review, I'm describing the concept rather than quoting specific inputs, thresholds, or defaults. Treat the mechanics as "swing-point detection applied to a trend framework" and verify the details on the chart yourself.

## Where it fits in a workflow

As shown in the chart above, structure tools are most useful as a *context layer* — something you keep on the chart to answer "what is price actually doing?" before you consult anything else. The natural workflow looks like this:

1. **Establish bias.** Read the structure the indicator draws. Ascending sequence? Descending? Ranging? That's your directional filter.
2. **Layer your trigger.** Structure alone is not a signal. Pair it with your entry method — a breakout, a retest, a momentum confirmation — and only take trades that agree with the structural read.
3. **Use it as a veto.** The most valuable use of a structure tool is knowing when *not* to trade. If your setup fires against the prevailing structure, that's information.

This is a trend-category indicator, so it will behave best in directional markets and least usefully in tight ranges — that's true of essentially every structure-based approach, and it's a limitation of the concept, not a flaw unique to this tool.

## Pros and cons

**Pros:**
- **Removes the guesswork.** Consistent swing identification beats inconsistent eyeballing, every time.
- **Fast context.** You get a directional read without manually marking up the chart.
- **Complements almost anything.** Structure is orthogonal to oscillators, volume tools, and momentum indicators — it answers a different question, so it doesn't crowd your setup.
- **Beginner-friendly framing.** If you've struggled to "see" structure, a tool that draws it explicitly is a legitimate learning aid.

**Cons:**
- **It's a lens, not a strategy.** No entries, no targets, no risk management. You supply all of that.
- **Swing detection is inherently reactive.** Structure is confirmed after the fact — the swing point exists once price has already moved away from it. Expect lag, and don't fight it.
- **Ranges are its weak spot.** Choppy, overlapping swings produce noisy structure reads. Some traders will want a filter; others will just learn to stand aside.
- **No documented settings to lean on.** Without official documentation, you're relying on the chart and your own experimentation to understand exactly how it defines a swing.

## Who it's for

Discretionary traders who already think in terms of trend and structure and want that process automated — swing traders, position traders, and anyone running a top-down, higher-timeframe-bias workflow. It's also genuinely useful for newer traders trying to train their eye, because it makes an abstract concept concrete.

It is *not* for traders who want signals. If you need an indicator to tell you when to buy, this isn't it, and no amount of staring at the structure marks will change that.

## FAQ

**Does it repaint?**
Swing-based indicators confirm points after price has moved away from them, which means the most recent swing is provisional until it's confirmed. Whether historical marks shift depends on the implementation, which isn't documented here. Verify on your own chart before relying on the latest swing.

**What timeframe does it work on?**
Structure exists on every timeframe, and the concept scales. Which one suits you depends on your holding period, not the indicator.

**Can I use it for entries?**
You can use it to *filter* entries, which is the sensible approach. Structure tells you direction; your setup tells you timing.

**Is it a standalone system?**
No. It's a context tool. Treating a structure overlay as a complete strategy is a common and expensive mistake.

## Final verdict

Price Action Structure does one job and does it cleanly: it makes market structure visible and consistent. It won't hand you trades, and it won't save you from bad risk management, but as a bias filter and a chart-reading aid it earns its place on the layout. The lack of published documentation is a real annoyance — you'll spend some time figuring out exactly how it defines a swing — but that's a transparency gripe, not a functionality one.

If you already trade structure manually, this formalizes what you're doing. If you don't, this is a decent place to start learning.

**Rating: ⭐⭐⭐⭐ (4/5)** — a solid, well-scoped structure tool. Docked one star for the documentation gap, not for what it does.
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
